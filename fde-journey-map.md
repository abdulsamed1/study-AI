# FDE Journey Map — Deep Engineering Roadmap

**Purpose:** Build durable engineering capability for taking a real business problem from discovery to a reliable, evaluated, secure, deployed AI-enabled system. This is a long-form learning journey.

**Mission alignment:** FDE = problem discovery → choose the right solution (including non-AI) → build → evaluate → secure → deploy → integrate into work → measure impact → hand over. The target is demonstrable engineering judgment, not completion of a syllabus.

---

## 1. Rules for this journey

1. **Follow dependencies, not enthusiasm.** Each lesson lists its prerequisite lesson IDs. A lesson is ready only when its prerequisite's exit evidence exists.
2. **Teach one lesson unit at a time.** A unit normally takes 45–90 minutes of teaching and guided practice; larger implementation units may span several sessions. Estimated times are planning aids, not promises.
3. **Teach → model → practice → review → retrieve later.** Do not quiz on a concept before teaching it. Re-test important ideas in a changed scenario after a delay.
4. **No progress by attendance.** Mark a lesson complete only when its proof artifact or practical performance meets the exit criteria.
5. **Respect established experience.** The user already has C++, OOP, and DSA experience. Do not teach beginner programming, object-oriented programming, or generic algorithm lessons. Use diagnostics to identify only the language, runtime, API, data, or AI-engineering gaps needed for the capstone.
6. **One evolving capstone.** Build a small, deterministic business workflow first; add persistence and integrations; introduce AI only when the use case justifies it; then evaluate, secure, deploy, pilot, and document it. Keep scope narrow.
7. **Source discipline.** `RESOURCES.md` remains the canonical project source register. Existing `S#` tags refer to it. The `F#` references below are official starting points checked on 2026-10-09; re-open the relevant page and record the exact section/version before teaching. Current API/model/security behavior must be verified at lesson time. A chapter tagged `[TOC]` was identified from a book's table of contents only and has not been read by the mentor; keep the tag until the exact passage is checked in ChatGPT Project or NotebookLM.
8. **Separate evidence from synthesis.** Each lecture labels source-backed facts, mentor synthesis, and practice. If reliable source coverage is missing, say so instead of filling the gap silently.
9. **No invented professional evidence.** A lab proves a lab skill; it does not prove production experience or business impact. Label simulated data and pilots honestly.
10. **This is a dependency graph represented as a mostly linear path.** Some concepts can be revisited later. Do not force advanced internals when the mission does not need them.
11. **Stay on the FDE/AI-engineer track.** Out of scope: training or building foundation models, ML research, and math beyond the applied evaluation protocol in P14.3 (see `MISSION.md`). Teach models and providers as engineering constraints — guarantees, cost, latency, failure modes — never as model internals.
12. **Human-in-the-loop engineering.** The learner directs coding agents and stays accountable for the result; an agent's output is an input to review, never proof by itself. Before delegating, write the problem, requirements, constraints, acceptance criteria, and architecture decisions. After the agent changes the code, review the diff, its dependencies and side effects, and the tests it wrote; design at least one verification independently of the agent's own tests; observe the real behavior across API, application logic, database, and user-facing workflow; diagnose failures from logs, traces, measurements, and failure injection; then record accept, reject, or redirect with evidence (the agent review record in section 3). Passing tests are necessary, not sufficient (S40, S41). Projects in other languages (for example Rust, React, Next.js) are code-review contexts, not additional language tracks.

## 2. Roadmap at a glance

```text
Business problem and engineering baseline
                 |
                 v
Developer workbench -> AI-engineering implementation bridge -> chosen runtime
                 |
                 v
      HTTP / APIs / integration contracts
                 |
                 v
       Relational data -> transactions -> concurrency
                 |
                 v
   testing / architecture / distributed systems
                 |
                 v
       production operations and reliability
                 |
                 v
       FDE discovery and solution selection
                 |
                 v
       LLM API -> context / retrieval / memory
                 |
                 v
    workflows / tools / agents / MCP
                 |
                 v
 evaluation / observability / security / governance
                 |
                 v
 deployment / rollout / adoption / measurable impact
                 |
                 v
         capstone + defensible evidence pack
```

This order deliberately puts HTTP, data correctness, testing, and failure handling before complex agent architectures. AI is a later capability layer built on software engineering foundations, not a substitute for them. The roadmap does not require learning every language or framework: practise backend and API-integration work in TypeScript/Node.js (Phases 2–10), and use Python for the AI-engineering labs from Phase 11. Code in other languages that the learner already uses (for example Rust, React, Next.js) is a code-review context, not an additional language track.

## 3. Lesson design and completion criteria

Every lesson follows this record shape:

- **ID and objective:** one capability that can be demonstrated.
- **Priority:** must-have, important, or useful — a planning weight, not permission to skip prerequisites (see Priority below).
- **Depends on (hard prerequisite):** required lesson IDs that must appear **earlier in this file's order**, not just earlier topics. `scripts/journey_inventory.py` runs the forward-dependency and cycle checks on these edges only.
- **Coupled with:** a non-blocking relationship built in one phase and verified (or completed) in a later one. May point forward; it must reference an existing unit ID but the cycle and file-order checks ignore it. Used so that an earlier unit does not silently re-teach a later phase's content.
- **Source:** specific project source IDs and/or official documentation to open.
- **Lesson:** scenario → concept → mechanism → failure modes → production implications.
- **Practice:** one tangible task, preferably on the evolving capstone or a deliberately small lab.
- **Exit evidence:** one primary proof artifact (checkable sub-items inside it are allowed).
- **Retrieval:** defined once in the Retrieval table below — a named later unit whose scenario re-tests this one. No per-unit Retrieval field.
- **Unit type:** lessons (about 45–90 minutes) vs **implementation unit (multi-session)** — oversized units carry this label explicitly instead of being silently long.

### Depth scale

| Depth | What it means | Example evidence |
|---|---|---|
| 0 — Recognize | Identify a concept when described | Correct classification with explanation |
| 1 — Explain | Describe why it exists and its limits | Clear explanation plus one failure mode |
| 2 — Use | Apply it in a guided, bounded task | Working implementation with basic tests |
| 3 — Engineer | Implement, debug, test, and handle failure cases | Tests, error paths, reproducible diagnosis |
| 4 — Design | Compare alternatives, consistency, security, operations, and cost | ADR plus failure analysis |
| 5 — Deep internals | Explain implementation details and edge cases | Only where required by project scope |

**Default standard:** Depth 2–3 for routine implementation lessons; Depth 3–4 for data correctness, integrations, evaluation, security, and production decisions. Depth 5 is selective, not a universal requirement.

### Priority

Each unit carries one of three priorities, keeping the priority vocabulary of the pre-rewrite journey map so the readiness check in `AGENTS.md` §4 has the metadata it names:

- **must-have** — the unit sits on the capstone's critical path: it is a dependency hub (seven or more units depend on it), it closes a gap listed in `EVIDENCE.md`, it produces the G0 problem brief/baseline, the provider contract sheet, the regression gate, or the threat model, or it is a Phase 17 capstone unit (selection, build, evidence pack, or defense).
- **important** — expected on the standard path: later units build on it or it grounds a phase gate.
- **useful** — valuable depth: compress or defer when diagnostics, the capstone, or a supporting branch show the capability is already present or not yet needed.

The old **awareness** tier has no units: every unit here carries a proof artifact, so deferral happens through the supporting branches or the project's needs, not by tagging a unit away.

### Agent review record

Used wherever a proof names an *agent review record* (rule 12). It is a short Markdown note kept with the change, with five fields:

1. **Delegation brief:** the problem, requirements, constraints, acceptance criteria, and the architecture decisions the agent must respect, written before delegating.
2. **Diff review:** the files changed, the dependencies and side effects found, and the most important changes explained in the learner's own words.
3. **Independent verification:** at least one test, query, or runtime check designed from the requirements rather than copied from the agent's own tests, plus the assumptions that remain untested.
4. **Observed evidence:** logs, traces, measurements, or failure-injection results that were actually seen.
5. **Decision:** accept, reject, or redirect, with the evidence that justifies it.

A passing generated test suite is an input to this record, never the verdict. The record is practice evidence only; it is not production experience (rule 9) and does not enter `EVIDENCE.md` as an achievement until the artifact exists.

---

# Phase 0 — Mission, baseline, and problem framing

**Goal:** Know what success means before choosing technologies. **Gate G0:** a written problem brief and an honest skills baseline.

- **P0.1 — FDE delivery loop** — **Priority:** important. Depends on: none. Learn the lifecycle from ambiguous request to handover; distinguish a demo, a working system, and a deployed outcome. **Proof:** draw the delivery loop and list evidence required at each stage. Sources: `AGENTS.md` §§1, 6, S1 (Claude Frontier Academy announcement, 2026-10-02 — primary role standard: medical-model residency, simulated deployment, graded practical, badges early 2027); S2 is a single listing, treat as stale unless re-opened.
- **P0.2 — Technical baseline and workbench check** — **Priority:** must-have. Depends on: P0.1. Inventory what can be explained, built, tested, debugged, and operated today. **Proof:** evidence-based skills ledger; no self-ratings without examples. Source: `EVIDENCE.md`.
- **P0.3 — Problem brief and baseline metric** — **Priority:** must-have. Depends on: P0.1–P0.2. Identify users, present workflow, pain, baseline, constraints, risk, and success metric. **Proof:** one-page problem brief with assumptions marked. Sources: S1–S2.

