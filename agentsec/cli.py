"""CLI entry point for AgentSec."""
import sys
import click
from pathlib import Path

from . import __version__


@click.group()
@click.version_option(version=__version__, prog_name="agentsec")
def cli():
    """AgentSec — security scanner and harness for AI agent configs."""
    pass


@cli.command("scan")
@click.argument("path", default=".", type=click.Path(exists=True, file_okay=False, dir_okay=True, resolve_path=True))
@click.option("--format", "-f", default="terminal", type=click.Choice(["terminal", "json", "markdown", "sarif", "html"], case_sensitive=False),
              help="Output format: terminal, json, markdown, sarif, html")
@click.option("--severity", default="all", help="Minimum severity: critical, high, medium, low, all")
@click.option("--fail-on", type=click.Choice(["critical", "high", "medium", "low"], case_sensitive=False),
              help="Exit with code 1 if any finding is at least this severity")
@click.option("--fail-on-score", type=int, default=None,
              help="Exit with code 1 if Security Score is below this threshold (0-100)")
@click.option("--suggest-fixes", is_flag=True, default=False,
              help="Display actionable scoped repair plans and patches for findings")
@click.option("--include-hidden", is_flag=True, help="Include hidden files and directories")
@click.option("--exclude", multiple=True, default=None,
              help="Exclude paths matching pattern (can be repeated). E.g., --exclude 'node_modules/**'")
@click.option("--no-gitignore", is_flag=True, default=False,
              help="Do not automatically respect .gitignore patterns")
@click.option("--ignore-file", type=click.Path(exists=True, dir_okay=False, resolve_path=True),
              help="Path to suppression file (defaults to .agentsecignore in scanned root)")
@click.option("--baseline", type=click.Path(exists=True, dir_okay=False, resolve_path=True),
              help="Path to baseline JSON file (lockfile). Compare findings against it.")
@click.option("--update-baseline", type=click.Path(dir_okay=False, resolve_path=True),
              help="Save current findings as baseline JSON file and exit.")
@click.option("--show-owasp", is_flag=True, default=False,
              help="Show OWASP Top 10 for LLM mapping IDs for each finding")
def scan(path, format, severity, include_hidden, exclude, no_gitignore, ignore_file=None, fail_on=None, fail_on_score=None, suggest_fixes=False, baseline=None, update_baseline=None, show_owasp=False):
    """Scan a directory for security risks in AI agent configurations."""
    from .scanner import Scanner
    from .report import print_summary
    from .baseline import load_baseline, save_baseline, compare_findings, compute_finding_id

    if format == "terminal":
        click.echo(f" Scanning {path}...")

    scanner = Scanner(
        Path(path),
        include_hidden=include_hidden,
        min_severity=severity,
        exclude_patterns=list(exclude) if exclude else None,
        no_gitignore=no_gitignore,
        ignore_file=Path(ignore_file) if ignore_file else None,
    )
    findings = scanner.scan()

    if update_baseline:
        save_baseline(update_baseline, findings)
        if format == "terminal":
            click.echo(f" Baseline saved to {update_baseline}")
        return

    if baseline:
        baseline_findings = load_baseline(baseline)
        new, changed, removed = compare_findings(findings, baseline_findings)
        if format == "terminal":
            click.echo(f"\n Baseline comparison against {baseline}:")
            click.echo(f"  New findings: {len(new)}")
            click.echo(f"  Changed severity: {len(changed)}")
            click.echo(f"  Removed findings: {len(removed)}")
            if new:
                click.echo("\n New findings:")
                for f in new:
                    click.echo(f"  [{f['severity']}] {f['rule']} ({f['file']})")
            if changed:
                click.echo("\n Changed findings:")
                for f in changed:
                    old_sev = baseline_findings.get(compute_finding_id(f), 'unknown')
                    click.echo(f"  [{old_sev} -> {f['severity']}] {f['rule']} ({f['file']})")
            if removed:
                click.echo("\n Removed findings (baseline only):")
                for r in removed:
                    click.echo(f"  [{r['severity']}] id: {r['id']}")
        print_summary(findings, format, show_owasp=show_owasp, suggest_fixes=suggest_fixes, scanned_path=str(path))
        if new or changed:
            sys.exit(1)
    else:
        if format == "terminal" and show_owasp:
            click.echo(" OWASP mapping enabled (LLM = OWASP Top 10 for LLM, AG = OWASP Agentic Security)\n")
        print_summary(findings, format, show_owasp=show_owasp, suggest_fixes=suggest_fixes, scanned_path=str(path))

    if fail_on:
        severity_levels = {"low": 0, "medium": 1, "high": 2, "critical": 3}
        min_fail = severity_levels.get(fail_on.lower(), -1)
        if min_fail >= 0:
            for f in findings:
                if severity_levels.get(f["severity"].lower(), -1) >= min_fail:
                    click.echo(f"Failing due to {f['severity']} finding: {f['rule']}")
                    sys.exit(1)

    if fail_on_score is not None:
        from .score import calculate_security_score
        metrics = calculate_security_score(findings)
        if metrics["score"] < fail_on_score:
            click.echo(f"Failing: Security Score {metrics['score']}/100 is below threshold of {fail_on_score}")
            sys.exit(1)


@cli.command("init-harness")
@click.argument("path", default=".", type=click.Path(exists=True, file_okay=False, dir_okay=True, resolve_path=True))
@click.option("--force", is_flag=True, default=False, help="Overwrite existing harness files")
def init_harness_cmd(path, force):
    """Initialize production-grade security harness files across the workspace."""
    from .harness import init_security_harness
    res = init_security_harness(Path(path), force=force)
    click.echo(f"Initialized AgentSec Security Harness in {path}:")
    for f in res["created"]:
        click.echo(f"  + Created/Updated: {f}")
    for f in res["skipped"]:
        click.echo(f"  - Skipped (already exists): {f}")
    click.echo("\nRun 'agentsec scan .' to audit your security posture.")


if __name__ == "__main__":
    cli()
