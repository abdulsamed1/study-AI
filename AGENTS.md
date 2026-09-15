# AI Engineer Learning Context

> **Purpose for educational agents:** This file is not only an implementation plan for a RAG environment. It is also the persistent learning context for the user's transition from **Software Engineer → AI Engineer** over the coming months. When teaching, reviewing progress, or choosing what to learn next, use this roadmap and its priorities as the user's intended direction.

## Long-term objective

The user is a **Software Engineer** who wants to become an **AI Engineer focused on production AI applications and agentic systems**.

The objective is **not** to become an ML researcher or to start with training models from scratch. The learning path should prioritize software/system engineering around existing foundation models:

- LLM application engineering
- RAG and retrieval systems
- Evaluation and observability
- Tool calling and agents
- MCP and external-system integration
- Reliability and recovery
- Context engineering
- Harness engineering and reusable skills
- Workflow orchestration and durable execution
- Production AI / MLOps concepts
- Model engineering later, when it becomes useful

The guiding principle is:

```text
Understand the concept
        ↓
Build it
        ↓
Evaluate it
        ↓
Make it reliable
        ↓
Deploy it
        ↓
Only then add another abstraction/framework
```

Avoid turning the roadmap into a collection of courses, certificates, or frameworks without implementation.

---

## The 10-phase roadmap

### Phase 1 — Software Engineering → AI Engineering
**Goal:** Transfer existing software-engineering skills into the AI stack.

Focus:
- Python for AI applications
- APIs and HTTP
- async programming
- typing
- testing
- PostgreSQL / data basics
- Git
- Docker
- FastAPI

**Do not restart software engineering from zero.**

---

### Phase 2 — LLM Engineering
**Goal:** Treat an LLM as a software component rather than a chatbot.

Focus:
- LLM APIs
- model selection
- prompts/instructions
- structured outputs
- function/tool calling
- API integration
- validation
- basic cost and latency awareness

Target architecture:

```text
Application
    ↓
LLM API
    ↓
Structured result
    ↓
Validation
    ↓
Application logic / tool
```

---

### Phase 3 — RAG / Retrieval Engineering
**Current practical focus of this repository.**

Focus:
- document ingestion
- parsing
- chunking
- embeddings
- vector stores
- retrieval
- metadata
- reranking
- grounded generation
- retrieval quality

Target architecture:

```text
Documents
    ↓
Parse
    ↓
Chunk
    ↓
Embed
    ↓
Vector Store
    ↓
Retrieve
    ↓
Context
    ↓
LLM
    ↓
Grounded Answer
```

This repository exists primarily to support this phase.

---

### Phase 4 — Evals + Observability
**Goal:** Stop judging AI systems only by whether an answer "looks good."

Focus:
- evaluation datasets
- test cases
- retrieval evaluation
- answer-quality evaluation
- regression testing
- tracing
- latency
- cost
- failure analysis

Target loop:

```text
AI System
    ↓
Trace / Evaluate
    ↓
Measure
    ↓
Find failure
    ↓
Change system
    ↓
Evaluate again
```

---

### Phase 5 — Agent Engineering
**Goal:** Move from request/response applications to systems that can use tools and execute multi-step tasks.

Focus:
- tool calling
- tool design
- agents
- agent loop
- state
- memory concepts
- orchestration
- MCP
- agentic RAG

Target architecture:

```text
User
 ↓
Agent
 ├── RAG Tool
 ├── Search/API Tool
 ├── Database Tool
 └── Other approved Tools
 ↓
Verification
 ↓
Result
```

---

### Phase 6 — Reliable AI Systems
**Goal:** Make non-deterministic AI components operate safely inside production software.

Focus:
- timeouts
- retries
- backoff
- idempotency
- rate limits
- fallbacks
- validation
- guardrails
- human-in-the-loop
- safe recovery
- observability

Core principle:

```text
Do not trust the model alone.
Design the surrounding system to detect and recover from failure.
```

