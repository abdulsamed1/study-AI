# FDE Journey Map — Deep Engineering Roadmap

**Purpose:** Build durable engineering capability for taking a real business problem from discovery to a reliable, evaluated, secure, deployed AI-enabled system. This is a long-form learning journey.

**Status:** Active canonical journey, revised 2026-10-09. This file combines the journey map and the detailed engineering roadmap. The interview-focused `estaie-study-map.md` remains a separate, time-boxed branch and must not determine the depth or order of this curriculum.

**Mission alignment:** FDE = problem discovery → choose the right solution (including non-AI) → build → evaluate → secure → deploy → integrate into work → measure impact → hand over. The target is demonstrable engineering judgment, not completion of a syllabus.

---

## 1. Rules for this journey

1. **Follow dependencies, not enthusiasm.** Each lesson lists its prerequisite lesson IDs. A lesson is ready only when its prerequisite's exit evidence exists.
2. **Teach one lesson unit at a time.** A unit normally takes 45–90 minutes of teaching and guided practice; larger implementation units may span several sessions. Estimated times are planning aids, not promises.
3. **Teach → model → practice → review → retrieve later.** Do not quiz on a concept before teaching it. Re-test important ideas in a changed scenario after a delay.
4. **No progress by attendance.** Mark a lesson complete only when its proof artifact or practical performance meets the exit criteria.
5. **Respect established experience.** The user already has C++, OOP, and DSA experience. Do not teach beginner programming, object-oriented programming, or generic algorithm lessons. Use diagnostics to identify only the language, runtime, API, data, or AI-engineering gaps needed for the capstone.
6. **One evolving capstone.** Build a small, deterministic business workflow first; add persistence and integrations; introduce AI only when the use case justifies it; then evaluate, secure, deploy, pilot, and document it. Keep scope narrow.
7. **Source discipline.** `RESOURCES.md` remains the canonical project source register. Existing `S#` tags refer to it. The `F#` references below are official starting points checked on 2026-10-09; re-open the relevant page and record the exact section/version before teaching. Current API/model/security behavior must be verified at lesson time.
8. **Separate evidence from synthesis.** Each lecture labels source-backed facts, mentor synthesis, and practice. If reliable source coverage is missing, say so instead of filling the gap silently.
9. **No invented professional evidence.** A lab proves a lab skill; it does not prove production experience or business impact. Label simulated data and pilots honestly.
10. **This is a dependency graph represented as a mostly linear path.** Some concepts can be revisited later. Do not force advanced internals when the mission does not need them.

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

This order deliberately puts HTTP, data correctness, testing, and failure handling before complex agent architectures. AI is a later capability layer built on software engineering foundations, not a substitute for them. The roadmap does not require learning every language or framework: use Python as the default AI/GenAI implementation track, and choose TypeScript/Node only when the capstone or deployment context benefits from it.

## 3. Lesson design and completion criteria

Every lesson follows this record shape:

- **ID and objective:** one capability that can be demonstrated.
- **Prerequisites:** required lesson IDs, not just earlier topics.
- **Source:** specific project source IDs and/or official documentation to open.
- **Lesson:** scenario → concept → mechanism → failure modes → production implications.
- **Practice:** one tangible task, preferably on the evolving capstone or a deliberately small lab.
- **Exit evidence:** artifact or reasoning that proves the objective.
- **Retrieval:** a later variation to ensure the idea was retained.

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

---

# Phase 0 — Mission, baseline, and problem framing

**Goal:** Know what success means before choosing technologies. **Gate G0:** a written problem brief and an honest skills baseline.

- **P0.1 — FDE delivery loop** — Depends on: none. Learn the lifecycle from ambiguous request to handover; distinguish a demo, a working system, and a deployed outcome. **Proof:** draw the delivery loop and list evidence required at each stage. Sources: `AGENTS.md` §§1–2, S1–S2.
- **P0.2 — Technical baseline and workbench check** — Depends on: P0.1. Inventory what can be explained, built, tested, debugged, and operated today. **Proof:** evidence-based skills ledger; no self-ratings without examples. Source: `EVIDENCE.md`.
- **P0.3 — Problem brief and baseline metric** — Depends on: P0.1–P0.2. Identify users, present workflow, pain, baseline, constraints, risk, and success metric. **Proof:** one-page problem brief with assumptions marked. Sources: S1–S2.

# Phase 1 — Engineering workbench and feedback loop

**Goal:** Work reproducibly in a repository and diagnose behavior instead of guessing. **Gate G1:** a small project that can be run, tested, debugged, and reviewed from a clean checkout.

