"""Output formatters for AgentSec findings."""

from .score import calculate_security_score


def print_summary(findings: list, format: str, show_owasp: bool = False) -> None:
    """Print findings in the requested format."""
    metrics = calculate_security_score(findings)

    if format == "terminal":
        for f in findings:
            owasp_tag = f" {f.get('owasp', '')}" if show_owasp and f.get('owasp') else ""
            print(f"[{f['severity'].upper()}]{owasp_tag} {f['rule']}")
            print(f"  File: {f['file']}")
            if f.get('server'):
                print(f"  Server: {f['server']}")
            print(f"  Description: {f['description']}")
            print(f"  Recommendation: {f['recommendation']}")
            if show_owasp and f.get('owasp'):
                print(f"  OWASP: {f['owasp']}")
            print()

        c = metrics["counts"]
        print(f"Security Score: {metrics['score']}/100 [Grade: {metrics['grade']}] · {metrics['status']}")
        print(f"Total findings: {metrics['total_findings']} · Critical: {c['critical']} · High: {c['high']} · Medium: {c['medium']} · Low: {c['low']}")
    elif format == "json":
        import json
        print(json.dumps(findings, indent=2))
    elif format == "markdown":
        print("# AgentSec Security Report\n")
        c = metrics["counts"]
        print(f"> **Security Score:** {metrics['score']}/100 (Grade {metrics['grade']}) — *{metrics['status']}*")
        print(f"> **Findings:** Total {metrics['total_findings']} (Critical: {c['critical']}, High: {c['high']}, Medium: {c['medium']}, Low: {c['low']})\n")
        for f in findings:
            owasp_tag = f" ({f.get('owasp')})" if show_owasp and f.get('owasp') else ""
            print(f"## [{f['severity'].upper()}] {f['rule']}{owasp_tag}")
            print(f"**File:** `{f['file']}`")
            if f.get('server'):
                print(f"**Server:** `{f['server']}`")
            print(f"**Description:** {f['description']}")
            print(f"**Recommendation:** {f['recommendation']}")
            if show_owasp and f.get('owasp'):
                print(f"**OWASP:** {f['owasp']}")
            print()
    elif format == "sarif":
        from .sarif import print_sarif
        print_sarif(findings)
