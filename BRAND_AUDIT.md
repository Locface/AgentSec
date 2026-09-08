# AgentSec Brand Audit

> Scope: first-principles visual identity redesign for AgentSec.  
> Status: audit and strategic recommendation only. **No SVG/logo implementation yet.**

## Executive summary

AgentSec should not visually behave like a generic cybersecurity company.

AgentSec is a developer-first, CLI-first static scanner for AI agent and MCP configuration risk. Its core promise is:

> **Know what your AI agent can touch before it runs.**

That sentence is the brand foundation. The identity should therefore communicate:

- visibility before execution;
- capability awareness;
- local/offline trust;
- engineering precision;
- deterministic inspection, not magical AI;
- calm confidence, not threat theatre.

The strongest direction is a **capability map / reach graph** identity: a minimal geometric mark showing a central agent node and the surfaces it can reach, with one controlled boundary or inspection frame. This is more specific than a shield, lock, bug, eye, or AI sparkle. It also maps directly to the product’s job: representing what an agent can access before it runs.

Final recommendation: **Direction A — Capability Map Mark**.

Do not implement yet. This document is for approval before SVG generation.

---

## Product truth that should drive the identity

AgentSec is not:

- antivirus;
- EDR;
- SOC;
- pentest platform;
- vulnerability scanner in the broad dependency/CVE sense;
- cloud security dashboard;
- AI assistant;
- runtime protection layer.

AgentSec is:

- offline-first;
- zero-network-trust;
- AI Agent Security Scanner;
- open source;
- developer-first;
- CLI-first;
- minimal;
- engineering-oriented;
- deterministic/static analysis;
- local visibility into risky agent capabilities.

Current repository facts checked during this audit:

- README describes AgentSec as a “Static security scanner for AI coding agents and MCP configurations.”
- README states that AgentSec inspects MCP manifests, Claude Desktop configs, Cursor rules, and agent instruction files with no LLM dependencies and no data leaving the machine.
- README currently references image files at `docs/images/agentsec-dark.svg` and `docs/images/agentsec-light.svg`, but those files were not found in the repository during this audit.
- No existing `.svg` or `.png` logo assets were found in the current AgentSec repository checkout.

This means the redesign is not replacing a strong existing symbol. It is an opportunity to establish the first durable visual system.

---

# Phase 1 — Competitive research

The goal of the competitive audit is not to imitate these projects. It is to understand which visual devices become memorable in developer infrastructure and which devices AgentSec should avoid.

Projects checked as part of this audit included official websites/docs for: Semgrep, Trivy, Checkov, Bandit, CodeQL, Gitleaks, Ruff, uv, Docker, GitHub, Terraform, OpenTofu, OpenSSH, Tailscale, Grafana, Prometheus, Sentry, Cloudflare, Supabase, Linear, and Vercel.

## 1. Semgrep

**Visual identity:** wordmark plus abstract mark; bright, modern developer-security SaaS presentation.

**Why it works:**

- The name is extremely strong: “semantic grep” is memorable to engineers before the logo even appears.
- The identity sits between developer tooling and security without looking like antivirus.
- The mark is simple enough to work as a favicon and product icon.
- It benefits from consistent repetition across docs, app, CLI references, and marketing.

**What makes it memorable:**

- The name itself is sticky and technical.
- The visual system feels code-native rather than enterprise-security-native.
- It avoids the worst security clichés: no shield, no lock, no hoodie.

**What AgentSec should not copy:**

- Do not copy the bright SaaS-security energy too closely; AgentSec should feel more local, minimal, and CLI-first.
- Do not use abstract geometry that does not clearly encode the product idea.
- Do not become “another SAST brand.” AgentSec’s domain is agent capability surfaces, not generic code scanning.

**What users recognize instantly:**

- The name “Semgrep.”
- The association with code scanning / static analysis.
- The simple app-security developer-tool register.

## 2. Trivy

**Visual identity:** approachable illustrated mascot/mark, associated with Aqua Security ecosystem.

**Why it works:**

- Friendly and approachable for an open-source scanner.
- The name is short and easy to remember.
- The mascot-like quality makes it more distinct than a generic shield.
- It feels OSS-friendly rather than corporate-only.

**What makes it memorable:**

- The combination of short name and recognizable mascot/creature mark.
- Strong association with container/image scanning and practical DevSecOps.

**What AgentSec should not copy:**

- Do not use a mascot unless it is truly ownable and durable. Mascots can make serious security tools feel cute or informal.
- Do not borrow the “scanner mascot” pattern; AgentSec should be more austere and engineering-oriented.
- Do not imply container vulnerability scanning; Trivy already owns that mental territory.

**What users recognize instantly:**

- Trivy as a practical scanner.
- The friendly icon and Aqua ecosystem connection.

## 3. Checkov

**Visual identity:** infrastructure-as-code scanner identity; comparatively functional and docs/product-led.

**Why it works:**

- The name is memorable because it sounds like “check” and has a distinctive suffix.
- The brand is strongly tied to IaC scanning and policy checks.
- It is recognizable in DevSecOps because of usage, not because the visual identity is exceptionally iconic.

**What makes it memorable:**

- The product category association: Terraform/Kubernetes/IaC scanning.
- The name works as an action: “run Checkov.”

**What AgentSec should not copy:**

- Do not rely on name recognition alone while using a weak or generic visual mark.
- Do not look like a policy dashboard or IaC-only scanner.
- Do not use generic checkmark/security imagery.

**What users recognize instantly:**

- The Checkov name in IaC/security scanning contexts.
- Policy check / configuration scanning association.

## 4. Bandit

**Visual identity:** Python security linter with minimal/older-docs style identity.

**Why it works:**

- The name is memorable and category-adjacent: “Bandit” suggests finding bad things in Python code.
- It is simple, utilitarian, and OSS-native.
- It does not depend on heavy marketing visuals.

**What makes it memorable:**

- Strong name.
- Long-term presence in Python security tooling.
- Utility over polish.

**What AgentSec should not copy:**

- Do not copy the “security character” implication too literally. A bandit/criminal metaphor would move AgentSec toward attacker imagery.
- Do not accept weak visual polish just because the tool is OSS.
- Do not feel dated.

**What users recognize instantly:**

- Python security linting.
- Simple docs/tooling context.

## 5. CodeQL

**Visual identity:** GitHub-native code analysis identity; technical and query-oriented.

**Why it works:**

