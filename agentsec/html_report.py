"""Standalone Self-Contained Interactive HTML Report Generator for AgentSec.

Generates a single self-contained HTML document with zero external CDN dependencies,
enabling offline inspection, interactive filtering, and actionable remediation plans.
"""

import html
from typing import List, Dict, Any
from .score import calculate_security_score
from .fixes import get_fix_plan


def generate_html_report(findings: List[Dict[str, Any]], scanned_path: str = ".") -> str:
    """Generate a self-contained HTML security report."""
    metrics = calculate_security_score(findings)
    c = metrics["counts"]
    score = metrics["score"]
    grade = metrics["grade"]
    status = metrics["status"]

    # Grade color
    grade_color = "#10b981" if score >= 80 else "#3b82f6" if score >= 70 else "#f59e0b" if score >= 50 else "#f43f5e"

    findings_json_items = []
    for f in findings:
        fix = get_fix_plan(f)
        findings_json_items.append({
            "code": f.get("code", ""),
            "rule": f.get("rule", ""),
            "severity": f.get("severity", "low"),
            "file": f.get("file", ""),
            "line": f.get("line"),
            "server": f.get("server"),
            "description": f.get("description", ""),
            "recommendation": f.get("recommendation", ""),
            "owasp": f.get("owasp", ""),
            "fix_title": fix["title"],
            "fix_action": fix["action"],
            "fix_patch": fix["patch"],
            "fix_suppression": fix["suppression"],
        })

    # Render finding cards HTML
    cards_html = []
    for f in findings_json_items:
        sev = f["severity"].lower()
        badge_class = f"badge--{sev}"
        line_str = f":{f['line']}" if f["line"] else ""
        owasp_pill = f'<span class="pill pill--owasp">{html.escape(f["owasp"])}</span>' if f["owasp"] else ""
        server_line = f'<div class="finding-meta-item"><strong>Server:</strong> {html.escape(f["server"])}</div>' if f["server"] else ""

        card = f"""
        <div class="finding-card" data-severity="{sev}" data-search="{html.escape(f['code'].lower())} {html.escape(f['rule'].lower())} {html.escape(f['file'].lower())} {html.escape(f['owasp'].lower())}">
            <div class="finding-header" onclick="this.parentElement.classList.toggle('expanded')">
                <div class="finding-badges">
                    <span class="badge {badge_class}">{html.escape(sev.upper())}</span>
                    <span class="badge badge--code">{html.escape(f['code'])}</span>
                    {owasp_pill}
                </div>
                <div class="finding-title">{html.escape(f['rule'])}</div>
                <div class="finding-file-summary">{html.escape(f['file'])}{line_str}</div>
                <div class="chevron">▼</div>
            </div>
            <div class="finding-body">
                <div class="finding-meta">
                    <div class="finding-meta-item"><strong>Target File:</strong> <code>{html.escape(f['file'])}{line_str}</code></div>
                    {server_line}
                </div>
                <div class="finding-section">
                    <div class="section-label">Description:</div>
                    <div class="section-content">{html.escape(f['description'])}</div>
                </div>
                <div class="finding-section">
                    <div class="section-label">Recommendation:</div>
                    <div class="section-content">{html.escape(f['recommendation'])}</div>
                </div>
                <div class="remediation-box">
                    <div class="remediation-header">
                        <span class="remediation-tag">SCOPED FIX PLAN</span>
                        <span class="remediation-title">{html.escape(f['fix_title'])}</span>
                    </div>
                    <p class="remediation-action">{html.escape(f['fix_action'])}</p>
                    <div class="code-wrapper">
                        <pre><code>{html.escape(f['fix_patch'])}</code></pre>
                    </div>
                    <div class="suppression-help">
                        <span>To suppress this finding in <code>.agentsecignore</code>:</span>
                        <code class="suppress-code">{html.escape(f['fix_suppression'])}</code>
                    </div>
                </div>
            </div>
        </div>
        """
        cards_html.append(card)

    rendered_cards = "\n".join(cards_html) if cards_html else '<div class="clean-state">✓ No security findings detected. Configuration meets baseline requirements.</div>'

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AgentSec Security Audit Report — {html.escape(scanned_path)}</title>
    <style>
        :root {{
            --bg-body: #07080d;
            --bg-card: #12141e;
            --bg-panel: #0a0b12;
            --border: rgba(255, 255, 255, 0.08);
            --border-hover: rgba(99, 102, 241, 0.35);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --accent: #6366f1;
            --crit: #f43f5e;
            --high: #f59e0b;
            --med: #3b82f6;
            --low: #64748b;
            --success: #10b981;
            --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: var(--font-sans);
            background-color: var(--bg-body);
            color: var(--text-primary);
            line-height: 1.55;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 1100px;
            margin: 0 auto;
        }}
        /* Header */
        .header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 20px;
            padding-bottom: 28px;
            border-bottom: 1px solid var(--border);
            margin-bottom: 32px;
        }}
        .brand {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .brand-icon {{
            width: 36px;
            height: 36px;
            border-radius: 9px;
            background: #6366f1;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .brand-title {{
            font-size: 1.4rem;
            font-weight: 700;
            letter-spacing: -0.02em;
        }}
        .report-meta {{
            font-size: 0.85rem;
            color: var(--text-secondary);
        }}
        /* Dashboard Summary */
        .dashboard {{
            display: grid;
            grid-template-columns: 280px 1fr;
            gap: 20px;
            margin-bottom: 36px;
        }}
        .score-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 24px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }}
        .score-gauge {{
            font-size: 3rem;
            font-weight: 800;
            color: {grade_color};
            line-height: 1;
            margin-bottom: 6px;
        }}
        .score-grade {{
            display: inline-block;
            font-size: 0.9rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 9999px;
            background: rgba(255, 255, 255, 0.06);
            margin-bottom: 10px;
        }}
        .score-status {{
            font-size: 0.82rem;
            color: var(--text-secondary);
        }}
        /* Metrics Grid */
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
        }}
        .metric-tile {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 18px 14px;
            text-align: center;
        }}
        .metric-tile.tile--crit {{ border-top: 3px solid var(--crit); }}
        .metric-tile.tile--high {{ border-top: 3px solid var(--high); }}
        .metric-tile.tile--med {{ border-top: 3px solid var(--med); }}
        .metric-tile.tile--low {{ border-top: 3px solid var(--low); }}
        .metric-val {{
            font-size: 1.8rem;
            font-weight: 800;
            margin-bottom: 4px;
        }}
        .metric-lbl {{
            font-size: 0.78rem;
            color: var(--text-secondary);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        /* Controls & Filter Bar */
        .controls {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 14px;
            margin-bottom: 24px;
        }}
        .filter-group {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }}
        .filter-btn {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--text-secondary);
            font-size: 0.82rem;
            font-weight: 600;
            padding: 7px 14px;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.15s ease;
        }}
        .filter-btn:hover {{
            color: #fff;
            border-color: rgba(255, 255, 255, 0.2);
        }}
        .filter-btn.active {{
            background: var(--accent);
            color: #fff;
            border-color: var(--accent);
        }}
        .search-input {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: #fff;
            font-size: 0.85rem;
            padding: 7px 14px;
            border-radius: 6px;
            width: 260px;
            outline: none;
        }}
        .search-input:focus {{
            border-color: var(--accent);
        }}
        /* Finding Card */
        .findings-list {{
            display: flex;
            flex-direction: column;
            gap: 14px;
        }}
        .finding-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 10px;
            overflow: hidden;
            transition: border-color 0.15s ease;
        }}
        .finding-card:hover {{
            border-color: var(--border-hover);
        }}
        .finding-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 16px 20px;
            cursor: pointer;
            user-select: none;
            background: rgba(255, 255, 255, 0.015);
        }}
        .finding-badges {{
            display: flex;
            align-items: center;
            gap: 6px;
            flex-shrink: 0;
        }}
        .badge {{
            font-size: 0.72rem;
            font-weight: 700;
            padding: 2px 7px;
            border-radius: 4px;
        }}
        .badge--critical {{ background: rgba(244, 63, 94, 0.2); color: var(--crit); border: 1px solid var(--crit); }}
        .badge--high {{ background: rgba(245, 158, 11, 0.2); color: var(--high); border: 1px solid var(--high); }}
        .badge--medium {{ background: rgba(59, 130, 246, 0.2); color: var(--med); border: 1px solid var(--med); }}
        .badge--low {{ background: rgba(100, 116, 139, 0.2); color: var(--low); border: 1px solid var(--low); }}
        .badge--code {{ background: rgba(255, 255, 255, 0.06); color: #cbd5e1; font-family: var(--font-mono); }}
        .pill--owasp {{
            font-size: 0.72rem;
            color: #a5b4fc;
            background: rgba(99, 102, 241, 0.12);
            padding: 2px 7px;
            border-radius: 4px;
        }}
        .finding-title {{
            font-size: 0.95rem;
            font-weight: 600;
            color: #ffffff;
            flex: 1;
        }}
        .finding-file-summary {{
            font-family: var(--font-mono);
            font-size: 0.8rem;
            color: var(--text-muted);
            max-width: 320px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }}
        .chevron {{
            font-size: 0.75rem;
            color: var(--text-muted);
            transition: transform 0.2s ease;
        }}
        .finding-card.expanded .chevron {{
            transform: rotate(180deg);
        }}
        .finding-body {{
            display: none;
            padding: 20px;
            border-top: 1px solid var(--border);
            background: var(--bg-panel);
        }}
        .finding-card.expanded .finding-body {{
            display: block;
        }}
        .finding-meta {{
            display: flex;
            gap: 20px;
            font-size: 0.85rem;
            color: var(--text-secondary);
            margin-bottom: 14px;
        }}
        .finding-section {{
            margin-bottom: 12px;
        }}
        .section-label {{
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            margin-bottom: 4px;
        }}
        .section-content {{
            font-size: 0.88rem;
            color: #e2e8f0;
        }}
        /* Remediation Box */
        .remediation-box {{
            margin-top: 18px;
            background: rgba(99, 102, 241, 0.04);
            border: 1px solid rgba(99, 102, 241, 0.25);
            border-radius: 8px;
            padding: 16px;
        }}
        .remediation-header {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 8px;
        }}
        .remediation-tag {{
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            background: var(--accent);
            color: #fff;
            padding: 2px 6px;
            border-radius: 3px;
        }}
        .remediation-title {{
            font-size: 0.9rem;
            font-weight: 600;
            color: #fff;
        }}
        .remediation-action {{
            font-size: 0.84rem;
            color: var(--text-secondary);
            margin-bottom: 10px;
        }}
        .code-wrapper {{
            background: #050608;
            border: 1px solid var(--border);
            border-radius: 6px;
            padding: 12px;
            margin-bottom: 10px;
            overflow-x: auto;
        }}
        .code-wrapper pre {{
            font-family: var(--font-mono);
            font-size: 0.82rem;
            color: #f1f5f9;
        }}
        .suppression-help {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.78rem;
            color: var(--text-muted);
        }}
        .suppress-code {{
            background: rgba(255, 255, 255, 0.06);
            color: #e2e8f0;
            font-family: var(--font-mono);
            padding: 2px 6px;
            border-radius: 4px;
        }}
        .clean-state {{
            padding: 40px;
            text-align: center;
            background: var(--bg-card);
            border: 1px dashed rgba(16, 185, 129, 0.4);
            border-radius: 12px;
            color: var(--success);
            font-weight: 600;
        }}
        @media (max-width: 850px) {{
            .dashboard {{ grid-template-columns: 1fr; }}
            .metrics-grid {{ grid-template-columns: repeat(2, 1fr); }}
            .finding-file-summary {{ display: none; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <div class="brand">
                <div class="brand-icon">
                    <svg viewBox="0 0 100 100" width="22" height="22" fill="none">
                        <path d="M50 20 L26 76 M50 20 L74 76 M35.5 54 L64.5 54" stroke="#ffffff" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <div>
                    <h1 class="brand-title">AgentSec Audit Report</h1>
                    <div class="report-meta">Target: <code>{html.escape(scanned_path)}</code> · 100% Offline Static Analysis</div>
                </div>
            </div>
            <div class="report-meta">
                <span>Rules: <strong>50</strong> · OWASP Agentic 2026 Mapped</span>
            </div>
        </header>

        <!-- Executive Summary Dashboard -->
        <section class="dashboard">
            <div class="score-card">
                <div class="score-gauge">{score}</div>
                <div class="score-grade">Security Grade: {grade}</div>
                <div class="score-status">{html.escape(status)}</div>
            </div>
            <div class="metrics-grid">
                <div class="metric-tile tile--crit">
                    <div class="metric-val" style="color: var(--crit);">{c['critical']}</div>
                    <div class="metric-lbl">Critical</div>
                </div>
                <div class="metric-tile tile--high">
                    <div class="metric-val" style="color: var(--high);">{c['high']}</div>
                    <div class="metric-lbl">High</div>
                </div>
                <div class="metric-tile tile--med">
                    <div class="metric-val" style="color: var(--med);">{c['medium']}</div>
                    <div class="metric-lbl">Medium</div>
                </div>
                <div class="metric-tile tile--low">
                    <div class="metric-val" style="color: var(--low);">{c['low']}</div>
                    <div class="metric-lbl">Low</div>
                </div>
            </div>
        </section>

        <!-- Interactive Filter Controls -->
        <section class="controls">
            <div class="filter-group">
                <button class="filter-btn active" data-filter="all">All ({metrics['total_findings']})</button>
                <button class="filter-btn" data-filter="critical">Critical ({c['critical']})</button>
                <button class="filter-btn" data-filter="high">High ({c['high']})</button>
                <button class="filter-btn" data-filter="medium">Medium ({c['medium']})</button>
                <button class="filter-btn" data-filter="low">Low ({c['low']})</button>
            </div>
            <input type="text" class="search-input" id="searchInput" placeholder="Filter by rule, code, or file...">
        </section>

        <!-- Findings List -->
        <main class="findings-list" id="findingsList">
            {rendered_cards}
        </main>
    </div>

    <!-- Client-Side Filter Logic -->
    <script>
        (function() {{
            const filterBtns = document.querySelectorAll('.filter-btn');
            const searchInput = document.getElementById('searchInput');
            const cards = document.querySelectorAll('.finding-card');

            let currentFilter = 'all';
            let searchQuery = '';

            function updateCards() {{
                cards.forEach(card => {{
                    const sev = card.getAttribute('data-severity');
                    const text = card.getAttribute('data-search') || '';

                    const matchesFilter = (currentFilter === 'all' || sev === currentFilter);
                    const matchesSearch = (!searchQuery || text.includes(searchQuery));

                    if (matchesFilter && matchesSearch) {{
                        card.style.display = 'block';
                    }} else {{
                        card.style.display = 'none';
                    }}
                }});
            }}

            filterBtns.forEach(btn => {{
                btn.addEventListener('click', () => {{
                    filterBtns.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    currentFilter = btn.getAttribute('data-filter');
                    updateCards();
                }});
            }});

            if (searchInput) {{
                searchInput.addEventListener('input', (e) => {{
                    searchQuery = e.target.value.toLowerCase().trim();
                    updateCards();
                }});
            }}
        }})();
    </script>
</body>
</html>
"""
    return html_content
