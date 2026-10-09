# Source-Grounded FDE Study Pack

## Goal

Create one tool-neutral study pack that can be moved into either a ChatGPT
Project or NotebookLM. It should make the FDE journey teachable, updateable,
and source-grounded without requiring a complete lesson library up front.

## Scope

### In scope

- A canonical `RESOURCES.md` registry with more than 20 relevant external
  sources.
- Verification metadata for every source: stable URL, publisher, type,
  coverage, access status, and last-verified date.
- Explicit separation between verified sources, candidates, and gaps.
- Mentor rules in `AGENTS.md` for citation, source freshness, uncertainty,
  lesson sequencing, and evidence claims.
- Reusable procedures in `TEACHING-PROTOCOLS.md` for source triage, lesson
  preparation, practice, retrieval, learning records, and export.
- Registry IDs in `fde-journey-map.md` so lessons point to teachable sources.
- Small platform adapters for ChatGPT Projects and NotebookLM where their
  persistence and citation behavior differ.

### Out of scope

- Rewriting every lesson or casebook before source verification.
- Maintaining two independent curricula.
- Reproducing copyrighted book content.
- Treating a source count as proof of curriculum quality.
- Claiming current vendor behavior without a dated official source.

## Source policy

The registry is the single source catalog. A source may be listed as:

1. **Verified** — existence, publisher, relevance, and URL were checked.
2. **Candidate** — potentially useful but not yet checked; it cannot support
   a lesson or factual claim.
3. **Gap** — a required topic has no adequate source yet.

Each verified source records its coverage and source type. Books may be listed
as citations even when access is paywalled; the pack must not reproduce them.
Changing API, product, model, and security claims require current official
documentation or an explicitly dated primary source. Conceptual foundations
may use books, academic tutorials, and papers. Production judgment should use
official postmortems and first-party case studies where possible.

## Teaching contract

The mentor teaches one capability at a time, beginning with the business
problem and the minimum autonomy that can solve it. Every lesson:

- names the journey unit and mission outcome;
- cites the exact registry source and chapter, section, or page when available;
- separates source-backed facts, mentor synthesis, and practice instructions;
- labels time-sensitive or unverified claims;
- introduces no more than two new concepts;
- ends with exactly one practice task;
- advances only after the user demonstrates the capability;
- updates learning state and evidence without inventing experience.

The mentor must not make the user read every source or use AI merely because a
source discusses agents. “Do not use AI” and “do not use an agent” remain valid
outcomes.

## Tool adapters

The same source registry and teaching contract are used in both tools.

- **ChatGPT Project:** upload the durable rules, mission, journey, registry,
  and evidence files; use Project instructions for behavior; treat recalled
  memory as unverified and restate state at session start.
- **NotebookLM:** add the same source files and selected external sources;
  require notebook citations for factual teaching; use generated study aids
  as practice artifacts, not as authoritative sources.

Neither tool may silently fill a source gap from model memory. If the source
pack does not support an answer, the mentor says so and names the source or
verification step needed.

## Data flow

`RESOURCES.md` → source selection → one journey unit → cited lesson → one
practice task → demonstrated capability → learning record/evidence update.

The journey map defines outcomes and ordering. `AGENTS.md` defines behavior.
`TEACHING-PROTOCOLS.md` defines procedures. `RESOURCES.md` defines authority.
`EVIDENCE.md` records only what the user can show.

## Validation

Before implementation is considered complete:

- the registry contains at least 21 relevant external sources;
- every source used by an active lesson is verified and has a registry ID;
- candidates and gaps cannot be cited as established evidence;
- no journey lesson points to a missing source ID;
- platform instructions do not contradict the common teaching contract;
- the files pass a manual placeholder, contradiction, and scope review.
