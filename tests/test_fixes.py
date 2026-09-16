"""Tests for AgentSec automated remediation plans and patches."""

from agentsec.fixes import get_fix_plan, FIX_TEMPLATES


def test_get_fix_plan_known_rule():
    finding = {
        "code": "AGENT001",
        "rule": "MCP shell execution",
        "file": "claude_desktop_config.json",
        "recommendation": "Constrain shell access",
    }
    plan = get_fix_plan(finding)
    assert plan["title"] == "Constrain or Remove Unrestricted Shell Access"
    assert "bash/sh" in plan["action"]
    assert "patch" in plan
    assert "command" in plan["patch"]
    assert plan["suppression"] == "claude_desktop_config.json: AGENT001"


def test_get_fix_plan_ast_rule():
    finding = {
        "code": "AGENT046",
        "rule": "Dynamic Python Eval / Exec in Agent Tool",
        "file": "tools.py",
        "recommendation": "Use safe parsing",
    }
    plan = get_fix_plan(finding)
    assert "ast.literal_eval" in plan["patch"]
    assert plan["suppression"] == "tools.py: AGENT046"


def test_get_fix_plan_shadowing_rule():
    finding = {
        "code": "AGENT050",
        "rule": "MCP Tool Shadowing Detected",
        "file": "agent_config.json",
        "recommendation": "Namespace tools",
    }
    plan = get_fix_plan(finding)
    assert "Shadowing" in plan["title"]
    assert "server_name__read_file" in plan["patch"]


def test_get_fix_plan_unknown_fallback():
    finding = {
        "code": "AGENT999",
        "rule": "Custom Proprietary Check",
        "file": "custom.yaml",
        "recommendation": "Custom action required.",
    }
    plan = get_fix_plan(finding)
    assert "Custom Proprietary Check" in plan["title"]
    assert plan["action"] == "Custom action required."
    assert plan["suppression"] == "custom.yaml: AGENT999"
