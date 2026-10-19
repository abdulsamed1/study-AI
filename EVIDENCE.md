# EVIDENCE.md

*Seed, uploaded once. Later changes live in project memory (ChatGPT) or in saved notes (NotebookLM); the mentor restates the ledger at the start of a session for correction. Rules: `AGENTS.md` section 11.*

## Supported by evidence

*Claim — the file, commit, record, or demo that proves it.*

- (empty until the first session, from what can actually be shown)

## Needs learning

- Engineering-foundation gaps: found by the P0.2 baseline check
- LLM application design, tool calling, retrieval, agent orchestration
- Evaluation harness and regression testing
- Tracing and observability for model calls
- Security: permissions, prompt injection, threat modeling
- Deployment, rollback, runbooks
- Adoption and measuring business impact
- Reviewing AI-produced code with verified findings, independent verification, and a recorded accept, reject, or redirect decision (P1.3, P7.2–P7.4)
- Choosing what to implement manually and what to delegate, stating the reason for the choice, and then explaining, modifying, or debugging the delegated result without the agent (journey rule 11; P4.7a, P7.4, P17.2, P17.4)
- Integration failure testing against a controllable stub provider: duplicate, out-of-order, timeout-after-commit, expired credentials, schema drift (P4.7, P4.8, P8.2–P8.4)
- Transactional outbox crash test and reconciliation replay (P8.6–P8.7)
- Migration rollback rehearsal and an expand → backfill → contract change (P5.5, P9.2)
- Node.js runtime diagnosis: event-loop blocking, resource growth, bounded shutdown (P3.5–P3.6)
- An SLI computed from recorded fault runs, and a runbook that a second person can follow (P9.4, P9.7)

## Must not be claimed

- Any production deployment, user count, metric, or ownership not listed above under "Supported by evidence"
- Production experience from training artifacts: lab runs, stub-provider tests, rollback rehearsals, and simulated incidents are practice evidence and must be labeled as such
- Skill in a language or framework from agent-generated code alone; code that agents wrote counts only after an agent review record shows the learner understood and verified it
- Behavior of any repository asserted from its documentation rather than from code, tests, or a recorded run
- A book chapter, source, or roadmap read as a demonstrated capability