- **P1.1 — Terminal, paths, processes, environment variables** — Depends on: P0.2. Navigate files; run commands; inspect exit codes, processes, and environment. **Proof:** documented run commands and diagnosis of a deliberately broken setup. Source: F1, F3.
- **P1.2 — Git fundamentals and history** — Depends on: P1.1. Working tree, staging, commits, branches, diffs, merge conflicts, ignore rules, remote repository. **Proof:** clean commit history and a resolved practice conflict. Source: F1.
- **P1.3 — Read an unfamiliar codebase** — Depends on: P1.1–P1.2. Trace entry points, configuration, module boundaries, data flow, and tests before changing code. **Proof:** a short architecture note with links to the actual files.
- **P1.4 — Debugging from evidence** — Depends on: P1.1–P1.3. Reproduce, reduce, inspect, hypothesize, test, and confirm a cause. **Proof:** a small bug report with reproduction steps, observations, cause, fix, and regression test.
- **P1.5 — Testing and feedback loop** — Depends on: P1.2–P1.4. Learn assertions, test setup/teardown, deterministic tests, failure output, and basic test boundaries. **Proof:** tests that fail before the fix and pass after it. Sources: F3, F8.

# Phase 2 — AI-engineering implementation bridge

**Goal:** Bridge existing C++/OOP/DSA experience into the languages, runtimes, and data contracts used by AI products. This is diagnostic and just-in-time, not beginner programming.

- **P2.1 — Choose the implementation language for the capstone** — Depends on: P1.3, P1.5. Use Python by default for AI/GenAI work; choose TypeScript/Node only when the capstone or deployment context justifies it. **Proof:** record an ADR and implement one minimal provider call in the chosen language. Sources: F2, F3, F13, F14.
- **P2.2 — AI-service data contracts and runtime validation** — Depends on: P2.1, P1.5. JSON, schemas, serialization, missing/null fields, provider responses, and validation at trust boundaries. **Proof:** reject malformed model/tool output before domain logic. Sources: F2, F5, S4, S21.
- **P2.3 — Async I/O, concurrency, cancellation, and timeouts** — Depends on: P2.1–P2.2. Apply existing programming knowledge to provider calls, retrieval, tools, queues, and bounded parallelism. **Proof:** run concurrent calls with deterministic timeout, cancellation, and cleanup behavior. Sources: F3, F13.
- **P2.4 — Python/TypeScript AI SDK ergonomics** — Depends on: P2.1–P2.3. Read SDK types, inspect request/response objects, manage dependencies, pin versions, and isolate provider adapters. **Proof:** a small adapter with typed inputs, safe configuration, and tests. Sources: F3, F5, S4, S21.
- **P2.5 — AI-engineering test seam** — Depends on: P2.2–P2.4. Mock provider boundaries without pretending mocks prove model quality; preserve fixtures for real evaluation later. **Proof:** unit tests for contract/error paths plus a clearly separated live smoke test. Sources: F8, S15, S22.

# Phase 3 — Chosen implementation runtime

**Goal:** Build production AI-service code in one chosen runtime. Python is the
default for AI/GenAI work; TypeScript/Node is an equivalent alternative when
the capstone, existing codebase, or deployment environment justifies it. Do not
study both tracks as separate curricula.

- **P3.1 — Types and compiler/runtime feedback** — Depends on: P2.1–P2.5. Use the chosen language's type system, static checks, and diagnostics where available. **Proof:** turn the Phase 2 payload normalizer into typed, checked code. Sources: F3, F5.
- **P3.2 — Valid and invalid data states** — Depends on: P3.1, P2.4, P2.2. Model optional data and event variants explicitly. **Proof:** process multiple event types without unsafe assumptions. Sources: F3, F5.
- **P3.3 — Runtime validation versus static types** — Depends on: P3.1–P3.2, P2.2. Understand that incoming JSON is untrusted at runtime. **Proof:** reject invalid payloads with actionable errors before domain logic runs. Sources: F3, F5.
- **P3.4 — Process, packages, configuration, and secrets** — Depends on: P1.1–P1.2, P2.5, P3.1. Process lifecycle, dependency lockfiles, scripts, environment config, and secret boundaries. **Proof:** bootstrap a reproducible AI service in the chosen runtime. Sources: F3.
- **P3.5 — Non-blocking I/O and blocking work** — Depends on: P2.3, P3.4. Understand why one slow/blocking operation can affect concurrency. **Proof:** identify and remove a blocking operation in a small lab. Sources: F3.
- **P3.6 — Async failure, cancellation, timeouts, and resource cleanup** — Depends on: P2.3, P3.4–P3.5. Avoid orphaned tasks, leaked resources, and work that outlives its request. **Proof:** implement timeout-aware I/O and cleanup paths. Sources: F3.
- **P3.7 — Logging, configuration, and secret hygiene** — Depends on: P3.4, P3.6. Structured logs, config validation, secret injection, and redaction. **Proof:** logs support diagnosis without exposing credentials. Sources: F3, F11.

For a Python capstone, translate P3.1–P3.7 into the equivalent Python
runtime, typing, packaging, async, validation, logging, and secret-management
work. The objective is the AI-service capability, not TypeScript itself.

# Phase 4 — Internet, HTTP, and API contracts

**Goal:** Understand the contract across a network boundary before designing integrations.

