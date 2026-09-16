import json
from pathlib import Path
from typing import Any, Dict, List, Optional

def parse_mcp_config(content: str, file_path: Path) -> Optional[List[Dict[str, Any]]]:
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return None
    
    servers = []
    
    if isinstance(data, dict) and "mcpServers" in data:
        mcp_servers = data["mcpServers"]
        if isinstance(mcp_servers, dict):
            for name, config in mcp_servers.items():
                if isinstance(config, dict):
                    server = {
                        "name": name,
                        "command": config.get("command", ""),
                        "args": config.get("args", []),
                        "env": config.get("env", {}),
                        "tools": config.get("tools", []),
                        "capabilities": _infer_capabilities(config)
                    }
                    servers.append(server)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and "command" in item:
                server = {
                    "name": item.get("name", ""),
                    "command": item.get("command", ""),
                    "args": item.get("args", []),
                    "env": item.get("env", {}),
                    "tools": item.get("tools", []),
                    "capabilities": _infer_capabilities(item)
                }
                servers.append(server)
    return servers if servers else None

def _infer_capabilities(config: Dict[str, Any]) -> List[str]:
    caps = []
    text = str(config).lower()
    
    if "filesystem" in text or "write" in text or "edit" in text or "delete" in text or "rm" in text or "mv" in text:
        caps.append("filesystem")
    if "bash" in text or "sh" in text or "powershell" in text or "cmd" in text or "exec" in text or "subprocess" in text or "terminal" in text or "run_command" in text:
        caps.append("shell")
    if "http" in text or "https" in text or "curl" in text or "wget" in text or "fetch" in text:
        caps.append("network")
    if "env" in text or ".env" in text or "secret" in text or "token" in text or "key" in text:
        caps.append("secrets")
    if "slack" in text or "gmail" in text or "email" in text or "send_message" in text or "post_message" in text or "create_issue" in text or "comment" in text or "reply" in text:
        caps.append("communication")
    if "postgres" in text or "mysql" in text or "mongodb" in text or "redis" in text or "delete" in text or "drop" in text or "update" in text or "insert" in text:
        caps.append("database")
    return caps
