"""Tests for setuptools-scm-based versioning.

These tests guard the migration away from manually-edited version strings:
Git tags are the single source of truth, and `agentsec/__init__.py` /
`agentsec/sarif.py` must always derive their version dynamically rather than
hardcoding a string that can drift from the actual release.
"""
import re
import subprocess
import sys

from agentsec import __version__
from agentsec.sarif import generate_sarif


def test_version_is_not_hardcoded_placeholder():
    """__version__ must resolve to something PEP 440-ish, not be empty/None."""
    assert __version__
    assert isinstance(__version__, str)
    # Loose PEP 440 sanity check: starts with a digit (release segment).
    assert re.match(r"^\d+(\.\d+)*", __version__), (
        f"__version__={__version__!r} does not look like a PEP 440 version "
        "(expected setuptools-scm-derived value)"
    )


def test_sarif_tool_version_matches_package_version():
    """SARIF output must report the same version as agentsec.__version__,
    not a separately hardcoded string that can drift out of sync."""
    sarif = generate_sarif([])
    assert sarif["runs"][0]["tool"]["driver"]["version"] == __version__


def test_cli_version_matches_package_version():
    """`agentsec --version` must report agentsec.__version__ exactly."""
    result = subprocess.run(
        [sys.executable, "-m", "agentsec.cli", "--version"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    assert __version__ in result.stdout


def test_pyproject_declares_dynamic_version():
    """pyproject.toml must not hardcode [project].version — it must be
    declared dynamic and sourced from setuptools-scm."""
    from pathlib import Path

    try:
        import tomllib
    except ImportError:  # Python 3.10
        import tomli as tomllib

    pyproject_path = Path(__file__).resolve().parent.parent / "pyproject.toml"
    data = tomllib.loads(pyproject_path.read_text())
    assert "version" not in data["project"], (
        "pyproject.toml must not hardcode [project].version; "
        "it must use dynamic = [\"version\"] with setuptools-scm"
    )
    assert "version" in data["project"].get("dynamic", [])
    assert "setuptools_scm" in data.get("tool", {}) or "setuptools-scm" in str(
        data.get("build-system", {}).get("requires", [])
    )