- **P4.1 — Network request mental model** — Depends on: P2.2, P3.4. Client/server, DNS at a conceptual level, connection, TLS purpose, and network failure boundaries. **Proof:** trace a request from client to server and name where failures may occur. Source: F4.
- **P4.2 — HTTP request and response anatomy** — Depends on: P4.1. Methods, paths, headers, body, status codes, content types, and caching semantics. **Proof:** inspect several real requests/responses and explain their contracts. Source: F4.
- **P4.3 — Resource design and REST-style APIs** — Depends on: P4.2, P3.2–P3.3. Resource identity, methods, representation, validation, pagination, and versioning. **Proof:** design an API contract for the capstone before implementation. Source: F4.
- **P4.4 — Authentication and authorization basics** — Depends on: P4.2–P4.3, P3.7. API keys, bearer tokens, OAuth concepts, scopes, ownership checks, and secret hygiene. **Proof:** test allowed and denied requests; state the difference between authentication and authorization. Sources: F4, F11.
- **P4.5 — HTTP failure semantics, retries, and rate limits** — Depends on: P2.3, P4.2. Timeouts, 4xx/5xx categories, 429, `Retry-After`, and why not every error should be retried. **Proof:** write a client policy table for retryable and permanent outcomes. Sources: F4, S25.
- **P4.6 — API data contracts and schema evolution** — Depends on: P3.3, P4.3. Validation, unknown fields, additive/breaking changes, compatibility, and idempotent client behavior. **Proof:** test old and new payload versions. Sources: F4, F11.
- **P4.7 — Build and test a small HTTP service/client** — Depends on: P3.1–P3.7, P4.1–P4.6. Implement one endpoint, one client, validation, errors, config, and tests. **Proof:** reproducible service and contract tests. Sources: F3, F4, F8.

# Phase 5 — Relational data and SQL

**Goal:** Model persisted facts correctly before relying on AI or distributed behavior.

- **P5.1 — Relational modeling and data invariants** — Depends on: P2.3, P4.3. Entities, relationships, keys, cardinality, nullability, and invariants. **Proof:** schema sketch for users, requests, events, and processing state.
- **P5.2 — SQL reads/writes, joins, aggregation** — Depends on: P5.1. CRUD, filtering, joins, grouping, ordering, and transaction boundaries at a basic level. **Proof:** answer business questions with SQL, not application loops. Source: F6.
- **P5.3 — Constraints and integrity** — Depends on: P5.1–P5.2. Primary/foreign keys, uniqueness, check constraints, and why application checks alone can race. **Proof:** encode key invariants in the database. Source: F6.
- **P5.4 — Indexes and query plans** — Depends on: P5.2–P5.3. Query patterns, B-tree mental model, selectivity, `EXPLAIN`, and index costs. **Proof:** measure one query before/after a justified index. Source: F6.
- **P5.5 — Schema migrations and safe change** — Depends on: P5.1–P5.4, P1.2. Versioned schema changes, backfill, deploy order, rollback limits, and compatibility. **Proof:** perform an additive migration and document its rollout sequence. Source: F6.
- **P5.6 — Database access from the application** — Depends on: P3.4, P4.7, P5.1–P5.5. Parameterized queries or a query builder, connection pooling concepts, mapping and validation. **Proof:** persist and retrieve capstone records with tests. Sources: F3, F6.
- **P5.7 — Backup, restore, and data lifecycle basics** — Depends on: P5.5–P5.6. What backups protect, what they do not, retention/deletion, and restore verification. **Proof:** document and test a local recovery procedure. Sources: S25, F10.

# Phase 6 — Transactions, concurrency, and correctness

**Goal:** Prevent data corruption when operations overlap or fail halfway.

- **P6.1 — Atomicity and transaction boundaries** — Depends on: P5.2–P5.6. Group state changes that must succeed or fail together. **Proof:** transactionally persist one business operation and test rollback. Source: F6, S19.
- **P6.2 — Isolation and anomalies** — Depends on: P6.1. Dirty/non-repeatable/phantom read concepts as applicable, lost updates, and check-then-act races. **Proof:** reproduce a race using two concurrent clients. Source: F6, S19.
- **P6.3 — Locking, optimistic concurrency, and uniqueness** — Depends on: P5.3, P6.1–P6.2. Unique constraints, version checks, row locks, and their trade-offs. **Proof:** fix the race from P6.2 and prove it with a concurrency test. Source: F6, S19.
- **P6.4 — Consistency invariants across multiple writes** — Depends on: P6.1–P6.3. Identify which records must remain consistent and what happens when only one write succeeds. **Proof:** failure matrix for a multi-step state change. Sources: S19, S26.
- **P6.5 — Time, ordering, and duplicate events** — Depends on: P2.2, P4.5–P4.6, P6.1–P6.4. Event time vs processing time, duplicate delivery, out-of-order updates, and event identity. **Proof:** define a state transition table for repeated and stale events. Sources: S19, S27.
- **P6.6 — Design and defend one correctness invariant** — Depends on: P6.1–P6.5. Translate a business guarantee into DB constraints, transaction behavior, tests, and known limits. **Proof:** ADR + tests + written failure analysis.

