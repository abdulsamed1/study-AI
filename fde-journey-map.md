# FDE Journey Map

*Revised 2026-10-09. This is the ACTIVE journey for the mission in `MISSION.md`. It says WHAT to teach and what proves it. How to teach, assess, and keep state: `AGENTS.md`. Formats and procedures: `TEACHING-PROTOCOLS.md`.*
*The first lesson is L0.1, after the first-session questions in `AGENTS.md` section 6. `production-performance-incident-study-map.md` and `estaie-study-map.md` are supporting branches: open them only where this map names them or the user asks.*

## Legend

- **P0** must-have for the mission · **P1** important · **P2** useful · **P3** awareness only.
- **[T=n]** estimated lessons of 45-60 minutes, each split into parts (`TEACHING-PROTOCOLS.md` P§3).
- **[S#]** entries in the source register below. **VERIFY**: open and re-check before teaching. **Evidence**: where the user's own work can anchor the lesson. **NO-EVIDENCE**: the user has nothing to show yet; the lesson ends in a small build.
- Branch IDs: the lesson number (`L3.2`); phase gates `FDE-A` … `FDE-E`.

## The tree

```
LEVEL 0: The FDE standard and the delivery loop                       P0 [T=3]
|- L0.1 What an FDE owns: the role standard, the delivery loop, what counts as proof
|        Evidence: Eagles and Opran integrations as adjacent, non-AI evidence (VERIFY what is in production)  [S1,S2]
|- L0.2 Use-case selection and the autonomy ladder: deterministic code, workflow, agent;
|        when the right answer is "do not use AI"                                                            [S3,S12]
|- L0.3 Discover: problem brief, workflow, baseline, success metric. NO-EVIDENCE: write one brief   [S1,S12]
v
LEVEL 1: Model API engineering                                        P0 [T=4]
|- L1.1 Request anatomy: messages, system prompt, tokens, stop reasons, context window     VERIFY      [S4]
|- L1.2 Structured outputs and schema validation; what to do with invalid output           VERIFY      [S4]
|- L1.3 The tool-calling contract: definition, call, result, error result                  VERIFY      [S4,S7]
|- L1.4 Cost, latency, rate limits, retries as a budget; bridge to PERF-L9
|        Evidence: skills-bank LLM calls and AegisFlow Whisper fallback (from the estaie map; VERIFY)    [S4,S11]
|- L1.5 Model versions and behavior change: pin, re-run the evaluation set on every change              [S4,S9]
v
LEVEL 2: Context, retrieval, memory                                   P0 [T=4]
|- L2.1 Context engineering: finite attention budget, smallest high-signal set, just-in-time retrieval   [S5]
|- L2.2 RAG pipeline: ingest, chunk, embed, store, retrieve. NO-EVIDENCE. Source gap: choose one primary RAG source
|- L2.3 Retrieval quality: hybrid search, reranking, recall at k, typical failures. Source gap as above
|- L2.4 State and memory: session vs durable, compaction, notes outside the window, sub-agent handoff     [S5,S8]
v
LEVEL 3: Workflows, agents, tools                                     P0 [T=5]
|- L3.1 The workflow patterns: chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer  [S3]
|- L3.2 The agent loop: termination, budgets, error recovery, checkpoints, long-running harnesses            [S3,S13]
|- L3.3 Tool design for agents: few, clear, non-overlapping tools; errors the model can act on               [S7]
|- L3.4 MCP: what it standardizes, trust and auth, efficiency of tool calls            VERIFY            [S6,S14]
|- L3.5 Permission gateway and human approval gates (shared with L5)
|- L3.6 Multi-agent systems: when the cost is justified                                  P1                 [S8]
v
LEVEL 4: Evaluation and observability                                 P0 [T=4]
|- L4.1 Evaluation sets built from real failures, with edge and adversarial cases                         [S15]
|- L4.2 Graders: code-based, model-based and their pitfalls, human spot checks                            [S15]
|- L4.3 Statistics for evaluations: sample size, run-to-run variance, when a difference is real. Source gap
|- L4.4 Regression gates: before/after on every change (model, prompt, context, retry policy)
|- L4.5 Tracing: per-call fields, correlation ids, replay                                                 [S8,S9]
v
LEVEL 5: Security and governance                                      P0 [T=4]
|- L5.1 Threat modeling: assets, trust boundaries, "what can the system do if the model is wrong"
|- L5.2 Prompt injection, direct and indirect; why there is no parameterized-query equivalent             [S16]
|- L5.3 OWASP LLM Top 10 2026 as a checklist; LLM as component vs as actor; the Agentic Top 10           [S16,S17]
|- L5.4 Least privilege, secrets, tenant isolation, data leakage
|        Evidence: Opran HMAC and secrets handling, Eagles AES-256-GCM fields (from the estaie map; VERIFY)  [S16]
|- L5.5 Audit logs, kill switch, incident response
v
LEVEL 6: Reliability and delivery                                     P1 [T=5]
|- L6.1 Idempotency, retries, and side effects of tool calls
|        Evidence: estaie L0.1 lesson on Eagles and Opran; PERF-L4                                          [S10,S11]
|- L6.2 Timeouts, circuit breakers, degradation order (smaller model, deterministic path, human review); PERF-L5, PERF-L9
|- L6.3 Deployment: containers, configuration, secrets, CI/CD. Evidence: Eagles Docker Compose (VERIFY)    [S11]
|- L6.4 Progressive rollout: prototype, pilot, shadow, limited production, rollback
|- L6.5 Durable execution concepts (workflow engines), concepts only                      P2
v
LEVEL 7: Adoption, impact, handover                                   P1 [T=3]
|- L7.1 Workflow integration and change management. NO-EVIDENCE: run a pilot with one to three real people
|- L7.2 Measuring impact: baseline, before/after, labeled real or simulated
|- L7.3 Runbook, ADRs, ownership, escalation, known limits
v
LEVEL 8: Capstone and readiness proof                                 P0 [open-ended]
|- L8.1 Choose the capstone: one real, narrow workflow, accessible data, bounded risk, measurable baseline
|- L8.2 Build in slices: each slice uses lessons from Levels 1-7 just in time
|- L8.3 The evidence pack: ADRs, threat model, evaluation report, runbook, short case deck
|- L8.4 Scenario drills in English against the role requirements                                       [S2]
```

## Phase gates

Phases keep the user's plan. A gate is passed by artifacts the user can defend, never by lessons finished (`AGENTS.md` section 12).

| Gate | Passed when | Levels |
|---|---|---|
| FDE-A | Given a failing system, I explain how it works and diagnose a likely mechanism from evidence. Foundations are studied just in time from the project books and the performance map, only for gaps a diagnostic finds. | supporting branch |
| FDE-B | A written design decision for the capstone compares at least three options including a non-AI one, names the autonomy level and where the design fails. | 0-3 |
| FDE-C | An evaluation set with edge and adversarial cases; one change measured before and after; one failure traced end to end; permission and injection cases tested. | 4-6 |
| FDE-D | A repository with code, tests, measurements, documentation, and an honest list of what is proven. | 6-8 |
| FDE-E | I explain what I built, why, what would make the choice wrong, and what I have not proven. | 8 |

Adoption and impact need real users: with none, run a small pilot or label the result "simulated" (`AGENTS.md` section 12).

## Source register

The canonical source register is [`RESOURCES.md`](RESOURCES.md). Lesson tags
refer to its IDs. Only entries marked **Verified** may support teaching;
References to verify and Coverage gaps are not evidence. Re-check current API,
product, model, and security sources before the lesson and record the date and
exact section used.

## Casebook concepts by level

`casebook/<slug>.md`, researched per `TEACHING-PROTOCOLS.md` P§2.

| Levels | Concepts |
|---|---|
| 0 | `use-case-selection-failure` |
| 1-2 | `context-overflow`, `retrieval-failure` |
| 3 | `tool-misuse`, `runaway-agent-loop` |
| 4 | `silent-quality-regression`, `evaluation-gaps` |
| 5 | `prompt-injection`, `permission-overreach` |
| 6-7 | `retry-storm`, `pilot-to-production-gap`, `adoption-failure` |
