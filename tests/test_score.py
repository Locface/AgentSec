"""Tests for security score calculation."""

from agentsec.score import calculate_security_score


def test_score_clean():
    res = calculate_security_score([])
    assert res["score"] == 100
    assert res["grade"] == "A"
    assert res["total_findings"] == 0


def test_score_penalties():
    findings = [
        {"severity": "critical", "rule": "MCP shell execution"},
        {"severity": "high", "rule": "Broad path access"},
        {"severity": "medium", "rule": "Prompt injection risk"},
        {"severity": "low", "rule": "No policy file"},
    ]
    # 100 - 20 - 10 - 4 - 1 = 65
    res = calculate_security_score(findings)
    assert res["score"] == 65
    assert res["grade"] == "C"
    assert res["counts"]["critical"] == 1
    assert res["counts"]["high"] == 1
    assert res["counts"]["medium"] == 1
    assert res["counts"]["low"] == 1


def test_score_floor_at_zero():
    findings = [{"severity": "critical", "rule": "Risk"}] * 10
    res = calculate_security_score(findings)
    assert res["score"] == 0
    assert res["grade"] == "F"