# Phase 7 — Software design and test strategy

**Goal:** Make changes safe to reason about and cheap to verify.

- **P7.1 — Boundaries, responsibilities, and dependency direction** — Depends on: P2.5, P3.1–P3.4, P4.7. Separate transport, application use cases, domain rules, and persistence where useful. **Proof:** draw a module diagram and justify each boundary. Sources: S20, S26.
- **P7.2 — Unit, integration, contract, and end-to-end tests** — Depends on: P1.5, P4.7, P5.6. Choose the test level that proves a claim; avoid testing implementation details unnecessarily. **Proof:** test one important invariant at multiple appropriate layers. Sources: F8, S20.
- **P7.3 — Test doubles and dependency boundaries** — Depends on: P7.1–P7.2. Know when a fake, stub, or real dependency improves confidence and when it hides a defect. **Proof:** replace one brittle test without losing meaningful integration coverage. Sources: F8.
- **P7.4 — Refactoring under tests and code review** — Depends on: P7.1–P7.3, P1.2–P1.4. Change structure without silently changing behavior. **Proof:** a reviewed refactor with a green regression suite and explanatory diff.
- **P7.5 — Architectural decisions and trade-offs** — Depends on: P7.1–P7.4. Make quality attributes, alternatives, costs, and constraints explicit. **Proof:** ADR comparing at least three options, including the simplest adequate option. Sources: S20, S26.

# Phase 8 — Integration and distributed-systems foundations

**Goal:** Reason about boundaries where networks, retries, queues, and independent state make success ambiguous.

- **P8.1 — Partial failure and ambiguous outcomes** — Depends on: P4.5, P6.1–P6.5. A timeout does not tell the caller whether the remote side effect occurred. **Proof:** failure timeline for a request that times out after the remote write. Sources: S19, S27.
- **P8.2 — Idempotency and deduplication** — Depends on: P6.5, P8.1. Stable operation keys, duplicate semantics, retention, and the role of database uniqueness. **Proof:** repeat a request and show it cannot create a second business effect. Sources: S1, S19.
- **P8.3 — Retry budgets, backoff, jitter, and timeouts** — Depends on: P4.5, P8.1–P8.2. Transient/permanent classification, deadlines, retry storms, and synchronized retries. **Proof:** bounded retry policy with a testable budget. Sources: S25, F10.
- **P8.4 — Webhook receiver and sender contracts** — Depends on: P4.2–P4.6, P6.5, P8.1–P8.3. Verify signatures, validate events, acknowledge deliberately, persist receipt, enqueue durable work, and process idempotently. **Proof:** locally tested webhook flow with invalid signature, duplicate, transient failure, and crash-window tests. Sources: F11, S4.
- **P8.5 — Queues, workers, and at-least-once delivery** — Depends on: P3.5–P3.6, P5.6, P8.2–P8.3. Consumer retry, delayed work, dead-letter strategy, per-key ordering, and idempotent consumers. **Proof:** worker that can restart without duplicating business effects. Sources: S19, S26.
- **P8.6 — Dual writes, outbox, saga, compensation** — Depends on: P6.4, P8.1–P8.5. Understand why independent writes can diverge and distinguish atomic database updates from cross-system workflows. **Proof:** design one safe path through a database write and external event. Source: S19, S26.
- **P8.7 — Synchronization and reconciliation loops** — Depends on: P6.5, P8.2–P8.6. Full/delta sync, watermarks, cursors, drift detection, source of truth, replay, and repair. **Proof:** reconciliation report that classifies missing, duplicate, stale, and conflicting records. Sources: S19, S26, S27.

# Phase 9 — Production engineering, reliability, and performance

**Goal:** Diagnose production behavior from evidence and run changes safely.

- **P9.1 — Runtime configuration, containers, and environments** — Depends on: P3.4, P3.7, P5.6, P7.2. Build a reproducible container and separate local/test/production configuration. **Proof:** clean startup following written instructions. Sources: F7, S26.
- **P9.2 — CI/CD and safe release workflow** — Depends on: P1.2, P7.2, P9.1. Automated checks, build artifacts, deployment steps, migrations, and rollback limits. **Proof:** CI runs tests and builds the service. Sources: F7, S25.
- **P9.3 — Logs, metrics, traces, and correlation** — Depends on: P4.7, P8.4–P8.5, P9.1. Understand what each signal answers and correlate one request across components. **Proof:** trace a request using a correlation ID and explain its timeline. Sources: F9, S25.
- **P9.4 — SLIs, SLOs, error budgets, and alerts** — Depends on: P9.3, P0.3. Define user-visible reliability and alert on actionable symptoms rather than every noisy signal. **Proof:** propose one SLI/SLO and one operational alert with rationale. Sources: S25, F10.
- **P9.5 — Incident response and postmortems** — Depends on: P9.3–P9.4, P8.3. Stabilize, gather evidence, communicate, restore service, and learn without prematurely declaring root cause. **Proof:** incident timeline, mitigation, causal mechanism, and prevention items. Sources: S9, S10, S25.
- **P9.6 — Performance diagnosis and capacity reasoning** — Depends on: P5.4, P8.3, P9.3–P9.5. Latency percentiles, throughput, saturation, queueing, resource pools, database bottlenecks, and workload shape. **Proof:** diagnose a controlled load test before selecting a fix. Source: `production-performance-incident-study-map.md`, S19, S25.
- **P9.7 — Graceful degradation, backups, and recovery** — Depends on: P5.7, P8.3–P8.7, P9.2–P9.6. Set dependency budgets, degrade safely, restore data, and verify recovery. **Proof:** documented recovery/rollback exercise. Sources: S25, F10.

