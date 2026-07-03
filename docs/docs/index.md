# AgentSec Documentation

**AgentSec** is a static security scanner for AI agent configurations. It detects dangerous permissions, prompt injection risks, secret exposure, and unsafe tool access in:

- **MCP** (Model Context Protocol) server manifests
- **Cursor** agent configurations
- **Claude Desktop** MCP setups
- **Codex** / **Cline** / **Continue** agent configs
- **Markdown** instruction files (CLAUDE.md, AGENTS.md, .cursorrules)

No LLM calls — pure static analysis. Every rule maps to OWASP Top 10 for LLM and OWASP Agentic Security standards.

---

## Quick Start

```bash
pip install agentsec
agentsec scan /path/to/project
```

## Key Features

| Feature | Description |
|---------|-------------|
| **41 rules** | Shell execution, filesystem access, secret exposure, prompt injection, supply-chain |
| **Multi-format** | JSON, YAML, TOML, Markdown, Dockerfile |
| **OWASP mapped** | Every rule maps to OWASP LLM Top 10 and Agentic Security Top 10 |
| **CI/CD ready** | SARIF, JSON, `--fail-on` gates, baseline comparison |
| **Zero LLM** | No API calls, no costs, no data leaks |

## Research

We scanned 50 public GitHub repositories with MCP configs and found **340 security issues** (83 critical, 172 high). [Read the full research](https://github.com/locface/AgentSec/blob/main/RESEARCH_GITHUB.md).
