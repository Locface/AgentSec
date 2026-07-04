"""Main scanner orchestrator."""
from pathlib import Path
from typing import List, Dict, Any
from .rules import Rule, load_rules
from .parsers import parse_file
from .parsers.json_parser import parse_mcp_config as parse_json_mcp
from .parsers.yaml_parser import parse_mcp_config as parse_yaml_mcp
from .parsers.toml_parser import parse_mcp_config as parse_toml_mcp
from .owasp import get_owasp_ids

SEVERITY_ORDER = {"critical": 3, "high": 2, "medium": 1, "low": 0}

class Scanner:
    def __init__(self, root: Path, include_hidden: bool = False, min_severity: str = "all"):
        self.root = root
        self.include_hidden = include_hidden
        self.min_severity = min_severity
        self.rules = load_rules()

    def _finding_meets_severity_threshold(self, finding: Dict[str, Any]) -> bool:
        if self.min_severity == "all":
            return True
        min_level = SEVERITY_ORDER.get(self.min_severity.lower(), 0)
        finding_level = SEVERITY_ORDER.get(finding["severity"].lower(), 0)
        return finding_level >= min_level

    def scan(self) -> List[Dict[str, Any]]:
        """Walk the directory, parse relevant files, and apply rules."""
        findings = []
        target_patterns = [
            "mcp.json", "mcp.yaml", "mcp.yml", "mcp.toml",
            "mcp-config.json", "claude_desktop_config.json", "settings.json",
            "AGENTS.md", "CLAUDE.md", ".cursorrules", ".cursor/rules",
            ".cursor", "cline_mcp", ".clinerules", "codex.toml",
            ".env", ".env.example",
            "docker-compose.yml", "Dockerfile",
            "package.json", "requirements.txt"
        ]
        mcp_patterns = [
            "mcp.json", "mcp.yaml", "mcp.yml", "mcp.toml",
            "mcp-config.json", "claude_desktop_config.json", "settings.json", "cline_mcp"
        ]
        
        for file_path in self.root.rglob("*"):
            if not file_path.is_file():
                continue
            if not self.include_hidden and file_path.name.startswith(".") and file_path.name not in [".env", ".env.example"]:
                continue
            
            if not any(p in str(file_path) for p in target_patterns):
                continue

            content = parse_file(file_path)
            if content is None:
                continue

            if any(mcp_pattern in str(file_path) for mcp_pattern in mcp_patterns):
                mcp_data = None
                if file_path.suffix == ".json":
                    mcp_data = parse_json_mcp(content, file_path)
                elif file_path.suffix in [".yaml", ".yml"]:
                    mcp_data = parse_yaml_mcp(content, file_path)
                elif file_path.suffix == ".toml":
                    mcp_data = parse_toml_mcp(content, file_path)
                if mcp_data:
                    for server in mcp_data:
                        for rule in self.rules:
                            if self._apply_rule_to_mcp_server(rule, server):
                                finding = self._make_finding(file_path, rule, server)
                                if self._finding_meets_severity_threshold(finding):
                                    findings.append(finding)
            else:
                for rule in self.rules:
                    if rule.detect(content, file_path):
                        finding = self._make_finding(file_path, rule)
                        if self._finding_meets_severity_threshold(finding):
                            findings.append(finding)

        return findings

    def _make_finding(self, file_path: Path, rule: Rule, server: Dict[str, Any] | None = None) -> Dict[str, Any]:
        """Build a finding dict with OWASP info."""
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
        """Apply a rule to a structured MCP server entry."""
        if rule.name == "MCP shell execution":
            command = server.get("command", "").lower()
            args = " ".join(server.get("args", [])).lower()
            shell_indicators = ["bash", "sh", "powershell", "cmd", "zsh", "fish"]
            if any(ind in command or ind in args for ind in shell_indicators):
                return True
            return False

        if rule.name == "MCP filesystem write access":
            args = " ".join(server.get("args", [])).lower()
            if server.get("command", "") == "npx" and "@modelcontextprotocol/server-filesystem" in args:
                return True
            write_indicators = ["write", "edit", "delete", "rm", "mv"]
            if any(ind in args for ind in write_indicators):
                return True
            return False

        if rule.name == "Secret exposure":
            args = " ".join(server.get("args", [])).lower()
            secret_patterns = [".env", "process.env", "aws_secret", "openai_api", "anthropic_api", "github_token", "slack_token"]
            if any(p in args for p in secret_patterns):
                return True
            return False

        if rule.name == "Broad path access":
            args = " ".join(server.get("args", [])).lower()
            if "/" in args or ".." in args or "~" in args:
                return True
            return False

        if rule.name == "Claude Desktop config with MCP server risks":
            server_text = str(server).lower()
            risky_indicators = ["filesystem", "shell", "bash", "network", "http", "https", "curl", "wget"]
            return any(indicator in server_text for indicator in risky_indicators)

        return rule.detect(str(server), Path("mcp"))