# Phase 10 — FDE discovery, solution selection, and system design

**Goal:** Choose the right solution before building it. This phase reuses the engineering knowledge already acquired.

- **P10.1 — Workflow observation and stakeholder questions** — Depends on: P0.3, P7.1. Map inputs, decisions, handoffs, exceptions, and existing tools. **Proof:** current-state workflow with unanswered questions labelled.
- **P10.2 — Deterministic code vs workflow vs agent** — Depends on: P10.1, P7.5, P8.1. Choose the least complex design that meets the need; identify where autonomy is useful and where it is dangerous. **Proof:** written option comparison including a non-AI option. Sources: S3, S12.
- **P10.3 — Baseline, outcome metric, and adoption constraints** — Depends on: P0.3, P9.4, P10.1. Separate technical proxy metrics from business outcomes; note how the baseline will be gathered. **Proof:** measurement plan with owner and collection method.
- **P10.4 — System design and risk boundary** — Depends on: P6.6, P7.5, P8.7, P9.7, P10.2–P10.3. Define components, data flows, trust boundaries, failure behavior, and ownership. **Proof:** architecture diagram and ADR. Sources: S20, S24.

# Phase 11 — LLM fundamentals and model API engineering

**Goal:** Treat a model as a probabilistic component behind an explicit software contract.

- **P11.1 — What a language model does and does not guarantee** — Depends on: P10.2, P4.6. Generation, nondeterminism, context limits, stale knowledge, and confident errors at an engineering level; no unnecessary ML math. **Proof:** list use-case-specific failure modes and what cannot be guaranteed. Sources: S3, S11.
- **P11.2 — Request anatomy, tokens, context window, and response metadata** — Depends on: P11.1, P3.3. Messages, instructions, output limits, finish reasons, and provider-specific request/response contracts. **Proof:** build a minimal model call and log safe request metadata. Sources: S4, S21.
- **P11.3 — Structured outputs and runtime validation** — Depends on: P3.3, P11.2. JSON/schema-constrained output where supported, parse/validation failure, and bounded repair. **Proof:** invalid model output cannot reach the domain layer unvalidated. Sources: S4, S21.
- **P11.4 — Model errors, rate limits, latency, cost, and budgets** — Depends on: P8.3, P9.3, P11.2. Provider failures, concurrency caps, request budgets, token accounting, and timeout behavior. **Proof:** cost/latency/error budget and tested fallback behavior. Sources: S4, S21.
- **P11.5 — Prompt/context versioning and model changes** — Depends on: P11.2–P11.4, P14.1. Treat prompts, schemas, retrieval settings, and model identifiers as versioned inputs to behavior. **Proof:** versioned configuration and an evaluation rerun on a deliberate change. Sources: S4, S15, S22.
- **P11.6 — Decide where an LLM belongs in the architecture** — Depends on: P10.2–P10.4, P11.1–P11.5. Keep deterministic invariants outside the model when possible; define fallback and human-review boundaries. **Proof:** updated ADR with failure containment and reasons not to use an LLM in selected steps. Sources: S3, S12.

# Phase 12 — Context engineering, retrieval, RAG, and memory

**Goal:** Provide the model with relevant, permissioned information and measure whether retrieval actually helps.

- **P12.1 — Context engineering and information budgets** — Depends on: P11.1–P11.2. Select useful context, keep it current, and avoid flooding the model with irrelevant material. **Proof:** compare two context assembly strategies using fixed examples. Sources: S5, F12.
- **P12.2 — Data ingestion and document lifecycle** — Depends on: P5.1–P5.6, P12.1. Sources, parsing, metadata, versioning, deletion, and permission inheritance. **Proof:** ingestion pipeline with provenance and re-index/delete behavior.
- **P12.3 — Chunking, embeddings, lexical search, and vector search** — Depends on: P12.2, P11.2. Understand the pipeline and what each retrieval method contributes without prematurely choosing a vector database. **Proof:** inspect results for a small controlled corpus. Sources: F12, S5.
- **P12.4 — Retrieval pipeline: filters, hybrid search, reranking** — Depends on: P12.3, P4.6, P9.3. Improve recall/relevance while preserving tenant and access filters. **Proof:** retrieval results with measured top-k quality on a labelled set. Sources: F12, S5.
- **P12.5 — RAG grounding, citations, abstention, and failure taxonomy** — Depends on: P12.1–P12.4, P11.3. Distinguish retrieval failure, missing source coverage, synthesis error, and unsupported answer. **Proof:** label a test set by failure type and make the system abstain appropriately. **Source note:** `RESOURCES.md` records a RAG failure-taxonomy coverage gap; research and verify a primary source before teaching this lesson.
- **P12.6 — Evaluate retrieval separately from generation** — Depends on: P12.4–P12.5, P14.1–P14.2. Measure whether the right evidence was retrieved before judging the final answer. **Proof:** report retrieval and answer-quality results separately. Sources: S15, S22; source gaps must remain explicit.
- **P12.7 — Conversation state, durable memory, compaction, and freshness** — Depends on: P6.5, P12.1–P12.6. Separate session state, durable business facts, retrieved knowledge, and generated summaries. **Proof:** define state ownership, retention, expiry, and update rules. Sources: S5, S8, S13.

