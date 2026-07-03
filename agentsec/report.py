"""Output formatters for AgentSec findings."""

def print_summary(findings: list, format: str, show_owasp: bool = False) -> None:
    """Print findings in the requested format."""
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
        print(f"Total findings: {len(findings)}")
    elif format == "json":
        import json
        print(json.dumps(findings, indent=2))
    elif format == "markdown":
        print("# AgentSec Report\n")
        for f in findings:
            owasp_tag = f" ({f.get('owasp')})" if show_owasp and f.get('owasp') else ""
            print(f"## {f['severity'].upper()}: {f['rule']}{owasp_tag}")
            print(f"**File:** {f['file']}")
            if f.get('server'):
                print(f"**Server:** {f['server']}")
            print(f"**Description:** {f['description']}")
            print(f"**Recommendation:** {f['recommendation']}")
            if show_owasp and f.get('owasp'):
                print(f"**OWASP:** {f['owasp']}")
            print()
    elif format == "sarif":
        from .sarif import print_sarif
        print_sarif(findings)