# Phase 1 — Engineering workbench and feedback loop

**Goal:** Work reproducibly in a repository and diagnose behavior instead of guessing. **Gate G1:** a small project that can be run, tested, debugged, and reviewed from a clean checkout.

- **P1.1 — Terminal, paths, processes, environment variables** — **Priority:** important. Depends on: P0.2. Navigate files; run commands; inspect exit codes, processes, and environment. **Proof:** documented run commands and diagnosis of a deliberately broken setup. Source: F1, F3.
- **P1.2 — Git fundamentals and history** — **Priority:** must-have. Depends on: P1.1. Working tree, staging, commits, branches, diffs, merge conflicts, ignore rules, remote repository. **Proof:** clean commit history and a resolved practice conflict. Source: F1.
- **P1.3 — Read an unfamiliar codebase** — **Priority:** must-have. Depends on: P1.1–P1.2. Trace entry points, configuration, module boundaries, data flow, and tests before changing code. **Proof:** a short architecture note with links to the actual files, marking each claim as verified in code or inferred; for an agent-generated codebase, state which parts could and could not be explained. Source: S40.
- **P1.4 — Debugging from evidence** — **Priority:** important. Depends on: P1.1–P1.3. Reproduce, reduce, inspect, hypothesize, test, and confirm a cause. **Proof:** a small bug report with reproduction steps, observations, cause, fix, and regression test; when an agent proposes the fix, confirm the cause by reproduction before accepting the patch. Source: F3 (runtime diagnostics).
- **P1.5 — Testing and feedback loop** — **Priority:** important. Depends on: P1.2–P1.4. Learn assertions, test setup/teardown, deterministic tests, failure output, and basic test boundaries. **Proof:** tests that fail before the fix and pass after it, including at least one test written from the stated requirement before reading the implementation. Sources: F3, F8, S41.

# Phase 2 — AI-engineering implementation bridge

**Goal:** Bridge existing C++/OOP/DSA experience into the languages, runtimes, and data contracts used by production services and AI products. This is diagnostic and just-in-time, not beginner programming. Backend and API-integration practice uses TypeScript/Node.js from here through Phase 10; Python is introduced at P11.2 for the AI-engineering labs. The external-service boundaries opened here — request/response contracts, adapters, test seams — are the same boundaries the capstone hardens in P4.7–P4.8 and P8.

- **P2.1 — Choose the implementation language for the capstone** — **Priority:** important. Depends on: P1.3, P1.5. Backend and API-integration practice uses TypeScript/Node.js; Python is introduced at P11.2 for AI-engineering labs only. **Proof:** an ADR (context, options, decision, consequences, what would make this choice wrong) recording the stack split, and one minimal HTTP call to a stub provider in TypeScript. Sources: F2, F3, F13, F14.
- **P2.2 — Data contracts and runtime validation at trust boundaries** — **Priority:** must-have. Depends on: P2.1, P1.5. JSON, schemas, serialization, missing/null/unknown fields, and the decision of where validation is enforced: at each point where data enters (HTTP requests, configuration, stored records, external-service and model-provider responses), not deep inside domain logic. The failure this addresses: a field the type system assumes exists is absent at runtime, or an external payload reaches domain logic unvalidated — including payloads a static type system accepts. Model-provider responses are one worked example, not the scope; later units reuse this discipline — model-output validation (P11.3), webhook payloads (P8.4), drift checks (P4.8a) — so do not re-teach it. **Proof:** reject malformed external payloads with actionable errors before domain logic, demonstrated with a table of valid/invalid fixtures, one of them a provider-style response and one a payload a static typechecker accepts; state which entry point each fixture covers. Sources: F2, F5, S4, S21.
- **P2.3 — Async I/O contract: concurrency, cancellation, and timeouts** — **Priority:** must-have. Depends on: P2.1–P2.2. Use existing programming knowledge over provider calls, retrieval, tools, queues, and bounded parallelism. This unit defines the async contract — which operations may run forever, which must be cancellable, how many may run at once. Node-runtime evidence (event-loop delay, resource leaks, bounded shutdown) is proven by P3.6, not here; do not re-teach it. **Proof:** a written cancellation/timeout contract for one async call plus a bounded-parallelism implementation that honors it deterministically. Sources: F3, F13.
- **P2.4 — External-service adapters and SDK ergonomics in TypeScript (AI SDKs as the worked example; Python equivalents at P11.2)** — **Priority:** important. Depends on: P2.1–P2.3. Read an SDK's types and versioning policy, inspect request/response objects, pin dependencies, and isolate third-party clients behind your own typed adapter so provider churn, retries, and SDK type gaps cannot leak into domain code. The failure this addresses: SDK types treated as runtime guarantees, or an SDK upgrade silently changing behavior under you. **Proof:** a small adapter with typed inputs, safe configuration, a pinned dependency, and tests against recorded or stub responses — the P4.7 stub provider extends these fixtures. Sources: F3, F5, S4, S21.
- **P2.5 — Test seams for external services (provider mocks without self-deception)** — **Priority:** important. Depends on: P2.2–P2.4. Mock external-service boundaries to test contract and error paths deterministically, without pretending mocks prove real-provider or model quality; decide what the mock must reproduce (status codes, malformed payloads, latency), what it must not claim (behavior nobody has verified against the real provider), and preserve recorded fixtures for later real evaluation. The failure this addresses: a green suite that only proves the mock and the implementation share the same wrong assumption. **Proof:** unit tests for contract/error paths plus a clearly separated live smoke test; list the assumptions the mock encodes and which later check (live test, P4.8 drift test, P14.1 evaluation) would falsify each. Sources: F8, S15; S22 is deprecated (OpenAI Evals read-only 2026-10-31, shutdown 2026-11-30 — use the Datasets/evaluation-getting-started flow, verified at teach time).

# Phase 3 — Chosen implementation runtime

**Goal:** Build production service code in TypeScript/Node.js. Python enters at
P11.2 for AI-engineering labs; do not study both as separate curricula.

- **P3.1 — Types and compiler/runtime feedback** — **Priority:** important. Depends on: P2.1–P2.5. Use the chosen language's type system, static checks, and diagnostics where available. **Proof:** turn the Phase 2 payload normalizer into typed, checked code. Sources: F3, F5.
- **P3.2 — Valid and invalid data states** — **Priority:** important. Depends on: P3.1, P2.4, P2.2. Model optional data and event variants explicitly. **Proof:** process multiple event types without unsafe assumptions. Sources: F3, F5.
- **P3.3 — merged into P2.2.** Tombstone: runtime validation at trust boundaries is taught once, in P2.2 (which now covers the runtime-vs-static distinction its fixture table demonstrates). Dependents re-pointed to P2.2.
- **P3.4 — Process, packages, and scripts** — **Priority:** must-have. Depends on: P1.1–P1.2, P2.5, P3.1. Process lifecycle, dependency lockfiles, package scripts, and reproducible startup. Configuration files, config validation, and secret boundaries are P3.7's unit; do not re-teach them here. **Proof:** bootstrap a reproducible service in TypeScript/Node.js using P3.7's configuration and secret conventions. Source: F3.
- **P3.5 — Non-blocking I/O and blocking work** — **Priority:** must-have. Depends on: P2.3, P3.4. Understand why one slow/blocking operation can affect concurrency. **Proof:** identify and remove a blocking operation in a small lab, and show event-loop delay or equivalent runtime evidence before and after. Sources: F3 (record the exact diagnostics page used), S28 ch. 4 [TOC].
- **P3.6 — Async failure, cancellation, timeouts, and resource cleanup** — **Priority:** must-have. Depends on: P2.3, P3.4–P3.5. Avoid orphaned tasks, leaked resources, and work that outlives its request. **Proof:** implement timeout-aware I/O and cleanup paths; find one seeded resource leak from runtime evidence; on shutdown, in-flight work and resources are cleaned up within a bound defined in the test. Sources: F3, S19 ch. 9 [TOC], S28 ch. 4 [TOC].
- **P3.7 — Logging, configuration, and secret hygiene** — **Priority:** important. Depends on: P3.4, P3.6. The single treatment of configuration, secrets, and diagnostics hygiene in Phases 1–10: structured logs, config validation, secret injection and storage, and redaction in logs. **Proof:** logs support diagnosis without exposing credentials. Sources: F3, F11.

P3.1–P3.2 and P3.4–P3.7 (P3.3 is merged into P2.2; see its tombstone) are not
repeated in Python. At P11.2, carry over only the Python equivalents the AI
labs need: typing, async, validation, packaging, and logging.

# Phase 4 — Internet, HTTP, and API contracts

**Goal:** Understand the contract across a network boundary before designing integrations.