# Phase 13 — Workflows, tools, agents, and MCP

**Goal:** Increase autonomy only when the workflow needs it and controls are adequate.

- **P13.1 — Workflow patterns before agents** — Depends on: P7.1, P10.2, P11.6. Chaining, routing, parallelization, orchestrator/worker, and evaluator/optimizer patterns. **Proof:** map a task to a workflow pattern and explain why. Sources: S3, S12.
- **P13.2 — Tool contracts and safe tool design** — Depends on: P4.6, P6.6, P11.3. Explicit arguments, schema, permissions, side effects, clear errors, and idempotency. **Proof:** implement a read-only tool with adversarial input tests. Sources: S7, S21.
- **P13.3 — Agent loop, stop conditions, and budgets** — Depends on: P13.1–P13.2, P8.2–P8.5, P11.4. Define state, action, observation, exit criteria, maximum steps, and failure recovery. **Proof:** a bounded agent cannot run forever or repeat a harmful side effect. Sources: S3, S13, S21.
- **P13.4 — State, checkpoints, and long-running workflows** — Depends on: P6.1–P6.5, P8.5–P8.7, P13.3. Resume work safely after interruptions and preserve an auditable progress record. **Proof:** kill and resume a job without losing correctness. Sources: S13, S19.
- **P13.5 — MCP and external tool integration** — Depends on: P4.4, P13.2–P13.4, P15.2. Understand the protocol boundary, server trust, authorization, and the difference between interoperability and safety. **Proof:** connect one low-risk tool and document its trust/permission boundary. Sources: S6, S14.
- **P13.6 — Multi-agent systems and delegation economics** — Depends on: P13.1–P13.5, P14.1. Learn when parallel agents help and when coordination, latency, cost, and failure risk outweigh benefits. **Proof:** compare a single-agent/workflow baseline to a justified multi-agent design; default is not to use multiple agents. Source: S8.

# Phase 14 — Evaluation, testing, and observability for AI systems

**Goal:** Treat quality as a measured property, not a few impressive demo outputs.

- **P14.1 — Turn requirements and failures into evaluation cases** — Depends on: P0.3, P7.2, P11.6. Build representative, edge, and adversarial cases from real workflows and documented failure modes. **Proof:** versioned evaluation set with expected outcomes and provenance. Sources: S15, S22.
- **P14.2 — Graders: code-based, model-based, and human review** — Depends on: P14.1, P11.3. Choose a grader that matches the property; analyze false positives/negatives and judge reliability. **Proof:** compare grader decisions against a human-reviewed sample. Sources: S15, S22.
- **P14.3 — Quality dimensions and statistical uncertainty** — Depends on: P14.1–P14.2, P9.4. Sample size, run-to-run variation, confidence, slices, and meaningful before/after comparison. **Proof:** evaluation report that states limits and avoids overclaiming. **Source note:** `RESOURCES.md` records a statistics-for-evaluation coverage gap; verify a suitable primary tutorial before teaching details.
- **P14.4 — Regression gates and change management** — Depends on: P11.5, P12.6, P14.1–P14.3. Re-run evaluations when prompts, models, retrieval, tools, or policies change. **Proof:** CI or documented release gate that blocks a known regression.
- **P14.5 — Trace a complete AI request** — Depends on: P9.3, P11.2–P11.4, P12.4, P13.3. Trace model calls, retrieval, tools, retries, token/cost information, and final outcomes while redacting sensitive data. **Proof:** diagnose a failed run from a trace. Sources: S9, F9, S21.
- **P14.6 — Failure analysis and operational learning loop** — Depends on: P9.5, P14.1–P14.5. Classify failures, add a regression case, make one change, and measure it. **Proof:** one complete loop from observed failure to verified improvement. Sources: S9, S15.

# Phase 15 — Security, privacy, and AI governance

**Goal:** Bound what the system, model, and tools can access or change, even when the model is wrong or manipulated.

