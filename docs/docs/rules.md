# Security Rules Reference

AgentSec ships with **45 security rules (AGENT001–AGENT045)** covering the full spectrum of AI agent risks, MCP configuration vulnerabilities, and autonomous execution hazards.

All rules map to the **OWASP Top 10 for LLM Applications (2025)** (LLM01–LLM10) and the **OWASP Agentic Security Top 10 (2026)** (AG01–AG10).

---

## Severity Levels

| Severity | Impact | Action Required |
|----------|--------|-----------------|
| **Critical** | Immediate RCE, arbitrary file write, secret leak, or autonomous shell execution | Block pipeline, remediate immediately |
| **High** | Significant attack surface expansion, SSRF, or broad privilege exposure | Fix before production deployment |
| **Medium** | Misconfiguration or unpinned dependencies increasing risk profile | Review and address according to policy |
| **Low** | Missing security policies or best practice deviation | Recommended configuration enhancement |

---

## Complete Rules Reference

| ID | Rule Name | Severity | Target Scope | OWASP Mapping | Description |
|---|---|---|---|---|---|
| **AGENT001** | MCP shell execution | Critical | MCP | LLM06, AG02 | MCP server can execute shell commands (`bash`, `sh`, `cmd`, etc.) |
| **AGENT002** | MCP filesystem write access | Critical | MCP | LLM08 | MCP server has filesystem write access (`server-filesystem`, `write`, `delete`) |
| **AGENT003** | Secret exposure | Critical | All | LLM02 | Config references API keys, secrets, or credential tokens |
| **AGENT004** | Broad path access | High | MCP, Container | LLM08 | MCP server or container has access to root (`/`) or user home (`~`, `/home`) |
| **AGENT005** | Prompt injection risk | Medium | Instructions | LLM01 | System instructions contain potential prompt injection phrases |
| **AGENT006** | Sensitive file reference | High | Instructions, MCP | LLM02 | References sensitive files (`.ssh`, `id_rsa`, `auth.json`) |
| **AGENT007** | Excessive autonomy | Medium | Instructions | LLM06, AG02 | Instructions request excessive autonomy (no user confirmation) |
| **AGENT008** | Unpinned dependency | Medium | MCP, Dependency | LLM03 | Dependency is not pinned to a specific version or hash |
| **AGENT009** | Remote script install | High | Instructions, MCP, Container | LLM03 | Config uses remote script pipe-to-shell pattern (`curl \| bash`) |
| **AGENT010** | Docker socket access | Critical | MCP, Container | LLM08, AG02 | Direct access to host Docker socket (`/var/run/docker.sock`) |
| **AGENT011** | Network + filesystem access | Critical | MCP | LLM04, AG05 | MCP server has both network and filesystem write capabilities (exfiltration) |
| **AGENT012** | Suspicious tool description | High | Instructions, MCP | LLM01, AG10 | Tool description contains override instructions or hidden prompt injection |
| **AGENT013** | GitHub token exposure | High | All | LLM02, AG02 | Exposure of `GITHUB_TOKEN` or elevated `actions:write` permissions |
| **AGENT014** | Communication tool write | High | Instructions, MCP | LLM04 | MCP tool can send messages to Slack, email, or GitHub (data leak) |
| **AGENT015** | Database write/delete | High | MCP | LLM08 | MCP server can modify or delete database records |
| **AGENT016** | Excessive autonomy directive | Medium | Instructions | LLM06 | Directives configured to run commands without asking confirmation |
| **AGENT017** | Prompt injection in markdown | Medium | Instructions | LLM01 | Markdown file contains prompt injection directives |
| **AGENT018** | MCP OAuth broad scopes | Medium | MCP | LLM07, AG06 | OAuth configuration grants broad wildcard (`*`) or admin scopes |
| **AGENT019** | Web + filesystem access | High | MCP | LLM04, LLM08 | Tool can fetch from web and write to local disk |
| **AGENT020** | Read repo + network | High | MCP | LLM04, AG05 | Tool can read repository files and make outbound network requests |
| **AGENT021** | Unknown/untrusted source | Medium | MCP, Instructions | LLM03 | Package loaded from raw URLs, gists, or pastebins |
| **AGENT022** | No policy file | Low | MCP | LLM09, AG06 | Project uses tools/MCP but lacks `.agentsec.yaml` policy file |
| **AGENT023** | Cursor dangerous permissions | High | Instructions | LLM08, AG02 | Cursor configuration grants combined shell, write, and network access |
| **AGENT024** | Claude Desktop MCP risks | High | MCP | LLM07 | Claude Desktop configuration contains unreviewed MCP servers |
| **AGENT025** | Codex/Cline unrestricted tools | High | Instructions | LLM08, AG02 | Codex or Cline agent has unrestricted access to system tools |
| **AGENT026** | Environment variable exposure | Critical | All | LLM02 | Configuration exposes environment variables containing sensitive secrets |
| **AGENT027** | Vulnerable dependency pattern | Medium | MCP, Dependency | LLM03 | Dependency uses version ranges known for breaking or vulnerable releases |
| **AGENT028** | Insecure default command | Critical | MCP, Container | LLM07 | Command invokes dynamic code execution flags (`-e`, `-c`, `eval`) |
| **AGENT029** | Read-only filesystem exposure | Medium | MCP | LLM08 | Read-only filesystem access can leak sensitive repository secrets |
| **AGENT030** | Missing input validation | Medium | Instructions, MCP | LLM05, AG07 | Configuration lacks input parameter validation parameters |
| **AGENT031** | Package manager execution | High | Instructions, MCP | LLM03 | Dynamic package execution via `npx`, `uvx`, `pipx` with install scripts |
| **AGENT032** | Container privileged mode | Critical | Container | LLM08, AG02 | Containerized MCP server runs in privileged mode or host network |
| **AGENT033** | Host mount exposure | Critical | Container, MCP | LLM08 | Container or MCP server mounts sensitive host directories |
| **AGENT034** | Browser automation + local files | High | Instructions, MCP | LLM04, AG05 | Browser automation tool paired with local filesystem read access |
| **AGENT035** | Dynamic code execution | Critical | Instructions, MCP | LLM06, AG10 | Agent or server can dynamically evaluate code (`eval`, `new Function`) |
| **AGENT036** | Wildcard tool allowlist | High | Instructions, MCP | LLM08 | Allowlist configured with wildcard (`*`), granting all tool access |
| **AGENT037** | Telemetry endpoint | Medium | Instructions, MCP | LLM04 | Telemetry or analytics endpoint that may ingest prompts/code |
| **AGENT038** | Credential helper access | High | Instructions, MCP | LLM02, AG02 | References credential helpers or system keystores |
| **AGENT039** | Insecure remote MCP transport | High | MCP | AG01, LLM07 | Remote MCP endpoint connects over cleartext HTTP or unencrypted ws:// |
| **AGENT040** | Unbounded resource execution | Medium | Instructions, MCP | AG04, LLM06 | Agent loop lacks iteration limit or execution timeouts (token bombing) |
| **AGENT041** | Unsanitized agent hook execution | High | Instructions, MCP | AG02, LLM06 | Dynamic shell hooks invoked on untrusted tool/agent outputs |
| **AGENT042** | Telemetry prompt leakage | High | Instructions, MCP | LLM02, AG05 | Telemetry explicitly captures full prompts and internal reasoning |
| **AGENT043** | SSRF via agent network tools | Critical | Instructions, MCP | LLM04, AG02 | Network tool configured to reach cloud metadata (`169.254.169.254`) |
| **AGENT044** | Runtime instruction hijacking | High | Instructions | LLM01, AG08 | Directives instruct agent to load instructions from dynamic URLs |
| **AGENT045** | Unsupervised destructive action | High | Instructions, MCP | LLM08, AG02 | Destructive file or database operations without Human-in-the-Loop review |

---

## Suppressing Findings

You can suppress findings either globally or per-file via `.agentsecignore`:

```gitignore
# Suppress rule globally
AGENT022

# Suppress rule for specific paths
tests/**: AGENT001, AGENT002
```

Or using inline comments:

```markdown
<!-- agentsec:ignore AGENT005 -->
```
