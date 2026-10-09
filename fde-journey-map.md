# FDE Journey Map — Personal Study Plan

*Revised 2026-10-09. This file says WHAT to learn and what proves it. `AGENTS.md` says how to teach and assess; `MISSION.md` says why; `TEACHING-PROTOCOLS.md` holds formats. Nothing here overrides them. Branch IDs: `FDE-A` … `FDE-E`, plus a topic suffix (for example `FDE-B-RAG`).*

## What makes this a plan and not a reading list

1. **Gates are artifacts, not completion.** A phase passes when its artifacts exist and the user can defend them (`AGENTS.md` section 12). Finishing a chapter or a lesson never passes a gate.
2. **The capstone starts early.** Discover and Select Use Case are done during Phase B. Phases B and C then happen inside the capstone, just in time. Otherwise the evidence arrives last.
3. **Foundations are just in time.** Phase A begins with a diagnostic; only the gaps it finds are studied. Books are opened when the capstone needs a decision.
4. **Honest scope of proof.** Adoption and Business Impact need real users. With none, run a pilot with one to three people or label the result "simulated". A simulation is never presented as a measured outcome.

Related journey: `production-performance-incident-study-map.md` is the diagnostic branch for Phase A (L0-L8) and the reliability branch for Phase C (L9). An interview journey with a deadline takes priority (`AGENTS.md` section 5).

## Phases

### Phase A — Engineering foundations

Diagnostic first: two or three scenarios over API design, data stores and consistency, distributed-systems failure, testing, cloud deployment, and security boundaries (authentication, authorization, secrets, tenant isolation). Study only the gaps found.

- Sources: the project's architecture, microservices, distributed-systems, scalable-systems, and data-intensive-applications books; the performance map `PERF-L0`..`PERF-L8`. Choose chapters from the table of contents in-session; do not guess chapter numbers.
- **Gate FDE-A:** given a failing system description, I explain how it works and diagnose a likely mechanism from evidence, and I have a record for each gap closed.

### Phase B — AI systems engineering (starts with capstone problem selection)

- `FDE-B-API`: model API integration, structured outputs with schema validation, tool calling, token budgeting.
- `FDE-B-RAG`: ingestion, chunking, embeddings, vector stores, retrieval quality, reranking.
- `FDE-B-CTX`: context assembly, progressive disclosure, session versus durable memory, state.
- `FDE-B-AGENT`: agent loops, orchestration, tool contracts, MCP, permission boundaries.
- `FDE-B-AUTONOMY`: deterministic code, workflow, assisted flow, or agent; always the minimum autonomy that works.
- Capstone work: stages 1-2 (Discover, Select Use Case) and a first design (stage 3).
- **Gate FDE-B:** a written design decision for the capstone comparing at least three options (one non-AI), naming where the chosen design fails and the autonomy level with its reason.

### Phase C — Production reliability

- `FDE-C-EVAL`: evaluation sets, acceptance thresholds, regression tests, basic statistics (sample size, run-to-run variance), adversarial cases.
- `FDE-C-TRACE`: tracing and observability for model and tool calls.
- `FDE-C-SEC`: threat modeling, least privilege, permission gateways, prompt injection, the OWASP LLM list (fetch the official list before citing).
- `FDE-C-RES`: timeouts, retry budgets, idempotency, rollback, cost and latency control (`PERF-L9`).
- Capstone work: stages 4-5 (Evaluation, Security).
- **Gate FDE-C:** an evaluation set with edge and adversarial cases; one change measured before and after with it; one failure traced end to end; permission boundaries and injection cases tested.

### Phase D — Capstone delivery

- Stages 6-9: Deploy, Adoption, Business Impact, Handover.
- Scope rule: one real, narrow workflow with a named user, accessible data, bounded risk from a wrong action, and a measurable before/after. Wide projects fail the gate by never finishing.
- **Gate FDE-D:** a repository with code, tests, measurements, documentation, and an honest list of what is proven and what is not.

### Phase E — Proof of readiness

- Convert the capstone into Architecture Decision Records, a Threat Model, an Evaluation Report, a Runbook, and a short case presentation (problem, impact, constraints).
- Drill new enterprise scenarios aloud, in English, with the interview structure in the performance map and the ten questions in `AGENTS.md` section 8.
- **Gate FDE-E:** I explain what I built, why, what would make the choice wrong, and what I have not proven.

## Artifact map for the nine delivery stages

| Stage | Artifact that proves it | Question it must answer |
|---|---|---|
| 1 Discover | Problem brief: users, workflow, constraints, outcome | What costs time, money, or risk today, and for whom? |
| 2 Select Use Case | Option comparison including a "do not use AI" option | Why this level of autonomy? |
| 3 Design | Architecture, permission and state design, ADRs | What can the system do, and what can it reach? |
| 4 Evaluation | Evaluation set, thresholds, regression results | How do we know it works, and notice when it stops? |
| 5 Security | Threat model, permission tests, injection tests | If the model is wrong or context is hostile, what can happen? |
| 6 Deploy | Rollout plan, monitoring, rollback | How do we ship gradually and undo it? |
| 7 Adoption | User feedback log, workflow integration notes | Do real people use it, and why or why not? |
| 8 Business Impact | Before/after measurement, labeled real or simulated | What changed, in numbers, and how sure are we? |
| 9 Handover | Runbook, ownership, escalation, limits | Can someone else operate it without me? |

## Casebook concepts per phase

Research with `TEACHING-PROTOCOLS.md` P§2; known primary-source gaps are in P§7.

| Phase | Concepts (`casebook/<slug>.md`) |
|---|---|
| A | `symptom-vs-mechanism`, `retry-storm`, `pool-exhaustion` |
| B | `retrieval-failure`, `context-overflow`, `tool-misuse` |
| C | `silent-quality-regression`, `prompt-injection`, `permission-overreach`, `evaluation-gaps` |
| D | `pilot-to-production-gap`, `adoption-failure` |

## Sources

- In the project: the books above and the performance map.
- To add after verification, each recorded in `RESOURCES.md`: current Anthropic documentation (API, tool use, evaluation); Anthropic Engineering posts on agents and context engineering; the official OWASP LLM project; real postmortems per casebook concept. The sources already in NotebookLM are scenario input.
