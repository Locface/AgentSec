"""Tests for Python AST Security Analyzer in AgentSec."""

import pytest
from pathlib import Path
from agentsec.parsers.python_ast import scan_python_tool_ast
from agentsec.scanner import Scanner


def test_ast_detects_eval_and_exec(tmp_path):
    code = """
def run_command(payload):
    eval(payload)
    exec(payload)
"""
    p = tmp_path / "handler.py"
    p.write_text(code)
    findings = scan_python_tool_ast(p, code)
    codes = [f["code"] for f in findings]
    assert "AGENT046" in codes
    assert len([c for c in codes if c == "AGENT046"]) == 2
    # Verify line numbers are captured
    lines = [f["line"] for f in findings if f["code"] == "AGENT046"]
    assert 3 in lines
    assert 4 in lines


def test_ast_detects_shell_execution(tmp_path):
    code = """
import os
import subprocess

def exec_tool(cmd):
    os.system(cmd)
    subprocess.run(["echo", cmd], shell=True)
"""
    p = tmp_path / "tool.py"
    p.write_text(code)
    findings = scan_python_tool_ast(p, code)
    codes = [f["code"] for f in findings]
    assert "AGENT047" in codes
    assert len([c for c in codes if c == "AGENT047"]) == 2


def test_ast_detects_insecure_deserialization(tmp_path):
    code = """
import pickle
import yaml

def parse_state(data):
    obj = pickle.loads(data)
    y = yaml.load(data, Loader=yaml.Loader)
    return obj
"""
    p = tmp_path / "deser.py"
    p.write_text(code)
    findings = scan_python_tool_ast(p, code)
    codes = [f["code"] for f in findings]
    assert "AGENT048" in codes
    assert len([c for c in codes if c == "AGENT048"]) == 2


def test_ast_detects_cloud_metadata_ssrf(tmp_path):
    code = """
import urllib.request

def fetch_creds():
    url = "http://169.254.169.254/latest/meta-data/iam/security-credentials/"
    return urllib.request.urlopen(url).read()
"""
    p = tmp_path / "fetcher.py"
    p.write_text(code)
    findings = scan_python_tool_ast(p, code)
    codes = [f["code"] for f in findings]
    assert "AGENT049" in codes


def test_ast_scanner_full_integration(tmp_path):
    # Test that Scanner finds the python tool findings and assigns OWASP IDs
    code = """
def execute_eval(x):
    eval(x)
"""
    p = tmp_path / "skill.py"
    p.write_text(code)
    scanner = Scanner(tmp_path)
    findings = scanner.scan()
    assert len(findings) >= 1
    f = next(item for item in findings if item["code"] == "AGENT046")
    assert f["severity"] == "critical"
    assert "LLM06" in f["owasp"]
    assert "AG02" in f["owasp"]


def test_ast_safe_code_produces_no_findings(tmp_path):
    code = """
import json

def safe_handler(data):
    parsed = json.loads(data)
    return {"status": "ok", "result": parsed}
"""
    p = tmp_path / "safe.py"
    p.write_text(code)
    scanner = Scanner(tmp_path)
    findings = scanner.scan()
    assert len(findings) == 0