- **P15.1 — Assets, threat actors, trust boundaries, and abuse cases** — Depends on: P4.4, P10.4, P11.6. Identify data, credentials, actions, tenants, external systems, and likely attack paths. **Proof:** threat model with mitigations and residual risk. Sources: S16–S17, S24, F11.
- **P15.2 — Prompt injection and untrusted content** — Depends on: P12.2–P12.5, P13.2. Direct/indirect injection, data-as-instruction confusion, and why prompting alone is not a security boundary. **Proof:** adversarial tests and an architecture-level mitigation plan. Sources: S16–S17.
- **P15.3 — Least privilege, authorization, and human approvals** — Depends on: P4.4, P13.2–P13.5, P15.1. Allowlisted tools, scoped identities, user confirmation for consequential actions, and server-side policy enforcement. **Proof:** tool permission matrix plus denied-action tests. Sources: S16–S17, S24.
- **P15.4 — Sensitive data, secrets, tenant isolation, and retention** — Depends on: P3.7, P5.1–P5.6, P12.2, P15.1. Data minimization, access controls, log redaction, encryption responsibilities, and deletion flows. **Proof:** data-flow and retention review. Sources: S16, S24, F11.
- **P15.5 — Secure API and dependency boundaries** — Depends on: P4.4–P4.6, P9.1–P9.2, P15.1–P15.4. Authorization flaws, injection, resource exhaustion, dependency trust, and configuration mistakes. **Proof:** security checklist and tests mapped to actual routes and tools. Source: F11.
- **P15.6 — Audit, incident response, and AI risk governance** — Depends on: P9.5, P14.5, P15.1–P15.5. Logs, kill switches, incident ownership, residual risk, and lifecycle-based risk review. **Proof:** operational security runbook and risk register. Sources: S16–S17, S24.

# Phase 16 — Production AI delivery, rollout, and adoption

**Goal:** Move from a technically working service to a controlled system that real users can trust and operate.

- **P16.1 — Service boundaries and failure containment for AI dependencies** — Depends on: P8.3–P8.7, P11.4, P13.3, P14.5. Decide where to time out, retry, degrade, fall back to deterministic code, or ask for human review. **Proof:** dependency failure matrix with tested degradation paths. Sources: S9–S10, S25.
- **P16.2 — Deployment architecture and environments** — Depends on: P9.1–P9.2, P14.4, P15.4–P15.6. Configuration, secrets, networks, database migration, model/provider configuration, and artifact provenance. **Proof:** repeatable deployment notes and smoke tests. Sources: F7, S25.
- **P16.3 — Progressive rollout, rollback, and launch criteria** — Depends on: P9.4, P14.4–P14.6, P15.6, P16.1–P16.2. Prototype → shadow/test → small pilot → expand, with explicit stop conditions. **Proof:** release plan with quality, security, reliability, and business gates. Sources: S25, F10.
- **P16.4 — Human workflow, feedback, and change management** — Depends on: P10.1–P10.3, P16.3. Place the system where users work; design correction, escalation, and fallback paths. **Proof:** observed pilot feedback and a prioritized improvement log. Source: S1–S2.
- **P16.5 — Measure outcome, handover, and ownership** — Depends on: P0.3, P9.4–P9.5, P14.3, P16.3–P16.4. Separate real from simulated impact and document limits, runbooks, alerts, escalation, cost, and accountable owners. **Proof:** before/after report with data provenance and honest limitations. Sources: S1–S2, S24–S25.

# Phase 17 — Capstone and evidence portfolio

**Goal:** Demonstrate end-to-end ownership. This phase is open-ended and should evolve from lessons and real constraints; it is not a fixed tutorial to copy.

- **P17.1 — Select a narrow, high-value workflow** — Depends on: P10.1–P10.4, P16.1. Confirm access to data/users, a measurable baseline, bounded risks, and a reason AI is appropriate. **Artifact:** problem brief, baseline, stakeholder map, and explicit non-goals.
- **P17.2 — Build in vertical slices** — Depends on: P4.7, P5.6, P7.2, P8.2–P8.7, and the chosen AI lessons. Each slice must run and be tested before the next layer is added. **Artifact:** repository with tests, migrations, integration contract, and failure-path coverage.
- **P17.3 — Produce the evidence pack** — Depends on: P7.5, P9.3–P9.7, P10.4, P14.1–P14.6, P15.1–P15.6, P16.2–P16.5. **Artifact:** ADRs, architecture diagram, threat model, evaluation report, trace examples, runbook, rollout plan, known-limitations list, and impact report. Mark simulated evidence explicitly.
- **P17.4 — Defend decisions and failure scenarios** — Depends on: all relevant capstone lessons. Explain why this design, what alternatives were rejected, where it fails, how a failure is detected, how the system recovers, and what remains unproven. **Artifact:** concise case deck and scenario walkthrough.

---

## 4. Phase gates: proof before progression

