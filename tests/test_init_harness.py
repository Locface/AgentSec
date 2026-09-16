"""Tests for init-harness command and CLI flags --suggest-fixes & --format html."""

import json
from pathlib import Path
from click.testing import CliRunner
from agentsec.cli import cli
from agentsec.harness import init_security_harness, HARNESS_FILES


def test_init_security_harness_creates_all_files(tmp_path: Path):
    res = init_security_harness(tmp_path, force=False)
    assert len(res["created"]) == len(HARNESS_FILES)
    assert len(res["skipped"]) == 0

    for filename in HARNESS_FILES:
        filepath = tmp_path / filename
        assert filepath.is_file(), f"File {filename} was not created"
        content = filepath.read_text(encoding="utf-8")
        assert len(content) > 10


def test_init_security_harness_skips_without_force(tmp_path: Path):
    # First init
    init_security_harness(tmp_path, force=False)
    # Second init without force
    res2 = init_security_harness(tmp_path, force=False)
    assert len(res2["created"]) == 0
    assert len(res2["skipped"]) == len(HARNESS_FILES)


def test_init_security_harness_overwrites_with_force(tmp_path: Path):
    init_security_harness(tmp_path, force=False)
    res_force = init_security_harness(tmp_path, force=True)
    assert len(res_force["created"]) == len(HARNESS_FILES)
    assert len(res_force["skipped"]) == 0


def test_cli_init_harness_command(tmp_path: Path):
    runner = CliRunner()
    result = runner.invoke(cli, ["init-harness", str(tmp_path)])
    assert result.exit_code == 0
    assert "Initialized AgentSec Security Harness" in result.output
    assert (tmp_path / ".agentsec.yaml").exists()


def test_cli_scan_suggest_fixes(tmp_path: Path):
    bad_config = {
        "mcpServers": {
            "shell": {
                "command": "bash",
                "args": ["-c", "echo test"]
            }
        }
    }
    (tmp_path / "claude_desktop_config.json").write_text(json.dumps(bad_config), encoding="utf-8")

    runner = CliRunner()
    result = runner.invoke(cli, ["scan", str(tmp_path), "--suggest-fixes"])
    assert result.exit_code == 0
    assert "AGENT001" in result.output
    assert "Fix: Replace raw shell interpreter" in result.output
    assert "Suppression (.agentsecignore):" in result.output


def test_cli_scan_format_html(tmp_path: Path):
    bad_config = {
        "mcpServers": {
            "shell": {
                "command": "bash",
                "args": ["-c", "echo test"]
            }
        }
    }
    (tmp_path / "claude_desktop_config.json").write_text(json.dumps(bad_config), encoding="utf-8")

    runner = CliRunner()
    result = runner.invoke(cli, ["scan", str(tmp_path), "--format", "html"])
    assert result.exit_code == 0
    assert "<!DOCTYPE html>" in result.output
    assert "AgentSec" in result.output
    assert "AGENT001" in result.output
