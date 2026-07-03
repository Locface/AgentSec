# Usage

## Basic scan

```bash
agentsec scan /path/to/project
```

Scans the directory for AI agent configs and MCP manifests, then prints findings to the terminal.

## Output formats

```bash
agentsec scan . --format json          # JSON for automation
agentsec scan . --format markdown      # Markdown report
agentsec scan . --format sarif         # SARIF for GitHub CodeQL
agentsec scan . --format terminal      # Human-readable (default)
```

### Terminal output example

```
 Scanning /home/dev/mcp-project...

[CRITICAL] MCP shell execution
  File: claude_desktop_config.json
  Server: shell-server
  Description: MCP server can execute shell commands
  Recommendation: Require explicit approval or remove shell access.

Total findings: 4 · Critical: 3 · High: 1 · Medium: 0 · Low: 0
```

## Severity filtering

```bash
agentsec scan . --severity critical    # Only critical findings
agentsec scan . --severity high        # Critical + high
agentsec scan . --severity all         # All (default)
```

## OWASP mapping

Show OWASP Top 10 for LLM and OWASP Agentic Security IDs for each finding:

```bash
agentsec scan . --show-owasp
```

Output:

```
[CRITICAL] LLM06 MCP shell execution
  OWASP: LLM06 (Code Injection), AG02 (Unauthorized Execution)
```

## CI/CD gating

Exit with code 1 if any finding is at least the specified severity:

```bash
agentsec scan . --fail-on high
agentsec scan . --fail-on critical
```

Useful for CI pipelines — prevents merging if dangerous configs are detected.

## Baseline (lockfile)

Save current findings as baseline:

```bash
agentsec scan . --update-baseline baseline.json
```

Compare against a baseline in later scans:

```bash
agentsec scan . --baseline baseline.json
```

Reports new, changed, and removed findings. Exits with code 1 on new or changed findings.

## Hidden files

Scan hidden files and directories (`.env`, `.ssh`, `.git/config`):

```bash
agentsec scan . --include-hidden
```

## CLI reference

| Option | Description |
|--------|-------------|
| `path` | Directory to scan |
| `-f, --format` | Output format: terminal, json, markdown, sarif |
| `--severity` | Minimum severity: critical, high, medium, low, all |
| `--fail-on` | Exit with code 1 if finding >= this severity |
| `--include-hidden` | Include hidden files and directories |
| `--baseline` | Path to baseline JSON for comparison |
| `--update-baseline` | Save current findings as baseline JSON |
| `--show-owasp` | Show OWASP mapping IDs for each finding |
