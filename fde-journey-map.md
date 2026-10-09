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

Status as of 2026-10-09. "Read" means opened and read in full for this revision. "Found" means a search returned the title or page; open it before teaching from it.

| ID | Source | Status |
|---|---|---|
| S1 | Anthropic, "Claude Frontier Academy" (2026-10-02), anthropic.com/news/claude-frontier-academy | Read. Nomination by employer; named project; scenario-based assessment |
| S2 | Deloitte, "Forward Deployed Engineer, Frontier GenAI", job 350555, apply.deloitte.com | Read. Requires 3+ years software or data engineering, 1+ year building GenAI in client or production settings, 1+ year on a frontier platform (Claude API, tool use, Claude Code, Gemini API, OpenAI Agents SDK named); travel about 50%; US locations; limited sponsorship; recruiting ends 2026-10-30 |
| S3 | Anthropic Engineering, "Building effective agents", anthropic.com/engineering/building-effective-agents | Found. Workflows vs agents; the five patterns |
| S4 | Claude API documentation (current messages, tool use, structured output, rate limits pages) | VERIFY at lesson time; state the date |
| S5 | Anthropic Engineering, "Effective context engineering for AI agents", anthropic.com/engineering/effective-context-engineering-for-ai-agents | Found. A secondary page dates it 2025-09-29 |
| S6 | Model Context Protocol specification, modelcontextprotocol.io | VERIFY. Open the current spec |
| S7 | Anthropic Engineering, "Writing tools for AI agents – with AI agents" | Found only as a reference inside S5; open before teaching |
| S8 | Anthropic Engineering, "How we built our multi-agent research system" | Found as a title in a secondary list; open |
| S9 | Anthropic Engineering, "A postmortem of three recent issues" (Sept 2025) | Unchecked; open |
| S10 | Google Cloud incident report 2025-06-12 (Service Control), status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW | Unchecked; open |
| S11 | Project books: *Fundamentals of Software Architecture*, *Building Microservices*, *Designing Data-Intensive Applications*, *Understanding Distributed Systems*, *Foundations of Scalable Systems*, *Designing Distributed Systems* | Tier 1 for what they cover; cite the chapter after reading the table of contents |
| S12 | Anthropic, "Building Effective AI Agents" enterprise guide, claude.com/resources/guides/building-effective-ai-agents | Found. Single vs multi-agent vs workflow decision framework |
| S13 | Anthropic Engineering, "Effective harnesses for long-running agents" | Found as a title in a secondary list; open |
| S14 | Anthropic Engineering, "Code execution with MCP: building more efficient AI agents" | Found as a title in a secondary list; open |
| S15 | Anthropic Engineering, "Demystifying evals for AI agents" | Found as a title in a secondary list; open |
| S16 | OWASP GenAI Security Project, "OWASP GenAI LLM Top 10 2026" (v1.0, 2026-08-03), genai.owasp.org/resource/owasp-genai-llm-top-10-2026/ | Found; official page not opened. Open it before citing the ranking |
| S17 | OWASP Top 10 for Agentic Applications (December 2025, ASI01-ASI10) | Found through a research note; open the official list |

Known gaps (add to `RESOURCES.md`): a primary RAG source; a primary statistics-for-evaluation source; a primary-source RAG failure; an agent tool-misuse incident; a vendor customer-deployment case study.

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
