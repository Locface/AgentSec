#!/usr/bin/env python3
"""Guard against reintroducing manual package-version management.

AgentSec's version is derived exclusively from Git tags via setuptools-scm.
This script fails fast (non-zero exit) if pyproject.toml no longer reflects
that policy — e.g. someone reintroduces a hardcoded [project].version, drops
the `dynamic = ["version"]` declaration, or removes the
[tool.setuptools_scm] configuration.

Run manually:
    python scripts/check_version_policy.py

Run automatically: wired into .github/workflows/agentsec.yml on every push
and pull request, so a regression fails CI immediately rather than being
noticed at release time.
"""
import sys
from pathlib import Path

try:
    import tomllib
except ImportError:  # Python 3.10
    import tomli as tomllib


def main() -> int:
    pyproject_path = Path(__file__).resolve().parent.parent / "pyproject.toml"
    data = tomllib.loads(pyproject_path.read_text())
    project = data.get("project", {})

    errors = []

    if "version" in project:
        errors.append(
            '[project].version is hardcoded in pyproject.toml — remove it. '
            'Version must be declared dynamic = ["version"] and derived from '
            "the Git tag via setuptools-scm."
        )

    if "version" not in project.get("dynamic", []):
        errors.append('[project].dynamic must include "version".')

    if "setuptools_scm" not in data.get("tool", {}):
        errors.append("[tool.setuptools_scm] section is missing from pyproject.toml.")

    build_requires = str(data.get("build-system", {}).get("requires", []))
    if "setuptools-scm" not in build_requires and "setuptools_scm" not in build_requires:
        errors.append("[build-system].requires must include setuptools-scm.")

    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        print(
            "\nAgentSec versioning policy violated. Git tags are the single "
            "source of truth for the package version — see the 'Versioning "
            "& Releases' section in CONTRIBUTING.md.",
            file=sys.stderr,
        )
        return 1

    print("OK: pyproject.toml versioning policy is intact (Git-tag-derived via setuptools-scm)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
