<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/locface/AgentSec/main/docs/images/agentsec-dark.svg">
  <img alt="AgentSec" src="https://raw.githubusercontent.com/locface/AgentSec/main/docs/images/agentsec-light.svg">
</picture>

# AgentSec

**Static security scanner for AI coding agents and MCP configurations.**

[![PyPI](https://img.shields.io/pypi/v/agentsec-cli.svg)](https://pypi.org/project/agentsec-cli/)
[![Python](https://img.shields.io/pypi/pyversions/agentsec-cli.svg)](https://pypi.org/project/agentsec-cli/)
[![License](https://img.shields.io/github/license/locface/AgentSec)](LICENSE)
[![Tests](https://img.shields.io/github/actions/workflow/status/locface/AgentSec/agentsec.yml?label=tests)](https://github.com/locface/AgentSec/actions)

AI coding agents have access to your shell, filesystem, network, and secrets. Most agent configurations are never audited for security risks. AgentSec inspects MCP server manifests, Claude Desktop configs, Cursor rules, and agent instruction files for dangerous permissions, prompt injection risks, and secret exposure — with no LLM dependencies and no data leaving your machine.

All findings map to [OWASP Top 10 for LLM Applications](https://genai.owasp.org/) (LLM01–LLM10) and the [OWASP Agentic Security Top 10](https://owasp.org/) (AG01–AG10).

## Features

- 41 security rules covering shell execution, filesystem access, network exfiltration, OAuth scopes, prompt injection, container escape, and credential exposure
- OWASP LLM + Agentic mapping on every finding
- 4 output formats: terminal, JSON, Markdown, SARIF v2.1.0
- CI/CD gating with `--fail-on` (exit code 1 at severity threshold)
- Baseline comparison for regression tracking
- Automatic detection of JSON, YAML, TOML, and Markdown configs
- Zero runtime dependencies beyond the Python standard library

## Installation

```bash
pip install agentsec-cli
```

Requires Python 3.10 or later.

## Quick Start

```bash
# Scan a project
agentsec scan /path/to/project

# Generate SARIF for CI/CD
agentsec scan . --format sarif > results.sarif

# Gate CI on critical findings
agentsec scan . --fail-on critical

# Baseline comparison
agentsec scan . --update-baseline baseline.json
agentsec scan . --baseline baseline.json

# OWASP mapping
agentsec scan . --show-owasp
```

Example output:

```text
 Scanning /home/user/dev/mcp-project...

[CRITICAL] MCP shell execution
  File: claude_desktop_config.json
  Server: shell-server
  Description: MCP server can execute shell commands
  Recommendation: Require explicit approval or remove shell access.

[CRITICAL] MCP filesystem write access
  File: claude_desktop_config.json
  Server: filesystem
  Description: MCP server has filesystem write access
  Recommendation: Restrict filesystem access to read-only or specific directories.

Total findings: 4 · Critical: 3 · High: 0 · Medium: 1 · Low: 0
```

### Output Formats

- **terminal** (default) — human-readable with severity coloring
- **json** — machine-parseable JSON array of findings
- **markdown** — formatted report suitable for commit comments
- **sarif** — SARIF v2.1.0, compatible with GitHub CodeQL

### Supported Config Files

AgentSec automatically detects and scans these file types:

- MCP servers: `mcp.json`, `mcp.yaml`, `mcp.toml`
- Claude Desktop: `claude_desktop_config.json`
- Cursor: `.cursorrules`, `.cursor/rules/*`
- Codex / Cline: `codex.toml`, `.clinerules`
- Agent instructions: `AGENTS.md`, `CLAUDE.md`
- Infrastructure: `Dockerfile`, `package.json`

## Documentation

Full documentation: [https://locface.github.io/AgentSec/docs/](https://locface.github.io/AgentSec/docs/)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, testing, and pull request workflow.

## Security

Report vulnerabilities privately. See [SECURITY.md](SECURITY.md) for our disclosure policy.

## License

MIT — see [LICENSE](LICENSE).
