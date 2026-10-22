# EVIDENCE.md

*Seed, uploaded once. Later changes arrive through the session-export block (P§6) and are merged into this file by the workspace agent. The repository is the source of truth. Rules: `AGENTS.md` section 11.*

## Supported by evidence

*Claim — the file, commit, record, or demo that proves it.*

- (empty until the first session, from what can actually be shown)

## Needs learning

- Engineering-foundation gaps: found by the P2.1 baseline check
- LLM application design, tool calling, retrieval, agent orchestration
- Evaluation harness and regression testing
- Tracing and observability for model calls
- Security: permissions, prompt injection, threat modeling
- Deployment, rollback, runbooks
- Adoption and measuring business impact
- Reviewing AI-produced code with verified findings, independent verification, and a recorded accept, reject, or redirect decision (P2.2, P7.2–P7.4)
- Choosing what to implement manually and what to delegate, stating the reason for the choice, and then explaining, modifying, or debugging the delegated result without the agent (journey rule 11; P4.7a, P7.4, P17.2, P17.4)
- Integration failure testing against a controllable stub provider: duplicate, out-of-order, timeout-after-commit, expired credentials, schema drift (P4.7b, P4.8a–P4.8b, P8.2–P8.4)
- Transactional outbox crash test and reconciliation replay (P8.6–P8.7)
- Migration rollback rehearsal and an expand → backfill → contract change (P5.5, P9.2)
- Python runtime diagnosis: event-loop blocking, resource growth, bounded shutdown (P3.5–P3.6)
- An SLI computed from recorded fault runs, and a runbook that a second person can follow (P9.4, P9.7)
- Defending opran and eagles decisions from code-verified evidence: authorship, alternatives, tradeoffs, and failure conditions (P17.4; decision defense card in `fde-journey-map.md` §3)
- Next.js server/client boundary and data flow in the existing opran website (P7.7)
- Twenty/NestJS platform literacy: what the host provides versus what the Eagles app owns (P7.8)
- Provider cost/latency levers: prompt caching (prefix ordering, breakpoints, cache-read fields), model routing, and semantic-cache trade-offs (P11.4)
- GraphRAG as a retrieval alternative and A2A agent-to-agent protocol at decision vocabulary (P12.4, P13.5)
- Voice and browser agent interfaces: modality architecture choice, latency budgets, and modality-specific failure modes (P13.7)
- LLM-judge design: direct vs pairwise scoring, calibration/agreement statistics, and known judge biases (P14.2)
- Agent-trace platform shape (trace → dataset → evaluator → CI regression gate) evaluated against the existing stack (P14.5)
- Automated black-box red-team harnesses supplementing the hand-built adversarial categories (P15.2)

## Must not be claimed

- Any production deployment, user count, metric, or ownership not listed above under "Supported by evidence"
- Production experience from training artifacts: lab runs, stub-provider tests, rollback rehearsals, and simulated incidents are practice evidence and must be labeled as such
- Skill in a language or framework from agent-generated code alone; code that agents wrote counts only after an agent review record shows the learner understood and verified it
- Platform-provided capabilities as own work: Twenty/NestJS modules, dependency injection, authentication, row-level permissions, or Cloudflare Workers/Hono/D1/KV mechanisms the owner did not design or implement
- Documented targets as measured results, including opran's ≥99.9% uptime and <1% price-variance targets and Eagles' 30-minute acknowledgement SLA and 2–4h RTO/<1h RPO targets, unless a measurement is recorded
- Behavior of any repository asserted from its documentation rather than from code, tests, or a recorded run — including opran and eagles, whose docs are as-built claims and can drift (opran `docs/ADR/adr-gap-analysis.md`; Eagles AD-15's deployed-filter trap)
- Mechanism-level knowledge of components outside the study scope (Cloudflare Workers, Hono, Zod, D1, KV, Durable Objects); describe them at the depth of the project's ADRs and no further
- A book chapter, source, or roadmap read as a demonstrated capability
- The designated AI Roadmap 2026's market statistics (LinkedIn growth percentages, fastest-growing-job ranks) or its ~25-week and 12-week duration claims as established facts or as this plan's pace
- Fine-tuning, quantization, or model-serving skills (SFT/DPO/LoRA, vLLM): excluded from scope by the 2026-10-21 designation; nothing was practiced and nothing may be claimed