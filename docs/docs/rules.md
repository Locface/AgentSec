# Security Rules

AgentSec ships with **41 security rules** covering the full spectrum of AI agent risks.

## Severity levels

| Severity | Meaning |
|----------|---------|
| **Critical** | Immediate RCE, privilege escalation, or data exfiltration risk |
| **High** | Significant attack surface expansion or supply-chain risk |
| **Medium** | Misconfiguration that increases attack surface |
| **Low** | Missing best practices or policy |

## Rules reference

### Shell execution

| Rule | Severity | Description |
|------|----------|-------------|
| MCP shell execution | Critical | MCP server can execute shell commands |
| Insecure default command | Critical | Uses eval, exec, or dangerous command-line flags |
| Dynamic code execution | Critical | Agent or MCP server can dynamically evaluate code |
| Package manager execution | High | Invokes npx, uvx, pipx — packages can run install scripts |

### Filesystem access

| Rule | Severity | Description |
|------|----------|-------------|
| MCP filesystem write access | Critical | MCP server can write, edit, or delete files |
| Broad path access | High | Filesystem access to root (`/`) or home (`~`) |
| Read-only filesystem | Medium | Read-only access can still leak sensitive files |
| Network + filesystem access | Critical | Can both read/write files and make network requests (exfiltration) |
| Web + filesystem access | High | Can browse web and write files |
| Read repo + network | High | Can read repo files and send network requests |

### Secrets & credentials

| Rule | Severity | Description |
|------|----------|-------------|
| Secret exposure | Critical | Environment variables with API keys, tokens, secrets |
| Environment variable exposure | Critical | Config exposes env vars like AWS_, OPENAI_, GITHUB_ |
| Sensitive file reference | High | References .env, id_rsa, .ssh, credentials |
| Credential helper access | High | References credential stores or auth helpers |
| GitHub token exposure | High | GitHub token or actions:write permission detected |

### Agent-specific risks

| Rule | Severity | Description |
|------|----------|-------------|
| Claude Desktop MCP risks | High | Risky shell/filesystem/network in Claude Desktop config |
| Cursor agent dangerous permissions | High | Cursor agent with shell, write, or network access |
| Codex/Cline unrestricted tools | High | Unrestricted access to tools in Codex or Cline config |
| Browser automation + local files | High | Combines browser automation with local file access |

### Prompt injection

| Rule | Severity | Description |
|------|----------|-------------|
| Prompt injection risk | Medium | Instructions contain prompt injection phrases |
| Prompt injection in markdown | Medium | Markdown files with system-level directives |
| Suspicious tool description | High | Tool descriptions with instruction-like language |
| Missing input validation | Medium | Lacks input validation for injection prevention |

### Access control

| Rule | Severity | Description |
|------|----------|-------------|
| Docker socket access | Critical | MCP server can access the Docker socket |
| Container privileged mode | Critical | Container may run with elevated host privileges |
| Host mount exposure | Critical | Container mounts sensitive host directories |
| Wildcard tool allowlist | High | Allows all tools via `*` or `allow_all` |
| Excessive autonomy | Medium | Agent told to never ask for confirmation |
| MCP OAuth broad scopes | Medium | Overly broad OAuth scopes (`*`, `admin`) |
| No policy file | Low | No local security policy file defined |

### Supply-chain

| Rule | Severity | Description |
|------|----------|-------------|
| Remote script install | High | `curl | bash` or `wget | sh` pattern |
| Unpinned dependency | Medium | Dependency not pinned to a specific version |
| Vulnerable dependency pattern | Medium | Uses known vulnerable version patterns |
| Unknown/untrusted source | Medium | Package from raw.githubusercontent, gist, pastebin |

### Communication

| Rule | Severity | Description |
|------|----------|-------------|
| Communication tool write | High | Can send messages to Slack, email, GitHub (data leak) |
| Database write/delete | High | Can modify or delete database records |
| Telemetry endpoint | Medium | References telemetry or analytics endpoints |

## Rule detection logic

Rules use content-based pattern matching. Each rule has a set of `detect_patterns` — substrings that trigger the finding.

For rules with `all_patterns`, ALL patterns must be present in the content (AND logic). For standard rules, ANY pattern triggers (OR logic).

### How to add custom rules

Rules are defined in `agentsec/rules/`. To add a custom rule:

1. Create a `Rule` object with name, severity, description, recommendation, and patterns
2. Register it in `load_additional_rules()` in `agentsec/rules/additional.py`

See [`agentsec/rules/base.py`](https://github.com/locface/AgentSec/blob/main/agentsec/rules/base.py) for the `Rule` class definition.
