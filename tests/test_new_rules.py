"""Tests for new rules AGENT051–AGENT057 and devcontainer classification."""

from pathlib import Path
import pytest
from agentsec.scanner import Scanner, classify_file
from agentsec.fixes import get_fix_plan


def test_classify_devcontainer():
    """Verify that devcontainer files are classified as container."""
    assert classify_file(Path("devcontainer.json")) == "container"
    assert classify_file(Path(".devcontainer/devcontainer.json")) == "container"
    assert classify_file(Path("my-project/.devcontainer/devcontainer.json")) == "container"


def test_agent051_docker_socket_mount(tmp_path):
    """AGENT051 detects /var/run/docker.sock in container configs."""
    cfg = tmp_path / "docker-compose.yml"
    cfg.write_text("""
version: '3'
services:
  agent:
    image: python:3.12
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
""")
    scanner = Scanner(tmp_path)
    findings = scanner.scan()
    codes = [f["code"] for f in findings]
    assert "AGENT051" in codes


def test_agent052_privileged_container(tmp_path):
    """AGENT052 detects privileged container execution."""
    cfg = tmp_path / "devcontainer.json"
    cfg.write_text('{"name": "agent-dev", "privileged": true}')
    scanner = Scanner(tmp_path)
    findings = scanner.scan()
    codes = [f["code"] for f in findings]
    assert "AGENT052" in codes


def test_agent053_insecure_browser_sandbox_flags(tmp_path):
    """AGENT053 detects --no-sandbox in MCP browser server args."""
    cfg = tmp_path / "mcp.json"
    cfg.write_text("""{
  "mcpServers": {
    "browser": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer", "--no-sandbox"]
    }
  }
}""")
    scanner = Scanner(tmp_path)
    findings = scanner.scan()
    codes = [f["code"] for f in findings]
    assert "AGENT053" in codes


def test_agent054_browser_remote_debugging_port(tmp_path):
    """AGENT054 detects --remote-debugging-port in MCP tools."""
    cfg = tmp_path / "claude_desktop_config.json"
    cfg.write_text("""{
  "mcpServers": {
    "chrome": {
      "command": "chromium",
      "args": ["--remote-debugging-port=9222"]
    }
  }
}""")
    scanner = Scanner(tmp_path)
    findings = scanner.scan()
    codes = [f["code"] for f in findings]
    assert "AGENT054" in codes


def test_agent055_cicd_workflow_modification(tmp_path):
    """AGENT055 detects prompts allowing modification of CI/CD workflows."""
    cfg = tmp_path / ".cursorrules"
    cfg.write_text("""# Agent Instructions
You can modify workflows in .github/workflows to fix build failures automatically.
""")
    scanner = Scanner(tmp_path)
    findings = scanner.scan()
    codes = [f["code"] for f in findings]
    assert "AGENT055" in codes


def test_agent056_git_hook_tampering(tmp_path):
    """AGENT056 detects prompts instructing modification of .git/hooks/."""
    cfg = tmp_path / "AGENTS.md"
    cfg.write_text("""# Repository Guidelines
Install git hooks by writing your custom script to .git/hooks/pre-commit.
""")
    scanner = Scanner(tmp_path)
    findings = scanner.scan()
    codes = [f["code"] for f in findings]
    assert "AGENT056" in codes


def test_agent057_plaintext_vector_db_credentials(tmp_path):
    """AGENT057 detects exposed vector DB credentials or connection strings."""
    cfg = tmp_path / "mcp.json"
    cfg.write_text("""{
  "mcpServers": {
    "knowledge": {
      "command": "mcp-qdrant",
      "args": ["--url=http://qdrant:6333"],
      "env": {
        "qdrant_api_key": "qdrant_live_secret_key_12345"
      }
    }
  }
}""")
    scanner = Scanner(tmp_path)
    findings = scanner.scan()
    codes = [f["code"] for f in findings]
    assert "AGENT057" in codes


def test_new_rules_have_scoped_fix_plans():
    """Verify get_fix_plan produces specialized remediation plans for AGENT051–AGENT057."""
    for i in range(1, 8):
        code = f"AGENT05{i}"
        plan = get_fix_plan({"code": code, "file": "config.json"})
        assert plan["title"] != f"Remediate {code}"
        assert plan["patch"] != "// Review config.json and apply least privilege."
        assert plan["suppression"] == f"config.json: {code}"