---

### Phase 7 — Context + Harness Engineering
**Goal:** Engineer the environment in which an agent operates.

Focus:
- context engineering
- context selection
- progressive disclosure
- context compression
- task contracts
- AGENTS.md / instruction files
- reusable Skills / SKILL.md
- permissioned tools
- verification gates
- feedback loops
- evidence-based completion

Target mental model:

```text
Task Contract
     ↓
Context
     ↓
Tools + Permissions
     ↓
Agent
     ↓
Verification
     ↓
Recovery / Feedback
```

This phase is intentionally later than basic prompting and RAG.

---

### Phase 8 — Graphs + Workflow Orchestration
**Goal:** Handle complex multi-step and long-running workflows.

Focus:
- graph-based workflows
- DAGs
- stateful workflows
- orchestration
- durable execution
- recovery across workflow steps
- independent verification

Frameworks such as Temporal should be learned when the underlying workflow problem is understood, not as an isolated framework-first exercise.

---

### Phase 9 — Production AI / MLOps
**Goal:** Operate AI systems as production services.

Focus:
- deployment
- CI/CD
- observability
- model/API versioning
- secrets/configuration
- cost controls
- scaling
- monitoring
- production incident thinking
- MLOps platforms when they solve an actual deployment/operations problem

The user does **not** need to learn every cloud/MLOps platform. Learn the concepts first, then the platform relevant to the target jobs/projects.

---

### Phase 10 — Model Engineering
**Goal:** Understand and modify models when application-level engineering is no longer sufficient.

Focus later:
- Hugging Face ecosystem
- transformer fundamentals
- fine-tuning
- LoRA / PEFT
- quantization
- inference
- model serving
- performance optimization

This phase is deliberately later. Do not derail the earlier phases by starting with heavy ML mathematics, CUDA, or training models from scratch.

---

## Learning priorities

### Highest priority

```text
LLM APIs
→ Structured Outputs
→ Tool Calling
→ RAG
→ Evals
→ Agents
→ MCP
→ Reliability
→ Observability
→ Context Engineering
→ Production
```

### Learn only when needed

```text
LangChain
LangGraph
LlamaIndex
Temporal
Cloud AI platforms
MLOps platforms
```

Framework knowledge must follow the underlying engineering concept.

### Deprioritize initially

```text
Training LLMs from scratch
Heavy ML mathematics
CUDA
GPU optimization
Research-level deep learning
Learning many competing agent frameworks
Collecting certificates
```

---

## Portfolio strategy

The roadmap should produce **three substantial portfolio systems**, not many disconnected tutorials.

### Project 1 — Production RAG
Should eventually demonstrate:

```text
FastAPI
+
Documents
+
RAG
+
Vector DB
+
Evaluation
+
Tracing
+
Tests
```

### Project 2 — Agentic System

```text
Agent
+
Tools
+
MCP
+
RAG
+
State
+
Guardrails
+
Evaluation
+
Human approval where appropriate
```

### Project 3 — Reliable AI Platform

```text
Agent
+
RAG
+
Evals
+
Observability
+
Retries
+
Recovery
+
Context management
+
Workflow orchestration
+
Deployment
```

The projects should evolve across phases instead of being rebuilt from scratch for every phase.

---

## Role of the current RAG repository

`~/ai-learning/rag-learning` is the **hands-on environment for Phase 3**, but it should be designed so later phases can extend it.

The repository should therefore favor:

- clear separation between notebooks and reusable source code
- tests
- experiments
- data/document separation
- configuration through environment variables
- local Chroma for learning
- API-based LLM/embeddings
- no CUDA/PyTorch GPU dependency
- a stack that can later grow toward tools, agents, evaluation, and production

The current environment is a **learning foundation**, not the final architecture.

---

## Educational-agent behavior

When acting as the user's educational agent:

1. Always identify the current roadmap phase before introducing new material.
2. Teach the concept before introducing a framework.
3. Prefer one practical implementation over several toy examples.
4. Reuse and extend the existing project whenever possible.
5. Do not introduce advanced phases prematurely.
6. Explicitly distinguish:
   - required for the current phase
   - useful later
   - optional
   - not needed now
7. Use the user's Software Engineering background as the starting point; do not reteach basic programming unless a gap is demonstrated.
8. When the user asks about a new technology, first determine which roadmap phase it belongs to and whether it is actually needed.
9. Measure progress by demonstrated capability and working projects, not by number of courses completed.
10. Keep the long-term destination visible: **production-grade AI systems and agentic applications**.
11. During "teach me" sessions, you are allowed to load the skill at `/home/abdu/production/skills-bank/lib/mattpocock/skills/productivity/teach/`.
12. During "teach me" sessions, you are allowed to load the skill at `/home/abdu/production/skills-bank/lib/Iterative-Learning-Pass/`.

---

# rag-learning Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** تجهيز بيئة RAG عملية لمهندس برمجيات ينتقل إلى AI Engineering في `~/ai-learning/rag-learning` باستخدام venv + pip وStack واحد، مع إبقاء البيئة قابلة للتوسع للمراحل اللاحقة من roadmap.

**Architecture:** مجلد مشروع معزول مع `.venv` خاصة، Chroma محلي بدون سيرفرات خارجية، LLM/Embeddings عبر API (بدون Torch/CUDA)، وJupyter kernel خاص بالمشروع.

**Tech Stack:** Python 3.14 (نظام Fedora 44)، pip 26، LangChain + langchain-openai + langchain-chroma + chromadb، pypdf، tiktoken، python-dotenv، Jupyter + ipykernel، pytest، Docker (مطلوب بدل Podman).

**Spec:** بيئة `rag-learning` كمرحلة عملية ضمن roadmap من 10 مراحل للانتقال من Software Engineer إلى AI Engineer؛ بدون Conda، وبدون CUDA/PyTorch GPU stack، مع هيكل notebooks/src/data/documents/experiments/tests/scripts.

## Global Constraints

- OS: Fedora Linux 44 KDE Plasma — استخدم `dnf` فقط عند الضرورة، ولا تثبت حزم Arch/Debian.
- لا Conda/Miniconda — استخدم `python3 -m venv .venv` + `pip` فقط.
- لا `sudo` إلا عند الضرورة، ولا تحذف/تعدل بيئات Python موجودة أو ملفات شخصية.
- لا NVIDIA GPU (AMD Renoir Vega) — CPU فقط، لا تثبت CUDA أو PyTorch GPU stack.
- Docker مطلوب — ثبّت Docker CE الرسمي (انظر الأوامر أدناه)، ولا تعتمد على Podman.
- لا Secrets في Git — `.env` في `.gitignore`، و`.env.example` placeholders فقط.
- اختر الأبسط والأكثر استقرارًا للتعلم واشرح الاختيار.

---

### Task 1: فحص النظام (تم)

**Files:**
- Modify: لا شيء (قراءة فقط)

**Interfaces:**
- Consumes: لا شيء
- Produces: نتائج الفحص (Fedora 44، Python 3.14.7، Git 2.55، Docker، gcc 16.2.1، AMD GPU بدون NVIDIA)

- [x] **Step 1: فحص OS وDesktop**

Run: `cat /etc/os-release; plasmashell --version; uname -r`
Expected: Fedora 44 KDE Plasma 6.7.5 — تم.

- [x] **Step 2: فحص Python وpip وvenv**

Run: `python3 --version; python3 -m pip --version; ls /usr/bin/python*`
Expected: Python 3.14.7 + pip 26.0.1 + venv متاح — تم. لا يوجد python3.12/3.13 بديل.

- [x] **Step 3: فحص Git/containers/devtools/GPU**

Run: `git --version; docker --version; gcc --version; lspci | grep -i vga`
Expected: Git موجود، Docker مثبت ويعمل، gcc/make موجودة، AMD Renoir ولا NVIDIA — تم.

