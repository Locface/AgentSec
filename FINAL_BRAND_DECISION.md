# Final Brand Decision — AgentSec

Founder-level consolidation of `BRAND_AUDIT.md` and `BAD_LOGO_PATTERNS.md`. This document overrides prior phase conclusions where they don't survive a second, harder attack. It contains no new research — only the decision.

**Status:** direction chosen, not approved for implementation. No SVG, no thumbnails, no images produced from this document.

---

## Decision

# Agent Reach Mark

One asymmetric actor node (the agent), connecting to exactly two or three **differently-shaped** endpoint terminals (representing distinct capability surfaces — e.g. shell, filesystem, network), partially enclosed by a single open boundary stroke (not a closed ring, not a radar circle).

Core semantic: **one actor, its limited reachable surfaces, before execution.** Not a network. Not a graph of peers. Not a permission dashboard.

This replaces the audit's "Capability Map Mark" label — same lineage, tighter constraints, new name because "map" implied cartography/dashboard and undersold the point: this is about **one agent's reach**, not a general-purpose graph primitive.

---

## What changed after re-challenge

The original audit treated "Capability Map Mark" as safely differentiated from Tailscale/network-graph iconography by "using a central actor instead of a mesh." That mitigation is necessary but was under-specified, and the audit did not test the strongest available rival, Permission Lattice, against the sharpest possible objection to it.

Two things changed on re-attack:

1. **The node-graph risk is worse than the audit stated.** Connected-dot iconography isn't just "similar to Tailscale" — it is the single most overused abstract mark in tech since ~2015 (AI, blockchain, IoT, cloud, data-mesh, "synergy" SaaS all use it). HN and r/programming specifically mock this genre by name ("connected dots logo"). This is a stronger and more specific objection than anything in Phase 5. It nearly killed the concept.

2. **Permission Lattice looks stronger on paper than it survives in context.** A small grid of filled/empty cells scores well on favicon robustness and originality-versus-security-clichés. But it collides with visual language AgentSec's own audience sees constantly, on the exact platform AgentSec lives on: GitHub's contribution heatmap, GitHub Actions build-matrix badges, and generic test-coverage-matrix icons. Placed next to real GitHub UI (contribution graph, Actions badges, CI matrix output) in a README or org page, a lattice mark risks being read as status noise, not a logo. This is a collision the original scoring table (which only checked "grid = generic app icon") did not catch. It is disqualifying for a GitHub-native OSS tool, regardless of its strong abstract scores.

Net effect: neither finalist survives unmodified. The node-actor direction survives only if forced into strict asymmetry (never a peer-graph). The lattice direction does not survive at all once checked against GitHub's actual UI chrome, which the original scoring never tested.

---

## Non-negotiable rejections (not re-litigated in detail)

Carried forward from `BAD_LOGO_PATTERNS.md`, restated only as a checklist — no new argument needed, the audit already made these cases:

- shield, lock, hoodie, hacker silhouette, skull — security-cliché, wrong category signal.
- green matrix / code rain — dated cyberpunk decoration.
- hexagon — generic B2B/security filler, zero ownership.
- gradient-as-primary-device — fails monochrome/favicon/print, dates fast.
- AI sparkle — contradicts AgentSec's own "no LLM, deterministic" trust story.
- stock security combo icons (shield+lock, eye+shield, fingerprint) — category noise.
- clipart/mascot — undermines credibility before the README is read.
- checkmark/checklist glyph, magnifier/lens, radar sweep, compass — all scored ≤39/60 in the audit for being either too generic or already owned by adjacent categories (linting, search, monitoring, navigation). No further debate warranted.

---

## Finalists actually compared

Only two concepts cleared the bar for a real head-to-head. Everything else in the audit's shortlist is downgraded to "supporting graphic element, not primary mark" and dismissed briefly below.

1. **Agent Reach Mark** (refined Capability Map Mark)
2. **Permission Lattice**

Demoted, with one-line reason each:

- **Cursor Node + Capability Endpoints** — not a separate concept; it's the execution detail that makes Agent Reach Mark work (asymmetric actor). Folded into the winner, not scored separately.
- **Permission Diff (+/−)** — reads as `git diff`/code review, not agent-capability security. Wrong category signal for a first glance.
- **Local Boundary / Touch Radius** — alone, reads as target/radar/monitoring. Useful only as the boundary stroke inside Agent Reach Mark, never standalone.
- **Deterministic Rule Stack / Config Brackets** — terminal-friendly but generic list/config icon; no brand recall after a week.

---

## Direct scoring — the only two that matter

Scale 1–10.

| Criterion | Agent Reach Mark | Permission Lattice |
|---|---:|---:|
| Memorability | 7 | 6 |
| Recognition after one glance | 6 | 5 |
| Works as GitHub avatar | 8 | 6 |
| Works as favicon (16×16) | 7 | 8 |
| Works in monochrome | 9 | 9 |
| Works in terminal docs | 6 | 8 |
| Works in print | 8 | 8 |
| Timelessness | 6 | 5 |
| Engineering aesthetic | 9 | 8 |
| Brand uniqueness | 6 | 4 |
| **Total** | **72 / 100** | **67 / 100** |

Lattice wins on raw favicon/terminal mechanics. It loses on the criterion that actually decides adoption: **brand uniqueness**, once the GitHub-chrome collision is factored in — a factor the raw abstract score can't see, because it isn't a property of the shape in isolation, it's a property of the shape *in the exact context where the audience will see it every day*. That context-collision is why Lattice is rejected despite comparable numbers.

---

## Why Permission Lattice loses (the decisive reason)

Not "too generic" in the abstract — the audit already conceded it's engineering-native and non-cliché versus security marks. It loses for one concrete, disqualifying reason:

