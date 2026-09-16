"""Output formatters for AgentSec findings."""

from .score import calculate_security_score


def print_summary(findings: list, format: str, show_owasp: bool = False) -> None:
    """Print findings in the requested format."""
    metrics = calculate_security_score(findings)

    if format == "terminal":
        for f in findings:
            owasp_tag = f" {f.get('owasp', '')}" if show_owasp and f.get('owasp') else ""
            line_str = f":{f['line']}" if f.get("line") else ""
            print(f"[{f['severity'].upper()}]{owasp_tag} {f['rule']}")
            print(f"  File: {f['file']}{line_str}")
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
        c = metrics["counts"]
        print("# AgentSec Security Scan Report\n")
        print("| Metric | Status |")
        print("|---|---|")
        print(f"| **Security Score** | **{metrics['score']}/100** (Grade `{metrics['grade']}`) |")
        print(f"| **Posture** | {metrics['status']} |")
        print(f"| **Findings Breakdown** | Total {metrics['total_findings']} (Critical: {c['critical']}, High: {c['high']}, Medium: {c['medium']}, Low: {c['low']}) |\n")

        if not findings:
            print("✓ **No security risks detected.** Security posture meets baseline standards.\n")
        else:
            print("### Findings Summary\n")
            print("| Severity | Rule | Code | File | OWASP |")
            print("|---|---|---|---|---|")
            for f in findings:
                code_str = f"`{f.get('code', 'AGENT')}`"
                line_str = f":{f['line']}" if f.get("line") else ""
                file_str = f"`{f['file']}{line_str}`"
                owasp_str = f"`{f.get('owasp', '')}`" if f.get('owasp') else "—"
                print(f"| **{f['severity'].upper()}** | {f['rule']} | {code_str} | {file_str} | {owasp_str} |")
            print()

            print("### Detailed Remediation\n")
            for f in findings:
                line_info = f" (line {f['line']})" if f.get("line") else ""
                print(f"#### [{f['severity'].upper()}] {f['rule']}{line_info}")
                print(f"- **File:** `{f['file']}`")
                if f.get("server"):
                    print(f"- **Server:** `{f['server']}`")
                if f.get("owasp"):
                    print(f"- **OWASP:** {f['owasp']}")
                print(f"- **Description:** {f['description']}")
                print(f"- **Recommendation:** {f['recommendation']}")
                print()

    elif format == "sarif":
        from .sarif import print_sarif
        print_sarif(findings)