### Task 2: هيكل المشروع + Git + ملفات الأساس

**Files:**
- Create: `~/ai-learning/rag-learning/{notebooks,src,data/raw,data/processed,documents,experiments,tests,scripts}/.gitkeep`
- Create: `~/ai-learning/rag-learning/.gitignore`
- Create: `~/ai-learning/rag-learning/.env.example`
- Create: `~/ai-learning/rag-learning/requirements.txt`
- Create: `~/ai-learning/rag-learning/README.md`

**Interfaces:**
- Consumes: لا شيء
- Produces: هيكل مجلدات + repo جاهز للمهام التالية

- [ ] **Step 1: إنشاء المجلدات**

```bash
mkdir -p ~/ai-learning/rag-learning/{notebooks,src,data/raw,data/processed,documents,experiments,tests,scripts}
```

- [ ] **Step 2: كتابة .gitignore**

```gitignore
.venv/
.env
__pycache__/
*.py[cod]
.pytest_cache/
.ipynb_checkpoints/
*.ipynb_checkpoints
.DS_Store
Thumbs.db
```

- [ ] **Step 3: كتابة .env.example**

```
OPENAI_API_KEY=
# ANTHROPIC_API_KEY= (اختياري لاحقًا)
# LANGCHAIN_TRACING_V2=false
```

- [ ] **Step 4: كتابة requirements.txt (Stack واحد: LangChain + Chroma)**

```
langchain
langchain-openai
langchain-community
langchain-chroma
chromadb
pypdf
tiktoken
python-dotenv
jupyter
ipykernel
requests
pytest
```

سبب الاختيار: LangChain يغطي أهدافك المستقبلية (RAG + Tool Calling + Agents + FastAPI) ومجتمعه وشروحاته أكبر من LlamaIndex، وChroma يعمل محليًا بدون سيرفر.

- [ ] **Step 5: git init + commit أول**

```bash
git init ~/ai-learning/rag-learning
git -C ~/ai-learning/rag-learning add -A
git -C ~/ai-learning/rag-learning commit -m "chore: scaffold rag-learning env"
```

### Task 3: venv + تثبيت + Jupyter kernel

**Files:**
- Create: `~/ai-learning/rag-learning/.venv/` (via venv)
- Test: `~/ai-learning/rag-learning/tests/test_smoke.py`

**Interfaces:**
- Consumes: requirements.txt من Task 2
- Produces: `.venv` مفعّلة + kernel باسم `rag-learning`

- [ ] **Step 1: إنشاء venv وتحديث pip**

```bash
python3 -m venv ~/ai-learning/rag-learning/.venv
~/ai-learning/rag-learning/.venv/bin/pip install --upgrade pip
```

- [ ] **Step 2: تثبيت المتطلبات**

```bash
~/ai-learning/rag-learning/.venv/bin/pip install -r ~/ai-learning/rag-learning/requirements.txt
```

ملاحظة Python 3.14: إذا فشلت حزمة native (chromadb/tokenizers) لعدم وجود wheel، ثبّت `python3-devel` عبر `sudo dnf install -y python3-devel` ثم أعد المحاولة — لا تثبت CUDA/torch.

- [ ] **Step 3: تسجيل Jupyter kernel**

```bash
~/ai-learning/rag-learning/.venv/bin/python -m ipykernel install --user --name=rag-learning --display-name="rag-learning (.venv)"
```

- [ ] **Step 4: اختبار استيراد**

```bash
~/ai-learning/rag-learning/.venv/bin/python -c "import langchain, langchain_openai, chromadb, pypdf, tiktoken, dotenv, jupyter, pytest; print('imports ok')"
```

- [ ] **Step 5: Commit**

```bash
git -C ~/ai-learning/rag-learning add requirements.txt
git -C ~/ai-learning/rag-learning commit -m "chore: add venv-tested requirements" || true
```
