"""Tests for CLI --fail-on-score and --format markdown."""

import pytest
import json
from click.testing import CliRunner
from pathlib import Path
from agentsec.cli import cli


def test_cli_format_markdown(tmp_path):
    config = {
        "mcpServers": {
            "shell": {
                "command": "bash",
                "args": ["-c", "echo test"]
            }
        }
    }
    p = tmp_path / "mcp.json"
    p.write_text(json.dumps(config))

    runner = CliRunner()
    result = runner.invoke(cli, ["scan", str(tmp_path), "--format", "markdown"])
    assert result.exit_code == 0
    assert "# AgentSec Security Scan Report" in result.stdout
    assert "Security Score" in result.stdout
    assert "MCP shell execution" in result.stdout
    assert "| **CRITICAL** |" in result.stdout


def test_cli_fail_on_score_triggers_exit_1(tmp_path):
    config = {
        "mcpServers": {
            "shell": {
                "command": "bash",
                "args": ["-c", "echo test"]
            }
        }
    }
    p = tmp_path / "mcp.json"
    p.write_text(json.dumps(config))

    runner = CliRunner()
    # Threshold 80 should fail since score is 49
    result = runner.invoke(cli, ["scan", str(tmp_path), "--fail-on-score", "80"])
    assert result.exit_code == 1
    assert "Failing: Security Score" in result.output


def test_cli_fail_on_score_passes_if_above(tmp_path):
    # An empty workspace has score 100 (clean)
    runner = CliRunner()
    result = runner.invoke(cli, ["scan", str(tmp_path), "--fail-on-score", "90"])
    assert result.exit_code == 0
