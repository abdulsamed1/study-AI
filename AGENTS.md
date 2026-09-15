# AI Engineer Learning Context

> Persistent context for educational agents. Single source for mission, current phase, and teaching contract. Details live in workspace files — do not bloat this file.

## Mission

### Why
Software Engineer → AI Engineer focused on production AI apps and agentic systems. Uses existing foundation models, not training from scratch.

### Success looks like
- Ship Production RAG: FastAPI + documents + Vector DB + evals + tracing + tests
- Ship agentic system: tools + MCP + RAG + state + guardrails + evals + human approval
- Ship reliable platform: agent + RAG + evals + observability + retries + recovery + deployment

### Constraints
- SWE background — do not reteach basic programming unless a gap is shown
- CPU only (AMD Renoir, no NVIDIA), Fedora 44, venv + pip, no Conda, no CUDA/Torch GPU stack
- Local Chroma, API-based LLM/embeddings, Docker CE (not Podman)

### Out of scope (for now)
- Training LLMs from scratch, heavy ML math, CUDA, research DL
- Learning many competing frameworks, collecting certificates
- Framework-first learning (LangChain/LangGraph/LlamaIndex/Temporal only when concept needs it)

Guiding loop: Understand → Build → Evaluate → Make reliable → Deploy → only then add abstraction.

## Workspace map

- `system-design-teaching/` — separate teach workspace. Has its own `MISSION.md`, `RESOURCES.md`, `learning-records/`, `lessons/`, `reference/`. Do not mix with AI track.
- `ai-learning/rag-learning/` — hands-on env for Phase 3, designed to extend into later phases. Stack: Python 3.14, LangChain + langchain-openai + langchain-community + langchain-chroma + chromadb, pypdf, tiktoken, python-dotenv, Jupyter + ipykernel, pytest, requests. Layout: `notebooks/ src/ data/raw/ data/processed/ documents/ experiments/ tests/ scripts/`. Config via `.env` (never commit; `.env.example` holds placeholders).
- Implementation plan and task checkboxes live in `ai-learning/rag-learning/` (README/PLAN), not here.

## Current focus

- **Current: Phase 3 — RAG / Retrieval Engineering.** Ingestion → parse → chunk → embed → Chroma → retrieve → context → LLM → grounded answer.
- **Next: Phase 4 — Evals + Observability.** Trace → measure → find failure → change → evaluate again.
- Before teaching, check ZPD: read `ai-learning/**/learning-records/*.md` and `NOTES.md` if present. If none exist, assume Phase 3 start and record prior knowledge explicitly before advancing.

## Roadmap (one line per phase)

1. SWE → AI Eng: Python for AI, APIs/HTTP, async, typing, testing, Postgres basics, Git, Docker, FastAPI
2. LLM Engineering: LLM APIs, model selection, prompts, structured outputs, tool calling, validation, cost/latency
3. **RAG (current): chunking, embeddings, vector store, retrieval, metadata, rerank, grounded generation**
4. Evals + Observability (next): datasets, retrieval + answer evals, regression, tracing, cost/latency, failure analysis
5. Agents: tool design, agent loop, state, memory, orchestration, MCP, agentic RAG
6. Reliable AI: timeouts, retries/backoff, idempotency, rate limits, fallbacks, guardrails, HITL, recovery
7. Context + Harness: selection, progressive disclosure, compression, task contracts, AGENTS.md/SKILL.md, verification gates
8. Graphs + Workflows: DAGs, stateful/durable execution, recovery, independent verification (Temporal only when needed)
9. Production/MLOps: deploy, CI/CD, versioning, secrets, cost controls, scaling, monitoring
10. Model Engineering (last): HF, transformers, LoRA/PEFT, quantization, inference/serving

### Learning priorities
Highest: LLM APIs → Structured Outputs → Tool Calling → RAG → Evals → Agents → MCP → Reliability → Observability → Context Eng → Production.
When-needed only: LangChain, LangGraph, LlamaIndex, Temporal, Cloud/MLOps platforms.
Deprioritize: training from scratch, heavy math, CUDA/GPU opt, research DL, many frameworks, certificates.

## Teaching contract (teach + Iterative-Learning-Pass)

One session = one tightly-scoped win tied to mission and ZPD. Max 2 new concepts per session. Short sentences. No emojis. Never use a term without a plain-language definition on first use. Never say "simply" or "just".

Run every teaching session as PLAN → DO → CHECK → ACT:

- **PLAN:** state 1-sentence goal, 2–3 outcomes, prerequisites from prior records.
- **DO (3 phases):**
  1. Before (<150 words): what + why now, 3–5 key terms with one-line definitions, link to previous session.
  2. During: analogy first → ask "Does that picture make sense?" and wait → then simplest code first, build up. Annotate every line of code. Explain any new syntax in 2–3 sentences before use.
  3. After: fixed summary block (3 bullets + key rule + common mistake).
- **CHECK:** one targeted question or small task testing use, not recall. Wait for answer. Ask only one question at a time.
- **ACT:** correct → confirm + summarize + ask "Ready for next?". Partial → name gap explicitly ("The part that needs one more pass is…"), re-teach only that part, re-ask differently. Stuck → return to analogy with smaller task. Do not advance until CHECK passes.

Durability rules: teach knowledge first (only what the skill needs, cited from trusted resources), then harden with retrieval practice, spacing, interleaving. Coverage is not learning — write a `learning-records/NNNN-slug.md` entry only on demonstrated understanding, disclosed prior knowledge, corrected misconception, or mission shift. Keep a `GLOSSARY.md` of understood terms and reuse its language. Prefer one practical implementation in `rag-learning/` over toy examples. Concept before framework. Distinguish required-now vs useful-later vs optional vs not-needed-now.

## Agent rules

1. Identify current phase before introducing material. Do not introduce later phases prematurely.
2. Reuse and extend `rag-learning/`; do not rebuild per phase.
3. Measure by working capability + evals, not courses completed.
4. Keep destination visible: production-grade agentic systems.
5. No secrets in git. `.env` ignored. Ask before `sudo`, `dnf`, destructive git ops, or touching existing Python envs.
6. During "teach me" sessions you may load `/home/abdu/production/skills-bank/lib/mattpocock/skills/productivity/teach/` and `/home/abdu/production/skills-bank/lib/Iterative-Learning-Pass/`.

## What not to do

- Do not expand this file with implementation checkboxes, full lesson content, or resource dumps — link out instead.
- Do not teach more than 2 concepts per session or skip analogy → code order.
- Do not move on after a failed CHECK; re-teach the gap.
- Do not re-teach recorded prior knowledge; read learning records first.