- It has extremely strong parent-brand leverage from GitHub.
- The name clearly says code + query language.
- Visual identity can be restrained because GitHub provides trust and distribution.
- It feels like analysis infrastructure, not security theatre.

**What makes it memorable:**

- “QL” anchors the idea of querying code.
- Association with GitHub Advanced Security.
- Clean technical presentation.

**What AgentSec should not copy:**

- Do not imitate GitHub’s visual language too closely; AgentSec needs its own identity.
- Do not use query/database metaphors unless they directly support the capability-awareness message.
- Do not become visually enterprise-heavy.

**What users recognize instantly:**

- Code scanning.
- GitHub security integration.
- Query-based analysis.

## 6. Gitleaks

**Visual identity:** direct, name-led secrets scanning identity.

**Why it works:**

- The name is the brand: Git + leaks is instantly understandable.
- The identity is narrow and specific.
- Users remember what it does after seeing the name once.

**What makes it memorable:**

- Semantic clarity.
- Strong CLI/security utility association.
- Focused problem: secrets leaks.

**What AgentSec should not copy:**

- Do not use “leak/drip” visual metaphors; that would over-index on secrets, while AgentSec is broader.
- Do not use Git-centric imagery; AgentSec scans agent/MCP configuration surfaces, not only repositories.
- Do not rely only on the wordmark. AgentSec needs a strong symbol for GitHub/PyPI/docs avatars.

**What users recognize instantly:**

- Secrets scanning.
- Git repository leak detection.

## 7. Ruff

**Visual identity:** fast Python linter/formatter; memorable dog/ruff association in the wider Astral ecosystem.

**Why it works:**

- The name is short, fast, and command-like.
- The identity is extremely developer-native.
- It feels fast and modern without heavy ornament.
- It benefits from the Astral ecosystem’s consistent docs and design.

**What makes it memorable:**

- Four-letter name.
- Strong speed reputation.
- Clean docs and tool experience.
- Dog/name association without needing a complex illustration everywhere.

**What AgentSec should not copy:**

- Do not force a cute animal/personality unless the product naturally supports it.
- Do not copy Astral’s exact visual register; AgentSec should feel more security-aware and capability-focused.
- Do not make speed the primary brand signal. AgentSec’s primary signal is pre-run awareness/trust.

**What users recognize instantly:**

- Python linting/formatting.
- Fast replacement for older tooling.
- Astral ecosystem.

## 8. uv

**Visual identity:** minimal Astral developer tooling identity.

**Why it works:**

- The name is extremely short and CLI-native.
- It looks and feels like infrastructure: low-friction, modern, fast.
- The identity does not need much decoration because the product experience is the brand.

**What makes it memorable:**

- Two-letter command.
- Speed and simplicity.
- Consistency with Ruff/Astral.

**What AgentSec should not copy:**

- AgentSec cannot rely on a two-letter name; it needs a stronger icon system.
- Do not over-minimize to the point of anonymity.
- Do not borrow the Astral ecosystem look directly.

**What users recognize instantly:**

- Fast Python package/project tooling.
- Minimal command-line product.

## 9. Docker

**Visual identity:** whale carrying containers.

**Why it works:**

- It turns an abstract technical concept into a concrete metaphor.
- The whale + containers is instantly recognizable even at small sizes.
- It is friendly without being unserious.
- The mark owns the category: containers.

**What makes it memorable:**

- Unique silhouette.
- Clear metaphor: carrying/shipping containers.
- Strong blue color association.

**What AgentSec should not copy:**

- Do not use a mascot just because Docker did. Docker’s mascot works because containers are physical and visual.
- Do not imitate the blue friendly infrastructure aesthetic too closely.
- Do not use stacked boxes unless the concept is specifically about capability surfaces.

**What users recognize instantly:**

- Whale silhouette.
- Containers.
- Developer infrastructure.

## 10. GitHub

**Visual identity:** Octocat; black/white minimal platform identity.

**Why it works:**

- The Octocat is one of the most distinctive developer mascots ever created.
- Black/white simplicity gives it endless flexibility.
- The symbol is not literal “git”; it is ownable and culturally embedded.
- The mark works as avatar, favicon, sticker, UI icon, and conference symbol.

**What makes it memorable:**

- Unique character silhouette.
- Massive repetition across developer culture.
- Strong monochrome compatibility.

**What AgentSec should not copy:**

- Do not attempt a character mascot unless it can reach similar distinctiveness, which is unlikely for a security scanner.
- Do not use cat/animal/cute OSS tropes without deep reason.
- Do not assume a weird mascot automatically creates memorability.

**What users recognize instantly:**

- Octocat.
- GitHub platform.
- Developer social/code hosting.

## 11. Terraform

**Visual identity:** geometric stacked blocks/cubes, purple HashiCorp ecosystem.

**Why it works:**

- The mark reflects infrastructure composition.
- Simple modular geometry matches the product’s mental model.
- Purple is distinctive in infrastructure tooling.
- It scales well across docs, CLI, and enterprise UI.

**What makes it memorable:**

- Three-dimensional block composition.
- Purple association.
- Strong link to declarative infrastructure.

**What AgentSec should not copy:**

- Do not use block/cube geometry unless clearly differentiated; Terraform strongly owns modular infrastructure blocks.
- Do not use purple simply to feel “infrastructure.”
- Do not look like an IaC product unless intentionally positioning near policy/config scanning.

**What users recognize instantly:**

- Infrastructure as code.
- HashiCorp ecosystem.
- Declarative resource graph.

## 12. OpenTofu

**Visual identity:** playful tofu/fork alternative to Terraform.

**Why it works:**

- It deliberately contrasts with corporate IaC branding.
- The name and mark are highly memorable because they are unusual.
- It signals open-source community ownership and independence.

**What makes it memorable:**

- Playful food metaphor.
- Clear relation/opposition to Terraform.
- OSS fork narrative.

**What AgentSec should not copy:**

- Do not use playful food/object metaphors unless they clarify the product.
- AgentSec should not look like a fork/replacement of an existing tool.
- Do not sacrifice seriousness for memorability.

**What users recognize instantly:**

- Open-source Terraform alternative.
- Community fork energy.

## 13. OpenSSH

**Visual identity:** old-school, utilitarian open-source security infrastructure.

**Why it works:**

- It is trusted because of utility, longevity, and cryptographic seriousness, not modern branding.
- The minimal/old-web presentation reinforces stability.
- It avoids marketing excess entirely.

**What makes it memorable:**