**It visually collides with GitHub's own UI that AgentSec's exact audience sees daily** — contribution heatmaps, Actions build-matrix badges, coverage-matrix badges. A grid-of-cells mark placed in a README next to a real GitHub Actions badge or contribution graph does not read as an identity — it reads as more status chrome. For a GitHub-native CLI tool whose primary distribution surface is a GitHub README, that's a fatal, not a cosmetic, problem. This was not tested in the original Phase 4/5 scoring, which only checked lattice-vs-generic-app-icon.

---

## Why Agent Reach Mark wins, once tightened

It is the only concept that passes all three of the founder-level filters simultaneously:

1. **Not fear-based, not cliché.** It has never been a security stock symbol.
2. **Semantically exact.** It literally is a small map of "one actor, its few reachable surfaces" — which is the product's own tagline, not an interpretation of it.
3. **Does not collide with adjacent-category iconography** — as long as it is built to reject peer-graph symmetry (see constraints below). Nothing in AgentSec's daily distribution context (GitHub README, PyPI badge row, terminal output, VS Code extension icon) already owns "one asymmetric actor with 2–3 distinct-shaped reach terminals."

It wins on the criteria that predict recall (memorability, GitHub avatar, engineering aesthetic, uniqueness) even though it costs a point versus Lattice on raw favicon/terminal mechanics — and those mechanical costs are solvable through disciplined geometry (below), whereas Lattice's context-collision is not solvable through geometry at all.

---

## One-week memory test

Five contexts, one question each: would a developer who saw this once, a week ago, recognize it again?

- **GitHub (org/repo avatar):** Yes, if the actor shape is distinct (not a plain circle). A generic circle-and-lines composition fails this test; a notched/wedge actor with two visibly different terminal shapes passes.
- **PyPI (package listing row, tiny thumbnail):** Marginal. At true PyPI-list thumbnail size, only the actor silhouette will register — the terminals may not. Acceptable, because the actor alone must still read as *a shape*, not the whole capability story. The full mark does its work at README/avatar size, not at PyPI-row size.
- **Hacker News (linked screenshot in a comment):** Passes if monochrome and sparse. Fails immediately if colored with a gradient or drawn with more than three terminals — that's when it reads as "AI startup node-graph, seen it before" and gets the exact mockery the audit's own Phase 5 predicted.
- **Terminal README (no color, fixed-width font nearby):** Passes as a static SVG image; do not attempt an ASCII-art equivalent as the primary identity — the skeleton sketch in the audit was illustrative only, never intended as shipped art.
- **VS Code (extension/marketplace icon, small square):** Passes only if rendered as a single flat-color silhouette with no thin hairline strokes. This is a hard production constraint, not a design nicety.

Verdict: passes 4 of 5 outright, and the fifth (PyPI row) degrades gracefully rather than breaking. Lattice fails the Hacker News test outright (reads as "another grid icon, is this a coverage badge?") and fails GitHub avatar recognition for the reason already given.

---

## Final attack on the winner

**"What would make this look outdated in five years?"**

Three concrete failure modes, each avoidable by construction — not inherent to the concept:

1. **Gradient, glow, or 3D bevel rendering.** Any of these date a mark within 2–3 years regardless of the underlying shape. Mitigation: flat single color, no shading, ever — the primary mark ships monochrome and stays monochrome.

2. **Symmetric peer-graph execution.** If the actor is a plain circle and the terminals are also plain circles connected by uniform thin lines, this collapses into the exact "connected-dots AI/network startup" cliché that is already tired today, let alone in five years. Mitigation is structural, not stylistic: the actor must be a distinct non-circular silhouette (wedge/notch), and the 2–3 terminals must each use a *different* shape from each other and from the actor. Symmetry is what makes a graph read as generic; asymmetry is what makes this one read as a specific idea.

3. **Endpoint creep.** Adding a fourth, fifth, sixth terminal as the product's rule count grows (currently ~41 rules across many categories) would turn the mark into a busy diagram and revive the "AI/data mesh" reading. Mitigation: the mark represents the *idea* of limited reach, not a literal enumeration of scanned categories. Hard cap at three terminals, permanently, regardless of how many rules AgentSec ships. This is a brand rule, not a product-accuracy rule — the logo is not a feature diagram.

All three failure modes are execution mistakes, not properties of the concept itself. Each has a specific, checkable construction rule that prevents it. Because the risk is avoidable by discipline rather than inherent to the direction, the concept survives this attack. If any future execution violates the three rules above, that specific execution — not the direction — should be rejected and redone.

---

## Permanent direction (for the next, separate approval)

Composition rules for whoever eventually builds the SVG (not now):

- One actor: a non-circular, asymmetric silhouette (wedge/notch/bracket-derived — never a plain circle or square).
- Exactly two or three reach terminals, each a visibly different simple shape from the actor and from each other (e.g., small square, small ring, small triangle) — never identical dots.
- One partial boundary stroke, open (not closed), suggesting a local/inspection edge — never a full circle (radar) or full frame (badge).
- Flat, single-color rendering as the canonical form. Color variants (severity palettes, accent colors) are secondary and never replace the monochrome base.
- No more than ~6 total SVG primitives in the base mark.
- Must be legible as a distinct silhouette at 16×16 before any wordmark lockup is attempted.

---

## Approval gate

This document recommends **Agent Reach Mark** — the sole surviving direction — as AgentSec's permanent identity concept, replacing the audit's "Capability Map Mark" label with tighter, non-negotiable construction constraints, and explicitly rejecting Permission Lattice for a context-collision reason the original audit did not test.

No visual asset has been produced. Next step, only after explicit approval, is 3–5 monochrome thumbnail sketches built strictly to the composition rules above, evaluated at favicon/avatar/README sizes before any production SVG work begins.

**Waiting for approval.**