- **P4.1 — Network request mental model** — **Priority:** important. Depends on: P2.2, P3.4. Client/server, DNS at a conceptual level, connection, TLS purpose, and network failure boundaries. **Proof:** trace a request from client to server and name where failures may occur. Source: F4.
- **P4.2 — HTTP request and response anatomy** — **Priority:** important. Depends on: P4.1. Methods, paths, headers, body, status codes, content types, and caching semantics. **Proof:** inspect several real requests/responses and explain their contracts. Source: F4.
- **P4.3 — Resource design and REST-style APIs** — **Priority:** important. Depends on: P4.2, P3.2, P2.2. Resource identity, methods, representation, validation, pagination, and versioning. **Proof:** design an API contract for the capstone before implementation, including an error model (status mapping, stable machine-readable codes, no internal detail leaked, and no 403/404 distinction that lets a caller enumerate resources). Sources: F4, S39 (§2.5, REC-API-23); RFC 9457 (to verify, see `RESOURCES.md`).
- **P4.4 — Authentication and authorization basics** — **Priority:** must-have. Depends on: P4.2–P4.3, P3.7. API keys, bearer tokens, OAuth concepts, scopes, ownership checks, and secret hygiene. **Proof:** test allowed and denied requests, including one cross-user object-access test written from the requirement rather than from the generated handler; state the difference between authentication and authorization. Sources: F4, F11, S39 (§2.2–2.3, REC-API-11–12).
- **P4.5 — HTTP failure semantics, retries, and rate limits** — **Priority:** must-have. Depends on: P2.3, P4.2. Timeouts, 4xx/5xx categories, 429, `Retry-After`, and why not every error should be retried. **Proof:** write a client policy table for retryable and permanent outcomes. Sources: F4, S25.
- **P4.6 — API data contracts and schema evolution** — **Priority:** must-have. Depends on: P2.2, P4.3. Validation, unknown fields, additive/breaking changes, compatibility, and idempotent client behavior. **Proof:** test old and new payload versions. Sources: F4, F11.
- **P4.7 — Build and test a small HTTP service/client** — **Priority:** must-have. Depends on: P3.1–P3.7, P4.1–P4.6. Implement one endpoint, one client, validation, errors, config, and tests. **Proof:** reproducible service and contract tests, built from a written delegation brief with an agent review record (§3) for each agent-written part, plus a stub provider with switchable fault modes (latency, 5xx, 429 with `Retry-After`, timeout-after-commit, duplicate and out-of-order delivery, invalid signature or replay, expired or revoked token, schema drift, outage) that later units reuse. Sources: F3, F4, F8, S37, S40.
- **P4.8 — Third-party API onboarding: provider contract sheet and credential lifecycle** — **Priority:** must-have. Depends on: P4.4–P4.7. Document what the provider guarantees instead of assuming it: authentication, scopes and permissions, quotas and rate limits, pagination, idempotency support, webhook delivery, ordering, and replay behavior, schema and versioning policy, and sandbox-versus-production differences. Cover token acquisition, expiry, refresh, revocation, and secret rotation where the provider's documented contract calls for them. **Proof:** a contract sheet for one real or sandbox API with every claim tagged documented (canonical URL and section), observed (fixture or test), or unknown; contract tests and a drift test that fails on a changed fixture; a credential-lifecycle test, including concurrent requests at token expiry where the provider issues expiring tokens; a short failure matrix with detection and recovery; and any agent-written client checked against the sheet, with each mismatch recorded as a finding. Sources: F4, F11, S19 ch. 5 [TOC], S27 ch. 5 [TOC], S37, S39 (§2.3, REC-API-11, REC-API-15–16); RFC 9700 (to verify, see `RESOURCES.md`).

# Phase 5 — Relational data and SQL

**Goal:** Model persisted facts correctly before relying on AI or distributed behavior.

- **P5.1 — Relational modeling and data invariants** — **Priority:** important. Depends on: P2.3, P4.3. Entities, relationships, keys, cardinality, nullability, and invariants. **Proof:** schema sketch for users, requests, events, and processing state. Source: F6.
- **P5.2 — SQL reads/writes, joins, aggregation** — **Priority:** must-have. Depends on: P5.1. CRUD, filtering, joins, grouping, ordering, and transaction boundaries at a basic level. **Proof:** answer business questions with SQL, not application loops. Source: F6.
- **P5.3 — Constraints and integrity** — **Priority:** must-have. Depends on: P5.1–P5.2. Primary/foreign keys, uniqueness, check constraints, and why application checks alone can race. **Proof:** encode key invariants in the database. Source: F6.
- **P5.4 — Indexes and query plans** — **Priority:** important. Depends on: P5.2–P5.3. Query patterns, B-tree mental model, selectivity, `EXPLAIN`, and index costs. **Proof:** measure one query before/after a justified index. Source: F6.
- **P5.5 — Schema migrations and safe change** — **Priority:** must-have. Depends on: P5.1–P5.4, P1.2. Versioned schema changes, backfill, deploy order, rollback limits, and compatibility. **Proof:** perform an additive migration and document its rollout sequence, then complete one expand → backfill → contract change while the old and new application versions both pass tests against the intermediate schema; review any agent-generated migration for destructive or locking steps before running it. Source: F6.
- **P5.6 — Database access from the application** — **Priority:** must-have. Depends on: P3.4, P4.7, P5.1–P5.5. Parameterized queries or a query builder, connection pooling concepts, mapping and validation. **Proof:** persist and retrieve capstone records with tests. Sources: F3, F6.
- **P5.7 — Backup, restore, and data lifecycle basics** — **Priority:** important. Depends on: P5.5–P5.6. What backups protect, what they do not, retention/deletion, and restore verification. **Proof:** document and test a local recovery procedure. Sources: S25, F10.

# Phase 6 — Transactions, concurrency, and correctness

**Goal:** Prevent data corruption when operations overlap or fail halfway.

- **P6.1 — Atomicity and transaction boundaries** — **Priority:** must-have. Depends on: P5.2–P5.6. Group state changes that must succeed or fail together. **Proof:** transactionally persist one business operation and test rollback. Source: F6, S19.
- **P6.2 — Isolation and anomalies** — **Priority:** important. Depends on: P6.1. Dirty/non-repeatable/phantom read concepts as applicable, lost updates, and check-then-act races. **Proof:** reproduce a race using two concurrent clients. Source: F6, S19.
- **P6.3 — Locking, optimistic concurrency, and uniqueness** — **Priority:** important. Depends on: P5.3, P6.1–P6.2. Unique constraints, version checks, row locks, and their trade-offs. **Proof:** fix the race from P6.2 and prove it with a concurrency test. Source: F6, S19.
- **P6.4 — Consistency invariants across multiple writes** — **Priority:** important. Depends on: P6.1–P6.3. Identify which records must remain consistent and what happens when only one write succeeds. **Proof:** failure matrix for a multi-step state change. Sources: S19, S26.
- **P6.5 — Time, ordering, and duplicate events** — **Priority:** must-have. Depends on: P2.2, P4.5–P4.6, P6.1–P6.4. Event time vs processing time, duplicate delivery, out-of-order updates, and event identity. **Proof:** define a state transition table for repeated and stale events, including a stale read after a successful write (replication or provider-index lag). Sources: S19 ch. 6 [TOC], S27 ch. 8 [TOC].
- **P6.6 — Design and defend one correctness invariant** — **Priority:** important. Depends on: P6.1–P6.5. Translate a business guarantee into DB constraints, transaction behavior, tests, and known limits. **Proof:** ADR + tests + written failure analysis; the invariant tests are designed by the learner before reading any generated implementation. Sources: F6, S19.

# Phase 7 — Software design and test strategy

**Goal:** Make changes safe to reason about and cheap to verify. Agent-written code and tests are review inputs: write the acceptance criteria first, then verify independently (rule 12).

- **P7.1 — Boundaries, responsibilities, and dependency direction** — **Priority:** important. Depends on: P2.5, P3.1, P3.2, P3.4–P3.7, P4.7a. Separate transport, application use cases, domain rules, and persistence where useful. **Proof:** draw a module diagram, justify each boundary, and add an automated check (script or lint rule) that fails on a deliberate dependency-direction violation. Sources: S20 ch. 2–3 and 8 [TOC], S26 ch. 2–3, S38 ch. 2–5 [TOC].
- **P7.2 — Unit, integration, contract, and end-to-end tests** — **Priority:** must-have. Depends on: P1.5, P4.7, P5.6. Choose the test level that proves a claim; avoid testing implementation details unnecessarily. **Proof:** test one important invariant at multiple appropriate layers, with at least one test designed from the requirement before reading the implementation and shown to fail when a defect is deliberately seeded. Sources: F8, S20, S40, S41.
- **P7.3 — Test doubles and dependency boundaries** — **Priority:** must-have. Depends on: P7.1–P7.2. Know when a fake, stub, or real dependency improves confidence and when it hides a defect. **Proof:** replace one brittle test without losing meaningful integration coverage; review one agent-generated test for assertions that only restate the implementation or mock the dependency under test, and record what it would fail to catch. Sources: F8, S41.
- **P7.4 — Refactoring under tests and code review** — **Priority:** must-have. Depends on: P7.1–P7.3, P1.2–P1.4. Change structure without silently changing behavior. **Proof:** a reviewed refactor with a green regression suite and explanatory diff, plus an agent review record (§3) for one actual diff produced by an AI coding tool such as OpenCode: the diff is small enough to review; the files, dependencies, and side effects it touches are listed and the key changes explained unaided; at least one finding is confirmed by a failing test or runtime evidence and at least one suspected finding is rejected or revised after checking evidence; verification does not rely on the agent's own tests; a regression suite exists; and the accept, reject, or redirect decision is recorded. The learner can explain and modify the result unaided (`AGENTS.md` §11). Sources: S34, S37, S40, S41; S26 ch. 7–9 [TOC].
- **P7.5a — Architecture characteristics, quality scenarios, styles, and decomposition** — **Priority:** important. Depends on: P7.1–P7.4. Learn to move from a real problem to an architecture that fits its constraints, rather than defaulting to a familiar style. The unit covers four connected skills:

  1. **Architecture characteristics:** identify which quality attributes matter for the actual problem (for example, availability, latency, modifiability, security, deployability, cost), which are hard constraints, and which compete with one another. Source-backed: S20 ch. 4–5 define, identify, and scope architecture characteristics; S19 ch. 2 defines nonfunctional requirements with measurable targets.
  2. **Measurable quality scenarios:** turn each important quality attribute into an observable scenario with a stimulus, expected response, threshold, and measurement method. Avoid vague criteria such as "high performance" or "reliable." Source-backed: S19 ch. 2 (latency percentiles, availability targets, throughput, growth); S42 (C4 model — review checklist helps verify diagram quality, not quality attributes themselves).
  3. **Architecture styles and boundaries:** understand the relevant trade-offs among a simple monolith, modular monolith, layered architecture, event-driven architecture, service-based architecture, and separately deployed services. The question is always which style satisfies the identified characteristics at the lowest justified complexity. Source-backed: S20 ch. 9 [TOC] and 11 (architecture foundations, modular monolith); S20 ch. 19 (choosing appropriate style); S26 ch. 2–3 (modeling and splitting the monolith); S33 (workload segmentation — vendor guidance: compare with the books before adopting).
  4. **Coupling and decomposition:** assess responsibilities, dependency direction (building on P7.1), data ownership, change patterns, operational coupling, and deployment boundaries before splitting components or services. Source-backed: S38 ch. 2–5 and 7 [TOC] (coupling, modularity, decomposition, service granularity); S26 ch. 2–3.

  **Proof:** a quality-attribute table for a realistic scenario, with at least three attributes that have measurable targets and named measurement methods; and a written comparison of at least two plausible architecture styles (including the simplest adequate option) against the identified attributes, with explicit trade-offs. Sources: S20 ch. 4–6, 11, and 19 (read) and ch. 7, 9 [TOC]; S26 ch. 2–3; S38 ch. 2–5 and 7 [TOC]; S19 ch. 1–2; S33; S41.