- Name and ubiquity.
- Functional austerity.
- Deep trust accumulated over time.

**What AgentSec should not copy:**

- Do not copy dated web aesthetics.
- Do not assume austere means visually unfinished.
- Do not use lock/key metaphors just because OpenSSH is security infrastructure.

**What users recognize instantly:**

- Secure shell.
- Foundational infrastructure.
- Serious open-source security.

## 14. Tailscale

**Visual identity:** dot-grid/network motif; friendly, calm secure connectivity.

**Why it works:**

- The dot/grid motif maps directly to networks and devices.
- It is simple, flexible, and not fear-based.
- It communicates connectivity and trust without shields/locks.
- The tone is highly developer-friendly.

**What makes it memorable:**

- Distinct dotted-device/network visual system.
- Calm copy and brand voice.
- Modern infrastructure trust without cyber clichés.

**What AgentSec should not copy:**

- Do not copy dot-grid networking too closely; AgentSec is not a mesh VPN.
- Be careful with node graphs: they can become Tailscale-like if too network-centric.
- Do not use rounded friendly minimalism so heavily that the security edge disappears.

**What users recognize instantly:**

- Secure private networking.
- Devices/nodes connected simply.
- Developer-first infrastructure.

## 15. Grafana

**Visual identity:** orange spiral/swirl.

**Why it works:**

- The spiral is distinctive and unlike most infrastructure marks.
- It implies dashboards, data, and observability without drawing charts literally.
- Orange is highly recognizable in the category.
- The mark is simple enough to survive as a favicon.

**What makes it memorable:**

- Ownable swirl shape.
- Strong color association.
- Observability ecosystem repetition.

**What AgentSec should not copy:**

- Do not use spirals or circular data motifs unless tied to inspection/capability mapping.
- Do not rely on an arbitrary abstract symbol; Grafana’s has become meaningful through repetition, but AgentSec needs clearer first-read semantics.
- Avoid orange if it pushes too close to Grafana/Cloudflare/Sentry territory unless justified.

**What users recognize instantly:**

- Grafana dashboards.
- Observability.
- Orange swirl.

## 16. Prometheus

**Visual identity:** flame/torch/meteor-like symbol in orange/red.

**Why it works:**

- The mythological name and flame symbol reinforce each other.
- The mark is bold and simple.
- It feels like infrastructure, metrics, and alerting without drawing a chart.

**What makes it memorable:**

- Flame silhouette.
- Strong single-color rendering.
- Long-term use in cloud-native monitoring.

**What AgentSec should not copy:**

- Do not use mythic/fire symbolism; it does not map to AgentSec.
- Do not adopt alerting/monitoring visual cues.
- Do not choose a bold icon that is memorable but semantically unrelated.

**What users recognize instantly:**

- Metrics/monitoring.
- Prometheus server.
- Cloud-native observability.

## 17. Sentry

**Visual identity:** sharp, geometric sentry/helmet-like mark; strong developer-error monitoring brand.

**Why it works:**

- The name and mark align: a sentry watches for problems.
- The mark is distinctive and angular.
- It has a strong silhouette and works in monochrome.
- It feels technical but not generic.

**What makes it memorable:**

- Strong black/white angular symbol.
- Name-symbol alignment.
- Developer workflow ubiquity.

**What AgentSec should not copy:**

- Do not use watchman/guard/helmet forms; they move toward security guard metaphors.
- Do not make AgentSec feel like error monitoring.
- Do not use aggressive angularity if it implies threat/blocking rather than inspection.

**What users recognize instantly:**

- Error monitoring.
- Developer observability.
- Sentry’s angular symbol.

## 18. Cloudflare

**Visual identity:** orange cloud.

**Why it works:**

- Extremely simple category association: cloud infrastructure.
- Color is distinctive and consistently owned.
- Works at small sizes and across many products.
- Friendly but infrastructure-grade.

**What makes it memorable:**

- Orange cloud silhouette.
- Broad repetition across internet infrastructure.
- Direct name-image relationship.

**What AgentSec should not copy:**

- Do not use cloud imagery; AgentSec is offline-first and zero-network-trust.
- Do not use orange cloud/security combinations.
- Do not imply hosted edge/network service.

**What users recognize instantly:**

- Internet edge/cloud/CDN/security.
- Orange cloud.

## 19. Supabase

**Visual identity:** green angular database/lightning-like mark.

**Why it works:**

- The mark is simple and sharp.
- Green/black palette is recognizable.
- It communicates developer infrastructure and open-source alternative energy.
- It scales well as a favicon and avatar.

**What makes it memorable:**

- Distinct angular green symbol.
- Open-source Firebase alternative positioning.
- Consistent dark developer aesthetic.

**What AgentSec should not copy:**

- Do not use green/black in a way that reads as database or generic dev SaaS.
- Do not borrow the angular split/lightning shape.
- Avoid “open-source alternative” visual tropes unless they support AgentSec’s own category.

**What users recognize instantly:**

- Supabase database/backend platform.
- Green mark.
- OSS developer backend.

## 20. Linear

**Visual identity:** ultra-minimal dark/neutral product system; refined wordmark and precise geometric mark.

**Why it works:**

- It feels focused, fast, and premium.
- It avoids gimmicks.
- The visual system supports the product’s promise: issue tracking with speed and clarity.
- The identity is quiet but extremely consistent.

**What makes it memorable:**

- Product experience and visual restraint reinforce each other.
- The name and UI design do much of the brand work.
- Dark refined minimalism.

**What AgentSec should not copy:**

- Do not become so minimal that the mark is anonymous.
- Do not copy the premium SaaS aesthetic at the expense of OSS/CLI friendliness.
- Do not use abstract lines without a product-specific idea.

**What users recognize instantly:**

- High-quality product design.
- Issue tracking/work planning.
- Minimal dark interface.

## 21. Vercel

**Visual identity:** black triangle.

**Why it works:**

- Extreme simplicity.
- The triangle is instantly recognizable due to repetition and consistency.
- It works perfectly in monochrome, favicons, avatars, and UI.
- It feels like deployment/infrastructure without visual clutter.

**What makes it memorable:**

- One shape.
- Black/white contrast.
- Consistency over time.

**What AgentSec should not copy:**

- Do not pick a primitive shape with no specific meaning and hope consistency will make it iconic.
- Avoid triangle/pyramid shapes that resemble Vercel too closely.
- Do not over-index on minimalism if it fails to communicate capability awareness.

