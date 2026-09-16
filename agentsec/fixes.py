"""Remediation and Scoped Fix Engine for AgentSec findings.

Provides actionable code patches, remediation plans, and suppression directives
for every security rule. Inspired by modern Harness Engineering patterns.
"""

from typing import Dict, Any, Optional
from pathlib import Path


FIX_TEMPLATES: Dict[str, Dict[str, str]] = {
    "AGENT001": {
        "title": "Constrain or Remove Unrestricted Shell Access",
        "action": "Replace raw shell interpreter (bash/sh) with specific bounded CLI binaries, or enable human confirmation.",
        "patch": """// Before:
"command": "bash",
"args": ["-c", "..."]

// After (Scoped execution):
"command": "git",
"args": ["status"],
"require_confirmation": true""",
    },
    "AGENT002": {
        "title": "Restrict Filesystem Write Access Scope",
        "action": "Change root directory ('/') mount to an explicit project-relative workspace directory.",
        "patch": """// Before:
"args": ["-y", "@modelcontextprotocol/server-filesystem", "/"]

// After:
"args": ["-y", "@modelcontextprotocol/server-filesystem", "./workspace"]""",
    },
    "AGENT003": {
        "title": "Extract Hardcoded Secrets to Environment Variables",
        "action": "Replace plaintext credentials and tokens with dynamic environment references.",
        "patch": """// Before:
"env": { "API_KEY": "sk-proj-xxxxxxxxxxxx" }

// After:
"env": { "API_KEY": "${ANTHROPIC_API_KEY}" }""",
    },
    "AGENT004": {
        "title": "Constrain Broad Filesystem Paths",
        "action": "Restrict tool arguments from root/home paths to explicit subfolders.",
        "patch": """// Before:
"args": ["/home/user"]

// After:
"args": ["./src", "./docs"]""",
    },
    "AGENT039": {
        "title": "Enforce Encrypted TLS/WSS for Remote MCP Servers",
        "action": "Upgrade cleartext HTTP or unencrypted WebSocket endpoints to HTTPS/WSS.",
        "patch": """// Before:
"url": "http://mcp-server.internal:8080"

// After:
"url": "https://mcp-server.internal:8443" """,
    },
    "AGENT046": {
        "title": "Eliminate Dynamic Code Execution",
        "action": "Replace eval() / exec() with safe literal parsing (ast.literal_eval) or static function dispatch.",
        "patch": """# Before:
result = eval(user_arg)

# After:
import ast
result = ast.literal_eval(user_arg)""",
    },
    "AGENT047": {
        "title": "Sanitize Subprocess Calls (Disable shell=True)",
        "action": "Pass command arguments as an explicit list and set shell=False to prevent shell injection.",
        "patch": """# Before:
subprocess.run(f"tool {arg}", shell=True)

# After:
subprocess.run(["tool", arg], shell=False, check=True)""",
    },
    "AGENT048": {
        "title": "Replace Insecure Deserialization",
        "action": "Use standard JSON or yaml.safe_load instead of pickle or unsafe YAML loader.",
        "patch": """# Before:
data = pickle.loads(raw_bytes)

# After:
import json
data = json.loads(raw_bytes)  # Or: yaml.safe_load(raw_bytes)""",
    },
    "AGENT049": {
        "title": "Block Link-Local Cloud Metadata Endpoints (SSRF)",
        "action": "Add egress validation blocking 169.254.169.254 and cloud IMDS URLs.",
        "patch": """# After:
if any(m in target_url for m in ["169.254.169.254", "metadata.google.internal"]):
    raise PermissionError("Egress to cloud metadata service is prohibited by AgentSec policy.")""",
    },
    "AGENT050": {
        "title": "Namespace MCP Tools to Prevent Shadowing",
        "action": "Assign distinct server-prefixed namespaces to tools to prevent malicious tool shadowing.",
        "patch": """// Before (Colliding tool name):
"tools": ["read_file"]

// After (Namespaced tool):
"tools": ["server_name__read_file"]""",
    },
}


def get_fix_plan(finding: Dict[str, Any]) -> Dict[str, str]:
    """Generate a scoped remediation plan for a finding."""
    code = finding.get("code", "AGENT000")
    file_path = finding.get("file", "")

    # Clean relative path for suppression advice
    rel_path = file_path
    try:
        p = Path(file_path)
        rel_path = p.name
    except Exception:
        pass

    template = FIX_TEMPLATES.get(code)
    if template:
        title = template["title"]
        action = template["action"]
        patch = template["patch"]
    else:
        title = f"Remediate {finding.get('rule', code)}"
        action = finding.get("recommendation", "Review and restrict permissions according to least-privilege principle.")
        patch = f"// Review {finding.get('file', '')} and apply least privilege."

    suppression_line = f"{rel_path}: {code}"

    return {
        "title": title,
        "action": action,
        "patch": patch,
        "suppression": suppression_line,
    }