- **P7.5b — Fitness functions, risk analysis, architecture diagrams, and ADRs** — **Priority:** important. Depends on: P7.5a. Validate and record an architecture decision so it can be checked, communicated, and revisited. The unit covers four connected skills:

  1. **Fitness functions and governance:** show how a valuable architectural constraint can be checked automatically or monitored consistently — for example, a dependency-direction check (extending P7.1's proof), a response-time budget in CI, or a module-coupling metric. The point is not to automate everything but to make the most important constraints observable. Source-backed: S20 ch. 6 (measuring and governing architecture characteristics, fitness functions).
  2. **Architecture risk analysis:** identify risky assumptions, expensive-to-reverse decisions, unknown failure modes, and the cheapest practical way to validate them before committing. Source-backed: S20 ch. 22 (analyzing architecture risk).
  3. **Architecture diagrams:** select the appropriate level of detail and communicate system context, components, dependencies, and important runtime interactions without creating misleading diagrams. Use the C4 model's abstraction hierarchy (system context → container → component) as a practical default; other notations are acceptable when they serve the same purpose. Source-backed: S20 ch. 23 (diagramming architecture); S42 (C4 model: abstractions, diagrams, notation, review checklist).
  4. **Decision records:** record the context, requirements identified in P7.5a, plausible alternatives, constraints, rationale, consequences, risks, and conditions for revisiting a decision. The ADR must be written before any AI coding agent implements the chosen design. Source-backed: S20 ch. 21 (architectural decisions); S38 ch. 1 and 15 [TOC] (trade-off analysis and ADRs).

  The architecture decision exercise must compare at least three plausible options, including the simplest adequate option and a meaningful comparison between an in-process modular boundary and a separately deployed alternative. Quality attributes must have measurable targets from P7.5a. Constraints, consequences, unresolved risks, and conditions that would trigger reconsideration are recorded.

  **Proof:** an ADR written before any agent implements the chosen option, comparing at least three options (including simplest adequate and modular-monolith vs. separately deployed); appropriately scoped architecture diagrams (at minimum a context diagram and a component/container diagram); at least one architecture fitness check that can be validated (automated or with a named manual verification method); and a risk assessment listing the top assumptions, their potential impact, and the cheapest way to test each. Compare any vendor guidance used (S33) with the books before adopting it. Sources: S20 ch. 6, 19, 21–23; S38 ch. 1 and 15 [TOC]; S42; S33; S41.

# Phase 8 — Integration and distributed-systems foundations

**Goal:** Reason about boundaries where networks, retries, queues, and independent state make success ambiguous. Practise each unit against the P4.7 stub provider, and design each unit's tests from the P8.1 failure timeline and the P4.8 contract sheet before reading any agent-written implementation.

- **P8.1 — Partial failure and ambiguous outcomes** — **Priority:** important. Depends on: P4.5, P6.1–P6.5. A timeout does not tell the caller whether the remote side effect occurred. **Proof:** failure timeline for a request that times out after the remote write. Sources: S19, S27 ch. 6–7 [TOC].
- **P8.2 — Idempotency and deduplication** — **Priority:** must-have. Depends on: P6.5, P8.1. Stable operation keys, duplicate semantics, retention, and the role of database uniqueness. **Proof:** repeat a request, sequentially and concurrently, and show it cannot create a second business effect. Sources: S19 ch. 8 and 13 [TOC], S27 ch. 5 [TOC]; Stripe idempotency lead (unopened, see `RESOURCES.md`).
- **P8.3 — Retry budgets, backoff, jitter, and timeouts** — **Priority:** must-have. Depends on: P4.5, P8.1–P8.2. Transient/permanent classification, deadlines, retry storms, and synchronized retries. **Proof:** bounded retry policy with a testable budget that honors a provider-supplied retry delay. Sources: S25, F10, S19 ch. 9 [TOC], S27 ch. 27 [TOC].
- **P8.4 — Webhook receiver and sender contracts** — **Priority:** must-have. Depends on: P4.2–P4.6, P4.8, P6.5, P8.1–P8.3. Verify signatures, validate events, acknowledge deliberately, persist receipt, enqueue durable work, and process idempotently. **Proof:** locally tested webhook flow with invalid signature, replay attempt, duplicate, out-of-order, transient failure, and crash-window tests, with the signature checked against the raw request bytes where the provider requires it (confirm in current provider documentation). Sources: provider webhook documentation (Stripe and GitHub leads in `RESOURCES.md`, unopened); F11 for general API risks; S26 ch. 4 [TOC].
- **P8.5 — Queues, workers, and at-least-once delivery** — **Priority:** must-have. Depends on: P3.5–P3.6, P5.6, P8.2–P8.3. Consumer retry, delayed work, dead-letter strategy, per-key ordering, and idempotent consumers. **Proof:** worker that can restart without duplicating business effects. Sources: S19, S26.
- **P8.6 — Dual writes, outbox, saga, compensation** — **Priority:** must-have. Depends on: P6.4, P8.1–P8.5. Understand why independent writes can diverge and distinguish atomic database updates from cross-system workflows. **Proof:** implement a transactional outbox in TypeScript/Node.js and PostgreSQL, crash the worker between database commit and publish, restart it, and show each event is published at least once and consumers deduplicate it (P8.2). Sources: S19 ch. 8 and 13 [TOC], S26, S27 ch. 6–13 [TOC range], S38 ch. 11–12 [TOC]; transactional-outbox lead (unopened).
- **P8.7 — Synchronization and reconciliation loops** — **Priority:** must-have. Depends on: P4.8, P6.5, P8.2–P8.6. Full/delta sync, watermarks, cursors, drift detection, source of truth, replay, and repair. **Proof:** reconciliation report that classifies missing, duplicate, stale, and conflicting records, plus a replay test that repairs them without creating duplicates. Sources: S19 ch. 12–13 [TOC], S26, S27 ch. 10–11 [TOC].

# Phase 9 — Production engineering, reliability, and performance

**Goal:** Diagnose production behavior from evidence and run changes safely. Agent-authored pipeline, migration, and configuration changes get the same review and rehearsal as application code.

- **P9.1 — Runtime configuration, containers, and environments** — **Priority:** important. Depends on: P3.4, P3.7, P5.6, P7.2. Build a reproducible container and separate local/test/production configuration. **Proof:** clean startup following written instructions. Sources: F7, S26.
- **P9.2 — CI/CD and safe release workflow** — **Priority:** must-have. Depends on: P1.2, P5.5, P7.2, P9.1. Automated checks, build artifacts, deployment steps, migrations, and rollback limits. **Proof:** CI runs tests and builds the service, plus a rollback rehearsal: deploy version N+1 with a migration, roll back to N, and state what could not be rolled back; review any agent-written pipeline or workflow change for secrets, permissions, and mutable references (the CI trust-boundary lesson in S34). Sources: F7, S25, S27 ch. 29–30 [TOC], S34, S36.
- **P9.3 — Logs, metrics, traces, and correlation** — **Priority:** must-have. Depends on: P4.7, P8.4–P8.5, P9.1. Understand what each signal answers and correlate one request across components. **Proof:** trace a request using a correlation ID and explain its timeline, then locate one seeded fault from the logs, the trace, and one runtime measurement before reading the code. Sources: F9, S25, S39 (§3.2.1, REC-API-18).
- **P9.4 — SLIs, SLOs, error budgets, and alerts** — **Priority:** must-have. Depends on: P9.3, P0.3. Define user-visible reliability and alert on actionable symptoms rather than every noisy signal. **Proof:** compute one SLI from recorded stub-provider fault runs, propose an SLO with rationale (justify any threshold in an ADR rather than inventing one), and show the alert condition fires on an injected failure and stays quiet on noise. Sources: S25, F10, S27 ch. 31 [TOC], S19 ch. 2.
- **P9.5 — Incident response and postmortems** — **Priority:** important. Depends on: P9.3–P9.4, P8.3. Stabilize, gather evidence, communicate, restore service, and learn without prematurely declaring root cause. **Proof:** incident timeline, mitigation, causal mechanism, and prevention items, plus a stakeholder update that separates impact, known facts, unknowns, and the next update time. Sources: S9, S10, S25, S35 (case), S36 (stated plan, not a measured outcome).
- **P9.6 — Performance diagnosis and capacity reasoning** — **Priority:** important. Depends on: P5.4, P8.3, P9.3–P9.5. Latency percentiles, throughput, saturation, queueing, resource pools, database bottlenecks, and workload shape. **Proof:** diagnose a controlled load test before selecting a fix. Source: `production-performance-incident-study-map.md`, S19, S25.
- **P9.7 — Graceful degradation, backups, and recovery** — **Priority:** must-have. Depends on: P5.7, P8.3–P8.7, P9.2–P9.6. Set dependency budgets, degrade safely, restore data, and verify recovery. **Proof:** an executed fault matrix against the stub provider (provider outage, duplicate-delivery storm, expired or revoked credential, worker crash, bad configuration file) and a runbook a second person can follow without undocumented oral context, with time-to-restore and deviations recorded. Sources: S25, F10, S27 ch. 24–28 [TOC], S29 ch. 16 [TOC], S35, S36.

# Phase 10 — FDE discovery, solution selection, and system design

**Goal:** Choose the right solution before building it. This phase reuses the engineering knowledge already acquired.

- **P10.1 — Workflow observation and stakeholder questions** — **Priority:** important. Depends on: P0.3, P7.1. Map inputs, decisions, handoffs, exceptions, and existing tools. **Proof:** current-state workflow with unanswered questions labelled. Sources: `AGENTS.md` §6; external discovery-practice sources remain NO-EVIDENCE — see `RESOURCES.md` coverage gaps.
- **P10.2 — Deterministic code vs workflow vs agent** — **Priority:** important. Depends on: P10.1, P7.5b, P8.1. Choose the least complex design that meets the need; identify where autonomy is useful and where it is dangerous. **Proof:** written option comparison including a non-AI option. Sources: S3 (note its banner: tooling landscape changed since Dec 2024 — patterns stand, tooling examples need re-check), S12.
- **P10.3 — Baseline, outcome metric, and adoption constraints** — **Priority:** important. Depends on: P0.3, P9.4, P10.1. Separate technical proxy metrics from business outcomes; note how the baseline will be gathered. **Proof:** measurement plan with owner and collection method. Sources: `AGENTS.md` §6; external measurement-planning sources remain NO-EVIDENCE — see `RESOURCES.md` coverage gaps.
- **P10.4 — System design and risk boundary** — **Priority:** important. Depends on: P6.6, P7.5b, P8.7, P9.7, P10.2–P10.3. Turn a real FDE problem and its constraints into a coherent proposed system with explicit assumptions and a way to validate the design. The workflow below is a reusable method, not a one-time exercise; it applies to systems with and without AI.

  **Stage 1 — Frame the problem.** Start with the real workflow, stakeholders, users, decisions, inputs, outputs, existing systems, constraints, and desired business outcome. Identify unresolved requirements instead of silently filling them in. Reuses P10.1 discovery and P10.3 baseline.

  **Stage 2 — Define the requirements and workload.** Distinguish functional requirements from nonfunctional requirements. Identify relevant quality attributes (from P7.5a) and define measurable acceptance targets. Record workload assumptions such as request rate, concurrency, bursts, read/write mix, data volume, retention, growth, and dependency behavior where relevant. Source-backed: S19 ch. 2 (defining nonfunctional requirements with measurable targets); S20 ch. 4–5 (architecture characteristics).

  **Stage 3 — Estimate capacity and identify constraints.** Use transparent back-of-the-envelope estimates when useful — for example, throughput, concurrent work, storage growth, request size, resource demand, or downstream capacity. State assumptions, uncertainty, units, and the measurements that would validate the estimates. Do not manufacture precise estimates when the inputs are unknown. Reuse the existing performance study map (`production-performance-incident-study-map.md`) and P9.6 for deeper bottleneck diagnosis and load testing; do not duplicate those lessons here. Source-backed: S28 ch. 1–2 [TOC] (scalability, capacity, service/data-tier decisions); S19 ch. 1 (data-system trade-offs).

  **Stage 4 — Design interfaces and data.** Define relevant API contracts, important data models, invariants, ownership boundaries, read/write paths, and integration contracts. Address consistency, transactional requirements, schema evolution, and idempotency wherever the scenario requires them. Reuses P4.3–P4.6, P5.1–P5.6, P6.1–P6.6, P8.2. Source-backed: S19 ch. 3 and 5 [TOC] (data models, encoding and evolution); S38 ch. 6, 9–10 [TOC] (operational data, data ownership, distributed data access).

  **Stage 5 — Design the component and runtime architecture.** Specify component responsibilities, dependency direction, data flows, trust boundaries, state ownership, communication patterns, and relevant deployment/runtime boundaries. Make synchronous versus asynchronous execution an explicit decision. Explain why each major component exists and what responsibility it owns. Source-backed: S20 ch. 8–9 [TOC] and 11 (component-based thinking, architecture foundations, modular monolith); S26 ch. 4–5 [TOC] (communication styles); S29 ch. 2 [TOC] (distributed-system concepts); S42 (C4 model diagrams for communicating the architecture).

  **Stage 6 — Compare alternatives and justify complexity.** Compare plausible designs, including a simpler non-AI or deterministic option when appropriate to the FDE problem, a modular-monolith option, and separately deployed components where warranted. Introduce queues, caches, replication, sharding, distributed workflows, or additional services only where requirements and evidence justify their complexity. Do not prescribe technologies by default. Explain what each major design choice solves, its costs and risks, and which conditions would make another option preferable. Source-backed: S20 ch. 19 (choosing appropriate style); S38 ch. 15 [TOC] (build your own trade-off analysis); S33 (workload segmentation — vendor guidance, compare with the books).

  **Stage 7 — Analyze reliability, failure, and security.** Cover relevant partial failures, timeouts, retries, duplicate operations, overload, recovery, data integrity, access control, trust boundaries, secrets, and degraded operation. Identify who owns each important failure and how that failure becomes observable. Reuse P8 and P9 rather than restating their full technical content. Source-backed: S27 ch. 24–28 [TOC] (failure causes, downstream/upstream resiliency); S29 ch. 16 [TOC] (common failure patterns); S24 (NIST AI RMF).

  **Stage 8 — Plan operations, observability, deployment, and cost.** Identify the telemetry needed to evaluate the system, the operational responsibilities, deployment and rollback strategy, resource/cost constraints, and relevant security controls. Connect technical targets to the business outcome and to an owner who can verify the result. Reuses P9.1–P9.7. Source-backed: S25 (SRE book); S29 ch. 14 [TOC] (monitoring and observability patterns).

  **Stage 9 — Define validation before implementation.** Produce a verification plan: tests, representative workload experiments, fault scenarios, security checks, measurable success thresholds, rollout criteria, and recovery conditions. State the most important unresolved assumptions and the cheapest experiment or prototype that could invalidate the design before full implementation. Reuses P7.5b (risk analysis and fitness functions) and P14 (evaluation).

  **Proof:** a concise system-design brief containing: (1) problem statement, constraints, and measurable functional/nonfunctional requirements; (2) workload assumptions and a transparent capacity-estimation worksheet where relevant; (3) context and component diagrams, plus the important data/request flows; (4) interface and data-ownership boundaries; (5) an ADR comparing at least three alternatives (including simplest adequate and modular-monolith vs. separately deployed) and explaining the chosen design; (6) a failure/security risk matrix appropriate to the scenario; (7) a validation plan with measurable targets, tests or experiments, and rollout/recovery criteria. The practice scenario and artifacts must be realistic for an FDE building a system around APIs, data, enterprise systems, and potentially models or tools; the method must also be usable for an ordinary backend system without AI. Sources: S20 ch. 11, 19, and 21–23 (read) and ch. 8–9 [TOC]; S19 ch. 1–2; S38 ch. 15 [TOC]; S24; S25; S26 ch. 2–3 and ch. 4–5 [TOC]; S27 ch. 24–28 [TOC]; S28 ch. 1–2 [TOC]; S29 ch. 2 and 14 and 16 [TOC]; S33; S42.

# Phase 11 — LLM fundamentals and model API engineering

**Goal:** Treat a model as a probabilistic component behind an explicit software contract.

- **P11.1 — What a language model does and does not guarantee** — **Priority:** important. Depends on: P10.2, P4.6. Generation, nondeterminism, context limits, stale knowledge, and confident errors at an engineering level; no unnecessary ML math. **Proof:** list use-case-specific failure modes and what cannot be guaranteed. Sources: S3, S11.
- **P11.2 — Request anatomy, tokens, context window, and response metadata** — **Priority:** must-have. Depends on: P11.1, P2.2, P2.4 (adapter contract only; re-implemented in Python here). Messages, instructions, output limits, finish reasons, and provider-specific request/response contracts. **Proof:** build a minimal model call in Python (the first Python use in this journey; carry over only the Python equivalents the AI labs need) and log safe request metadata. Sources: S4, S21.
- **P11.3 — Structured outputs and runtime validation** — **Priority:** important. Depends on: P2.2, P11.2. JSON/schema-constrained output where supported, parse/validation failure, and bounded repair. **Proof:** invalid model output cannot reach the domain layer unvalidated. Builds on P2.2; do not re-teach validation. Sources: S4, S21.
- **P11.4 — Model errors, rate limits, latency, cost, and budgets** — **Priority:** important. Depends on: P8.3, P9.3, P11.2. Provider failures, concurrency caps, request budgets, token accounting, and timeout behavior. **Proof:** cost/latency/error budget and tested fallback behavior. Sources: S4, S21.
- **P11.5 — Prompt/context versioning and model changes** — **Priority:** important. Depends on: P11.2–P11.4. Treat prompts, schemas, retrieval settings, and model identifiers as versioned inputs to behavior: every artifact that can silently change model behavior is stored, versioned, and recorded with what a change invalidates. The failure this addresses: an unversioned prompt or model swap ships with no way to say what behavior changed. **Proof:** versioned configuration for all four artifact types plus a change record stating what each change invalidates (evaluation cases, fixtures, regression expectations); the evaluation rerun after such a change is exercised in P14.4, where the evaluation set exists — do not re-teach it here. Sources: S4, S15; S22 is deprecated (see P2.5 note).
- **P11.6 — Decide where an LLM belongs in the architecture** — **Priority:** important. Depends on: P10.2–P10.4, P11.1–P11.5. Keep deterministic invariants outside the model when possible; define fallback and human-review boundaries. **Proof:** updated ADR with failure containment and reasons not to use an LLM in selected steps, including whether the model call runs in-process through a TypeScript SDK or in a separate Python service behind a stable contract, and why. Sources: S3, S12.

# Phase 12 — Context engineering, retrieval, RAG, and memory

**Goal:** Provide the model with relevant, permissioned information and measure whether retrieval actually helps.

- **P12.1 — Context engineering and information budgets** — **Priority:** important. Depends on: P11.1–P11.2. Select useful context, keep it current, and avoid flooding the model with irrelevant material. **Proof:** compare two context assembly strategies using fixed examples. Sources: S5, F12.
- **P12.2 — Data ingestion and document lifecycle** — **Priority:** important. Depends on: P5.1–P5.6, P12.1. Coupled with: P15.4. Sources, parsing, metadata, versioning, deletion, and permission inheritance. Permission inheritance, retention, and deletion are designed at ingestion time, not retrofitted: build the hooks now so the later system-wide review in P15.4 verifies them instead of adding them. **Proof:** ingestion pipeline with provenance, a recorded re-index/delete test, and a note listing which permission and retention decisions P15.4 must review. Sources: S5, F12 (context selection); the ingestion/access-control lifecycle itself is NO-EVIDENCE — see `RESOURCES.md` coverage gaps.
- **P12.3 — Chunking, embeddings, lexical search, and vector search** — **Priority:** important. Depends on: P12.2, P11.2. Understand the pipeline and what each retrieval method contributes without prematurely choosing a vector database. Engineering scope only (rule 11): treat chunking/embedding settings as API parameters and measure their effect; no model training or embedding math. **Proof:** inspect results for a small controlled corpus. Sources: F12, S5.
- **P12.4 — Retrieval pipeline: filters, hybrid search, reranking** — **Priority:** important. Depends on: P12.3, P4.6, P9.3. Improve recall/relevance while preserving tenant and access filters. **Proof:** retrieval results with measured top-k quality on a labelled set. Sources: F12, S5.
- **P12.5 — RAG grounding, citations, abstention, and failure taxonomy** — **Priority:** important. Depends on: P12.1–P12.4, P11.3. Distinguish retrieval failure, missing source coverage, synthesis error, and unsupported answer. **Proof:** label a test set by failure type and make the system abstain appropriately. Sources: Barnett et al., *Seven Failure Points When Engineering a RAG System* (arXiv:2401.05856, 2024-01-11; CAIN 2024): FP1 missing content, FP2 missed top-rank, FP3 consolidation exclusion, FP4 extraction failure under noise/contradiction, FP5 wrong format, FP6 specificity, FP7 incompleteness. Residual gap: chunking/embedding/reranking tuning depth (their §6 future work) — label it as such.
- **P12.6 — Evaluate retrieval separately from generation** — **Priority:** important. Depends on: P12.4–P12.5, P14.1–P14.2. Measure whether the right evidence was retrieved before judging the final answer. **Proof:** report retrieval and answer-quality results separately. Sources: S15 (method); S22 deprecated (see P2.5 note); the P14.3 statistics caveat applies.
- **P12.7 — Conversation state, durable memory, compaction, and freshness** — **Priority:** useful. Depends on: P6.5, P12.1–P12.6. Separate session state, durable business facts, retrieved knowledge, and generated summaries. **Proof:** define state ownership, retention, expiry, and update rules. Sources: S5, S8, S13.

# Phase 13 — Workflows, tools, agents, and MCP

**Goal:** Increase autonomy only when the workflow needs it and controls are adequate.

- **P13.1 — Workflow patterns before agents** — **Priority:** important. Depends on: P7.1, P10.2, P11.6. Chaining, routing, parallelization, orchestrator/worker, and evaluator/optimizer patterns. **Proof:** map a task to a workflow pattern and explain why. Sources: S3, S12.
- **P13.2 — Tool contracts and safe tool design** — **Priority:** important. Depends on: P4.6, P6.6, P11.3. Explicit arguments, schema, permissions, side effects, clear errors, and idempotency. **Proof:** implement a read-only tool with adversarial input tests. Sources: S7, S21.
- **P13.3 — Agent loop, stop conditions, and budgets** — **Priority:** important. Depends on: P13.1–P13.2, P8.2–P8.5, P11.4. Define state, action, observation, exit criteria, maximum steps, and failure recovery. **Proof:** a bounded agent cannot run forever or repeat a harmful side effect. Sources: S3, S13, S21.
- **P13.4 — State, checkpoints, and long-running workflows** — **Priority:** important. Depends on: P6.1–P6.5, P8.5–P8.7, P13.3. Resume work safely after interruptions and preserve an auditable progress record. **Proof:** kill and resume a job without losing correctness. Sources: S13, S19.
- **P13.5 — MCP and external tool integration** — **Priority:** important. Depends on: P4.4, P13.2–P13.4, P15.2. Understand the protocol boundary, server trust, authorization, and the difference between interoperability and safety. **Proof:** connect one low-risk tool and document its trust/permission boundary. Sources: S6 (pin the spec date in the lesson record — current 2026-07-28; authorization is OAuth 2.1 with RFC9728 discovery and RFC8707 audience binding; tool descriptions are untrusted; explicit user consent before invocation), S14 (verify before citing). Interoperability is not safety.
- **P13.6 — Multi-agent systems and delegation economics** — **Priority:** useful. Depends on: P13.1–P13.5, P14.1. Learn when parallel agents help and when coordination, latency, cost, and failure risk outweigh benefits. **Proof:** compare a single-agent/workflow baseline to a justified multi-agent design; default is not to use multiple agents. Source: S8.

# Phase 14 — Evaluation, testing, and observability for AI systems

**Goal:** Treat quality as a measured property, not a few impressive demo outputs.

- **P14.1 — Turn requirements and failures into evaluation cases** — **Priority:** must-have. Depends on: P0.3, P7.2, P11.6. Build representative, edge, and adversarial cases from real workflows and documented failure modes. **Proof:** versioned evaluation set with expected outcomes and provenance. Sources: S15 (2026-01-09 refresh: start with 20–50 tasks from real failures, isolate trials, read transcripts, eval-driven development); S22 deprecated (see P2.5 note).
- **P14.2 — Graders: code-based, model-based, and human review** — **Priority:** important. Depends on: P14.1, P11.3. Choose a grader that matches the property; analyze false positives/negatives and judge reliability. **Proof:** compare grader decisions against a human-reviewed sample. Sources: S15; S22 deprecated (see P2.5 note). Grader pattern: single-call 0.0–1.0 LLM judge against a rubric (factual accuracy, citation accuracy, completeness, source quality, tool efficiency) per S8.
- **P14.3 — Quality dimensions and statistical uncertainty** — **Priority:** important. Depends on: P14.1–P14.2, P9.4. Sample size, run-to-run variation, confidence, slices, and meaningful before/after comparison. **Proof:** evaluation report that states limits and avoids overclaiming. **Method (interim, mentor synthesis — not a statistics text; rule 11 caps math here):** fixed prompts and seeds, at least three repeats on small sets, report n plus observed range, split results by failure slice, compare before/after on identical sets only, and pre-register a block threshold calibrated from baseline repeat noise. Sources: none yet — NO-EVIDENCE (interim mentor synthesis); `RESOURCES.md` still records a primary statistics tutorial as missing.
- **P14.4 — Regression gates and change management** — **Priority:** must-have. Depends on: P11.5, P12.6, P14.1–P14.3. Re-run evaluations when prompts, models, retrieval, tools, or policies change (the versioned configuration from P11.5 defines what counts as a change), and block a release that regresses the evaluation set. The failure this addresses: a quiet prompt or model swap reaching users because nothing re-ran. **Proof:** CI or documented release gate that blocks a known regression, plus one executed rerun after a versioned prompt or model change with the before/after results recorded. Sources: S15.
- **P14.5 — Trace a complete AI request** — **Priority:** important. Depends on: P9.3, P11.2–P11.4, P12.4, P13.3. Trace model calls, retrieval, tools, retries, token/cost information, and final outcomes while redacting sensitive data. **Proof:** diagnose a failed run from a trace. Sources: S9, F9, S21.
- **P14.6 — Failure analysis and operational learning loop** — **Priority:** important. Depends on: P9.5, P14.1–P14.5. Classify failures, add a regression case, make one change, and measure it. **Proof:** one complete loop from observed failure to verified improvement. Sources: S9, S15.

# Phase 15 — Security, privacy, and AI governance

**Goal:** Bound what the system, model, and tools can access or change, even when the model is wrong or manipulated.

**Source pins for every lesson below:** OWASP LLM Top 10 2026 (published 2026-08-04) and OWASP Top 10 for Agentic Applications 2026 (December 2025, ASI01–ASI10) — always cite the edition; NIST AI RMF 1.0 (January 2023) plus the GenAI Profile NIST AI 600-1 (July 2024, twelve GAI risks with Govern/Map/Measure/Manage actions) — cite the profile, not just the framework homepage.

- **P15.1 — Assets, threat actors, trust boundaries, and abuse cases** — **Priority:** must-have. Depends on: P4.4, P10.4, P11.6. Identify data, credentials, actions, tenants, external systems, and likely attack paths. **Proof:** threat model with mitigations and residual risk. Sources: S16–S17, S24, F11.
- **P15.2 — Prompt injection and untrusted content** — **Priority:** important. Depends on: P12.2–P12.5, P13.2. Direct/indirect injection, data-as-instruction confusion, and why prompting alone is not a security boundary. **Proof:** adversarial tests and an architecture-level mitigation plan. Sources: S16–S17; anchor case EchoLeak (CVE-2025-32711, CVSS 9.3, disclosed by Aim Labs June 2025): benign-email XPIA bypass → reference-style Markdown link-redaction bypass → image auto-fetch → Teams preview-API CSP proxy; fixed server-side May/June 2025; no in-the-wild exploitation observed. Teach it as demonstrated vulnerability with defense-in-depth mitigations (provenance-based access control, output sandboxing, strict CSP without open proxies), never as a how-to.
- **P15.3 — Least privilege, authorization, and human approvals** — **Priority:** important. Depends on: P4.4, P13.2–P13.5, P15.1. Allowlisted tools, scoped identities, user confirmation for consequential actions, and server-side policy enforcement. **Proof:** tool permission matrix plus denied-action tests. Sources: S16–S17, S24.
- **P15.4 — Sensitive data, secrets, tenant isolation, and retention** — **Priority:** important. Depends on: P3.7, P5.1–P5.6, P15.1. Coupled with: P12.2. Data minimization, access controls, log redaction, encryption responsibilities, and deletion flows. **Proof:** data-flow and retention review that checks the ingestion-time permission and retention hooks built in P12.2 and records any gap rather than retrofitting silently. Sources: S16, S24, F11.
- **P15.5 — Secure API and dependency boundaries** — **Priority:** important. Depends on: P4.4–P4.6, P9.1–P9.2, P15.1–P15.4. Authorization flaws, injection, resource exhaustion, dependency trust, and configuration mistakes. **Proof:** security checklist and tests mapped to actual routes and tools, including a cross-user or cross-tenant access test written from the requirement rather than from the generated handler. Sources: F11, S39 (§2.2, REC-API-12.3).
- **P15.6 — Audit, incident response, and AI risk governance** — **Priority:** important. Depends on: P9.5, P14.5, P15.1–P15.5. Logs, kill switches, incident ownership, residual risk, and lifecycle-based risk review. **Proof:** operational security runbook and risk register. Sources: S16–S17, S24.

# Phase 16 — Production AI delivery, rollout, and adoption

**Goal:** Move from a technically working service to a controlled system that real users can trust and operate.

- **P16.1 — Service boundaries and failure containment for AI dependencies** — **Priority:** important. Depends on: P8.3–P8.7, P11.4, P13.3, P14.5. Decide where to time out, retry, degrade, fall back to deterministic code, or ask for human review. **Proof:** dependency failure matrix with tested degradation paths. Sources: S9–S10, S25.
- **P16.2 — Deployment architecture and environments** — **Priority:** important. Depends on: P9.1–P9.2, P14.4, P15.4–P15.6. Configuration, secrets, networks, database migration, model/provider configuration, and artifact provenance. **Proof:** repeatable deployment notes and smoke tests. Sources: F7, S25.
- **P16.3 — Progressive rollout, rollback, and launch criteria** — **Priority:** important. Depends on: P9.4, P14.4–P14.6, P15.6, P16.1–P16.2. Prototype → shadow/test → small pilot → expand, with explicit stop conditions. **Proof:** release plan with quality, security, reliability, and business gates. Sources: S25, F10.
- **P16.4 — Human workflow, feedback, and change management** — **Priority:** important. Depends on: P10.1–P10.3, P16.3. Place the system where users work; design correction, escalation, and fallback paths. **Proof:** observed pilot feedback and a prioritized improvement log. Source: S1–S2.
- **P16.5 — Measure outcome, handover, and ownership** — **Priority:** important. Depends on: P0.3, P9.4–P9.5, P14.3, P16.3–P16.4. Separate real from simulated impact and document limits, runbooks, alerts, escalation, cost, and accountable owners. **Proof:** before/after report with data provenance and honest limitations. Sources: S1–S2, S24–S25.

# Phase 17 — Capstone and evidence portfolio

**Goal:** Demonstrate end-to-end ownership. This phase is open-ended and should evolve from lessons and real constraints; it is not a fixed tutorial to copy.

- **P17.1 — Select a narrow, high-value workflow** — **Priority:** must-have. Depends on: P10.1–P10.4, P16.1. Confirm access to data/users, a measurable baseline, bounded risks, and a reason AI is appropriate. **Artifact:** problem brief, baseline, stakeholder map, and explicit non-goals. Sources: `AGENTS.md` §11; external scoping sources remain unverified — the real engagement is the evidence.
- **P17.2 — Build in vertical slices** — **Priority:** must-have. Depends on: P4.7, P5.6, P7.2, P8.2–P8.7, and the chosen AI lessons. Each slice must run and be tested before the next layer is added, starts from a written delegation brief, is small enough to review, and ends with an agent review record (§3). **Artifact:** repository with tests, migrations, integration contract, failure-path coverage, and an agent review record per slice. Sources: S40, S41.
- **P17.3 — Produce the evidence pack** — **Priority:** must-have. Depends on: P7.5b, P9.3–P9.7, P10.4, P14.1–P14.6, P15.1–P15.6, P16.2–P16.5. **Artifact:** ADRs, architecture diagram, threat model, evaluation report, trace examples, runbook, rollout plan, known-limitations list, impact report, and the agent review records. Mark simulated evidence explicitly and state which agent-written parts were independently verified. Source: `AGENTS.md` §11.
- **P17.4 — Defend decisions and failure scenarios** — **Priority:** must-have. Depends on: all relevant capstone lessons. Explain why this design, what alternatives were rejected, where it fails, how a failure is detected, how the system recovers, and what remains unproven; state which parts an agent wrote, how each was verified, and why the accepted changes can be trusted. **Artifact:** concise case deck and scenario walkthrough. Sources: `AGENTS.md` §11–12.

---

## 4. Phase gates: proof before progression

| Gate | Required proof | Lessons generally involved |
|---|---|---|
| **G0 — Clear mission** | Problem brief, baseline, skills ledger | Phase 0 |
| **G1 — Can build and debug** | Reproducible repo, tests, bug diagnosis | Phases 1–3 |
| **G2 — Can build a correct service** | HTTP contract with error model, validation, database schema, migration, provider contract sheet, integration tests, agent review record for one diff, quality-attribute table, architecture ADR with fitness check | Phases 4–7 |
| **G3 — Understands failure and concurrency** | Idempotency, concurrency test, bounded retries, durable processing, outbox crash test, reconciliation replay | Phases 6–9 |
| **G4 — Can reason about production** | CI/CD with rollback rehearsal, logs/metrics/traces, SLI computed from fault runs, incident analysis with stakeholder update, executed fault matrix and runbook | Phase 9 |
| **G5 — Can choose and design an AI use case** | Option comparison including non-AI, system-design brief (requirements, capacity worksheet, diagrams, ADR with alternatives, failure/security risk matrix, validation plan), baseline | Phase 10 |
| **G6 — Can build an LLM application with context** | Validated model interface, measurable retrieval, explicit state and failure behavior | Phases 11–12 |
| **G7 — Can control agent behavior** | Bounded tool use, permissions, stop conditions, recovery and approval paths | Phase 13 + Phase 15 |
| **G8 — Can measure and secure quality** | Evaluation set/report, regression gate, threat model, adversarial tests, traces | Phases 14–15 |
| **G9 — Can deliver and hand over** | Deployment evidence, pilot/feedback, outcome report, runbook, known limitations | Phases 16–17 |

Passing a gate means the user can explain and defend the evidence. It does not mean the user is guaranteed employment or that a lab is equivalent to production experience.

## 5. Suggested capstone shape

Start with a narrow workflow such as an internal operations request or support-triage process using synthetic or approved data. Do not start by building a general-purpose autonomous assistant.

1. **Deterministic baseline:** request intake, validation, persisted state, audit history, and a clear human workflow.
2. **Integration:** one external API or webhook with authentication, deduplication, bounded retries, and reconciliation.
3. **AI feature only if justified:** for example classification, extraction, or grounded knowledge lookup. Compare its results with a deterministic baseline.
4. **Evaluation and safety:** labelled test set, edge/adversarial cases, regression checks, permission controls, and human approval for consequential actions.
5. **Production shape:** observability, timeouts/budgets, deployment, rollback, small pilot, runbook, and honest impact measurement.

The capstone must remain small enough to finish and test. Add a component only when a requirement or observed failure justifies it. Build the backend and integration parts in TypeScript/Node.js with PostgreSQL; use Python for the AI feature where the AI lessons require it, behind a stable contract. Delegate each slice from a written brief and close it with an agent review record.

## 6. Supporting branches — not required all at once

- **Production performance and traffic spikes:** open `production-performance-incident-study-map.md` when the P0.2 baseline check or a Phase 9 diagnosis (P9.6) exposes a gap, or a real project needs it. Do not study all performance topics up front.
- **AI Security specialization:** deepen OWASP/NIST, red teaming, secure SDLC, and security labs after Phase 15 or when the capstone risk requires it.
- **Distributed systems depth:** use *Designing Data-Intensive Applications*, 2nd ed.; *Understanding Distributed Systems*, 2nd ed.; *Building Microservices*, 2nd ed.; *Designing Distributed Systems*, 2nd ed.; *Software Architecture: The Hard Parts*; and *Foundations of Scalable Systems* as chapter-level sources only when the lesson needs them. Author/title/edition confirmed from each book's epub OPF metadata (2026-10-17); chapters tagged `[TOC]` come from a table of contents only.
- **Framework specialization:** Avoid framework-first tutorials disconnected from the capstone.

## 7. Source register for this map

The F-series foundational sources are maintained in the canonical
[`RESOURCES.md`](RESOURCES.md) registry. Lesson references such as `F1` and
`F12` must be resolved there. Re-open the exact page used before teaching and
record the subsection or version; a landing-page check is not proof that every
chapter or page has been read.

### S-series — existing project source registry

The following IDs are defined in `RESOURCES.md`; consult that file for publisher, verification state, edition, and access notes. Only entries marked **Verified** may support a factual claim. The most relevant starting points are:

- **S1:** FDE role standard — the Claude Frontier Academy announcement (2026-10-02) is primary: $100M program, 10,000 FDEs by end-2027, medical-model residency, simulated enterprise deployment, graded practical, badges from early 2027. **S2:** single Deloitte job listing — treat as stale/unverified until re-opened; superseded by S1.
- **S3, S7–S8, S12–S14:** agent/workflow patterns, tool design, multi-agent trade-offs, long-running execution, MCP-related engineering. Note S3's banner (tooling landscape changed since Dec 2024): patterns stand, tooling examples need re-checking.
- **S6:** MCP specification — pin the spec date in each lesson record (current 2026-07-28; priors 2025-11-25, 2025-06-18).
- **S4, S21–S23:** official model APIs, agent SDKs, and evaluation tools; re-check current versions. S22 (OpenAI evals guide) is deprecated — the Evals platform goes read-only 2026-10-31 and shuts down 2026-11-30; teach the Datasets/evaluation-getting-started flow instead (banner verified 2026-10-09).
- **S5:** context engineering.
- **S9–S10:** reliability postmortem and incident evidence.
- **S15:** evaluation methodology and agent-eval practice (2026-01-09 refresh). **S22:** deprecated (see S4/S21–S23 note).
- **S16–S17:** OWASP LLM Top 10 2026 and Agentic Top 10 2026 — always cite the edition. **S24:** NIST AI RMF 1.0 plus GenAI Profile NIST AI 600-1 — cite the profile.
- **S18–S19, S25–S29:** distributed systems, data systems, architecture, scalability, and SRE foundations.
- **S33–S42 (S33–S41 added 2026-10-15; S42 added 2026-10-16):** S33 AWS Well-Architected REL03-BP01 (workload segmentation; vendor guidance), S34 Node.js test-CI security incident, S35 and S36 Cloudflare's 2025 outage account and resilience plan, S37 Stripe's AI-agent integration benchmark, S38 *Software Architecture: The Hard Parts* (chapters `[TOC]` only), S39 NIST SP 800-228-upd1 (the original SP 800-228 was withdrawn 2026-03-13 and superseded in its entirety), S40 GitHub's guide to human oversight in AI-assisted code review, S41 Faler's essay on AI-assisted engineering antipatterns, S42 C4 model for architecture diagramming (site structure verified). Read the caveats in `RESOURCES.md` first: S33, S36, S37, S40, and S41 are vendor or practitioner material, not independent measurement.

### Known source gaps — keep visible

- RAG failure taxonomy: adopted Barnett et al. 2024 (FP1–FP7) for P12.5; the residual gap is chunking/embedding/reranking tuning depth, still flagged in `RESOURCES.md`.
- `RESOURCES.md` still flags a suitable primary tutorial on statistical uncertainty for LLM evaluation as missing; P14.3 uses the labeled interim protocol.
- Agent tool-misuse: EchoLeak (CVE-2025-32711) is verified for casebook use; further incidents named in the OWASP Agentic 2026 announcement remain leads until their primaries are opened.
- Webhook signature verification and raw-body handling (P8.4): no verified provider source yet; the provider documentation leads in `RESOURCES.md` are unopened.
- Human-in-the-loop practice (rule 12): S40 and S41 are qualitative vendor and practitioner material and S37 is a small vendor benchmark. None measures the effect of a review practice, so teach the requirements as engineering judgment, not as proven effect sizes.
- For any topic whose supporting source is not verified, the lesson must label it as a research gap and avoid stating it as established fact.

## 8. Progress ledger template

Only update a checkbox when proof exists. Record the artifact path, commit, test report, decision record, or learning record next to it.

```text
Phase 0  [ ] P0.1 [ ] P0.2 [ ] P0.3
Phase 1  [ ] P1.1 [ ] P1.2 [ ] P1.3 [ ] P1.4 [ ] P1.5
Phase 2  [ ] P2.1 [ ] P2.2 [ ] P2.3 [ ] P2.4 [ ] P2.5
Phase 3  [ ] P3.1 [ ] P3.2 [ ] P3.4 [ ] P3.5 [ ] P3.6 [ ] P3.7
Phase 4  [ ] P4.1 [ ] P4.2 [ ] P4.3 [ ] P4.4 [ ] P4.5 [ ] P4.6 [ ] P4.7 [ ] P4.8
Phase 5  [ ] P5.1 [ ] P5.2 [ ] P5.3 [ ] P5.4 [ ] P5.5 [ ] P5.6 [ ] P5.7
Phase 6  [ ] P6.1 [ ] P6.2 [ ] P6.3 [ ] P6.4 [ ] P6.5 [ ] P6.6
Phase 7  [ ] P7.1 [ ] P7.2 [ ] P7.3 [ ] P7.4 [ ] P7.5a [ ] P7.5b
Phase 8  [ ] P8.1 [ ] P8.2 [ ] P8.3 [ ] P8.4 [ ] P8.5 [ ] P8.6 [ ] P8.7
Phase 9  [ ] P9.1 [ ] P9.2 [ ] P9.3 [ ] P9.4 [ ] P9.5 [ ] P9.6 [ ] P9.7
Phase 10 [ ] P10.1 [ ] P10.2 [ ] P10.3 [ ] P10.4
Phase 11 [ ] P11.1 [ ] P11.2 [ ] P11.3 [ ] P11.4 [ ] P11.5 [ ] P11.6
Phase 12 [ ] P12.1 [ ] P12.2 [ ] P12.3 [ ] P12.4 [ ] P12.5 [ ] P12.6 [ ] P12.7
Phase 13 [ ] P13.1 [ ] P13.2 [ ] P13.3 [ ] P13.4 [ ] P13.5 [ ] P13.6
Phase 14 [ ] P14.1 [ ] P14.2 [ ] P14.3 [ ] P14.4 [ ] P14.5 [ ] P14.6
Phase 15 [ ] P15.1 [ ] P15.2 [ ] P15.3 [ ] P15.4 [ ] P15.5 [ ] P15.6
Phase 16 [ ] P16.1 [ ] P16.2 [ ] P16.3 [ ] P16.4 [ ] P16.5
Phase 17 [ ] P17.1 [ ] P17.2 [ ] P17.3 [ ] P17.4
```

Merged unit: the former P3.3 (runtime validation versus static types) now lives in P2.2; the tombstone stands in Phase 3 above.


## 9. What this roadmap does and does not claim

- It **does** give a pedagogical dependency order that builds from programming and web/data correctness into distributed systems, AI applications, and production FDE delivery.
- It **does** reference official documentation, engineering material, books, and standards to ground individual lessons.
- It **does not** claim that an external authority has validated this exact sequence as uniquely optimal, that every learner needs every lesson, or that finishing it guarantees employment.