**What users recognize instantly:**

- Vercel deployment platform.
- Black triangle.
- Frontend/cloud infrastructure.

---

## Competitive patterns that matter for AgentSec

### What strong developer-tool identities share

1. **They work in one color.** GitHub, Vercel, Terraform, Prometheus, Sentry, Docker, and Tailscale all survive monochrome usage.
2. **They have a clear silhouette.** The icon is not dependent on texture or tiny detail.
3. **They map to a product mental model.** Docker has containers. Terraform has blocks. Tailscale has connected nodes. Prometheus has a torch/flame tied to the name.
4. **They avoid generic cyber fear imagery.** The best developer-security tools do not need hoodies, matrix code, skulls, or locks.
5. **They become memorable through repetition and restraint.** A simple mark used consistently beats a complex mark used inconsistently.

### What AgentSec should borrow conceptually

- From Docker: use a metaphor tied to the product’s actual model.
- From Tailscale: communicate trust and infrastructure without fear.
- From Vercel: make the silhouette simple enough to survive anywhere.
- From Terraform: use geometry only when it reflects the domain model.
- From Semgrep/Gitleaks: make the category understandable quickly.
- From OpenSSH: maintain security seriousness and avoid hype.
- From Linear: prefer precision and restraint over decoration.

### What AgentSec should reject

- Security cliché marks: shields, locks, hackers, bugs, crosshairs.
- Generic AI marks: sparkles, robot heads, neural-network blobs.
- Cloud/network implications: clouds, edge arcs, global mesh unless tightly tied to risk surfaces.
- Overly playful mascots unless the concept becomes uniquely ownable.
- Abstract shapes that could belong to any SaaS startup.

---

# Phase 2 — Anti-patterns

A separate document has been created:

- [`BAD_LOGO_PATTERNS.md`](BAD_LOGO_PATTERNS.md)

Summary of its position:

AgentSec should avoid:

- shields;
- locks;
- hacker icons;
- hoodies;
- green matrix visuals;
- hexagons as generic technical filler;
- decorative gradients;
- generic AI sparkles;
- stock security symbols;
- clipart style.

The core reason is that all of these communicate the wrong category. AgentSec is not “cybersecurity in general.” It is deterministic visibility into AI-agent capabilities.

---

# Phase 3 — Brand positioning

## Visual language

AgentSec should visually live at the intersection of:

- static analysis;
- local developer tools;
- access/capability mapping;
- preflight checks;
- trust through inspectability;
- minimal OSS infrastructure.

The identity should feel closer to:

- `git diff`;
- `terraform plan`;
- `docker inspect`;
- `tailscale status`;
- `semgrep scan`;
- `ruff check`;
- `codeql query`;

than to:

- antivirus dashboard;
- SIEM/SOC console;
- hacker-themed security product;
- AI chatbot;
- cloud posture dashboard.

## What should the logo make a developer feel?

A developer should feel:

- “This tool is precise.”
- “This runs locally and does not phone home.”
- “This helps me understand blast radius before execution.”
- “This is engineering infrastructure, not marketing theatre.”
- “This can belong in a README badge, CI log, and terminal output.”
- “I can trust this because it is inspectable.”

The emotional target is **calm control**.

Not fear.  
Not excitement.  
Not magic.  
Not cyber-drama.  
Not enterprise dashboard polish.

## What should it communicate in 2 seconds?

In two seconds, the mark should communicate:

> AgentSec maps what an AI agent can reach.

Secondary messages:

- local/offline inspection;
- capability awareness;
- deterministic scanner;
- security without fear-based symbolism;
- developer-first precision.

## What should distinguish it from every security startup?

Most security startups visually say:

- “we protect you” with a shield;
- “we lock things” with a lock;
- “we detect hackers” with attacker imagery;
- “we use AI” with sparkles/neural blobs;
- “we are enterprise” with blue gradients and abstract hexagons.

AgentSec should instead say:

> “Here is the map of what your agent can touch.”

This is the differentiator. It is not about generic defense. It is about **pre-execution visibility**.

## Proposed personality traits

- **Precise** — geometric, measured, intentional.
- **Local** — no cloud symbolism, no global swooshes.
- **Minimal** — few paths, strong silhouette.
- **Technical** — comfortable in docs, CLIs, GitHub, PyPI.
- **Trustworthy** — calm, static, non-hysterical.
- **Open-source** — not overproduced, not enterprise-only.
- **Deterministic** — no magical AI visuals.

## Color direction

Logo must work in pure monochrome first.

Possible palette later:

- near-black / off-white base;
- muted terminal green as a secondary accent, but **not** matrix green;
- cool cyan/blue only if used sparingly for “visibility/inspection,” not corporate security;
- amber only as warning severity accent, not primary brand unless carefully separated from Grafana/Cloudflare/Sentry.

Avoid making the brand dependent on gradients. If a gradient is ever used, it should be optional web decoration, never the mark’s core recognition mechanism.

---

# Phase 4 — Concept generation

Scoring scale: 1–10.

Criteria:

- **Memorability** — will users remember it?
- **Recognition** — will it be identifiable at small sizes and repeated contexts?
- **Originality** — does it avoid category clichés?
- **Engineering aesthetic** — does it feel like developer infrastructure?
- **OSS fit** — does it feel credible for an open-source CLI tool?
- **Timelessness** — will it still work in five years?

## Concept 1 — Capability Map Mark

**Description:** A central minimal node representing the agent, with three or four small endpoint nodes representing shell, filesystem, network, and secrets. A partial boundary or inspection frame shows the reachable surfaces.

**Symbolism:** AgentSec maps what the agent can touch before it runs.

**Uniqueness:** Strongly tied to the product idea; avoids generic security symbols.

**Scalability:** Excellent if reduced to one central node and three endpoints.

**Favicon quality:** Strong. A node/edge structure can survive at 16×16 if simplified.

**GitHub avatar quality:** Strong. Circular/square avatar can hold a compact graph mark.

**Terminal friendliness:** Good. Can be represented in ASCII conceptually: `agent -> fs/net/shell`.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent: circles, lines, possibly one boundary path.

**Long-term brand value:** High. It can become the visual language for docs diagrams, scan reports, and website sections.

| Criterion | Score |
|---|---:|
| Memorability | 8 |
| Recognition | 8 |
| Originality | 8 |
| Engineering aesthetic | 10 |
| OSS fit | 9 |
| Timelessness | 9 |
| **Total** | **52 / 60** |

