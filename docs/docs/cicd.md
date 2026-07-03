# CI/CD Integration

## GitHub Actions

Add AgentSec to your GitHub workflow to automatically scan MCP configs and AI agent settings on every PR.

### Basic workflow

```yaml
name: AgentSec Security Scan
on: [push, pull_request]

jobs:
  agentsec:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install AgentSec
        run: pip install agentsec

      - name: Run AgentSec scan
        run: agentsec scan . --format sarif > results.sarif

      - name: Upload SARIF to GitHub CodeQL
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: results.sarif
```

### With fail-on gate

```yaml
- name: Run AgentSec (fail on high+)
  run: agentsec scan . --fail-on high
```

This exits with code 1 if any high or critical finding is detected, failing the workflow.

### With baseline comparison

For regressions only:

```yaml
- name: Run AgentSec with baseline
  run: |
    agentsec scan . --baseline baseline.json --format sarif > results.sarif
  continue-on-error: true
```

## GitLab CI

```yaml
agentsec-scan:
  image: python:3.12
  script:
    - pip install agentsec
    - agentsec scan . --format json > agentsec-report.json
    - agentsec scan . --fail-on high
  artifacts:
    paths:
      - agentsec-report.json
```

## Pre-commit (coming soon)

AgentSec will support pre-commit hooks for local scans before commit:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/locface/AgentSec
    rev: v0.1.0
    hooks:
      - id: agentsec
```

## Output format reference

| Format | Use case |
|--------|----------|
| `terminal` | Local development, quick checks |
| `json` | Custom pipelines, data processing |
| `sarif` | GitHub CodeQL, GitHub Advanced Security |
| `markdown` | Reports, PR comments, wikis |

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | No findings at threshold |
| 1 | Findings at or above `--fail-on` severity, or new/changed findings vs baseline |
