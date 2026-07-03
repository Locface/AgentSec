"""OWASP Top 10 for LLM Applications — rule mapping for AgentSec.

Maps each AgentSec rule to the relevant OWASP categories.

OWASP Top 10 for LLM Applications (2025):
https://genai.owasp.org/

LLM01 — Prompt Injection
LLM02 — Sensitive Information Disclosure
LLM03 — Supply Chain Vulnerabilities
LLM04 — Data Leakage via External Services
LLM05 — Insecure Output Handling
LLM06 — Excessive Agency / Unrestricted Autonomy
LLM07 — Insecure Plugin / Extension Design
LLM08 — Excessive Permissions / Overprivileged Access
LLM09 — Over-reliance / Insufficient Oversight
LLM10 — Model Theft / Intellectual Property Loss

OWASP Agentic Security Top 10 (2025):
AG01 — Insecure Agent-to-Agent Communication
AG02 — Unauthorized Tool Access
AG03 — Agent Impersonation
AG04 — Task Delegation Abuse
AG05 — Memory / Prompt Leakage
AG06 — Inconsistent Authorization
AG07 — Output Validation Failure
AG08 — Agent Workflow Manipulation
AG09 — Inadequate Audit Trail
AG10 — Privilege Escalation
"""

# Mapping: OWASP ID -> (short name, description)
OWASP_CATEGORIES = {
    "LLM01": ("Prompt Injection", "Attacker injects malicious instructions via user prompts or indirect inputs"),
    "LLM02": ("Sensitive Information Disclosure", "LLM or agent exposes sensitive data (secrets, PII, internal info)"),
    "LLM03": ("Supply Chain Vulnerabilities", "Compromised dependencies, packages, or third-party components"),
    "LLM04": ("Data Leakage via External Services", "Sensitive data exfiltrated through network calls, APIs, or integrations"),
    "LLM05": ("Insecure Output Handling", "Agent output is not validated before being used in downstream operations"),
    "LLM06": ("Excessive Agency", "Agent has more autonomy than necessary — can perform actions without oversight"),
    "LLM07": ("Insecure Plugin/Extension Design", "Plugins or extensions have weak security boundaries"),
    "LLM08": ("Excessive Permissions", "Agent or tool has overly broad filesystem/network/OS permissions"),
    "LLM09": ("Over-reliance / Insufficient Oversight", "No guardrails, audit, or policy enforcement for agent actions"),
    "LLM10": ("Model Theft / IP Loss", "Risk of proprietary model weights or IP extraction"),
    # Agentic Security
    "AG01": ("Insecure Agent-to-Agent Communication", "Agents communicate without proper authentication or encryption"),
    "AG02": ("Unauthorized Tool Access", "Agent can invoke tools or capabilities without proper authorization gates"),
    "AG03": ("Agent Impersonation", "Attacker impersonates a legitimate agent to gain access"),
    "AG04": ("Task Delegation Abuse", "Malicious tasks can be delegated to sub-agents without validation"),
    "AG05": ("Memory/Prompt Leakage", "Agent memory or prompt context can leak across sessions or users"),
    "AG06": ("Inconsistent Authorization", "Authorization policies are missing, incomplete, or not enforced"),
    "AG07": ("Output Validation Failure", "Agent output is not validated for safety or correctness"),
    "AG08": ("Agent Workflow Manipulation", "Attacker manipulates the agent's workflow or decision chain"),
    "AG09": ("Inadequate Audit Trail", "Agent actions are not logged or traceable"),
    "AG10": ("Privilege Escalation", "Agent can escalate its own privileges beyond intended scope"),
}