| Gate | Required proof | Lessons generally involved |
|---|---|---|
| **G0 — Clear mission** | Problem brief, baseline, skills ledger | Phase 0 |
| **G1 — Can build and debug** | Reproducible repo, tests, bug diagnosis | Phases 1–3 |
| **G2 — Can build a correct service** | HTTP contract, validation, database schema, migration, integration tests | Phases 4–7 |
| **G3 — Understands failure and concurrency** | Idempotency, concurrency test, bounded retries, durable processing, reconciliation design | Phases 6–9 |
| **G4 — Can reason about production** | CI/CD, logs/metrics/traces, SLI/SLO, incident analysis, recovery exercise | Phase 9 |
| **G5 — Can choose and design an AI use case** | Option comparison including non-AI, architecture diagram, ADR, baseline | Phase 10 |
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

The capstone must remain small enough to finish and test. Add a component only when a requirement or observed failure justifies it.

## 6. Supporting branches — not required all at once

- **Production performance and traffic spikes:** open `production-performance-incident-study-map.md` when Phase 9 diagnosis exposes a gap or a real project needs it. Do not study all performance topics up front.
- **Integration interview preparation:** open `estaie-study-map.md` only when that specific interview or role is active. Its compressed order reflects time pressure and interview evidence, not the full prerequisite path.
- **AI Security specialization:** deepen OWASP/NIST, red teaming, secure SDLC, and security labs after Phase 15 or when the capstone risk requires it.
- **Distributed systems depth:** use *Designing Data-Intensive Applications*, 2nd ed.; *Understanding Distributed Systems*, 2nd ed.; *Building Microservices*; *Designing Distributed Systems*, 2nd ed.; and *Foundations of Scalable Systems* as chapter-level sources only when the lesson needs them. Confirm the author/title/edition from each book's title page before citing it.
- **Framework specialization:** learn NestJS, Next.js, a specific queue, vector store, cloud platform, or agent SDK after the underlying contract/problem is understood. Avoid framework-first tutorials disconnected from the capstone.

## 7. Source register for this map

The F-series foundational sources are maintained in the canonical
[`RESOURCES.md`](RESOURCES.md) registry. Lesson references such as `F1` and
`F12` must be resolved there. Re-open the exact page used before teaching and
record the subsection or version; a landing-page check is not proof that every
chapter or page has been read.

### S-series — existing project source registry

The following IDs are defined in `RESOURCES.md`; consult that file for publisher, verification state, edition, and access notes. Only entries marked **Verified** may support a factual claim. The most relevant starting points are:

- **S1–S2:** FDE role standard and role expectations.
- **S3, S7–S8, S12–S14:** agent/workflow patterns, tool design, multi-agent trade-offs, long-running execution, MCP-related engineering.
- **S4, S21–S23:** official model APIs, agent SDKs, and evaluation tools; re-check current versions.
- **S5:** context engineering.
- **S9–S10:** reliability postmortem and incident evidence.
- **S15, S22:** evaluation methodology and tooling.
- **S16–S17, S24:** AI security and risk management.
- **S18–S19, S25–S29:** distributed systems, data systems, architecture, scalability, and SRE foundations.

### Known source gaps — keep visible

- `RESOURCES.md` flags that a comprehensive, verified primary-source RAG failure taxonomy is still missing.
- `RESOURCES.md` flags that a suitable primary tutorial on statistical uncertainty for LLM evaluation is still missing.
- Agent tool-misuse incident evidence needs stronger verification before it becomes a casebook claim.
- For any topic whose supporting source is not verified, the lesson must label it as a research gap and avoid stating it as established fact.

## 8. Progress ledger template

Only update a checkbox when proof exists. Record the artifact path, commit, test report, decision record, or learning record next to it.

```text
Phase 0  [ ] P0.1 [ ] P0.2 [ ] P0.3
Phase 1  [ ] P1.1 [ ] P1.2 [ ] P1.3 [ ] P1.4 [ ] P1.5
Phase 2  [ ] P2.1 [ ] P2.2 [ ] P2.3 [ ] P2.4 [ ] P2.5
Phase 3  [ ] P3.1 [ ] P3.2 [ ] P3.3 [ ] P3.4 [ ] P3.5 [ ] P3.6 [ ] P3.7
Phase 4  [ ] P4.1 [ ] P4.2 [ ] P4.3 [ ] P4.4 [ ] P4.5 [ ] P4.6 [ ] P4.7
Phase 5  [ ] P5.1 [ ] P5.2 [ ] P5.3 [ ] P5.4 [ ] P5.5 [ ] P5.6 [ ] P5.7
Phase 6  [ ] P6.1 [ ] P6.2 [ ] P6.3 [ ] P6.4 [ ] P6.5 [ ] P6.6
Phase 7  [ ] P7.1 [ ] P7.2 [ ] P7.3 [ ] P7.4 [ ] P7.5
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

## 9. What this roadmap does and does not claim

- It **does** give a pedagogical dependency order that builds from programming and web/data correctness into distributed systems, AI applications, and production FDE delivery.
- It **does** reference official documentation, engineering material, books, and standards to ground individual lessons.
- It **does not** claim that an external authority has validated this exact sequence as uniquely optimal, that every learner needs every lesson, or that finishing it guarantees employment.
- It is a carefully structured mentor-designed curriculum. The order should be adjusted using diagnostic evidence, demonstrated skill, project constraints, and gaps revealed during practice.
