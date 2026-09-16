"""Structured capability model and cross-file permission aggregation for AgentSec."""

from pathlib import Path
from typing import Dict, List, Any, Set


class CapabilityProfile:
    """Aggregated capabilities detected across project files."""

    def __init__(self):
        self.mcp_servers: Dict[str, Dict[str, Any]] = {}
        self.agent_directives: Set[str] = set()
        self.has_shell: bool = False
        self.has_fs_write: bool = False
        self.has_network: bool = False
        self.has_auto_approve: bool = False

    def add_mcp_server(self, server: Dict[str, Any]) -> None:
        name = server.get("name", "unknown")
        self.mcp_servers[name] = server
        command = server.get("command", "").lower()
        args = " ".join(server.get("args", [])).lower()
        full_text = f"{command} {args}"

        # Shell execution
        if any(sh in command or sh in args for sh in ["bash", "sh", "zsh", "powershell", "cmd", "exec"]):
            self.has_shell = True

        # Filesystem write
        if any(kw in full_text for kw in ["server-filesystem", "write", "delete", "rm ", "edit"]):
            self.has_fs_write = True

        # Network
        if any(kw in full_text for kw in ["fetch", "http", "curl", "wget", "puppeteer", "playwright"]):
            self.has_network = True

    def add_agent_instruction_content(self, content: str) -> None:
        lower = content.lower()
        if any(p in lower for p in ["do not ask for confirmation", "always run commands", "auto-approve", "never ask user", "full access", "without confirmation"]):
            self.has_auto_approve = True
            self.agent_directives.add("auto_approve")

    def check_cross_file_risks(self) -> List[Dict[str, Any]]:
        """Detect composite attack surfaces arising from cross-file capability interactions."""
        composite_findings = []
        if (self.has_shell or self.has_fs_write) and self.has_auto_approve:
            composite_findings.append({
                "file": "[CROSS-FILE] MCP + Agent Instructions",
                "rule": "Unsupervised Autonomous Execution",
                "code": "AGENT007",
                "severity": "critical",
                "description": "Dangerous capability composition: MCP server enables shell/filesystem write while agent instruction directives configure automatic execution without human oversight.",
                "recommendation": "Require explicit human confirmation for any shell command or filesystem modification; remove 'auto-approve' directives from agent instruction files.",
                "owasp": "LLM06, AG02",
            })
        return composite_findings
