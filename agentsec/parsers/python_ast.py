"""Python AST Security Analyzer for AI Agent Tools and Skills.

Statically parses Python scripts (agent skills, tool handlers, hooks)
using Python's standard `ast` library. Zero external dependencies,
zero LLM calls, and zero network access.
"""

import ast
from pathlib import Path
from typing import List, Dict, Any


class PythonToolASTVisitor(ast.NodeVisitor):
    """AST visitor detecting dangerous patterns in agent tool code."""

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.findings: List[Dict[str, Any]] = []

    def visit_Call(self, node: ast.Call):
        func_name = ""
        func_mod = ""

        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            func_name = node.func.attr
            if isinstance(node.func.value, ast.Name):
                func_mod = node.func.value.id

        # AGENT046: eval / exec / __import__
        if func_name in {"eval", "exec", "__import__"}:
            self.findings.append({
                "code": "AGENT046",
                "rule": "Arbitrary code execution in tool handler",
                "severity": "critical",
                "file": str(self.file_path),
                "line": node.lineno,
                "description": f"Tool code executes dynamic code via '{func_name}()'",
                "recommendation": "Remove dynamic code execution; use safe parameter parsing or dispatch tables.",
            })

        # AGENT047: subprocess with shell=True, or os.system / os.popen
        if func_mod == "os" and func_name in {"system", "popen"}:
            self.findings.append({
                "code": "AGENT047",
                "rule": "Unsanitized shell invocation in tool code",
                "severity": "critical",
                "file": str(self.file_path),
                "line": node.lineno,
                "description": f"Tool code executes raw shell commands via 'os.{func_name}()'",
                "recommendation": "Avoid os.system/os.popen; use subprocess.run with explicit argument lists (shell=False).",
            })
        elif (func_mod == "subprocess" and func_name in {"run", "Popen", "call", "check_call", "check_output"}) or func_name in {"run", "Popen", "call", "check_call", "check_output"}:
            for kw in node.keywords:
                if kw.arg == "shell":
                    is_true = False
                    if isinstance(kw.value, ast.Constant) and kw.value.value is True:
                        is_true = True
                    elif isinstance(kw.value, ast.Name) and kw.value.id == "True":
                        is_true = True
                    if is_true:
                        self.findings.append({
                            "code": "AGENT047",
                            "rule": "Unsanitized shell invocation in tool code",
                            "severity": "critical",
                            "file": str(self.file_path),
                            "line": node.lineno,
                            "description": f"Tool code executes command with shell=True in '{func_name}()'",
                            "recommendation": "Set shell=False and pass command as list of arguments to prevent shell injection.",
                        })

        # AGENT048: pickle / unsafe yaml deserialization
        if func_mod in {"pickle", "_pickle", "cPickle"} and func_name in {"load", "loads"}:
            self.findings.append({
                "code": "AGENT048",
                "rule": "Insecure deserialization in tool handler",
                "severity": "high",
                "file": str(self.file_path),
                "line": node.lineno,
                "description": f"Insecure object deserialization via '{func_mod}.{func_name}()'",
                "recommendation": "Replace pickle with safe structured data serialization formats like json.",
            })
        elif func_mod == "yaml" and func_name == "load":
            has_safe = any(
                kw.arg == "Loader" and isinstance(kw.value, ast.Attribute) and kw.value.attr in {"SafeLoader", "CSafeLoader"}
                for kw in node.keywords
            )
            if not has_safe:
                self.findings.append({
                    "code": "AGENT048",
                    "rule": "Insecure deserialization in tool handler",
                    "severity": "high",
                    "file": str(self.file_path),
                    "line": node.lineno,
                    "description": "Insecure YAML deserialization with yaml.load() without SafeLoader",
                    "recommendation": "Use yaml.safe_load() to prevent arbitrary Python object instantiation.",
                })

        self.generic_visit(node)

    def visit_Constant(self, node: ast.Constant):
        # AGENT049: Cloud metadata SSRF endpoints
        if isinstance(node.value, str):
            val = node.value.lower()
            if "169.254.169.254" in val or "metadata.google.internal" in val or "fd00:ec2::254" in val:
                self.findings.append({
                    "code": "AGENT049",
                    "rule": "Hardcoded cloud metadata SSRF in agent tool",
                    "severity": "critical",
                    "file": str(self.file_path),
                    "line": node.lineno,
                    "description": f"Tool code references cloud metadata endpoint: '{node.value}'",
                    "recommendation": "Enforce network egress filtering; block requests to link-local metadata endpoints to prevent IAM role theft.",
                })
        self.generic_visit(node)


def scan_python_tool_ast(file_path: Path, content: str) -> List[Dict[str, Any]]:
    """Scan Python tool or skill code using AST.

    Returns a list of finding dictionaries. If syntax error occurs, returns empty list.
    """
    try:
        tree = ast.parse(content, filename=str(file_path))
        visitor = PythonToolASTVisitor(file_path)
        visitor.visit(tree)
        return visitor.findings
    except SyntaxError:
        return []
