"""Main scanner orchestrator."""

from pathlib import Path
from typing import List, Dict, Any, Optional
import pathspec

from .rules import Rule, load_rules
from .parsers import parse_file
from .parsers.json_parser import parse_mcp_config as parse_json_mcp
from .parsers.yaml_parser import parse_mcp_config as parse_yaml_mcp
from .parsers.toml_parser import parse_mcp_config as parse_toml_mcp
from .parsers.python_ast import scan_python_tool_ast
from .shadowing import detect_tool_shadowing
from .owasp import get_owasp_ids
from .ignore import SuppressionManager
from .capabilities import CapabilityProfile

SEVERITY_ORDER = {"critical": 3, "high": 2, "medium": 1, "low": 0}

ALLOWED_DOTFILES = {".env", ".env.example", ".cursorrules", ".clinerules", ".mcp.json"}


def is_broad_path(arg: str) -> bool:
    """Determine if an argument represents broad root/home filesystem access."""
    clean = arg.strip().strip("'\"").rstrip("/")
    if clean in {"/", "~", "/home", "/root", "/users", "c:", "c:\\"} or clean.startswith(("/home/", "/Users/", "/root/")):
        return True
    if clean in {"..", ".", "../.."} or "/../" in clean or clean.endswith("/.."):
        return True
    return False


def classify_file(file_path: Path) -> Optional[str]:
    """Classify a file into one of the target categories."""
    name = file_path.name.lower()
    path_str = str(file_path).replace("\\", "/").lower()

    if name in {"mcp.json", "mcp.yaml", "mcp.yml", "mcp.toml", "mcp-config.json", "claude_desktop_config.json", ".mcp.json"}:
        return "mcp"
    if "cline_mcp" in path_str or path_str == "mcp":
        return "mcp"
    if name == "settings.json" and ("mcp" in path_str or ".vscode" in path_str or ".cursor" in path_str):
        return "mcp"

    if name in {"agents.md", "claude.md", ".cursorrules", ".clinerules", "codex.toml", "system.md", "prompt.md"}:
        return "agent_instructions"
    if ".cursor/rules" in path_str or name.endswith(".mdc"):
        return "agent_instructions"

    if name in {".env", ".env.example", ".env.local", ".env.development", ".env.production", ".env.test"} or name.startswith(".env."):
        return "env"

    if name in {"dockerfile", "docker-compose.yml", "docker-compose.yaml", "devcontainer.json"} or name.startswith("dockerfile.") or "devcontainer" in path_str:
        return "container"

    if name in {"package.json", "requirements.txt", "pipfile"}:
        return "dependency"

    if name.endswith(".py"):
        # Avoid self-scanning scanner's own internal engine or test fixtures
        if "/agentsec/" in path_str or path_str.startswith("agentsec/"):
            return None
        if "/tests/" in path_str or path_str.startswith("tests/"):
            return None
        return "python_tool"

    return None


def _load_gitignore_spec(root: Path, extra_patterns: List[str], no_gitignore: bool) -> Optional[pathspec.PathSpec]:
    patterns: List[str] = []
    if not no_gitignore:
        gitignore_path = root / ".gitignore"
        if gitignore_path.exists():
            lines = gitignore_path.read_text(encoding="utf-8", errors="ignore").splitlines()
            for line in lines:
                stripped = line.strip()
                if stripped and not stripped.startswith("#"):
                    patterns.append(stripped)
    for ep in extra_patterns:
        patterns.append(ep)

    if not patterns:
        return None
    return pathspec.PathSpec.from_lines("gitignore", patterns)


