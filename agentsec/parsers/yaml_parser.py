import yaml
from pathlib import Path
from typing import Any, Dict, List, Optional
from .json_parser import _infer_capabilities

def parse_mcp_config(content: str, file_path: Path) -> Optional[List[Dict[str, Any]]]:
    """Parse MCP config from YAML content."""
    try:
        data = yaml.safe_load(content)
    except yaml.YAMLError:
        return None
    
    if not isinstance(data, dict):
        return None
    
    servers = []
    if "mcpServers" in data and isinstance(data["mcpServers"], dict):
        for name, config in data["mcpServers"].items():
            if isinstance(config, dict):
                server = {
                    "name": name,
                    "command": config.get("command", ""),
                    "args": config.get("args", []),
                    "env": config.get("env", {}),
                    "capabilities": _infer_capabilities(config)
                }
                servers.append(server)
    return servers if servers else None
