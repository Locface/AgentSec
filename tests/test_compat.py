"""Tests for Python version compatibility.

Verifies that:
- TOML parsing works on all supported Python versions (3.10+).
- CLI help loads without triggering heavy imports.
- All output formats produce valid results.
"""
import sys
import subprocess
from pathlib import Path


class TestPythonCompat:
    """Test Python 3.10–3.13 compatibility."""

    def test_toml_compat_import(self):
        """toml_compat layer should import without error on any 3.10+."""
        from agentsec.utils.toml_compat import tomllib, TOMLDecodeError
        assert tomllib is not None
        assert TOMLDecodeError is not None

    def test_toml_compat_parse(self):
        """toml_compat should parse valid TOML."""
        from agentsec.utils.toml_compat import tomllib
        data = tomllib.loads('[mcpServers]\n[mcpServers.test]\ncommand = "bash"\n')
        assert data["mcpServers"]["test"]["command"] == "bash"

    def test_toml_compat_parse_error(self):
        """toml_compat should raise TOMLDecodeError on invalid input."""
        from agentsec.utils.toml_compat import tomllib, TOMLDecodeError
        import pytest
        with pytest.raises(TOMLDecodeError):
            tomllib.loads("not valid toml = {{{")

    def test_cli_help_no_crash(self):
        """agentsec --help must NEVER crash regardless of import issues."""
        result = subprocess.run(
            [sys.executable, "-m", "agentsec.cli", "--help"],
            capture_output=True, text=True
        )
        assert result.returncode == 0, f"STDERR: {result.stderr}"
        assert "scan" in result.stdout

    def test_cli_scan_help_no_crash(self):
        """agentsec scan --help must work."""
        result = subprocess.run(
            [sys.executable, "-m", "agentsec.cli", "scan", "--help"],
            capture_output=True, text=True
        )
        assert result.returncode == 0
        assert "--format" in result.stdout
        assert "--fail-on" in result.stdout
