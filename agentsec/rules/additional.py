"""Additional security rules for AgentSec."""

from .base import Rule

def load_additional_rules():
    return [
        Rule(
            code="AGENT011",
            name="Network + filesystem access",
            severity="critical",
            description="MCP server has both network and filesystem access (exfiltration risk)",
            recommendation="Separate network and filesystem capabilities, or implement strict allowlists.",
            detect_patterns=["http", "https", "curl", "wget", "fetch", "filesystem", "write", "edit", "delete", "rm", "mv"]
        ),
        Rule(
            code="AGENT012",
            name="Suspicious tool description",
            severity="high",
            description="Tool description contains suspicious instructions (prompt injection)",
            recommendation="Review and sanitize tool descriptions; avoid instruction-like language.",
            detect_patterns=["ignore previous instructions", "ignore all instructions", "do not tell the user", "secretly", "exfiltrate", "send to", "bypass", "disable security", "you are now", "system prompt"]
        ),
        Rule(
            code="AGENT013",
            name="GitHub token exposure",
            severity="high",
            description="GitHub token or actions:write permission detected",
            recommendation="Use fine-grained tokens with minimal permissions; avoid actions:write unless necessary.",
            detect_patterns=["GITHUB_TOKEN", "gh auth token", ".git/config", "actions: write", "contents: write"]
        ),
        Rule(
            code="AGENT014",
            name="Communication tool write permission",
            severity="high",
            description="MCP server can send messages to Slack/email/GitHub (data leak risk)",
            recommendation="Limit write permissions for communication tools; use separate accounts with restricted scopes.",
            detect_patterns=["slack", "gmail", "email", "send_message", "post_message", "create_issue", "comment", "reply"]
        ),
        Rule(
            code="AGENT015",
            name="Database write/delete permission",
            severity="high",
            description="MCP server can modify or delete database records",
            recommendation="Use read-only credentials for MCP servers; require manual approval for destructive operations.",
            detect_patterns=["postgres", "mysql", "mongodb", "redis", "delete", "drop", "update", "insert"]
        ),
        Rule(
            code="AGENT016",
            name="Excessive autonomy instruction",
            severity="medium",
            description="Agent instruction requests excessive autonomy (no confirmation)",
            recommendation="Require user confirmation for important actions; avoid 'auto-approve' instructions.",
            detect_patterns=["do not ask for confirmation", "always run commands", "auto-approve", "never ask user", "full access", "without confirmation"]
        ),
        Rule(
            code="AGENT017",
            name="Prompt injection in markdown",
            severity="medium",
            description="Markdown file contains potential prompt injection phrases",
            recommendation="Sanitize agent instructions; avoid embedding system-level directives in markdown.",
            detect_patterns=["ignore previous instructions", "as an AI agent", "system prompt", "developer message", "hidden instruction"]
        ),
        Rule(
            code="AGENT018",
            name="MCP OAuth broad scopes",
            severity="medium",
            description="MCP OAuth configuration has overly broad scopes",
            recommendation="Use minimal required scopes; avoid '*' or 'admin' scopes.",
            detect_patterns=["oauth", "*", "admin", "full_access"]
        ),
        Rule(
            code="AGENT019",
            name="Web + filesystem access",
            severity="high",
            description="Tool can browse web and write files (prompt injection to file write risk)",
            recommendation="Isolate web browsing from filesystem write; use separate tools with restricted permissions.",
            detect_patterns=["http", "https", "curl", "wget", "fetch", "write", "edit", "delete", "rm", "mv"]
        ),
        Rule(
            code="AGENT020",
            name="Read repo + network",
            severity="high",
            description="Tool can read repo files and send network requests (exfiltration risk)",
            recommendation="Restrict read access for network-capable tools; use separate credentials.",
            detect_patterns=["read_file", "read", "http", "https", "curl", "wget", "fetch"]
        ),
        Rule(
            code="AGENT021",
            name="Unknown/untrusted source",
            severity="medium",
            description="MCP server package from unknown or untrusted source",
            recommendation="Use packages from trusted registries (npm, PyPI) with known maintainers.",
            detect_patterns=["raw.githubusercontent.com", r"raw\.", "gist", "pastebin", "dropbox", "bitbucket"]
        ),
        Rule(
            code="AGENT022",
            name="No policy file",
            severity="low",
            description="Project uses MCP/tools but no local security policy file",
            recommendation="Define a policy file (e.g., .agentsec.yaml) to specify allow/deny lists.",
            detect_patterns=["mcpServers", "tools", "allowed", "denied"]
        ),
        Rule(
            code="AGENT023",
            name="Cursor agent config with dangerous permissions",
            severity="high",
            description="Cursor agent configuration grants dangerous permissions (shell, filesystem write, network)",
            recommendation="Restrict permissions for Cursor agent to minimal required; use project-specific configs.",
            detect_patterns=["cursor-agent"],
            all_patterns=["cursor", "shell", "write", "network"]
        ),
        Rule(
            code="AGENT024",
            name="Claude Desktop config with MCP server risks",
            severity="high",
            description="Claude Desktop MCP server configuration has risky settings (shell, filesystem, network)",
            recommendation="Review Claude Desktop MCP config; restrict shell and filesystem access.",
            detect_patterns=["claude-desktop", "claude_desktop", "claude_desktop_config.json"],
            all_patterns=["mcpservers", "filesystem"]
        ),
        Rule(
            code="AGENT025",
            name="Codex/Cline agent with unrestricted tools",
            severity="high",
            description="Codex or Cline agent has unrestricted access to tools (shell, filesystem, network)",
            recommendation="Restrict tool access for Codex/Cline agents; use permission prompts.",
            detect_patterns=["codex", "cline", "tools", "shell", "filesystem", "network", "permissions"]
        ),
        Rule(
            code="AGENT026",
            name="Environment variable exposure",
            severity="critical",
            description="MCP server or agent config exposes environment variables with secrets",
            recommendation="Avoid exposing env vars in configs; use .env files and gitignore them.",
            detect_patterns=["process.env", "AWS_", "OPENAI_", "ANTHROPIC_", "GOOGLE_", "GITHUB_", "SLACK_", "DISCORD_"]
        ),
        Rule(
            code="AGENT027",
            name="Vulnerable dependency pattern",
            severity="medium",
            description="MCP server dependency uses known vulnerable version pattern (e.g., outdated package)",
            recommendation="Update dependencies to latest secure versions; use tools like npm audit or pip-audit.",
            detect_patterns=["@modelcontextprotocol", "^0.1", "~0.0", "<1.0", ">=0.1"]
        ),
        Rule(
            code="AGENT028",
            name="Insecure default command",
            severity="critical",
            description="MCP server command uses insecure defaults (e.g., exec, eval, dangerous flags)",
            recommendation="Avoid using eval, exec, or dangerous command-line flags; use safe alternatives.",
            detect_patterns=["eval", "exec", "-e", "-c", "--eval", "--exec", "child_process"]
        ),
        Rule(
            code="AGENT029",
            name="Read-only file system in MCP server",
            severity="medium",
            description="MCP server has read-only filesystem access but may still expose sensitive files",
            recommendation="Even read-only access can leak secrets; restrict path to necessary directories.",
            detect_patterns=["read", "readonly", "read-only", "filesystem", "path"]
        ),
        Rule(
            code="AGENT030",
            name="Missing input validation",
            severity="medium",
            description="Agent or MCP server lacks input validation, potentially allowing injection attacks",
            recommendation="Validate and sanitize all inputs from the agent or external sources.",
            detect_patterns=["input", "prompt", "argument", "parameter", "validate", "sanitize"]
        ),
        Rule(
            code="AGENT031",
            name="Package manager execution",
            severity="high",
            description="Agent config invokes package managers that can execute install scripts",
            recommendation="Pin packages, disable lifecycle scripts where possible, and avoid dynamic package execution.",
            detect_patterns=["npx", "uvx", "pipx", "bunx", "pnpm dlx", "npm exec"]
        ),
        Rule(
            code="AGENT032",
            name="Container privileged mode",
            severity="critical",
            description="Containerized MCP server may run with elevated host privileges",
            recommendation="Avoid privileged mode and host namespace sharing; use minimal container capabilities.",
            detect_patterns=["privileged: true", "--privileged", "pid: host", "network_mode: host", "--network=host"]
        ),
        Rule(
            code="AGENT033",
            name="Host mount exposure",
            severity="critical",
            description="MCP server or container mounts sensitive host directories",
            recommendation="Mount only required project directories and prefer read-only mounts.",
            detect_patterns=["/var/run/docker.sock", "/:/", "/home:/", "/root:/", "~:/", "/Users:/"]
        ),
        Rule(
            code="AGENT034",
            name="Browser automation with local file access",
            severity="high",
            description="Agent config combines browser automation with local file access",
            recommendation="Isolate browser automation from sensitive filesystem paths.",
            detect_patterns=["playwright", "puppeteer", "browser", "filesystem", "file://"]
        ),
        Rule(
            code="AGENT035",
            name="Dynamic code execution",
            severity="critical",
            description="Agent or MCP server can dynamically evaluate code",
            recommendation="Avoid eval-style execution and route code execution through reviewed, sandboxed tools.",
            detect_patterns=["eval(", "exec(", "new Function", "child_process.exec", "python -c", "node -e"]
        ),
        Rule(
            code="AGENT036",
            name="Wildcard tool allowlist",
            severity="high",
            description="Agent config appears to allow all tools or permissions via wildcard",
            recommendation="Use explicit allowlists for tools, paths, hosts, and permissions.",
            detect_patterns=["allowed_tools: *", "allow_all", "allowed: [\"*\"]", "permissions: *", "tools: *"]
        ),
        Rule(
            code="AGENT037",
            name="Telemetry or analytics endpoint",
            severity="medium",
            description="Agent or MCP server references telemetry or analytics endpoints",
            recommendation="Ensure telemetry is opt-in and never includes prompts, secrets, or source code.",
            detect_patterns=["telemetry", "analytics", "posthog", "segment", "sentry", "datadog"]
        ),
        Rule(
            code="AGENT038",
            name="Credential helper access",
            severity="high",
            description="Agent config references credential stores or auth helpers",
            recommendation="Do not expose credential helpers to agents; use scoped tokens with least privilege.",
            detect_patterns=["credential.helper", "keychain", "secretservice", "wincred", "gh auth", "aws configure"]
        ),
    ]
