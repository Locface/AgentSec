"""Security score calculation for AgentSec findings."""

from typing import List, Dict, Any


def calculate_security_score(findings: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calculate a 0–100 security score and letter grade from scan findings.

    Scoring formula:
    - Base: 100
    - Critical finding: -20 pts
    - High finding: -10 pts
    - Medium finding: -4 pts
    - Low finding: -1 pt
    """
    score = 100
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}

    for f in findings:
        sev = f.get("severity", "low").lower()
        if sev == "critical":
            score -= 20
            counts["critical"] += 1
        elif sev == "high":
            score -= 10
            counts["high"] += 1
        elif sev == "medium":
            score -= 4
            counts["medium"] += 1
        elif sev == "low":
            score -= 1
            counts["low"] += 1

    score = max(0, score)

    if score >= 90:
        grade = "A"
        status = "Strong security posture"
    elif score >= 75:
        grade = "B"
        status = "Acceptable posture with manageable risks"
    elif score >= 60:
        grade = "C"
        status = "Needs remediation; high-risk configurations detected"
    elif score >= 40:
        grade = "D"
        status = "Poor security posture; critical risks detected"
    else:
        grade = "F"
        status = "Dangerous configuration; immediate intervention required"

    return {
        "score": score,
        "grade": grade,
        "status": status,
        "counts": counts,
        "total_findings": len(findings),
    }
