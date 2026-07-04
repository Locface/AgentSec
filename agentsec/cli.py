"""CLI entry point for AgentSec."""
import sys
import click
from pathlib import Path


from . import __version__


@click.group()
@click.version_option(version=__version__, prog_name="agentsec")
def cli():
    """AgentSec — security scanner for AI agent configs."""
    pass


@cli.command()
@click.argument("path", default=".", type=click.Path(exists=True, file_okay=False, dir_okay=True, resolve_path=True))
@click.option("--format", "-f", default="terminal", type=click.Choice(["terminal", "json", "markdown", "sarif"], case_sensitive=False),
              help="Output format: terminal, json, markdown, sarif")
@click.option("--severity", default="all", help="Minimum severity: critical, high, medium, low, all")
@click.option("--fail-on", type=click.Choice(["critical", "high", "medium", "low"], case_sensitive=False),
              help="Exit with code 1 if any finding is at least this severity")
@click.option("--include-hidden", is_flag=True, help="Include hidden files and directories")
@click.option("--exclude", multiple=True, default=None,
              help="Exclude paths matching pattern (can be repeated). E.g., --exclude 'node_modules/**'")
@click.option("--no-gitignore", is_flag=True, default=False,
              help="Do not automatically respect .gitignore patterns")
@click.option("--baseline", type=click.Path(exists=True, dir_okay=False, resolve_path=True),
              help="Path to baseline JSON file (lockfile). Compare findings against it.")
@click.option("--update-baseline", type=click.Path(dir_okay=False, resolve_path=True),
              help="Save current findings as baseline JSON file and exit.")
@click.option("--show-owasp", is_flag=True, default=False,
              help="Show OWASP Top 10 for LLM mapping IDs for each finding")
def scan(path, format, severity, include_hidden, exclude, no_gitignore, fail_on=None, baseline=None, update_baseline=None, show_owasp=False):
    """Scan a directory for security risks in AI agent configurations."""
    # Lazy imports: scanner + parsers are only loaded when scan runs,
    # not when --help is displayed. This keeps `agentsec --help` fast
    # and prevents import-time failures (e.g. missing tomli on Python 3.10).
    from .scanner import Scanner
    from .report import print_summary
    from .baseline import load_baseline, save_baseline, compare_findings, compute_finding_id
    from .owasp import format_owasp

    if format == "terminal":
        click.echo(f" Scanning {path}...")

    scanner = Scanner(Path(path), include_hidden=include_hidden, min_severity=severity,
                     exclude_patterns=list(exclude) if exclude else None,
                     no_gitignore=no_gitignore)
    findings = scanner.scan()

    # If update-baseline is provided, save baseline and exit
    if update_baseline:
        save_baseline(update_baseline, findings)
        if format == "terminal":
            click.echo(f" Baseline saved to {update_baseline}")
        return

    # Load baseline if provided
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
        print_summary(findings, format, show_owasp=show_owasp)
        if new or changed:
            sys.exit(1)
    else:
        # Add OWASP tags to terminal output header if show_owasp
        if format == "terminal" and show_owasp:
            click.echo(" OWASP mapping enabled (LLM = OWASP Top 10 for LLM, AG = OWASP Agentic Security)\n")
        print_summary(findings, format, show_owasp=show_owasp)

    # Existing fail-on logic
    if fail_on:
        severity_levels = {"low": 0, "medium": 1, "high": 2, "critical": 3}
        min_fail = severity_levels.get(fail_on.lower(), -1)
        if min_fail >= 0:
            for f in findings:
                if severity_levels.get(f["severity"].lower(), -1) >= min_fail:
                    click.echo(f"Failing due to {f['severity']} finding: {f['rule']}")
                    sys.exit(1)


if __name__ == "__main__":
    cli()
