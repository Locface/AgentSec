# OWASP Mapping

Every AgentSec rule maps to the **OWASP Top 10 for LLM Applications** (LLM01–10) and/or the **OWASP Agentic Security Top 10** (AG01–10).

## OWASP Top 10 for LLM Applications

| ID | Category | AgentSec Rules |
|----|----------|----------------|
| **LLM01** | Prompt Injection | Prompt injection risk, Suspicious tool description, Prompt injection in markdown, Missing input validation |
| **LLM02** | Insecure Output Handling | Secret exposure, Sensitive file reference, Environment variable exposure, Credential helper access |
| **LLM03** | Training Data Poisoning | *(not applicable — pure static analysis)* |
| **LLM04** | Model Denial of Service | *(not applicable)* |
| **LLM05** | Supply Chain | Unpinned dependency, Remote script install, Vulnerable dependency pattern, Unknown/untrusted source, Package manager execution |
| **LLM06** | Code Injection | MCP shell execution, Dynamic code execution, Insecure default command, Package manager execution |
| **LLM07** | Insecure Plugin Design | Wildcard tool allowlist, MCP OAuth broad scopes, Excessive autonomy, No policy file |
| **LLM08** | Vector Communication (Excessive Agency) | MCP filesystem write access, Broad path access, Network + filesystem access, Web + filesystem access, Read repo + network, Claude Desktop MCP risks, Cursor agent dangerous permissions, Codex/Cline unrestricted tools, Browser automation + local files, Read-only filesystem |
| **LLM09** | Misinformation | *(not applicable)* |
| **LLM10** | Unbounded Consumption | *(not applicable)* |

## OWASP Agentic Security Top 10

| ID | Category | AgentSec Rules |
|----|----------|----------------|
| **AG01** | Agency Overreach | MCP filesystem write, Broad path access, Wildcard tool allowlist, Excessive autonomy, Claude Desktop/Cursor/Codex risks |
| **AG02** | Unauthorized Execution | MCP shell execution, Dynamic code execution, Insecure default command, Docker socket access, Container privileged mode |
| **AG03** | Data Exfiltration | Network + filesystem, Web + filesystem, Read repo + network, Communication tool write, Database write/delete, Browser + local files |
| **AG04** | Insecure Composition | MCP server with multiple capabilities (network + filesystem), Host mount exposure |
| **AG05** | Confused Deputy | Suspicious tool description, Prompt injection, Missing input validation |
| **AG06** | Supply Chain | Unpinned dependency, Remote script install, Unknown source, Vulnerable dependency pattern, Package manager execution |
| **AG07** | Credential Abuse | Secret exposure, Environment variable exposure, Sensitive file reference, GitHub token exposure, Credential helper access |
| **AG08** | Privilege Escalation | Docker socket access, Container privileged mode, Host mount exposure |
| **AG09** | Denial of Service | *(not applicable)* |
| **AG10** | Audit & Accountability | No policy file, Telemetry endpoint |

## View mapping at runtime

```bash
agentsec scan . --show-owasp
```

Output includes the OWASP ID for each finding:

```
[CRITICAL] LLM06 MCP shell execution
  OWASP: LLM06 (Code Injection), AG02 (Unauthorized Execution)

[CRITICAL] LLM08 MCP filesystem write access
  OWASP: LLM08 (Vector Communication), AG01 (Agency Overreach)
```

JSON and SARIF output always include OWASP mapping regardless of the `--show-owasp` flag.

## Source

The mapping is defined in [`agentsec/owasp.py`](https://github.com/locface/AgentSec/blob/main/agentsec/owasp.py).