**Verdict:** Keep.

## Concept 2 — Agent Reach Radar

**Description:** A simplified radar/sweep circle showing an agent point and detected reach zones.

**Symbolism:** Inspection and visibility.

**Uniqueness:** Somewhat specific, but radar is common in security/monitoring.

**Scalability:** Good if simple.

**Favicon quality:** Good.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Medium; radar is less CLI-native.

**Monochrome compatibility:** Good.

**SVG simplicity:** Good.

**Long-term brand value:** Medium. Risk of looking like monitoring/SOC.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 7 |
| Originality | 5 |
| Engineering aesthetic | 7 |
| OSS fit | 7 |
| Timelessness | 6 |
| **Total** | **39 / 60** |

**Verdict:** Reject. Too close to monitoring/security radar clichés.

## Concept 3 — Preflight Checklist Glyph

**Description:** A minimal checklist or terminal prompt with a check state before execution.

**Symbolism:** Scan before run; preflight check.

**Uniqueness:** Clear but generic.

**Scalability:** Good.

**Favicon quality:** Medium; checkmarks become generic.

**GitHub avatar quality:** Medium.

**Terminal friendliness:** Excellent.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent.

**Long-term brand value:** Medium; checkmark logos are overused.

| Criterion | Score |
|---|---:|
| Memorability | 5 |
| Recognition | 5 |
| Originality | 4 |
| Engineering aesthetic | 8 |
| OSS fit | 8 |
| Timelessness | 7 |
| **Total** | **37 / 60** |

**Verdict:** Reject. Too generic and checkmark-heavy.

## Concept 4 — Permission Lattice

**Description:** A small lattice/grid where selected cells show allowed capabilities and blocked cells are absent or muted.

**Symbolism:** Permission matrix; capability model.

**Uniqueness:** Good. Security tools rarely use a permission-matrix mark.

**Scalability:** Medium; grids can become muddy at small sizes.

**Favicon quality:** Medium if reduced to 2×2 or 3×3.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Excellent: maps to table/matrix output.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent.

**Long-term brand value:** High if executed with a distinct pattern.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 7 |
| Originality | 8 |
| Engineering aesthetic | 10 |
| OSS fit | 9 |
| Timelessness | 8 |
| **Total** | **49 / 60** |

**Verdict:** Keep as finalist.

## Concept 5 — Static Scan Aperture

**Description:** A square/crop-frame/aperture inspecting a small agent node or config block.

**Symbolism:** Inspection frame; static scan; visibility.

**Uniqueness:** Moderate. Apertures/scan frames are common.

**Scalability:** Strong.

**Favicon quality:** Strong.

**GitHub avatar quality:** Strong.

**Terminal friendliness:** Medium.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent.

**Long-term brand value:** Medium-high if paired with agent/capability motif.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 8 |
| Originality | 6 |
| Engineering aesthetic | 8 |
| OSS fit | 8 |
| Timelessness | 8 |
| **Total** | **45 / 60** |

**Verdict:** Keep only if merged with capability-map idea; reject as standalone.

## Concept 6 — Local Boundary Ring

**Description:** A simple ring or square boundary around an agent node, with endpoints inside/outside showing local trust boundary.

**Symbolism:** Offline/local boundary; controlled environment.

**Uniqueness:** Good, but ring marks are common.

**Scalability:** Excellent.

**Favicon quality:** Excellent.

**GitHub avatar quality:** Excellent.

**Terminal friendliness:** Medium.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent.

**Long-term brand value:** Good.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 8 |
| Originality | 6 |
| Engineering aesthetic | 8 |
| OSS fit | 8 |
| Timelessness | 8 |
| **Total** | **45 / 60** |

**Verdict:** Keep as supporting idea, not main idea.

## Concept 7 — Agent Footprint

**Description:** A stylized footprint/path showing what an agent would touch.

**Symbolism:** Trace of access before execution.

**Uniqueness:** Medium.

**Scalability:** Medium.

**Favicon quality:** Weak-medium; footprints can read as tracking/analytics.

**GitHub avatar quality:** Medium.

**Terminal friendliness:** Medium.

**Monochrome compatibility:** Good.

**SVG simplicity:** Good.

**Long-term brand value:** Medium.

| Criterion | Score |
|---|---:|
| Memorability | 6 |
| Recognition | 5 |
| Originality | 6 |
| Engineering aesthetic | 6 |
| OSS fit | 6 |
| Timelessness | 6 |
| **Total** | **35 / 60** |

**Verdict:** Reject. Too close to tracking/forensics.

## Concept 8 — Touch Radius

**Description:** A central point with a radius/arc indicating reach, not protection.

**Symbolism:** Blast radius/capability radius.

**Uniqueness:** Good conceptually, but arcs are visually generic.

**Scalability:** Good.

**Favicon quality:** Good.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Medium.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent.

**Long-term brand value:** Medium-high.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 7 |
| Originality | 7 |
| Engineering aesthetic | 8 |
| OSS fit | 8 |
| Timelessness | 8 |
| **Total** | **45 / 60** |

**Verdict:** Keep as possible element inside finalist direction.

## Concept 9 — Config Brackets

**Description:** Curly braces or square brackets enclosing a small capability marker.

**Symbolism:** Config scanning; structured files; code-native.

**Uniqueness:** Medium; many developer tools use brackets.

**Scalability:** Good.

**Favicon quality:** Medium-good.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Excellent.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent.

**Long-term brand value:** Medium.

| Criterion | Score |
|---|---:|
| Memorability | 6 |
| Recognition | 6 |
| Originality | 5 |
| Engineering aesthetic | 9 |
| OSS fit | 9 |
| Timelessness | 8 |
| **Total** | **43 / 60** |

**Verdict:** Reject as main logo; useful for supporting graphics.

## Concept 10 — Terminal Cursor + Boundary

**Description:** A terminal prompt/cursor shape intersecting with a boundary line.

**Symbolism:** CLI-first scanner before execution.

**Uniqueness:** Medium.

**Scalability:** Good.

**Favicon quality:** Medium; terminal icons are common.

**GitHub avatar quality:** Medium.

**Terminal friendliness:** Excellent.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent.

**Long-term brand value:** Medium.

| Criterion | Score |
|---|---:|
| Memorability | 6 |
| Recognition | 6 |
| Originality | 5 |
| Engineering aesthetic | 9 |
| OSS fit | 9 |
| Timelessness | 8 |
| **Total** | **43 / 60** |

