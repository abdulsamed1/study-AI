# S38 follow-up list — what to read when the epub lands in `books/`

**S38** = *Software Architecture: The Hard Parts: Modern Trade-Off Analyses for Distributed Architectures*,
Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani, 1st ed. (2021). No epub is in `books/` yet
(2026-10-19), so every S38 citation below is still `[TOC]`.

Procedure when it lands (per the approved rule 7): extract the chapter, read the section that supports the
claim, retag `(read: <sections>)` in the unit, and record book, edition, chapter/page, date, and tool in
`RESOURCES.md`.

## Units that still depend on S38, and the claim each needs from it

| Unit | S38 chapters cited | Claim in the unit that needs S38 | What the read must supply (paraphrase) | Priority |
|---|---|---|---|---|
| **P7.1** (boundaries, responsibilities, dependency direction) | ch. 2–5 | "Separate transport, application use cases, domain rules, and persistence where useful" + an automated check that fails on a deliberate dependency-direction violation | Coupling and cohesion categories that justify which boundaries to draw, and how coupling/change-pattern arguments are made concretely (the unit currently leans on S20 ch. 2–3/8 and S26 ch. 2–3) | Medium — the proof is already supportable without it |
| **P7.5a** (architecture characteristics, styles, decomposition) | ch. 2–5 and 7 | Skill 4: "assess responsibilities, dependency direction … data ownership, change patterns, operational coupling, and deployment boundaries before splitting components or services" | The trade-off analysis method the chapter group is cited for: how to weigh coupling against deployment boundaries, and where service granularity is justified | High — this is the unit's decomposition core |
| **P7.5b** (diagrams and ADRs) | ch. 1 and 15 | "record the context, requirements … plausible alternatives, constraints, rationale, consequences, risks, and conditions for revisiting a decision"; the three-option ADR exercise | A worked trade-off-analysis + ADR method (how alternatives are compared and documented), to sit alongside S20 ch. 21 | Medium-high — S20 ch. 21 already covers ADRs |
| **P7.6** (evolutionary architecture, build-vs-buy) | ch. 15 | "identify which decisions are expensive to reverse … schedule their re-evaluation"; the build-vs-buy comparison whose costs state their assumptions | A concrete method for costing a "build vs buy vs adopt" decision over time (licence, operation, exit, lock-in) — the part S26 ch. 16 (read) does not cover | High — the unit's build-vs-buy half has no book support yet |
| **P8.6** (dual writes, outbox, saga, compensation) | ch. 11–12 | "distinguish atomic database updates from cross-system workflows"; the transactional-outbox crash test and compensation | Whatever the book offers on distributed transactions / saga-style compensation; note the outbox mechanism itself is sourced from an unopened lead, not from S38 | Low-medium — S19 ch. 8 (read) covers the divergence claim |
| **P10.4b** (design II: interfaces, data, components, decision) | ch. 6, 9–10, 15 | Stage 4–6: interface and data-ownership boundaries, component responsibilities, and the one new architecture decision with alternatives and consequences | A decision/trade-off framing for distributed-component choices (the "hard parts" lens: data ownership, consistency, and coupling costs of a split) | High — this unit is the S38-dependent design unit |

## Chapters to read, in order of value

1. **ch. 15** (trade-off analysis / ADRs) — unlocks P7.6's build-vs-buy and sharpens P7.5b and P10.4b.
2. **ch. 6** — needed by P10.4b (and informs P7.1).
3. **ch. 9–10** — needed by P10.4b.
4. **ch. 2–5, 7** — needed by P7.5a's decomposition skill; partially redundant with S20 ch. 2–3 (read).

## Constraints on the pass

- Do not tag `(read)` for a chapter that was only skimmed; use `(read: <sections>)`.
- Do not paste book text; the map keeps paraphrases and short phrases only.
- If a chapter does not actually support the claim the unit attaches to it, **remove that citation** rather
  than keeping a decorative reference, and record the decision in the commit message.
- S38 is the last book cited without a local epub: S18 (MIT 6.5840) is a web course whose lecture notes
  were not opened, and S25 (Google SRE) has no local copy either.
