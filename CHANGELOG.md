# CHANGELOG

All notable changes to AgentSec will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Migrated versioning from manually-edited version strings to
  [`setuptools-scm`](https://setuptools-scm.readthedocs.io/). The Git tag is
  now the single source of truth: `pyproject.toml` no longer hardcodes a
  `version`, `agentsec/__init__.py` no longer hardcodes `__version__`, and
  `agentsec/sarif.py` no longer hardcodes the SARIF `tool.driver.version`.
  All three now derive from the current Git tag at build/install time via
  `agentsec/_version.py` (generated, gitignored).
- `agentsec --version` and the SARIF output's `tool.driver.version` now
  report the Git-derived version (exact tag on a tagged commit, e.g. `1.0.4`;
  a PEP 440 dev version like `1.0.4.dev5+gabcdef1` on untagged commits).
- Release process is now exactly: `git tag vX.Y.Z && git push origin main --tags`.
  No file edits are required to cut a release — CI builds, validates,
  publishes to PyPI, and creates the GitHub Release automatically from the tag.
- `.github/workflows/agentsec.yml`: `actions/checkout` now uses
  `fetch-depth: 0` in the `test` and `build` jobs so `setuptools-scm` can see
  the full tag history; added a step verifying the built wheel/sdist
  filenames match the pushed tag exactly.

## [1.0.3] - 2026-07-03

### Fixed
- Recovered local development history that had never been pushed to GitHub (remote `main` only contained the LICENSE file). Realigned local repo as the canonical history.
- Corrected version drift: PyPI had `1.0.1` published manually (out-of-band of CI/CD), local files were on `1.0.2` and never tagged or released through the pipeline. Bumped to `1.0.3` as a clean, tagged, pipeline-published baseline.

## [1.0.2] - 2026-07-02

### Fixed
- Fixed SARIF spec version (`sarif["version"]` was accidentally set to `1.0.1` instead of `2.1.0`). This broke compatibility with all SARIF consumers including GitHub CodeQL.

## [1.0.1] - 2026-07-02

### Fixed
- Fixed version number in SARIF output (was 1.0.0, now 1.0.1)
- Fixed CI workflow: removed duplicate install steps, added fail-fast, fixed Python matrix
- Fixed publish workflow: added package validation (wheel install + version check), fixed fail-fast, added Python compatibility check
- Fixed duplicated dependencies in pyproject.toml (already correct)
- Fixed version inconsistency across files

### Changed
- Updated version to 1.0.1 in pyproject.toml, agentsec/__init__.py, agentsec/sarif.py

## [1.0.0] - 2026-07-02

### Added

- Initial public release.
- 41 security rules for MCP, Cursor, Claude Desktop, Codex, Cline, and Continue configurations.
- CLI interface with `scan` command.
- Output formats: terminal, JSON, SARIF, Markdown.
- OWASP Top 10 for LLM Applications (LLM01–LLM10) mapping on every rule.
- OWASP Agentic Security Top 10 (AG01–AG10) mapping on applicable rules.
- CI/CD gating with `--fail-on critical|high|medium|low`.
- Baseline/lockfile support with `--baseline` and `--update-baseline`.
- SARIF v2.1.0 output for GitHub CodeQL integration.
- Support for JSON, YAML, TOML, Markdown config files.
- Automatic detection of MCP server manifests, Claude Desktop configs, Cursor rules, Codex configs, Cline configs, and agent instruction files.
- MkDocs documentation (installation, usage, rules reference, OWASP mapping, FAQ, CI/CD).
- Landing page at https://locface.github.io/AgentSec/.
- PyPI package `agentsec-cli`.

### Security

- Every security rule is mapped to industry-standard OWASP frameworks.
- No LLM dependencies — purely static analysis, zero data leakage.