**Verdict:** Reject as primary. It says CLI, but not AgentSec’s unique value.

## Concept 11 — Capability Fingerprint

**Description:** A fingerprint-like set of lines, but each ridge represents a capability path.

**Symbolism:** Unique capability profile of an agent.

**Uniqueness:** Interesting but risky.

**Scalability:** Weak; fingerprints need detail.

**Favicon quality:** Weak.

**GitHub avatar quality:** Medium.

**Terminal friendliness:** Weak.

**Monochrome compatibility:** Medium.

**SVG simplicity:** Weak-medium.

**Long-term brand value:** Medium.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 5 |
| Originality | 7 |
| Engineering aesthetic | 6 |
| OSS fit | 6 |
| Timelessness | 6 |
| **Total** | **37 / 60** |

**Verdict:** Reject. Too detailed and too close to identity/security cliché.

## Concept 12 — Permission Diff

**Description:** A compact `+ / -` diff mark showing allowed and risky capabilities.

**Symbolism:** Developer review of access changes.

**Uniqueness:** Strong for developer audience.

**Scalability:** Medium; plus/minus can become generic.

**Favicon quality:** Medium.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Excellent.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent.

**Long-term brand value:** High for docs/report system, medium as logo.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 6 |
| Originality | 8 |
| Engineering aesthetic | 10 |
| OSS fit | 10 |
| Timelessness | 8 |
| **Total** | **49 / 60** |

**Verdict:** Keep as finalist or secondary system.

## Concept 13 — Agent Wiring Diagram

**Description:** A tiny circuit/wiring diagram showing input config routed to tools.

**Symbolism:** Agent wiring/capabilities.

**Uniqueness:** Good but risks circuit-board cliché.

**Scalability:** Medium.

**Favicon quality:** Medium.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Medium.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Medium.

**Long-term brand value:** Medium-high.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 6 |
| Originality | 7 |
| Engineering aesthetic | 9 |
| OSS fit | 8 |
| Timelessness | 7 |
| **Total** | **44 / 60** |

**Verdict:** Reject as standalone; overlaps with generic circuit/security logos.

## Concept 14 — Inspection Lens Without Eye

**Description:** A minimal lens or magnifier over a config node, carefully avoiding eye symbolism.

**Symbolism:** Inspect before run.

**Uniqueness:** Medium-low. Magnifiers are common scanning symbols.

**Scalability:** Excellent.

**Favicon quality:** Excellent.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Medium.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent.

**Long-term brand value:** Medium.

| Criterion | Score |
|---|---:|
| Memorability | 5 |
| Recognition | 7 |
| Originality | 4 |
| Engineering aesthetic | 7 |
| OSS fit | 7 |
| Timelessness | 7 |
| **Total** | **37 / 60** |

**Verdict:** Reject. Too generic scanning/search icon.

## Concept 15 — Blast Radius Rings

**Description:** Concentric rings around an agent node, with clipped sectors for allowed reach.

**Symbolism:** Agent blast radius.

**Uniqueness:** Good within security, but can resemble radar/observability.

**Scalability:** Good.

**Favicon quality:** Good.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Medium.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Good.

**Long-term brand value:** Medium-high.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 7 |
| Originality | 7 |
| Engineering aesthetic | 8 |
| OSS fit | 8 |
| Timelessness | 8 |
| **Total** | **45 / 60** |

**Verdict:** Keep only as subordinate idea; risk of radar cliché.

## Concept 16 — File/Socket/Network Triad

**Description:** Three simple endpoints around an agent: file, socket, globe/network represented abstractly.

**Symbolism:** AgentSec checks dangerous capability combinations.

**Uniqueness:** Strong if abstracted enough.

**Scalability:** Medium; pictograms may be too detailed.

**Favicon quality:** Medium.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Good.

**Monochrome compatibility:** Good.

**SVG simplicity:** Medium.

**Long-term brand value:** High as explanatory diagram, medium as logo.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 6 |
| Originality | 8 |
| Engineering aesthetic | 9 |
| OSS fit | 9 |
| Timelessness | 8 |
| **Total** | **47 / 60** |

**Verdict:** Keep as possible detailed lockup, but simplify for icon.

## Concept 17 — Safe Run Gate

**Description:** A minimal gate before a run/play symbol.

**Symbolism:** Scan before execution.

**Uniqueness:** Low-medium.

**Scalability:** Good.

**Favicon quality:** Good.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Medium.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent.

**Long-term brand value:** Medium.

| Criterion | Score |
|---|---:|
| Memorability | 6 |
| Recognition | 6 |
| Originality | 5 |
| Engineering aesthetic | 7 |
| OSS fit | 7 |
| Timelessness | 7 |
| **Total** | **38 / 60** |

**Verdict:** Reject. Too close to CI gate/play-button generic imagery.

## Concept 18 — Policy Compass

**Description:** Compass-like mark indicating allowed directions/capabilities.

**Symbolism:** Guidance and orientation in agent risk.

**Uniqueness:** Medium.

**Scalability:** Good.

**Favicon quality:** Good.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Weak-medium.

**Monochrome compatibility:** Good.

**SVG simplicity:** Good.

**Long-term brand value:** Medium.

| Criterion | Score |
|---|---:|
| Memorability | 6 |
| Recognition | 6 |
| Originality | 6 |
| Engineering aesthetic | 6 |
| OSS fit | 6 |
| Timelessness | 7 |
| **Total** | **37 / 60** |

**Verdict:** Reject. Too metaphorical; not enough scanner specificity.

## Concept 19 — AgentSec Monogram AS as Graph

**Description:** Construct `A` and `S` from nodes/edges or angular paths.

**Symbolism:** Product initials plus graph/capability paths.

**Uniqueness:** Medium-high if executed well.

**Scalability:** Medium; monograms often blur at small sizes.

**Favicon quality:** Medium.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Good.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Medium.

**Long-term brand value:** Medium-high, but depends heavily on execution.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 6 |
| Originality | 7 |
| Engineering aesthetic | 8 |
| OSS fit | 8 |
| Timelessness | 8 |
| **Total** | **44 / 60** |

**Verdict:** Reject as primary. Initials do not explain the product enough.

## Concept 20 — Zero Network Trust Mark

**Description:** A local square/terminal block with an external network line visibly absent or cut.

**Symbolism:** Offline-first, no data leaving the machine.

**Uniqueness:** Good for product truth.

