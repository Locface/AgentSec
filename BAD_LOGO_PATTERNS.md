# Bad Logo Patterns for AgentSec

AgentSec should not look like a generic cybersecurity company. It is an offline-first, CLI-first static scanner for AI agent and MCP configuration risk. The visual identity should communicate **capability awareness**: knowing what an agent can touch before it runs.

This rules out many familiar security-logo tropes.

## 1. Shields

**Why it is tempting:** Shields are the default visual shorthand for protection.

**Why AgentSec should avoid it:**

- A shield implies a protective runtime barrier, antivirus, EDR, firewall, SOC product, or managed security platform.
- AgentSec does not sit in front of execution and block attacks live. It inspects configuration before execution.
- The category is already saturated with shields; another shield would be invisible on GitHub, PyPI, docs sidebars, and security-tool lists.
- A shield communicates “we protect you” more than “you can see the agent’s capabilities.”

**Brand risk:** Users assume AgentSec is a generic defensive security product instead of a developer scanner.

## 2. Locks

**Why it is tempting:** Locks mean security and access control.

**Why AgentSec should avoid it:**

- Locks imply encryption, password management, secrets storage, key management, or access enforcement.
- AgentSec is not a vault and does not lock anything.
- A lock mark narrows the product to “secret protection,” while AgentSec also covers shell execution, filesystem writes, network exfiltration, OAuth scopes, prompt-injection risks, Docker socket access, CI gating, and policy drift.
- Lock icons are among the most overused stock security marks.

**Brand risk:** Users understand “private/locked” instead of “inspectable/capability-aware.”

## 3. Hacker icons

Examples: anonymous masks, skulls, terminal skulls, crossbones, cracked screens, hostile silhouettes.

**Why AgentSec should avoid it:**

- AgentSec is engineering infrastructure, not threat-intel theatre.
- Hacker imagery shifts attention from configuration visibility to attacker fantasy.
- It makes the project feel unserious to the exact audience that matters: developers, DevOps engineers, maintainers, and security-conscious OSS users.
- It ages badly and looks like CTF branding or a toy exploit project.

**Brand risk:** The tool feels adversarial and gimmicky rather than trustworthy and precise.

## 4. Hoodies

**Why it is tempting:** Hoodie silhouettes are common in “cyber” visuals.

**Why AgentSec should avoid it:**

- A hoodie represents the attacker, not the product’s value.
- It says “cybersecurity marketing deck,” not “developer CLI.”
- It is culturally stale and instantly reduces credibility.
- It suggests fear-based selling, while AgentSec should sell clarity.

**Brand risk:** The identity becomes threat-centred instead of user-centred.

## 5. Green matrix

**Why it is tempting:** Green code rain is instantly associated with computers and hacking.

**Why AgentSec should avoid it:**

- It is nostalgic cyberpunk decoration, not product meaning.
- It makes the project look like a generic hacking tool.
- It does not communicate offline-first static analysis or agent capability modelling.
- It competes poorly with modern developer-tool identities, which are simpler, flatter, and more system-like.

**Brand risk:** AgentSec looks like a 2000s security wallpaper rather than a modern OSS scanner.

## 6. Hexagons

**Why it is tempting:** Hexagons feel technical, modular, and scientific.

**Why AgentSec should avoid it:**

- Hexagons are now a default B2B SaaS/security motif.
- They imply generic platform architecture more than a specific product idea.
- Many security, blockchain, Kubernetes, AI, and observability tools use hex grids; the shape does not create ownership.
- A hexagon can work only if the inner concept is extremely distinctive; on its own it is visual filler.

**Brand risk:** The logo disappears into a sea of abstract technical badges.

## 7. Gradients for the sake of gradients

**Why it is tempting:** Gradients can make a simple mark feel premium.

**Why AgentSec should avoid decorative gradients:**

- Trend gradients date quickly.
- Gradients often fail in terminal contexts, monochrome docs, tiny favicons, sticker printing, and GitHub avatars.
- A gradient cannot carry the core idea by itself.
- If the base silhouette is weak, a gradient only hides the weakness.

**Acceptable use:** A restrained secondary palette or website accent, after the mark works perfectly in one color.

**Brand risk:** The identity feels like a startup template, not a durable engineering tool.

## 8. Generic AI sparkles

**Why it is tempting:** Sparkles are now the universal icon for AI features.

**Why AgentSec should avoid it:**

- AgentSec scans AI-agent configurations, but its trust story is explicitly **no LLM calls, no cloud dependency, no data leaving the machine**.
- Sparkles imply magic, generation, assistant UX, and model intelligence — the opposite of deterministic static analysis.
- AI sparkles are already visually exhausted by copilots, chatbots, browser extensions, and productivity SaaS.
- They communicate “AI-powered” when AgentSec should communicate “AI-agent-aware, but deterministic.”

**Brand risk:** Users misunderstand AgentSec as another AI assistant or AI security dashboard.

## 9. Stock security symbols

Examples: shield + checkmark, lock + circuit, eye + shield, bug + crosshair, fingerprint + lock.

**Why AgentSec should avoid them:**

- They are category clichés.
- They are hard to trademark mentally; users remember “some security icon,” not AgentSec.
- They do not express the specific product idea: mapping an agent’s allowed touchpoints before execution.
- They invite comparison with antivirus, SOC, and vulnerability management tools.

**Brand risk:** AgentSec becomes visually interchangeable with tools it is explicitly not.

## 10. Clipart style

**Why it is tempting:** Clipart is fast and approachable.

**Why AgentSec should avoid it:**

- Clipart fails at favicon size and looks weak in a README header.
- It suggests amateur packaging around a serious security tool.
- It rarely survives monochrome rendering.
- It makes later brand expansion harder: docs, CLI screenshots, PyPI, GitHub org/avatar, stickers, and conference slides all need a stronger system.

**Brand risk:** The first impression undercuts trust before a developer reads the README.

## Positive constraints instead

AgentSec’s identity should be built from these constraints:

- **Works in one color first.** Color is secondary.
- **Recognizable at 16×16.** Favicon quality is non-negotiable.
- **Feels like a developer tool.** More GitHub/Docker/Tailscale/Linear than cyber vendor.
- **Communicates visibility and capability mapping.** The mark should imply “what can this agent reach?”
- **Minimal geometry.** Few paths, clear silhouette, no illustration dependency.
- **Terminal-friendly.** It should survive ASCII naming, monochrome docs, CLI output, and small badges.
- **Not fear-based.** No attacker theatre. AgentSec is about control, inspection, and confidence.
