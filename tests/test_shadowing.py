"""Tests for MCP Tool Shadowing & Collision Detector in AgentSec."""

import pytest
import json
from pathlib import Path
from agentsec.shadowing import detect_tool_shadowing
from agentsec.scanner import Scanner


def test_detect_tool_shadowing_direct():
    servers = [
        {
            "name": "filesystem-trusted",
            "file": "mcp.json",
            "tools": ["read_file", "write_file", "list_dir"]
        },
        {
            "name": "untrusted-extension",
            "file": "claude_desktop_config.json",
            "tools": ["read_file", "custom_log"]
        }
    ]
    findings = detect_tool_shadowing(servers)
    assert len(findings) == 1
    f = findings[0]
    assert f["code"] == "AGENT050"
    assert f["severity"] == "high"
    assert "read_file" in f["description"]
    assert "filesystem-trusted" in f["description"]
    assert "untrusted-extension" in f["description"]


def test_no_shadowing_when_tools_are_distinct():
    servers = [
        {
            "name": "fs-server",
            "file": "mcp.json",
            "tools": ["read_file", "write_file"]
        },
        {
            "name": "db-server",
            "file": "mcp.json",
            "tools": ["query_sql", "execute_sql"]
        }
    ]
    findings = detect_tool_shadowing(servers)
    assert len(findings) == 0


def test_shadowing_scanner_integration(tmp_path):
    config = {
        "mcpServers": {
            "server1": {
                "command": "python",
                "args": ["s1.py"],
                "tools": ["ping", "execute_task"]
            },
            "server2": {
                "command": "node",
                "args": ["s2.js"],
                "tools": ["execute_task", "healthcheck"]
            }
        }
    }
    p = tmp_path / "mcp.json"
    p.write_text(json.dumps(config))

    scanner = Scanner(tmp_path)
    findings = scanner.scan()
    shadow = [f for f in findings if f["code"] == "AGENT050"]
    assert len(shadow) == 1
    assert "execute_task" in shadow[0]["description"]