**Scalability:** Medium.

**Favicon quality:** Medium.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Good.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Good.

**Long-term brand value:** Medium-high but too narrow: AgentSec is more than no-network.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 6 |
| Originality | 8 |
| Engineering aesthetic | 9 |
| OSS fit | 9 |
| Timelessness | 8 |
| **Total** | **47 / 60** |

**Verdict:** Keep as supporting message, not main logo.

## Concept 21 — Risk Surface Topology

**Description:** A topographic contour-like map around an agent, with reachable surfaces shown as contours.

**Symbolism:** Risk surface and capability terrain.

**Uniqueness:** Strong conceptually.

**Scalability:** Weak; contours require detail.

**Favicon quality:** Weak.

**GitHub avatar quality:** Medium.

**Terminal friendliness:** Weak.

**Monochrome compatibility:** Medium.

**SVG simplicity:** Weak.

**Long-term brand value:** Medium as illustration, poor as logo.

| Criterion | Score |
|---|---:|
| Memorability | 7 |
| Recognition | 4 |
| Originality | 8 |
| Engineering aesthetic | 7 |
| OSS fit | 6 |
| Timelessness | 6 |
| **Total** | **38 / 60** |

**Verdict:** Reject for logo. Could inspire website graphics.

## Concept 22 — Deterministic Rule Stack

**Description:** A stack of horizontal rule bars feeding into a single finding marker.

**Symbolism:** Rule-based deterministic scanner.

**Uniqueness:** Medium.

**Scalability:** Good.

**Favicon quality:** Medium-good.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Excellent.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent.

**Long-term brand value:** Medium.

| Criterion | Score |
|---|---:|
| Memorability | 6 |
| Recognition | 6 |
| Originality | 6 |
| Engineering aesthetic | 9 |
| OSS fit | 9 |
| Timelessness | 8 |
| **Total** | **44 / 60** |

**Verdict:** Reject as primary; too close to generic list/report icon.

## Concept 23 — Agent Silhouette Abstracted as Cursor Node

**Description:** A cursor-like triangular/chevron agent marker connected to capability endpoints.

**Symbolism:** Agent as actor; reachable tools as endpoints.

**Uniqueness:** Good if not too cursor/play-button-like.

**Scalability:** Excellent.

**Favicon quality:** Excellent.

**GitHub avatar quality:** Excellent.

**Terminal friendliness:** Good.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Excellent.

**Long-term brand value:** High if merged with capability map.

| Criterion | Score |
|---|---:|
| Memorability | 8 |
| Recognition | 8 |
| Originality | 7 |
| Engineering aesthetic | 9 |
| OSS fit | 9 |
| Timelessness | 9 |
| **Total** | **50 / 60** |

**Verdict:** Keep as finalist, likely within Direction A.

## Concept 24 — Minimal “Can Touch” Hand/Pointer

**Description:** A pointer/hand/cursor touching a node through a boundary.

**Symbolism:** What the agent can touch.

**Uniqueness:** Medium.

**Scalability:** Medium; hands are too illustrative.

**Favicon quality:** Medium.

**GitHub avatar quality:** Medium.

**Terminal friendliness:** Weak.

**Monochrome compatibility:** Good.

**SVG simplicity:** Medium.

**Long-term brand value:** Medium.

| Criterion | Score |
|---|---:|
| Memorability | 6 |
| Recognition | 5 |
| Originality | 6 |
| Engineering aesthetic | 5 |
| OSS fit | 5 |
| Timelessness | 6 |
| **Total** | **33 / 60** |

**Verdict:** Reject. Too literal and too clipart-prone.

## Concept 25 — Agent Manifest Seal

**Description:** A minimal document/config card with embedded capability graph.

**Symbolism:** AgentSec scans manifests and config files.

**Uniqueness:** Medium.

**Scalability:** Medium; document icons are common.

**Favicon quality:** Medium.

**GitHub avatar quality:** Good.

**Terminal friendliness:** Good.

**Monochrome compatibility:** Excellent.

**SVG simplicity:** Good.

**Long-term brand value:** Medium.

| Criterion | Score |
|---|---:|
| Memorability | 6 |
| Recognition | 6 |
| Originality | 6 |
| Engineering aesthetic | 8 |
| OSS fit | 8 |
| Timelessness | 8 |
| **Total** | **42 / 60** |

**Verdict:** Reject as logo; useful as docs illustration.

---

## Shortlist after concept rejection

The best surviving ideas are:

1. **Capability Map Mark** — best overall and most directly tied to the core idea.
2. **Cursor Node + Capability Endpoints** — strong execution variant of the capability map.
3. **Permission Lattice** — highly engineering-native, strong for CLI/static-analysis identity.
4. **Permission Diff** — excellent developer metaphor, but weaker as a standalone mark.
5. **Local Boundary Ring / Touch Radius** — useful supporting geometry, but not enough alone.

Finalist directions should be interpreted as directions, not finished logos.

---

# Phase 5 — Critical review

Assume the concepts are posted on Hacker News, Reddit, r/programming, and r/opensource.

## Likely criticism from Hacker News

### Criticism: “This looks like yet another security startup.”

Valid if the mark uses shields, locks, gradients, cyber-blue, abstract hexagons, or threat imagery.

**Response:** The selected direction must avoid these entirely. A capability map is better because it describes the product’s actual function rather than the category label “security.”

### Criticism: “Why does an open-source CLI need branding?”

Valid if the branding feels overproduced or SaaS-like.

**Response:** The logo should be minimal, functional, and README/PyPI-friendly. It should not feel like a funded enterprise platform pretending to be bigger than it is.

### Criticism: “The icon does not tell me what it does.”

Valid for abstract monograms, rings, scan apertures, and primitive shapes.

**Response:** The capability-map direction has a better chance of communicating “agent reach/capabilities” even before reading copy.

### Criticism: “Looks like Tailscale/networking.”

Valid risk for any node graph.

**Mitigation:** Do not make it a generic mesh. Use a central agent/cursor/config node with only a few capability endpoints, not a network of equal peers. The visual grammar should be “one actor, known reachable surfaces,” not “many devices connected.”

## Likely criticism from Reddit / r/programming

### Criticism: “Security logos are all shields and locks; boring.”

Correct. This supports rejecting all shield/lock directions.

### Criticism: “AI sparkles are cringe.”

Correct. AgentSec should not use sparkles because the tool is deterministic and no-LLM.

