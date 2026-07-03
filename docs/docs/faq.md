# FAQ

## What is AgentSec?

AgentSec is a static security scanner for AI agent configurations. It detects dangerous permissions, prompt injection risks, secret exposure, and unsafe tool access in MCP servers, Cursor, Claude Desktop, Codex, and Cline configurations.

## How is it different from other scanners?

| Feature | AgentSec | Others |
|---------|----------|--------|
| Zero LLM dependencies | ✅ Pure static analysis | ❌ Often require LLM API calls |
| OWASP mapping | ✅ All 41 rules mapped | ❌ Usually no security standard mapping |
| MCP-specific rules | ✅ 20+ MCP rules | ❌ Generic SAST tools miss agent context |
| CI/CD ready | ✅ SARIF, JSON, fail-on | Varies |
| Offline | ✅ No network needed | Varies |

## Does AgentSec use an LLM?

**No.** AgentSec is purely static pattern matching. No API calls, no model costs, no data leaks. It runs entirely offline.

## What files does AgentSec scan?

AgentSec auto-detects and scans:

- `mcp.json`, `mcp.yaml`, `mcp.yml`, `mcp.toml`, `mcp-config.json`
- `claude_desktop_config.json`, `CLAUDE.md`, `AGENTS.md`
- `.cursorrules`, `.cursor/rules/*`, `.clinerules`, `cline_mcp`
- `codex.toml`
- `settings.json`, `package.json`, `requirements.txt`
- `Dockerfile`, `docker-compose.yml`
- `.env`

## What does "critical" mean?

Critical severity means the finding represents an immediate and exploitable security risk — remote code execution, privilege escalation, secret exposure, or data exfiltration. These should be fixed before deploying any AI agent infrastructure.

## How do I suppress a false positive?

Use the baseline feature to suppress known findings:

```bash
# Create a baseline of current findings
agentsec scan . --update-baseline baseline.json

# Future scans compare against it
agentsec scan . --baseline baseline.json
```

Only new and changed findings will be reported.

## Can I add custom rules?

Yes. Rules are defined in `agentsec/rules/additional.py`. Each rule is a `Rule` object with:

- `name` — unique identifier
- `severity` — critical, high, medium, low
- `description` — what it detects
- `recommendation` — how to fix
- `detect_patterns` — strings to match in file content

## Is there a GitHub Action?

Yes, see the [CI/CD guide](cicd.md) for a complete workflow example with SARIF upload to GitHub CodeQL.

## Can AgentSec scan Docker images?

Currently AgentSec scans Dockerfiles and docker-compose.yml for dangerous configurations (privileged mode, host mounts, Docker socket access). Full container image scanning is not supported.

## What is OWASP mapping?

Every AgentSec rule is mapped to the [OWASP Top 10 for LLM Applications](https://genai.owasp.org/) (LLM01-10) and [OWASP Agentic Security Top 10](https://owasp.org/www-project-agentic-security/) (AG01-10). This helps teams align agent security with industry standards and compliance frameworks.

## Is it free?

Yes. AgentSec is open source under the MIT license.

## Can I use it commercially?

Yes. MIT license allows commercial use, modification, and distribution.

## How do I contribute?

1. Fork the [repository](https://github.com/locface/AgentSec)
2. Create a feature branch
3. Write tests
4. Submit a PR

See the repository README for development setup instructions.
