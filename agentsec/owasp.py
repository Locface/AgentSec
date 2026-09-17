"""OWASP Top 10 for LLM Applications and OWASP Agentic Security mappings.

Maps AgentSec rules to standard industry frameworks:
- OWASP Top 10 for LLM Applications (2025): LLM01–LLM10
- OWASP Agentic Security Top 10 (2025/2026): AG01–AG10
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
RULE_OWASP_MAP = {
    # === Base rules (AGENT001–AGENT010) ===
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
    # === Additional rules (AGENT011–AGENT045) ===
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
    "Insecure remote MCP transport": [
        ("AG01", "Insecure Agent-to-Agent Communication"),
        ("LLM07", "Insecure Plugin/Extension Design"),
    ],
    "Unbounded resource execution": [
        ("AG04", "Task Delegation Abuse"),
        ("LLM06", "Excessive Agency"),
    ],
    "Unsanitized agent hook execution": [
        ("AG02", "Unauthorized Tool Access"),
        ("LLM06", "Excessive Agency"),
    ],
    "Prompt and secret leakage in telemetry": [
        ("LLM02", "Sensitive Information Disclosure"),
        ("AG05", "Memory/Prompt Leakage"),
    ],
    "SSRF vulnerability via agent network tools": [
        ("LLM04", "Data Leakage via External Services"),
        ("AG02", "Unauthorized Tool Access"),
    ],
    "Runtime instruction hijacking risk": [
        ("LLM01", "Prompt Injection"),
        ("AG08", "Agent Workflow Manipulation"),
    ],
    "Unsupervised destructive action": [
        ("LLM08", "Excessive Permissions"),
        ("AG02", "Unauthorized Tool Access"),
    ],
    # === AST & Shadowing rules (AGENT046–AGENT050) ===
    "Arbitrary code execution in tool handler": [
        ("LLM06", "Excessive Agency"),
        ("AG02", "Unauthorized Tool Access"),
    ],
    "Unsanitized shell invocation in tool code": [
        ("LLM06", "Excessive Agency"),
        ("AG02", "Unauthorized Tool Access"),
    ],
    "Insecure deserialization in tool handler": [
        ("LLM08", "Excessive Permissions"),
        ("AG07", "Output Validation Failure"),
    ],
    "Hardcoded cloud metadata SSRF in agent tool": [
        ("LLM04", "Data Leakage via External Services"),
        ("AG05", "Memory/Prompt Leakage"),
    ],
    "Tool shadowing & naming collision": [
        ("AG03", "Agent Impersonation"),
        ("AG08", "Agent Workflow Manipulation"),
    ],
    "Docker socket mount in agent container": [
        ("LLM08", "Excessive Permissions"),
        ("AG10", "Privilege Escalation"),
    ],
    "Privileged container execution": [
        ("LLM08", "Excessive Permissions"),
        ("AG10", "Privilege Escalation"),
    ],
    "Insecure browser sandbox flags in MCP": [
        ("LLM07", "Insecure Plugin/Extension Design"),
        ("AG02", "Unauthorized Tool Access"),
    ],
    "Exposed browser remote debugging port": [
        ("LLM06", "Excessive Agency"),
        ("AG02", "Unauthorized Tool Access"),
    ],
    "CI/CD workflow modification directive": [
        ("LLM06", "Excessive Agency"),
        ("AG08", "Agent Workflow Manipulation"),
    ],
    "Git hook tampering directive": [
        ("LLM06", "Excessive Agency"),
        ("AG10", "Privilege Escalation"),
    ],
    "Plaintext vector DB / memory store credentials": [
        ("LLM02", "Sensitive Information Disclosure"),
        ("AG05", "Memory/Prompt Leakage"),
    ],
}

RULE_CODE_MAP = {
    "AGENT001": "MCP shell execution",
    "AGENT002": "MCP filesystem write access",
    "AGENT003": "Secret exposure",
    "AGENT004": "Broad path access",
    "AGENT005": "Prompt injection risk",
    "AGENT006": "Sensitive file reference",
    "AGENT007": "Excessive autonomy",
    "AGENT008": "Unpinned dependency",
    "AGENT009": "Remote script install",
    "AGENT010": "Docker socket access",
    "AGENT011": "Network + filesystem access",
    "AGENT012": "Suspicious tool description",
    "AGENT013": "GitHub token exposure",
    "AGENT014": "Communication tool write permission",
    "AGENT015": "Database write/delete permission",
    "AGENT016": "Excessive autonomy instruction",
    "AGENT017": "Prompt injection in markdown",
    "AGENT018": "MCP OAuth broad scopes",
    "AGENT019": "Web + filesystem access",
    "AGENT020": "Read repo + network",
    "AGENT021": "Unknown/untrusted source",
    "AGENT022": "No policy file",
    "AGENT023": "Cursor agent config with dangerous permissions",
    "AGENT024": "Claude Desktop config with MCP server risks",
    "AGENT025": "Codex/Cline agent with unrestricted tools",
    "AGENT026": "Environment variable exposure",
    "AGENT027": "Vulnerable dependency pattern",
    "AGENT028": "Insecure default command",
    "AGENT029": "Read-only file system in MCP server",
    "AGENT030": "Missing input validation",
    "AGENT031": "Package manager execution",
    "AGENT032": "Container privileged mode",
    "AGENT033": "Host mount exposure",
    "AGENT034": "Browser automation with local file access",
    "AGENT035": "Dynamic code execution",
    "AGENT036": "Wildcard tool allowlist",
    "AGENT037": "Telemetry or analytics endpoint",
    "AGENT038": "Credential helper access",
    "AGENT039": "Insecure remote MCP transport",
    "AGENT040": "Unbounded resource execution",
    "AGENT041": "Unsanitized agent hook execution",
    "AGENT042": "Prompt and secret leakage in telemetry",
    "AGENT043": "SSRF vulnerability via agent network tools",
    "AGENT044": "Runtime instruction hijacking risk",
    "AGENT045": "Unsupervised destructive action",
    "AGENT046": "Arbitrary code execution in tool handler",
    "AGENT047": "Unsanitized shell invocation in tool code",
    "AGENT048": "Insecure deserialization in tool handler",
    "AGENT049": "Hardcoded cloud metadata SSRF in agent tool",
    "AGENT050": "Tool shadowing & naming collision",
    "AGENT051": "Docker socket mount in agent container",
    "AGENT052": "Privileged container execution",
    "AGENT053": "Insecure browser sandbox flags in MCP",
    "AGENT054": "Exposed browser remote debugging port",
    "AGENT055": "CI/CD workflow modification directive",
    "AGENT056": "Git hook tampering directive",
    "AGENT057": "Plaintext vector DB / memory store credentials",
}


def get_owasp(key: str) -> list:
    """Return OWASP mappings for a rule name or rule code. Returns [(owasp_id, category_name), ...] or empty list."""
    if key in RULE_OWASP_MAP:
        return RULE_OWASP_MAP[key]
    if key in RULE_CODE_MAP:
        return RULE_OWASP_MAP.get(RULE_CODE_MAP[key], [])
    return []


def get_owasp_ids(key: str) -> str:
    """Return OWASP IDs as a comma-separated string (e.g. 'LLM06, AG02')."""
    mappings = get_owasp(key)
    return ", ".join(owasp_id for owasp_id, _ in mappings)


def format_owasp(key: str) -> str:
    """Format OWASP info for terminal output: '[LLM06, AG02]' or empty string."""
    mappings = get_owasp(key)
    if not mappings:
        return ""
    ids = ", ".join(f"{owasp_id}" for owasp_id, _ in mappings)
    return f"[{ids}]"