### Criticism: “This looks like a JS framework logo.”

Valid if using abstract geometric shapes, gradients, or monograms.

**Mitigation:** Keep the identity grounded in scan/capability semantics.

### Criticism: “Too polished for an OSS CLI; feels like marketing.”

Valid if the execution uses glassmorphism, gradients, or startup-web decoration.

**Mitigation:** Use a plain geometric SVG with strong monochrome behavior. Let the seriousness come from restraint.

## Likely criticism from r/opensource

### Criticism: “Looks proprietary/corporate.”

Valid if overly glossy.

**Mitigation:** Prioritize monochrome, simple SVG, permissive asset usage, and a mark that looks at home in README/docs.

### Criticism: “The logo is too abstract; I cannot draw it from memory.”

Valid for aperture, ring, topology, and monogram ideas.

**Mitigation:** The final mark should be drawable from memory: center node + three reach nodes + boundary/cursor. If it cannot be sketched in 10 seconds, it is too complex.

### Criticism: “This is just a graph icon.”

Valid risk for Capability Map.

**Mitigation:** Add one distinctive structural rule:

- use an asymmetric three-endpoint layout representing `shell`, `fs`, `net`;
- use a clipped local boundary;
- use a cursor/agent wedge as the central actor rather than a generic dot;
- avoid equal mesh-network distribution.

The mark must say “agent reach” rather than “network graph.”

## Critical review of shortlisted concepts

### 1. Capability Map Mark

**Attack:** Could look like any graph/network product. Could overlap with Tailscale. Could become too detailed at favicon size.

**Defense:** It is still the strongest semantic match. The issue is execution, not concept. To avoid Tailscale, do not use a full mesh or many equal nodes. Use a central actor and three capability surfaces.

**Decision:** Keep.

### 2. Cursor Node + Capability Endpoints

**Attack:** Could look like a play button, cursor logo, or Vercel-like triangle if simplified poorly.

**Defense:** The cursor/agent node gives the graph a clear actor. Combined with endpoints, it becomes more specific than a generic triangle.

**Decision:** Keep as preferred execution variant of Capability Map.

### 3. Permission Lattice

**Attack:** Could become a generic grid/app icon. At small sizes, cells blur. It may communicate policy matrix more than AI-agent reach.

**Defense:** It is very engineering-native and deterministic. It would work well in CLI docs and scan output visuals.

**Decision:** Keep as backup direction, not primary recommendation.

### 4. Permission Diff

**Attack:** Plus/minus is generic. It may look like git/diff tooling, not security scanning. It may imply code review rather than pre-run agent inspection.

**Defense:** Extremely developer-native and terminal-friendly.

**Decision:** Reject as primary logo. Use as secondary brand language in docs/report UI.

### 5. Local Boundary Ring / Touch Radius

**Attack:** Too generic alone. Can look like radar, monitoring, or target.

**Defense:** Good supporting element for offline/local trust.

**Decision:** Do not use standalone. Use only as a boundary element inside the Capability Map direction.

---

# Phase 6 — Final recommendation

## Choose ONE direction

Choose:

# Direction A — Capability Map Mark

A minimal geometric mark showing:

- one central **agent/cursor node**;
- three reachable **capability endpoints**;
- a restrained **local boundary / inspection frame**;
- no shield, lock, eye, sparkle, bug, skull, cloud, or matrix code.

The core visual message:

> **AgentSec maps what your AI agent can touch before it runs.**

## Why this should become the permanent AgentSec identity

### 1. It is product-specific

A shield says “security.”  
A lock says “access.”  
A sparkle says “AI.”  
A graph says “relationships.”  

But a central agent connected to reachable capability surfaces says something much closer to AgentSec’s actual function:

> This tool reveals the agent’s capability map.

That is the durable idea.

### 2. It distinguishes AgentSec from generic security startups

Most security brands communicate fear or protection. AgentSec should communicate inspection and understanding.

Capability mapping is not a generic cybersecurity trope. It is specific to agentic systems, MCP servers, tool access, filesystem/network/shell reach, and pre-run review.

### 3. It works for CLI-first open source

The mark can be:

- simple SVG;
- monochrome;
- favicon-safe;
- GitHub-avatar-safe;
- readable in docs;
- compatible with terminal/report metaphors;
- expandable into diagrams for documentation.

It does not require a complex illustration system.

### 4. It can scale into a full visual language

The same motif can support:

- docs diagrams: agent → shell/filesystem/network/secrets;
- scan result cards: risky edge highlighted;
- README header: mark + wordmark;
- favicon: simplified central node + endpoints;
- social preview: capability map expanded around the product promise;
- CLI screenshots: permission/capability table language.

This gives AgentSec a coherent design system, not just a logo.

### 5. It is timeless enough

Developer infrastructure marks age well when they are:

- geometric;
- simple;
- monochrome-first;
- tied to product semantics;
- not trend-dependent.

The capability-map direction satisfies those constraints.

## Recommended execution constraints for the later SVG phase

Do not implement yet, but when implementation begins:

1. Start in black and white only.
2. Use at most 4–6 SVG primitives/paths if possible.
3. Design favicon first, then wordmark lockup second.
4. Test at 16×16, 32×32, 64×64, GitHub avatar size, README header size.
5. Avoid thin strokes that disappear in favicons.
6. Avoid a full mesh graph; show one actor and limited reachable surfaces.
7. Avoid equal node networks that resemble Tailscale.
8. Avoid triangles that resemble Vercel.
9. Avoid a circular radar look.
10. Keep the wordmark simple: likely a technical sans or custom minimal lettering, not futuristic cyber type.

## Suggested symbolic structure

Potential final mark structure:

```text
      ●
      │
  ●── ▶ ──●
      │
     ◜ ◝
```

This is not the logo. It is only a conceptual skeleton:

- `▶` / wedge / cursor-like center = agent/action before execution;
- three nodes = reachable capabilities;
- partial boundary = local inspection/trust boundary;
- sparse geometry = CLI/developer friendliness.

## Final decision

Proceed with **Capability Map Mark** after approval.

Do **not** generate SVG yet.

Next approved phase should be:

1. produce 3–5 monochrome thumbnail sketches of the Capability Map direction;
2. evaluate them at favicon/GitHub/avatar/README sizes;
3. select one;
4. only then generate production SVG and associated assets.

---

## Approval gate

This audit recommends **Capability Map Mark** as the permanent AgentSec identity direction.

Implementation should wait for explicit approval.
