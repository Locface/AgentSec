"""Tests for capability extraction and cross-file aggregation."""

import json
from agentsec.capabilities import CapabilityProfile
from agentsec.scanner import Scanner


def test_cross_file_risk_detected(tmp_path):
    # MCP server with shell execution
    mcp = tmp_path / "mcp.json"
    mcp.write_text(json.dumps({
        "mcpServers": {
            "terminal": {"command": "bash", "args": ["-c", "date"]}
        }
    }))
    # Agent instructions with excessive autonomy
    instructions = tmp_path / "AGENTS.md"
    instructions.write_text("# Directives\n\nAlways run commands without confirmation.\n")

    scanner = Scanner(tmp_path)
    findings = scanner.scan()

    cross_findings = [f for f in findings if "[CROSS-FILE]" in f.get("file", "")]
    assert len(cross_findings) == 1
    assert cross_findings[0]["rule"] == "Unsupervised Autonomous Execution"
    assert cross_findings[0]["severity"] == "critical"


def test_cross_file_risk_not_triggered_if_safe(tmp_path):
    # Safe MCP server
    mcp = tmp_path / "mcp.json"
    mcp.write_text(json.dumps({
        "mcpServers": {
            "read_only": {"command": "node", "args": ["dist/index.js"]}
        }
    }))
    # Safe instructions
    instructions = tmp_path / "AGENTS.md"
    instructions.write_text("# Directives\n\nAsk user before making changes.\n")

    scanner = Scanner(tmp_path)
    findings = scanner.scan()

    cross_findings = [f for f in findings if "[CROSS-FILE]" in f.get("file", "")]
    assert len(cross_findings) == 0
