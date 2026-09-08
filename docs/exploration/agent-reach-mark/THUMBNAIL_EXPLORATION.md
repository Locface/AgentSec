# Agent Reach Mark — Thumbnail Exploration

Execution sketches only, per `FINAL_BRAND_DECISION.md`. 26 rough thumbnails, one variable tested per file. No color, no polish, no new concept — every file is an attempt at the approved Agent Reach Mark: one asymmetric actor, 2–3 differently-shaped reach terminals, one open boundary stroke.

## All thumbnails

1. **thumbnail-01.svg** — proportion (large actor, small tight terminal cluster). Compliant: asymmetric dart actor, 3 distinct terminal shapes (square/ring/triangle), open arc boundary, 5 primitives.
2. **thumbnail-02.svg** — proportion (small actor, oversized terminals). Compliant: dart actor, square/ring/diamond terminals, open bracket, 5 primitives.
3. **thumbnail-03.svg** — balance (terminals evenly spaced ~120° despite asymmetric actor). Compliant: dart actor, square/ring/triangle, open half-arc, 5 primitives.
4. **thumbnail-04.svg** — balance (all weight pushed to one corner, actor isolated opposite). Compliant: dart actor, square/ring/triangle, corner-notch boundary, 5 primitives.
5. **thumbnail-05.svg** — silhouette (bold near-touching shapes, thick boundary stroke). Compliant: dart actor, square/ring/triangle, open 3-sided frame, 5 primitives.
6. **thumbnail-06.svg** — silhouette (elements spread far apart to stress-test cohesion). Technically compliant (asymmetric actor, 3 distinct terminals, open diagonal-cut boundary, 5 primitives) but rejected — see below.
7. **thumbnail-07.svg** — negative space (open arc cups the terminals like a mouth). Compliant: dart actor, square/ring/triangle, open arc, 5 primitives.
8. **thumbnail-08.svg** — negative space (one terminal straddles the boundary's open edge, one sits fully outside it). Compliant: dart actor, ring/square/triangle, open 3-sided frame, 5 primitives.
9. **thumbnail-09.svg** — terminal placement (terminals fan out directly ahead of the actor's tip — directional reach). Compliant: dart actor, square/ring/triangle, open arc, 5 primitives.
10. **thumbnail-10.svg** — terminal placement (terminals scattered at extreme angles: up, far right, far down). Compliant: dart actor, square/ring/triangle, open 3-sided frame, 5 primitives.
11. **thumbnail-11.svg** — boundary shape (plain large open arc, only 2 terminals). Compliant: dart actor, square/ring, open arc, 4 primitives.
12. **thumbnail-12.svg** — boundary shape (open square-bracket "[" ). Compliant: dart actor, square/ring/triangle, open bracket, 5 primitives.
13. **thumbnail-13.svg** — boundary shape (minimal corner-notch, boundary barely present). Compliant: dart actor, ring/triangle/square, corner-notch, 5 primitives.
14. **thumbnail-14.svg** — boundary shape (single diagonal slash stands in for the whole boundary). Compliant: dart actor, square/ring, diagonal-cut, 4 primitives.
15. **thumbnail-15.svg** — proportion (terminals graduated small/medium/large to test hierarchy). Compliant: dart actor, square/ring/triangle, open arc, 5 primitives.
16. **thumbnail-16.svg** — balance (diagonal cascade: actor top-left, terminals stepping toward bottom-right). Compliant: dart actor, square/ring/triangle, corner-notch, 5 primitives.
17. **thumbnail-17.svg** — silhouette (chunky bold strokes/fills, bracket-derived actor, industrial weight). Compliant: non-circular bracket-derived actor, square/ring/diamond, open 3-sided frame, 5 primitives.
18. **thumbnail-18.svg** — negative space (boundary arc dominates the frame, actor+terminals shrink to a tiny cluster inside it). Compliant: dart actor, square/ring, open arc, 4 primitives.
19. **thumbnail-19.svg** — terminal placement (two terminals clustered close, one pushed far away as an outlier). Compliant: dart actor, square/ring/triangle, open bracket, 5 primitives.
20. **thumbnail-20.svg** — terminal placement (terminals in a straight linear row instead of radial spread). Compliant: dart actor, square/ring/triangle, corner-notch, 5 primitives.
21. **thumbnail-21.svg** — boundary shape (boundary reduced to a tight ~90° quarter-arc tucked in one corner). Compliant: dart actor, ring/triangle, quarter-arc, 4 primitives.
22. **thumbnail-22.svg** — proportion (actor and terminals sized near-equally, testing peer-weight risk). Technically compliant (asymmetric actor, 3 distinct terminal shapes, open arc, 5 primitives) but rejected — see below.
23. **thumbnail-23.svg** — terminal placement (radial 3-terminal fan using the full distinct-shape set). Compliant: asymmetric dart actor, square/ring/triangle terminals, open arc boundary (~153° gap), 5 primitives.
24. **thumbnail-24.svg** — silhouette (jagged 6-vertex actor stress-test). Compliant: asymmetric polygon actor, square/ring/triangle terminals, open arc boundary (~146° gap), 5 primitives — but rejected, see below.
25. **thumbnail-25.svg** — boundary shape (wide near-complete arc, testing how large a gap still reads as clearly "open" rather than "closed ring"). Compliant: dart actor, square/ring/triangle terminals, open arc boundary (~122° gap), 5 primitives.
26. **thumbnail-26.svg** — balance (bilateral vertical symmetry using the minimum of 2 terminals). Compliant: dart actor, square/ring, open 3-sided frame, 4 primitives.

## Rejected

- **thumbnail-06** — the actor, terminals, and boundary notch are spread so far apart that the mark reads as several unrelated scattered marks rather than one silhouette; at 16×16 it dissolves into disconnected specks.
- **thumbnail-22** — actor and terminals are sized nearly identically, so despite using three distinct shapes it reads closer to a cluster of equal peers than "one actor, its reachable surfaces" — this is the exact reading the direction document warns is a fatal five-year failure mode (symmetric peer-graph).
- **thumbnail-24** — the actor's six concave vertices create a jagged, lightning-bolt-like silhouette; a useful stress-test of how much actor complexity survives shrinking, but at 16×16 the notches fill in and it reads as a blob rather than a distinct asymmetric shape. Confirms less detail is better; not advanced.
- **thumbnail-11** — while compliant, the boundary arc is large enough and the terminals few enough (2) that at small size it can be misread as a plain incomplete circle rather than a deliberate boundary; weaker than the bracket/corner-notch variants for communicating "inspection edge" rather than "broken circle." Not advanced to finalists.
- **thumbnail-18** — boundary arc so dominant that the actor/terminal cluster (the actual product idea) shrinks to near-illegibility; interesting as a negative-space study but fails the 16×16 recognizability bar on its own.

Everything else produced is compliant and usable as supporting exploration but was not strong enough on silhouette/memorability to advance past the five finalists below.

## Finalists

### thumbnail-01.svg — proportion study (dominant actor, small cluster)

- **Strengths:** The oversized dart actor anchors the whole mark; even if the terminal cluster blurs, the silhouette still reads as "one large asymmetric shape reaching toward something small," which matches the product idea (one actor, limited reach) better than a balanced composition would.
- **Weaknesses:** The three terminals are packed tightly enough that their individual shapes (square/ring/triangle) may merge into one blob at the smallest sizes.
- **Favicon quality (16×16):** Good — the actor silhouette alone survives; the terminal cluster reads as "something small and detailed is there" even if the exact shapes don't resolve.
- **GitHub avatar quality:** Strong — the large actor gives the mark a confident, non-timid presence in a square avatar crop.
- **Memorability:** High — an oversized, unmistakably non-circular wedge is easy to sketch from memory.
- **Uniqueness:** Good — the size imbalance (actor much bigger than what it reaches) is a distinct compositional choice not seen in typical connected-node marks, which usually equalize node size.

### thumbnail-05.svg — silhouette study (bold, near-touching, thick boundary)

- **Strengths:** Thick strokes and near-touching shapes are built specifically to survive downscaling; this is the most favicon-robust thumbnail in the set by construction.
- **Weaknesses:** The tight touching arrangement slightly obscures the "reach" idea — actor and terminals nearly forming one mass reads more like a single blob than "one actor plus its surfaces" at first glance.
- **Favicon quality (16×16):** Excellent — thick fills and thick strokes are exactly what favicon rendering needs; nothing here is thin enough to vanish.
- **GitHub avatar quality:** Excellent — the boldness reads with confidence in a small square crop.
- **Memorability:** Good — the bold silhouette is easy to recall, though slightly less "storytelling" than a more spread composition.
- **Uniqueness:** Moderate — the boldness helps it avoid the thin-hairline SaaS-node look, which is one of the direction document's specific five-year failure modes.

### thumbnail-09.svg — terminal placement study (forward directional reach)

- **Strengths:** All three terminals fan out directly ahead of the actor's tip, which visually narrates "this actor reaches these surfaces" more literally than a radial or scattered layout — the strongest storytelling of the set.
- **Weaknesses:** Because the terminals sit in a line ahead of the tip, the composition is left-heavy/right-heavy rather than filling the frame, which could look off-center in a square avatar crop without adjustment.
- **Favicon quality (16×16):** Good — the directional cluster is compact enough to hold together at small size.
- **GitHub avatar quality:** Good, with a caveat — off-center weighting needs a recentered viewBox or padding adjustment before production.
- **Memorability:** High — "wedge pointing at three different small shapes" is an easy mental sketch.
- **Uniqueness:** Good — directional (asymmetric) terminal placement is a clear structural difference from the equal-distribution node graphs this direction is defined against.

### thumbnail-12.svg — boundary shape study (open square bracket)

- **Strengths:** The open bracket is unambiguous — it cannot be misread as a ring, a badge, or a frame, since it only occupies one edge of the composition. Clean, calm, easy to reproduce at any size.
- **Weaknesses:** Of the five finalists this one is the most "quiet" — it relies entirely on the actor/terminal arrangement for personality since the boundary itself is minimal.
- **Favicon quality (16×16):** Good — a bracket built from a few straight strokes holds up well at tiny sizes, better than a curved arc does.
- **GitHub avatar quality:** Good — reads as a clean, restrained mark, consistent with the "calm control" personality target in `BRAND_AUDIT.md`.
- **Memorability:** Moderate-high — simple enough to redraw from memory, though less distinctive than the bolder options.
- **Uniqueness:** Good — a bracket boundary is a clearer, more code-native reference ("[", config/array syntax) than an arc, and is visually farther from the generic "radar circle" risk than any arc-based boundary in this set.

### thumbnail-17.svg — silhouette study (bracket-derived actor, industrial weight)

- **Strengths:** The only finalist using a bracket-derived actor instead of a dart, giving the direction visual range beyond one silhouette family; the thick strokes throughout make it the second-most favicon-robust option after thumbnail-05.
- **Weaknesses:** The actor's L/bracket shape is less immediately "actor-like" than a wedge/dart — it may read more like a structural bracket than a pointed, agentive shape on first glance.
- **Favicon quality (16×16):** Excellent — chunky geometry across every element means nothing thins out at small size.
- **GitHub avatar quality:** Strong — the industrial weight gives it a serious, engineering-tool feel consistent with the "not fear-based, not SaaS-polished" positioning.
- **Memorability:** Good — bold and blocky, easy to recall, though the actor reads slightly more abstract than the dart-based finalists.
- **Uniqueness:** High — combining a bracket-derived actor with a 3-sided open frame is the most structurally distinct entry in the set, furthest from any circle-and-line network-graph reading.

