"""Tests for AgentSec standalone HTML report generator."""

from agentsec.html_report import generate_html_report


def test_html_report_basic_structure():
    findings = [
        {
            "code": "AGENT001",
            "rule": "MCP shell execution",
            "severity": "critical",
            "file": "agent_config.json",
            "line": 12,
            "description": "Agent configured with unrestricted shell execution tool.",
            "recommendation": "Constrain shell access.",
            "owasp": "LLM02: Sensitive Information Disclosure",
        },
        {
            "code": "AGENT046",
            "rule": "Dynamic Python Eval / Exec in Agent Tool",
            "severity": "high",
            "file": "tools.py",
            "line": 45,
            "description": "Dynamic code execution allows arbitrary code execution in agent sandbox.",
            "recommendation": "Use safe parsing or ast.literal_eval.",
            "owasp": "LLM02: Sensitive Information Disclosure",
        }
    ]
    html = generate_html_report(findings, scanned_path="/test/path")

    assert "<!DOCTYPE html>" in html
    assert "<html lang=\"en\">" in html
    assert "</html>" in html
    assert "AGENT001" in html
    assert "AGENT046" in html
    assert "MCP shell execution" in html
    assert "/test/path" in html
    assert "Executive Summary" in html
    assert "CRITICAL" in html
    assert "SCOPED FIX PLAN" in html


def test_html_report_zero_external_network_dependencies():
    """Ensure report contains zero external CDN scripts or stylesheet links."""
    findings = []
    html = generate_html_report(findings, scanned_path=".")

    # Verify no external CDN/HTTP resources are imported
    assert "<script src=" not in html.lower()
    assert "<link rel=\"stylesheet\" href=\"http" not in html.lower()
    assert "http://" not in html.lower()
    assert "https://" not in html.lower()


def test_html_report_escapes_untrusted_input():
    """Verify that malicious strings in findings are properly escaped in HTML."""
    xss_payload = '<script>alert("xss")</script>'
    findings = [
        {
            "code": "AGENT001",
            "rule": "XSS Injection Test",
            "severity": "low",
            "file": xss_payload,
            "line": 1,
            "description": xss_payload,
            "recommendation": xss_payload,
            "owasp": xss_payload,
        }
    ]
    html = generate_html_report(findings, scanned_path=".")

    assert '<script>alert("xss")</script>' not in html
    assert '&lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt;' in html or '&lt;script&gt;' in html