class Scanner:
    def __init__(self, root: Path, include_hidden: bool = False, min_severity: str = "all",
                 exclude_patterns: Optional[List[str]] = None, no_gitignore: bool = False,
                 ignore_file: Optional[Path] = None):
        self.root = root
        self.include_hidden = include_hidden
        self.min_severity = min_severity
        self.exclude_patterns = exclude_patterns or []
        self.no_gitignore = no_gitignore
        self._ignore_spec = _load_gitignore_spec(root, self.exclude_patterns, no_gitignore)
        self.suppression = SuppressionManager(root, ignore_file=ignore_file)
        self.rules = load_rules()

    def _finding_meets_severity_threshold(self, finding: Dict[str, Any]) -> bool:
        if self.min_severity == "all":
            return True
        min_level = SEVERITY_ORDER.get(self.min_severity.lower(), 0)
        finding_level = SEVERITY_ORDER.get(finding["severity"].lower(), 0)
        return finding_level >= min_level

    def scan(self) -> List[Dict[str, Any]]:
        findings = []
        cap_profile = CapabilityProfile()
        all_mcp_servers: List[Dict[str, Any]] = []

        for file_path in self.root.rglob("*"):
            if not file_path.is_file():
                continue

            # Allow recognized dotfiles (.cursorrules, .clinerules, .env, .mcp.json, etc.)
            is_recognized_dotfile = (
                file_path.name in ALLOWED_DOTFILES
                or file_path.name.startswith(".env.")
                or ".cursor/rules" in str(file_path).replace("\\", "/")
            )
            if not self.include_hidden and file_path.name.startswith(".") and not is_recognized_dotfile:
                continue

            # Check .gitignore and --exclude patterns
            rel_path = ""
            if self._ignore_spec is not None:
                try:
                    rel_path = file_path.relative_to(self.root).as_posix()
                    if self._ignore_spec.match_file(rel_path):
                        continue
                except ValueError:
                    pass
            else:
                try:
                    rel_path = file_path.relative_to(self.root).as_posix()
                except ValueError:
                    rel_path = str(file_path)

            file_type = classify_file(file_path)
            if not file_type:
                continue

            content = parse_file(file_path)
            if content is None:
                continue

            if file_type == "agent_instructions":
                cap_profile.add_agent_instruction_content(content)

            if file_type == "mcp":
                mcp_data = None
                if file_path.suffix == ".json":
                    mcp_data = parse_json_mcp(content, file_path)
                elif file_path.suffix in [".yaml", ".yml"]:
                    mcp_data = parse_yaml_mcp(content, file_path)
                elif file_path.suffix == ".toml":
                    mcp_data = parse_toml_mcp(content, file_path)

                if mcp_data:
                    for server in mcp_data:
                        server["file"] = str(file_path)
                        all_mcp_servers.append(server)
                        cap_profile.add_mcp_server(server)
                        for rule in self.rules:
                            if not rule.applies_to("mcp"):
                                continue
                            if self._apply_rule_to_mcp_server(rule, server):
                                finding = self._make_finding(file_path, rule, server)
                                if self._finding_meets_severity_threshold(finding):
                                    if not self.suppression.is_ignored(finding, rel_path, content):
                                        findings.append(finding)

            elif file_type == "python_tool":
                # 1. AST analysis for Python tools
                ast_findings = scan_python_tool_ast(file_path, content)
                for af in ast_findings:
                    af["owasp"] = get_owasp_ids(af["rule"])
                    if self._finding_meets_severity_threshold(af):
                        if not self.suppression.is_ignored(af, rel_path, content):
                            findings.append(af)

                # 2. General pattern rules for python_tool (skip what AST already flagged)
                for rule in self.rules:
                    if not rule.applies_to("python_tool"):
                        continue
                    if any(af["code"] == rule.code for af in ast_findings):
                        continue
                    if rule.detect(content, file_path, file_type="python_tool"):
                        finding = self._make_finding(file_path, rule)
                        if self._finding_meets_severity_threshold(finding):
                            if not self.suppression.is_ignored(finding, rel_path, content):
                                findings.append(finding)
            else:
                for rule in self.rules:
                    if not rule.applies_to(file_type):
                        continue
                    if rule.detect(content, file_path, file_type=file_type):
                        finding = self._make_finding(file_path, rule)
                        if self._finding_meets_severity_threshold(finding):
                            if not self.suppression.is_ignored(finding, rel_path, content):
                                findings.append(finding)

        # Cross-file composite risk analysis
        cross_findings = cap_profile.check_cross_file_risks()
        for cf in cross_findings:
            if self._finding_meets_severity_threshold(cf):
                if not self.suppression.is_ignored(cf, cf["file"]):
                    findings.append(cf)

        # Tool Shadowing detection across all configured MCP servers
        if all_mcp_servers:
            shadow_findings = detect_tool_shadowing(all_mcp_servers)
            for sf in shadow_findings:
                sf["owasp"] = get_owasp_ids(sf["rule"])
                if self._finding_meets_severity_threshold(sf):
                    if not self.suppression.is_ignored(sf, sf["file"]):
                        findings.append(sf)

        return findings

    def _make_finding(self, file_path: Path, rule: Rule, server: Dict[str, Any] | None = None) -> Dict[str, Any]:
        finding = {
            "file": str(file_path),
            "rule": rule.name,
            "code": rule.code,
            "severity": rule.severity,
            "description": rule.description,
            "recommendation": rule.recommendation,
            "owasp": get_owasp_ids(rule.name),
        }
        if server:
            finding["server"] = server.get("name", "unknown")
        return finding

    def _apply_rule_to_mcp_server(self, rule: Rule, server: Dict[str, Any]) -> bool:
        command = server.get("command", "").lower()
        args_list = [str(a) for a in server.get("args", [])]
        args = " ".join(args_list).lower()

        if rule.name == "MCP shell execution":
            shell_indicators = ["bash", "sh", "powershell", "cmd", "zsh", "fish"]
            return any(ind == command or f"/{ind}" in command or ind in args for ind in shell_indicators)

        if rule.name == "MCP filesystem write access":
            if command == "npx" and "@modelcontextprotocol/server-filesystem" in args:
                return True
            write_indicators = ["write", "edit", "delete", "rm", "mv"]
            return any(ind in args for ind in write_indicators)

        if rule.name == "Secret exposure":
            env_str = str(server.get("env", {})).lower()
            secret_patterns = [".env", "process.env", "aws_secret", "openai_api", "anthropic_api", "github_token", "slack_token", "api_key"]
            return any(p in args or p in env_str for p in secret_patterns)

        if rule.name == "Broad path access":
            return any(is_broad_path(arg) for arg in args_list)

        if rule.name == "Claude Desktop config with MCP server risks":
            server_text = str(server).lower()
            risky_indicators = ["filesystem", "shell", "bash", "network", "http", "https", "curl", "wget"]
            return any(indicator in server_text for indicator in risky_indicators)

        return rule.detect(str(server), Path("mcp"), file_type="mcp")
