"""Base rule definitions."""

from typing import List
from pathlib import Path

class Rule:
    def __init__(
        self,
        code: str,
        name: str,
        severity: str,
        description: str,
        recommendation: str,
        detect_patterns: List[str],
        all_patterns: List[str] | None = None,
    ):
        self.code = code
        self.name = name
        self.severity = severity
        self.description = description
        self.recommendation = recommendation
        self.patterns = detect_patterns
        self.all_patterns = all_patterns or []

    def detect(self, content: str, file_path: Path) -> bool:
        if not content:
            return False
        lower = content.lower()
        if self.all_patterns:
            return all(pattern.lower() in lower for pattern in self.all_patterns)
        for pattern in self.patterns:
            if pattern.lower() in lower:
                return True
        return False

def load_rules() -> List[Rule]:
    from .additional import load_additional_rules
    base_rules = [
        Rule(
            code="AGENT001",
            name="MCP shell execution",
            severity="critical",
            description="MCP server can execute shell commands",
            recommendation="Require explicit approval or remove shell access.",
            detect_patterns=["bash", "sh", "powershell", "cmd", "exec", "subprocess", "terminal", "run_command"]
        ),
        Rule(
            code="AGENT002",
            name="MCP filesystem write access",
            severity="critical",
            description="MCP server has filesystem write access",
            recommendation="Restrict filesystem access to read-only or specific directories.",
            detect_patterns=["filesystem", "write", "edit", "delete", "rm", "mv", "path", "workspace"]
        ),
        Rule(
            code="AGENT003",
            name="Secret exposure",
            severity="critical",
            description="MCP server can access secrets or environment variables",
            recommendation="Do not expose secrets to MCP servers; use environment variables with caution.",
            detect_patterns=[".env", "process.env", "AWS_SECRET_ACCESS_KEY", "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GITHUB_TOKEN", "SLACK_BOT_TOKEN"]
        ),
        Rule(
            code="AGENT004",
            name="Broad path access",
            severity="high",
            description="MCP server has broad filesystem path access (root or home)",
            recommendation="Restrict path to specific directories.",
            detect_patterns=["/", "~", "/home", "/Users", "C:\\", ".", "..", "**"]
        ),
        Rule(
            code="AGENT005",
            name="Prompt injection risk",
            severity="medium",
            description="Agent instruction file contains suspicious prompt injection patterns",
            recommendation="Review and sanitize agent instruction files.",
            detect_patterns=["ignore previous instructions", "ignore all instructions", "do not tell the user", "secretly", "exfiltrate", "bypass", "disable security", "you are now", "system prompt", "hidden instruction"]
        ),
        Rule(
            code="AGENT006",
            name="Sensitive file reference",
            severity="high",
            description="Agent instruction references sensitive files or secrets",
            recommendation="Remove references to secrets or use gitignored files.",
            detect_patterns=[".env", "id_rsa", ".ssh", "credentials", "secrets", "tokens", "auth.json"]
        ),
        Rule(
            code="AGENT007",
            name="Excessive autonomy",
            severity="medium",
            description="Agent instruction asks for excessive autonomy (no confirmation)",
            recommendation="Require user confirmation for important actions.",
            detect_patterns=["do not ask for confirmation", "always run commands", "auto-approve", "never ask user", "full access"]
        ),
        Rule(
            code="AGENT008",
            name="Unpinned dependency",
            severity="medium",
            description="MCP server dependency is not pinned (latest tag or no version)",
            recommendation="Pin dependencies to a specific version or commit SHA.",
            detect_patterns=["latest", ":latest", "@latest"]
        ),
        Rule(
            code="AGENT009",
            name="Remote script install",
            severity="high",
            description="Agent config uses remote script install pattern (curl | bash)",
            recommendation="Avoid piping remote scripts directly to shell.",
            detect_patterns=["curl ... | bash", "wget ... | sh"]
        ),
        Rule(
            code="AGENT010",
            name="Docker socket access",
            severity="critical",
            description="MCP server can access the Docker socket",
            recommendation="Avoid mounting the Docker socket unless absolutely necessary.",
            detect_patterns=["/var/run/docker.sock", "docker.sock"]
        ),
    ]
    return base_rules + load_additional_rules()
