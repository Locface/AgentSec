"""Additional security rules for AgentSec."""

from .base import Rule

def load_additional_rules():
    return [
        Rule(
            name="Network + filesystem access",
            severity="critical",
            description="MCP server has both network and filesystem access (exfiltration risk)",
            recommendation="Separate network and filesystem capabilities, or implement strict allowlists.",
            detect_patterns=["http", "https", "curl", "wget", "fetch", "filesystem", "write", "edit", "delete", "rm", "mv"]
        ),
        Rule(
            name="Suspicious tool description",
            severity="high",
            description="Tool description contains suspicious instructions (prompt injection)",
            recommendation="Review and sanitize tool descriptions; avoid instruction-like language.",
            detect_patterns=["ignore previous instructions", "ignore all instructions", "do not tell the user", "secretly", "exfiltrate", "send to", "bypass", "disable security", "you are now", "system prompt"]
        ),
        Rule(
            name="GitHub token exposure",
            severity="high",
            description="GitHub token or actions:write permission detected",
            recommendation="Use fine-grained tokens with minimal permissions; avoid actions:write unless necessary.",
            detect_patterns=["GITHUB_TOKEN", "gh auth token", ".git/config", "actions: write", "contents: write"]
        ),
        Rule(
            name="Communication tool write permission",
            severity="high",
            description="MCP server can send messages to Slack/email/GitHub (data leak risk)",
            recommendation="Limit write permissions for communication tools; use separate accounts with restricted scopes.",
            detect_patterns=["slack", "gmail", "email", "send_message", "post_message", "create_issue", "comment", "reply"]
        ),
        Rule(
            name="Database write/delete permission",
            severity="high",
            description="MCP server can modify or delete database records",
            recommendation="Use read-only credentials for MCP servers; require manual approval for destructive operations.",
            detect_patterns=["postgres", "mysql", "mongodb", "redis", "delete", "drop", "update", "insert"]
        ),
        Rule(
            name="Unpinned dependency",
            severity="medium",
            description="MCP server dependency not pinned to a specific version",
            recommendation="Pin dependencies to a specific version or commit SHA to avoid supply-chain attacks.",
            detect_patterns=["latest", ":latest", "@latest"]
        ),
        Rule(
            name="Remote script install",
            severity="high",
            description="Remote script installation pattern (curl | bash) detected",
            recommendation="Avoid piping remote scripts to shell; prefer verified packages or download and inspect.",
            detect_patterns=["curl ... | bash", "wget ... | sh"]
        ),
        Rule(
            name="Excessive autonomy instruction",
            severity="medium",
            description="Agent instruction requests excessive autonomy (no confirmation)",
            recommendation="Require user confirmation for important actions; avoid 'auto-approve' instructions.",
            detect_patterns=["do not ask for confirmation", "always run commands", "auto-approve", "never ask user", "full access", "without confirmation"]
        ),
        Rule(
            name="Prompt injection in markdown",
            severity="medium",
            description="Markdown file contains potential prompt injection phrases",
            recommendation="Sanitize agent instructions; avoid embedding system-level directives in markdown.",
            detect_patterns=["ignore previous instructions", "as an AI agent", "system prompt", "developer message", "hidden instruction"]
        ),
        Rule(
            name="Sensitive file reference",
            severity="high",
            description="Agent instruction references sensitive files or secrets",
            recommendation="Remove references to secrets or use gitignored files for credentials.",
            detect_patterns=[".env", "id_rsa", ".ssh", "credentials", "secrets", "tokens", "auth.json"]
        ),
        Rule(
            name="MCP OAuth broad scopes",
            severity="medium",
            description="MCP OAuth configuration has overly broad scopes",
            recommendation="Use minimal required scopes; avoid '*' or 'admin' scopes.",
            detect_patterns=["oauth", "*", "admin", "full_access"]
        ),
        Rule(
            name="Web + filesystem access",
            severity="high",
            description="Tool can browse web and write files (prompt injection to file write risk)",
            recommendation="Isolate web browsing from filesystem write; use separate tools with restricted permissions.",
            detect_patterns=["http", "https", "curl", "wget", "fetch", "write", "edit", "delete", "rm", "mv"]
        ),
        Rule(
            name="Read repo + network",
            severity="high",
            description="Tool can read repo files and send network requests (exfiltration risk)",
            recommendation="Restrict read access for network-capable tools; use separate credentials.",
            detect_patterns=["read_file", "read", "http", "https", "curl", "wget", "fetch"]
        ),
        Rule(
            name="Unknown/untrusted source",
            severity="medium",
            description="MCP server package from unknown or untrusted source",
            recommendation="Use packages from trusted registries (npm, PyPI) with known maintainers.",
            detect_patterns=["raw.githubusercontent.com", r"raw\.", "gist", "pastebin", "dropbox", "bitbucket"]
        ),
        Rule(
            name="No policy file",
            severity="low",
            description="Project uses MCP/tools but no local security policy file",
            recommendation="Define a policy file (e.g., .agentsec.yaml) to specify allow/deny lists.",
            detect_patterns=["mcpServers", "tools", "allowed", "denied"]
        ),
        # Новые правила для популярных AI-агентов и дополнительных уязвимостей
        Rule(
            name="Cursor agent config with dangerous permissions",
            severity="high",
            description="Cursor agent configuration grants dangerous permissions (shell, filesystem write, network)",
            recommendation="Restrict permissions for Cursor agent to minimal required; use project-specific configs.",
            detect_patterns=["cursor-agent"],
            all_patterns=["cursor", "shell", "write", "network"]
        ),
        Rule(
            name="Claude Desktop config with MCP server risks",
            severity="high",
            description="Claude Desktop MCP server configuration has risky settings (shell, filesystem, network)",
            recommendation="Review Claude Desktop MCP config; restrict shell and filesystem access.",
            detect_patterns=["claude-desktop", "claude_desktop", "claude_desktop_config.json"],
            all_patterns=["mcpservers", "filesystem"]
        ),
        Rule(
            name="Codex/Cline agent with unrestricted tools",
            severity="high",
            description="Codex or Cline agent has unrestricted access to tools (shell, filesystem, network)",
            recommendation="Restrict tool access for Codex/Cline agents; use permission prompts.",
            detect_patterns=["codex", "cline", "tools", "shell", "filesystem", "network", "permissions"]
        ),
        Rule(
            name="Environment variable exposure",
            severity="critical",
            description="MCP server or agent config exposes environment variables with secrets",
            recommendation="Avoid exposing env vars in configs; use .env files and gitignore them.",
            detect_patterns=["process.env", "AWS_", "OPENAI_", "ANTHROPIC_", "GOOGLE_", "GITHUB_", "SLACK_", "DISCORD_"]
        ),
        Rule(
            name="Vulnerable dependency pattern",
            severity="medium",
            description="MCP server dependency uses known vulnerable version pattern (e.g., outdated package)",
            recommendation="Update dependencies to latest secure versions; use tools like npm audit or pip-audit.",
            detect_patterns=["@modelcontextprotocol", "^0.1", "~0.0", "<1.0", ">=0.1"]
        ),
        Rule(
            name="Insecure default command",
            severity="critical",
            description="MCP server command uses insecure defaults (e.g., exec, eval, dangerous flags)",
            recommendation="Avoid using eval, exec, or dangerous command-line flags; use safe alternatives.",
            detect_patterns=["eval", "exec", "-e", "-c", "--eval", "--exec", "child_process"]
        ),
        Rule(
            name="Read-only file system in MCP server",
            severity="medium",
            description="MCP server has read-only filesystem access but may still expose sensitive files",
            recommendation="Even read-only access can leak secrets; restrict path to necessary directories.",
            detect_patterns=["read", "readonly", "read-only", "filesystem", "path"]
        ),
        Rule(
            name="Missing input validation",
            severity="medium",
            description="Agent or MCP server lacks input validation, potentially allowing injection attacks",
            recommendation="Validate and sanitize all inputs from the agent or external sources.",
            detect_patterns=["input", "prompt", "argument", "parameter", "validate", "sanitize"]
        ),
        Rule(
            name="Package manager execution",
            severity="high",
            description="Agent config invokes package managers that can execute install scripts",
            recommendation="Pin packages, disable lifecycle scripts where possible, and avoid dynamic package execution.",
            detect_patterns=["npx", "uvx", "pipx", "bunx", "pnpm dlx", "npm exec"]
        ),
        Rule(
            name="Container privileged mode",
            severity="critical",
            description="Containerized MCP server may run with elevated host privileges",
            recommendation="Avoid privileged mode and host namespace sharing; use minimal container capabilities.",
            detect_patterns=["privileged: true", "--privileged", "pid: host", "network_mode: host", "--network=host"]
        ),
        Rule(
            name="Host mount exposure",
            severity="critical",
            description="MCP server or container mounts sensitive host directories",
            recommendation="Mount only required project directories and prefer read-only mounts.",
            detect_patterns=["/var/run/docker.sock", "/:/", "/home:/", "/root:/", "~:/", "/Users:/"]
        ),
        Rule(
            name="Browser automation with local file access",
            severity="high",
            description="Agent config combines browser automation with local file access",
            recommendation="Isolate browser automation from sensitive filesystem paths.",
            detect_patterns=["playwright", "puppeteer", "browser", "filesystem", "file://"]
        ),
        Rule(
            name="Dynamic code execution",
            severity="critical",
            description="Agent or MCP server can dynamically evaluate code",
            recommendation="Avoid eval-style execution and route code execution through reviewed, sandboxed tools.",
            detect_patterns=["eval(", "exec(", "new Function", "child_process.exec", "python -c", "node -e"]
        ),
        Rule(
            name="Wildcard tool allowlist",
            severity="high",
            description="Agent config appears to allow all tools or permissions via wildcard",
            recommendation="Use explicit allowlists for tools, paths, hosts, and permissions.",
            detect_patterns=["allowed_tools: *", "allow_all", "allowed: [\"*\"]", "permissions: *", "tools: *"]
        ),
        Rule(
            name="Telemetry or analytics endpoint",
            severity="medium",
            description="Agent or MCP server references telemetry or analytics endpoints",
            recommendation="Ensure telemetry is opt-in and never includes prompts, secrets, or source code.",
            detect_patterns=["telemetry", "analytics", "posthog", "segment", "sentry", "datadog"]
        ),
        Rule(
            name="Credential helper access",
            severity="high",
            description="Agent config references credential stores or auth helpers",
            recommendation="Do not expose credential helpers to agents; use scoped tokens with least privilege.",
            detect_patterns=["credential.helper", "keychain", "secretservice", "wincred", "gh auth", "aws configure"]
        ),
    ]
