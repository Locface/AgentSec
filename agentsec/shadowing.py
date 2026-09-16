"""Tool Shadowing & Naming Collision Detector for MCP configurations."""

from typing import List, Dict, Any
from pathlib import Path


def detect_tool_shadowing(mcp_servers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Detect tool shadowing and naming conflicts across configured MCP servers.

    Flags when two or more distinct MCP servers declare tools with identical names,
    which creates a tool shadowing risk where an untrusted server can intercept
    agent tool calls intended for another server.
    """
    tool_map: Dict[str, List[Dict[str, str]]] = {}
    findings: List[Dict[str, Any]] = []

    for s in mcp_servers:
        s_name = s.get("name", "unknown")
        s_file = s.get("file", "mcp.json")
        tools = s.get("tools", [])
        if not isinstance(tools, list):
            continue

        for t in tools:
            t_name = ""
            if isinstance(t, str):
                t_name = t.strip()
            elif isinstance(t, dict):
                t_name = t.get("name", "").strip()

            if not t_name:
                continue

            if t_name not in tool_map:
                tool_map[t_name] = []

            tool_map[t_name].append({
                "server": s_name,
                "file": s_file,
            })

    for t_name, occurrences in tool_map.items():
        unique_servers = {occ["server"] for occ in occurrences}
        if len(unique_servers) > 1:
            involved_str = ", ".join(f"{occ['server']} ({occ['file']})" for occ in occurrences)
            primary_file = occurrences[0]["file"]
            findings.append({
                "code": "AGENT050",
                "rule": "Tool shadowing & naming collision",
                "severity": "high",
                "file": primary_file,
                "description": f"Tool name '{t_name}' is declared by multiple MCP servers: {involved_str}. This creates a tool shadowing risk.",
                "recommendation": "Assign unique namespaces or prefixes to tools per MCP server to prevent collision and tool hijacking.",
            })

    return findings