# Rule-to-OWASP mapping: rule_name -> list of (owasp_id, category_name)
# Covers all 41 rules from base.py + additional.py (deduplicated)
RULE_OWASP_MAP = {
    # === Base rules ===
    "MCP shell execution": [
        ("LLM06", "Excessive Agency"),
        ("AG02", "Unauthorized Tool Access"),
    ],
    "MCP filesystem write access": [
        ("LLM08", "Excessive Permissions"),
    ],
    "Secret exposure": [
        ("LLM02", "Sensitive Information Disclosure"),
    ],
    "Broad path access": [
        ("LLM08", "Excessive Permissions"),
    ],
    "Prompt injection risk": [
        ("LLM01", "Prompt Injection"),
    ],
    "Sensitive file reference": [
        ("LLM02", "Sensitive Information Disclosure"),
    ],
    "Excessive autonomy": [
        ("LLM06", "Excessive Agency"),
    ],
    "Unpinned dependency": [
        ("LLM03", "Supply Chain Vulnerabilities"),
    ],
    "Remote script install": [
        ("LLM03", "Supply Chain Vulnerabilities"),
    ],
    "Docker socket access": [
        ("LLM08", "Excessive Permissions"),
        ("AG02", "Unauthorized Tool Access"),
    ],
    # === Additional rules ===
    "Network + filesystem access": [
        ("LLM04", "Data Leakage via External Services"),
        ("AG05", "Memory/Prompt Leakage"),
    ],
    "Suspicious tool description": [
        ("LLM01", "Prompt Injection"),
        ("AG10", "Privilege Escalation"),
    ],
    "GitHub token exposure": [
        ("LLM02", "Sensitive Information Disclosure"),
        ("AG02", "Unauthorized Tool Access"),
    ],
    "Communication tool write permission": [
        ("LLM04", "Data Leakage via External Services"),
    ],
    "Database write/delete permission": [
        ("LLM08", "Excessive Permissions"),
    ],
    "Excessive autonomy instruction": [
        ("LLM06", "Excessive Agency"),
    ],
    "Prompt injection in markdown": [
        ("LLM01", "Prompt Injection"),
    ],
    "MCP OAuth broad scopes": [
        ("LLM07", "Insecure Plugin/Extension Design"),
        ("AG06", "Inconsistent Authorization"),
    ],
    "Web + filesystem access": [
        ("LLM04", "Data Leakage via External Services"),
        ("LLM08", "Excessive Permissions"),
    ],
    "Read repo + network": [
        ("LLM04", "Data Leakage via External Services"),
        ("AG05", "Memory/Prompt Leakage"),
    ],
    "Unknown/untrusted source": [
        ("LLM03", "Supply Chain Vulnerabilities"),
    ],
    "No policy file": [
        ("LLM09", "Over-reliance / Insufficient Oversight"),
        ("AG06", "Inconsistent Authorization"),
    ],
    "Cursor agent config with dangerous permissions": [
        ("LLM08", "Excessive Permissions"),
        ("AG02", "Unauthorized Tool Access"),
    ],
    "Claude Desktop config with MCP server risks": [
        ("LLM07", "Insecure Plugin/Extension Design"),
    ],
    "Codex/Cline agent with unrestricted tools": [
        ("LLM08", "Excessive Permissions"),
        ("AG02", "Unauthorized Tool Access"),
    ],
    "Environment variable exposure": [
        ("LLM02", "Sensitive Information Disclosure"),
    ],
    "Vulnerable dependency pattern": [
        ("LLM03", "Supply Chain Vulnerabilities"),
    ],
    "Insecure default command": [
        ("LLM07", "Insecure Plugin/Extension Design"),
    ],
    "Read-only file system in MCP server": [
        ("LLM08", "Excessive Permissions"),
    ],
    "Missing input validation": [
        ("LLM05", "Insecure Output Handling"),
        ("AG07", "Output Validation Failure"),
    ],
    "Package manager execution": [
        ("LLM03", "Supply Chain Vulnerabilities"),
    ],
    "Container privileged mode": [
        ("LLM08", "Excessive Permissions"),
        ("AG02", "Unauthorized Tool Access"),
    ],
    "Host mount exposure": [
        ("LLM08", "Excessive Permissions"),
    ],
    "Browser automation with local file access": [
        ("LLM04", "Data Leakage via External Services"),
        ("AG05", "Memory/Prompt Leakage"),
    ],
    "Dynamic code execution": [
        ("LLM06", "Excessive Agency"),
        ("AG10", "Privilege Escalation"),
    ],
    "Wildcard tool allowlist": [
        ("LLM08", "Excessive Permissions"),
    ],
    "Telemetry or analytics endpoint": [
        ("LLM04", "Data Leakage via External Services"),
    ],
    "Credential helper access": [
        ("LLM02", "Sensitive Information Disclosure"),
        ("AG02", "Unauthorized Tool Access"),
    ],
}


def get_owasp(rule_name: str) -> list:
    """Return OWASP mappings for a rule name. Returns [(owasp_id, category_name), ...] or empty list."""
    return RULE_OWASP_MAP.get(rule_name, [])


def get_owasp_ids(rule_name: str) -> str:
    """Return OWASP IDs as a comma-separated string (e.g. 'LLM06, AG02')."""
    mappings = get_owasp(rule_name)
    return ", ".join(owasp_id for owasp_id, _ in mappings)


def format_owasp(rule_name: str) -> str:
    """Format OWASP info for terminal output: '[LLM06, AG02]' or empty string."""
    mappings = get_owasp(rule_name)
    if not mappings:
        return ""
    ids = ", ".join(f"{owasp_id}" for owasp_id, _ in mappings)
    return f"[{ids}]"
