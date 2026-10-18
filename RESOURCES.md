# FDE Study Resources

Updated: 2026-10-17

## How to use this file

This is the canonical source catalog for the FDE study path. Every reference
belongs in one of three sections:

1. **Verified references** — opened and checked; may support a lesson or factual
   claim.
2. **References to verify** — provided as a research lead; useful for finding
   material, but not evidence until its specific artifact is opened and checked.
3. **Coverage gaps** — a needed topic for which no adequate reference has been
   verified yet.

The AI must read this file before teaching. It must not silently ignore a
reference in the second section or treat it as verified.

This file is not a dump of names, newsletters, communities, or broad roadmap
ideas. Only concrete artifacts may enter a source section: a book, paper,
course page, blog post, job listing, official documentation, or another
specific publication with a canonical URL. User-supplied roadmaps and lists of
people or organizations are discovery leads only until they are tied to a
specific artifact and date-verified.

Books may be listed as citations even when access is paywalled; do not
reproduce copyrighted text. API, product, model, and security claims require
current official documentation or a dated primary source. Cite the exact
chapter, section, page, or heading used when available. A chapter tagged
`[TOC]` in a journey file was identified from a book's table of contents only
and has not been read by the mentor; keep the tag until the passage is checked.

Availability, bibliography, and reading are three separate states: an uploaded
book is available; its title page, author, and edition may still be unverified;
and `[TOC]` chapters have not been read. An uploaded book whose title page or
edition has not been checked is listed under **References to verify**, not
under Verified references.

Books marked **Uploaded in both study tools** are fully supplied by the user in
both NotebookLM and the ChatGPT Project. They may be used as study references
in either tool. Cite the book title, edition, author, and chapter or page; do
not reproduce the book or treat a generated summary as the source.

People, organizations, newsletters, conferences, and communities are discovery
leads only. A durable entry must identify a specific artifact with a canonical
URL, explain its relevance, and record its verification status. A person or an
organization name by itself is never a source. Roadmaps and career feeds such as
[roadmap.sh/ai-engineer](https://roadmap.sh/ai-engineer),
[FDE Academy](https://fde.academy/), and
[The Batch — AI Careers](https://www.deeplearning.ai/the-batch/tag/ai-careers)
are valid discovery inputs only when they are opened and tied to a specific
artifact used by the lesson.

## Verified references

| ID | Source | Publisher | Type | Coverage | Access | Last verified |
|---|---|---|---|---|---|---|
| S1 | [Claude Frontier Academy](https://www.anthropic.com/news/claude-frontier-academy) | Anthropic | Role standard | FDE Residency standard (announced 2026-10-02): $100M, 10,000 FDEs by end-2027, medical-model residency, simulated enterprise deployment, graded practical, badges from early 2027; re-read 2026-10-14 (eligibility and program-structure sections): targets hands-on engineers with strong fundamentals, simulated deployment covers use-case selection, security review, and handover, no technologies named | Public | 2026-10-14 |
| S2 | [Forward Deployed Engineer, Frontier GenAI](https://apply.deloitte.com/careers/JobDetail/Forward-Deployed-Engineer-Frontier-GenAI/350555) | Deloitte | Job evidence — STALE unless re-opened | Single listing; superseded by S1 as role standard | Public listing | 2026-10-09 |
| S3 | [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Anthropic Engineering | Engineering article | Workflows, agents, and composition patterns. Note page banner: tooling landscape changed since Dec 2024 — patterns stand, tooling examples need re-check | Public | 2026-10-09 |
| S4 | [Claude API documentation](https://docs.anthropic.com/en/docs) | Anthropic | Official documentation | Messages, tools, structured output, limits, and model behavior | Public; re-check per lesson | 2026-10-09 |
| S5 | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anthropic Engineering | Engineering article | Context budgets, retrieval, and just-in-time context (article 2025-09-29: smallest high-signal token set, just-in-time loading, compaction, structured note-taking, sub-agent distillation) | Public | 2026-10-09 |
| S6 | [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest) | Model Context Protocol | Specification | Tool/context interop (not safety) + authorization (OAuth 2.1, RFC9728 discovery, RFC8707 audience binding, PKCE; descriptions untrusted, consent before invoke). Pin spec date per lesson — current 2026-07-28 | Public; versioned | 2026-10-09 |
| S7 | [Writing tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Anthropic Engineering | Engineering article | Tool contracts and eval-driven iteration (article 2025-09-11): minimal toolset, namespacing, token-efficient returns, description-as-new-hire-doc | Public | 2026-10-09 |
| S8 | [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | Anthropic Engineering | Engineering article | Multi-agent decomposition and trade-offs (article 2025-06-13): parallelization cuts, 40% tool-ergonomics win, single-call 0.0–1.0 LLM judge, end-state eval, resume-from-checkpoint | Public | 2026-10-09 |
| S9 | [A postmortem of three recent issues](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues) | Anthropic Engineering | Postmortem | Reliability failures and operational learning | Public | 2026-10-09 |
| S10 | [Google Cloud Service Control incident](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW) | Google Cloud | Official incident report | Dependency failure, impact, and mitigation | Public | 2026-10-09 |
| S11 | [Building AI-powered products](https://www.oreilly.com/library/view/building-ai-powered/9781098166505/) | O'Reilly | Book | AI engineering product and production foundations | Book access may be paid | 2026-10-09 |
| S12 | [Building Effective AI Agents enterprise guide](https://claude.com/resources/guides/building-effective-ai-agents) | Anthropic | Enterprise guide | Choosing single-agent, workflow, and multi-agent designs | Public | 2026-10-09 |
| S13 | [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Anthropic Engineering | Engineering article | Checkpoints, progress, and long-running agent execution | Public | 2026-10-09 |
| S14 | [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) | Anthropic Engineering | Engineering article | Efficient tool use and MCP code execution | Public | 2026-10-09 |
| S15 | [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Anthropic Engineering | Engineering article | Evaluation design, graders, and regression practice (2026-01-09 refresh: 20–50 starter tasks from real failures, trial isolation, transcript review, eval-driven development) | Public | 2026-10-09 |
| S16 | [OWASP GenAI LLM Top 10](https://genai.owasp.org/llm-top-10/) | OWASP GenAI Security Project | Security guidance | LLM Top 10 2026 (published 2026-08-04) — always cite the edition | Public; use current edition | 2026-10-09 |
| S17 | [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/initiatives/agentic-security/) | OWASP GenAI Security Project | Security guidance | Agentic Top 10 2026 (Dec 2025, ASI01–ASI10, 100+ experts) — always cite the edition | Public; use current edition | 2026-10-09 |
| S18 | [MIT 6.824 Distributed Systems](https://pdos.csail.mit.edu/6.824/) | MIT | University course | Replication, fault tolerance, and distributed-system reasoning | Public materials | 2026-10-09 |
| S19 | *Designing Data-Intensive Applications*, 2nd Edition — Martin Kleppmann and Chris Riccomini, O'Reilly Media, Feb 2026. ISBN 978-1-098-11905-8. [Publisher page](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/). Audit note: the uploaded EPUB OPF records identifier `978-1-449-37332-0`, which is the first-edition (2017) product ISBN; the second-edition ISBN `978-1-098-11905-8` is from the publisher page | Martin Kleppmann and Chris Riccomini | Book — Uploaded in both study tools | Data systems, consistency, replication, and stream processing. Bibliography verified from epub OPF and cross-checked against publisher page (2026-10-17). Ch. 1–2 body text read (2026-10-16); remaining chapters cited in the journey are TOC-identified only | NotebookLM + ChatGPT Project | 2026-10-17 |
| S20 | *Fundamentals of Software Architecture: A Modern Engineering Approach*, 2nd Edition — Mark Richards and Neal Ford, O'Reilly Media, Mar 2025. ISBN 978-1-098-17551-1. [Publisher page](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/) | Mark Richards and Neal Ford | Book — Uploaded in both study tools | Architecture characteristics, modularity, component boundaries, fitness functions, style selection, architectural decisions, risk, and diagramming. Bibliography verified from epub OPF (2026-10-17). Ch. 4, 5, 6, 11, 19, 21, 22, 23 body text read (2026-10-16); remaining chapters cited in the journey are TOC-identified only | NotebookLM + ChatGPT Project | 2026-10-17 |
| S21 | [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | OpenAI | Official SDK documentation | Agents, tools, handoffs, guardrails, sessions, sandbox agents, MCP, human-in-the-loop, tracing (verified current 2026-10-09) | Public; re-check per lesson | 2026-10-09 |
| S22 | [OpenAI evaluations guide](https://platform.openai.com/docs/guides/evals) | OpenAI | Official documentation — DEPRECATED for procedures | Evals platform read-only 2026-10-31, shutdown 2026-11-30 (banner verified 2026-10-09); teach the Datasets/evaluation-getting-started flow instead | Public; do not use for procedures | 2026-10-09 |
| S23 | [Google Agent Development Kit](https://google.github.io/adk-docs/) | Google | Official SDK documentation | Agent workflows, tools, sessions, and deployment concepts | Public; re-check per lesson | 2026-10-09 |
| S24 | [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | NIST | Government framework | AI RMF 1.0 (Jan 2023) + GenAI Profile NIST AI 600-1 (July 2024): twelve GAI risks with Govern/Map/Measure/Manage actions — cite the profile | Public | 2026-10-09 |
| S25 | [Site Reliability Engineering book](https://sre.google/sre-book/table-of-contents/) | Google | Book | Reliability, monitoring, incident response, and operations | Public online edition | 2026-10-09 |
| S26 | *Building Microservices: Designing Fine-Grained Systems*, 2nd Edition — Sam Newman, O'Reilly Media, Aug 2021. ISBN 978-1-492-03402-5. [Publisher page](https://www.oreilly.com/library/view/building-microservices-2nd/9781492034018/) | Sam Newman | Book — Uploaded in both study tools | Service modeling, splitting the monolith, communication, workflows, deployment, testing, observability, resilience, scaling, and the evolutionary architect. Bibliography verified from epub OPF (2026-10-17); edition confirmed from epub title page (2026-10-16). Ch. 2, 3, 16 body text read (2026-10-16); remaining chapters cited in the journey are TOC-identified only | NotebookLM + ChatGPT Project | 2026-10-17 |
| S27 | *Understanding Distributed Systems: What Every Developer Should Know About Large Distributed Applications*, 2nd Edition — Roberto Vitillo, self-published, 2022. Paperback ISBN 978-1-8384302-1-4 (from external bibliographic records including Open Library and Google Books; the uploaded EPUB OPF records only a UUID `urn:uuid:d5070ed1-fad9-48cc-a871-36c1e4e3c976`). [Author page](https://understandingdistributed.systems/). [Book listing](https://vitillo.gumroad.com/l/xDBTX) | Roberto Vitillo | Book — Uploaded in both study tools | Distributed-system fundamentals, failure, consistency, and operations. Bibliography verified from epub OPF and external bibliographic records (2026-10-17). No chapters read; all citations in the journey are TOC-identified only | NotebookLM + ChatGPT Project | 2026-10-17 |
| S29 | *Designing Distributed Systems: Patterns and Paradigms for Scalable, Reliable Systems Using Kubernetes*, 2nd Edition — Brendan Burns, O'Reilly Media, Dec 2024. ISBN 978-1-098-15635-0. [Publisher page](https://www.oreilly.com/library/view/designing-distributed-systems/9781098156343/) | Brendan Burns | Book — Uploaded in both study tools | Patterns and paradigms for scalable, reliable Kubernetes systems. Bibliography verified from epub OPF (2026-10-17). No chapters read; all citations in the journey are TOC-identified only | NotebookLM + ChatGPT Project | 2026-10-17 |
| S30 | [FDE Academy](https://fde.academy/) | FDE Academy | FDE curriculum/role signal | Technical background, Python or SQL foundation, cloud exposure, AI/ML foundations, and technical communication | Public; re-check for current program details | 2026-10-09 |
| S31 | [Seven Failure Points When Engineering a Retrieval Augmented Generation System](https://arxiv.org/abs/2401.05856) | Barnett et al., Deakin University (CAIN 2024) | Peer-reviewed experience report | RAG failure taxonomy FP1–FP7 (missing content, missed rank, consolidation exclusion, extraction failure, wrong format, specificity, incompleteness); validation-in-operation, robustness evolves | Public (arXiv) | 2026-10-09 |
| S32 | EchoLeak chain: [Aim Labs disclosure](https://www.aim.security/lp/aim-labs-echoleak-blogpost) · CVE-2025-32711 · [Reddy & Gujral analysis](https://arxiv.org/abs/2509.10540) | Aim Security / Microsoft / AAAI-SS | Disclosure + CVE + peer analysis | Zero-click indirect prompt injection in M365 Copilot (CVSS 9.3): XPIA bypass, ref-style Markdown redaction bypass, image auto-fetch, Teams CSP-proxy; patched server-side May/June 2025; no in-the-wild exploitation observed | Public | 2026-10-09 |
| S33 | [REL03-BP01 Choose how to segment your workload](https://docs.aws.amazon.com/wellarchitected/2025-02-25/framework/rel_service_architecture_monolith_soa_microservice.html) | AWS Well-Architected Framework (framework snapshot 2025-02-25) | Vendor architecture guidance | Read in full 2026-10-14: choice among monolith, service-oriented, and microservice segmentation; stated trade-offs (latency, harder debugging, operational burden); modular-monolith caveat; strangler-fig step; data segmentation. Supports P7.5a, P10.4. Caveats: vendor stance favors segmentation; gives no measurable thresholds; compare with S20, S26, S38 before use; a newer framework version may exist | Public | 2026-10-14 |
| S34 | [Node.js Test CI Security Incident](https://nodejs.org/en/blog/vulnerability/march-2025-ci-incident) | Node.js Technical Steering Committee (full disclosure update 2025-04-23) | Primary incident report | Read in full 2026-10-14: Summary, Remediation, Timeline. Time-of-check/time-of-use gap between triggering CI and checkout, mutable git refs, commit-SHA validation, 24 hosts rebuilt, 140 jobs audited. Supports P7.4, P9.2. Caveats: development infrastructure, not the Node.js runtime; not a substitute for F3 | Public | 2026-10-14 |
| S35 | [Cloudflare outage on November 18, 2025](https://blog.cloudflare.com/18-november-2025-outage/) | Cloudflare (Matthew Prince; published 2025-11-18) | Primary postmortem | Read in full 2026-10-14: timeline, a permissions change altering query results, a preallocated feature limit, an unhandled error, a configuration file alternating between good and bad, initial misdiagnosis as DDoS, retry backlog on dashboard login. Supports P9.5, P9.7. Caveats: first-party account; remediation items are plans | Public | 2026-10-14 |
| S36 | [Code Orange: Fail Small — our resilience plan following recent incidents](https://blog.cloudflare.com/fail-small-resilience-plan/) | Cloudflare (Dane Knecht; published 2025-12-19) | Vendor resilience plan | Read in full 2026-10-14: controlled rollout of configuration changes, assume-failure interface contracts, break-glass access and circular dependencies. Supports P9.2, P9.5, P9.7. Caveats: a stated plan with a Q1 2026 target; completion not verified; distinguish plans from measured outcomes | Public | 2026-10-14 |
| S37 | [Can AI agents build real Stripe integrations? We built a benchmark to find out](https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations) | Stripe Engineering (Carol Liang, Kevin Ho; 2026-03-02) | Vendor benchmark report | Read in full 2026-10-14: 11 environments (backend-only, full-stack, gym), mostly deterministic graders, observed failure modes (declaring success after 400 errors on invalid test data; browser-use dead ends). Supports P4.7, P4.8, P7.4. Caveats: vendor-run, small sample, specific models and harness; does not show coding skill is obsolete or that results generalize; benchmark repository not opened | Public | 2026-10-14 |
| S39 | [NIST SP 800-228-upd1, Guidelines for API Protection for Cloud-Native Systems](https://doi.org/10.6028/NIST.SP.800-228-upd1) | NIST (Ramaswamy Chandramouli, Zack Butcher); June 2025, includes updates as of 2026-03-13 | Standards-body guideline | Sections 1–4.5 of the [PDF](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-228-upd1.pdf) read 2026-10-15: §2.2 authorization, §2.3 authentication, §2.4 resource consumption, §2.5 information leakage, §2.6 input validation, §3.1 pre-runtime controls (REC-API-1 to 8), §3.2 runtime controls (REC-API-9 to 26), §4 gateway patterns. Not read: Appendix F change log, §5, Appendices A–E. The original SP 800-228 (2025-06-27) was withdrawn 2026-03-13 and superseded in its entirety by this edition; do not cite the original. Supports P4.3, P4.4, P4.8, P9.3, P15.5. Caveats: enterprise gateway and zero-trust orientation; recommendations, not requirements for a single-service capstone; differences from the original are unread | Public | 2026-10-15 |
| S40 | [The executive's guide: How engineering teams are balancing AI and human oversight in modern code reviews](https://github.com/resources/insights/human-oversight-modern-code-review) | GitHub (Jared Bauer; 2025-07-29) | Vendor insight article | Read in full 2026-10-15: the sections on what is new (AI reviews first, needle-in-haystack detection, guarding against confirmation bias) and on what remains bedrock (small changes, tests necessary but not sufficient, human oversight). Supports P1.3, P4.7, P7.2, P7.4, P17.2. Caveats: qualitative engineer quotes, no measurement; the page says the observations are not yet universal; GitHub sells an AI review tool | Public | 2026-10-15 |
| S41 | [Antipatterns of Software Engineering with AI](https://www.principalengineer.com/p/antipatterns-of-software-engineering) | The Principal Engineer (Wille Faler; 2026-07-17) | Practitioner essay | Read in full 2026-10-15: spec-driven development as a big bang, architectural over-engineering, AI grading its own homework, comprehension debt, conclusion. Supports P1.5, P7.2, P7.3, P7.5a, P7.5b, P17.2. Caveats: one practitioner's experience; claims about model behavior are opinion, not measurement; the author notes the limits of trust shift monthly | Public | 2026-10-15 |
| S42 | [C4 model for visualising software architecture](https://c4model.com/) | Simon Brown | Architecture diagramming model | Site structure verified 2026-10-16: four hierarchical abstractions (software system, container, component, code), seven diagram types (system context, container, component, code, system landscape, dynamic, deployment), notation guidance, and a [review checklist](https://c4model.com/diagrams/checklist). CC BY 4.0 licensed. Supports P7.5b (architecture diagrams) and P10.4 (system-design communication). Caveats: a diagramming convention, not an architecture methodology; does not replace architecture-characteristic identification or trade-off analysis | Public | 2026-10-16 |

## F-series — foundational sources used by the roadmap

These are concrete artifacts used by the active journey. Re-open the exact
page used before teaching and record the subsection or version in the lesson
record. F13 and F14 are cross-check and discovery sources, not a replacement
for primary technical evidence.

| ID | Source | Publisher | Type | Coverage | Access | Last verified |
|---|---|---|---|---|---|---|
| F1 | [Pro Git, 2nd Edition — online book](https://git-scm.com/book/en/v2) | Git | Online book | Git, collaboration, history, branching, and reproducible work | Public | 2026-10-09 |
| F2 | [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) | MDN | Official guide | JavaScript language and core concepts | Public; re-check per lesson | 2026-10-09 |
| F3 | [Node.js Learn](https://nodejs.org/learn) | Node.js | Official learning documentation | Runtime, async work, testing, HTTP, diagnostics, and security | Public; re-check per lesson | 2026-10-09 |
| F4 | [MDN HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) | MDN | Official guide | HTTP messages, methods, status codes, and API mental models | Public; re-check per lesson | 2026-10-09 |
| F5 | [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro) | TypeScript | Official handbook | Types, narrowing, functions, modules, and compiler behavior | Public; re-check per lesson | 2026-10-09 |
| F6 | [PostgreSQL Documentation](https://www.postgresql.org/docs/current/) | PostgreSQL | Official documentation | SQL, constraints, indexes, transactions, isolation, and concurrency | Public; re-check per lesson | 2026-10-09 |
| F7 | [Docker Get Started](https://docs.docker.com/get-started/) | Docker | Official guide | Containers and local environment fundamentals | Public; re-check per lesson | 2026-10-09 |
| F8 | [Playwright Test documentation](https://playwright.dev/docs/intro) | Playwright | Official documentation | Practical automated testing and CI tests | Public; re-check per lesson | 2026-10-09 |
| F9 | [OpenTelemetry documentation](https://opentelemetry.io/docs/) | OpenTelemetry | Official documentation | Traces, metrics, logs, instrumentation, and context propagation | Public; re-check per lesson | 2026-10-09 |
| F10 | [Google Cloud Well-Architected Framework — Reliability](https://docs.cloud.google.com/architecture/framework/reliability) | Google Cloud | Architecture guidance | Reliability goals, observation, response, recovery, and postmortems | Public; re-check per lesson | 2026-10-09 |
| F11 | [OWASP API Security Project](https://owasp.org/projects/api-security-project) | OWASP | Security guidance | API attack surfaces and authorization/security risks | Public; use current edition | 2026-10-09 |
| F12 | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) and [Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval) | Anthropic Engineering | Engineering articles | Context budgets, retrieval design, and retrieval improvement techniques; these do not replace independent evaluation | Public; re-check per lesson | 2026-10-09 |
| F13 | [AI Engineer roadmap](https://roadmap.sh/ai-engineer) | roadmap.sh | Roadmap cross-check | AI-engineering coverage across implementation, LLM applications, RAG, agents, deployment, and MLOps | Public; re-check for current scope | 2026-10-09 |
| F14 | [The Batch — AI Careers](https://www.deeplearning.ai/the-batch/tag/ai-careers) | DeepLearning.AI | Career discovery feed | Current AI-career articles and evolving industry skills; not a prerequisite order or sole evidence | Public; re-check per lesson | 2026-10-09 |

## References to verify

These are research leads, not evidence. Keep them here until the exact artifact
is opened and checked. Do not cite a person or organization by name alone.

- A first-party customer deployment case study with measured adoption and business outcomes at honest provenance (leads: Coinbase support-chatbot write-up, Thomson Reuters CoCounsel/Cowork write-ups — vendor-reported numbers only until independently confirmed).
- The titles *A Common-Sense Guide to AI Engineering* and *An Illustrated
  Guide to AI Agents* must each be tied to a canonical publication page or
  publisher listing before use.

- **S28 — *Foundations of Scalable Systems: Designing Distributed Architectures*, Ian Gorton, First Edition** — uploaded in both study tools (available as a study source). O'Reilly Media, June 2022 (per canonical publisher page; the uploaded EPUB OPF metadata and copyright page record July 2022). ISBN 978-1-098-10606-5. [Publisher page](https://www.oreilly.com/library/view/foundations-of-scalable/9781098106058/). Bibliography verified from epub OPF, copyright page, and publisher record (2026-10-17). A foundational 2022 source, not a 2025/2026 source. No chapters read; all citations in the journey are TOC-identified only. Stays here until at least one cited chapter passage is read.
- **S38 — *Software Architecture: The Hard Parts: Modern Trade-Off Analyses for Distributed Architectures*, Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani, First Edition** — O'Reilly Media, October 2021. ISBN-13: 978-1-492-08688-8. [Publisher page](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/). Bibliographic details verified from canonical publisher listing (2026-10-17). Uploaded in both study tools (available as a study source per learner crosswalk of 2026-10-14), though not present as a local EPUB file in `/books/` on disk for this agent. Stays in References to verify because no chapter text has been read or examined by the mentor; all chapter citations in the journey remain `[TOC]` only.
- A primary statistics-for-LLM-evaluation tutorial covering variance, sample size, and meaningful comparison (applied level per journey rule 11 — no ML-theory texts).
- Python-track authorities for the Phase 11–14 AI labs: official Python docs (typing, asyncio, packaging) and a runtime-validation library guide — open before registering.
- Integration hardening for P8.2–P8.7 (leads, unopened on 2026-09-30; migrated from estaie-study-map 2026-10-09 — open and record exact section before teaching): Stripe idempotency (https://stripe.com/blog/idempotency); AWS Builders' Library timeouts/retries/backoff-with-jitter (https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/); GitHub webhooks best practices (https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks); Stripe webhooks guide (docs.stripe.com/webhooks); Airbnb double-payments post (https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb); Google SRE ch. 22 cascading failures (https://sre.google/sre-book/addressing-cascading-failures/); Kleppmann distributed locking (https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html) + antirez Redlock reply (https://www.antirez.com/news/101); transactional outbox (https://microservices.io/patterns/data/transactional-outbox.html); Supabase range columns (https://supabase.com/blog/range-columns); Django ExclusionConstraint (https://docs.djangoproject.com/en/dev/ref/contrib/postgres/constraints); RateGain ARI push (https://developer.rategain.com/our-products/channel-manager/rg-bridge-supply-push/interface-specifications-availability-and-rates-notification-service); oneuptime Stripe-webhook atomic-enqueue 2026-09-13 (https://oneuptime.com/blog/post/2026-09-13-stripe-webhook-event-id-atomic-enqueue/view — Tier 2, confirm against provider docs).
- Further agent-incident primaries beyond EchoLeak (e.g., names in the OWASP Agentic 2026 announcement) — open the primary before any casebook use.
- OpenAI Datasets / evaluation-getting-started guide (successor to the deprecated S22 flow); Anthropic enterprise guide procedures (S12); code execution with MCP (S14).
- RFC 9457, *Problem Details for HTTP APIs* (https://www.rfc-editor.org/rfc/rfc9457; IETF Proposed Standard, July 2023; obsoletes RFC 7807). Found, not read. Candidate unit: P4.3.
- RFC 9700 / BCP 240, *Best Current Practice for OAuth 2.0 Security* (https://www.rfc-editor.org/rfc/rfc9700; January 2025). Found, not read. Candidate unit: P4.8; also cross-check S6's OAuth statements.
- Postman, *API Security Best Practices* (https://blog.postman.com/api-security-best-practices/; dated 2026-02-19 in the learner's list). Not opened; at most a secondary checklist, never a substitute for S39, OWASP, or primary platform documentation.
- Cloudflare API Shield, BOLA vulnerability detection (https://developers.cloudflare.com/api-shield/security/bola-vulnerability-detection/; updated 2026-09-29 in the learner's list). Not opened; product-specific, so separate Cloudflare's detection description from general authorization-testing requirements.
- Stripe's AI-benchmark repository (https://github.com/stripe/ai/tree/main/benchmarks), described in S37. Not opened.
- OpenAPI Specification 3.1 (https://spec.openapis.org/oas/v3.1.0; JSON Schema 2020-12 dialect): lead for P4.6's machine-readable contract work and the P4.8a contract-sheet claims; not opened.
- roadmap.sh pages for API security best practices, backend, software architect, and forward deployed engineer: all four were opened 2026-10-14. They render their skill nodes client-side and the fetched text contained none (only page descriptions and, on the Backend page, introductory prose), so no skill cluster could be extracted and none is registered as a source.
- Additional high-signal leads may be added only as links to specific articles,
  talks, papers, repos, or course pages; generic names and broad lists are not
  accepted entries.

## Coverage gaps

- No verified primary source yet provides a practical statistical treatment for comparing noisy LLM evaluation results (P14.3 uses the labeled interim protocol).
- No verified Python-track authorities yet for the Phase 11–14 AI labs (typing, asyncio, packaging, runtime validation); Phases 2–10 practice is TypeScript/Node.js.
- No verified source yet for webhook signature verification and raw-request-body handling (P8.4); the provider webhook leads above are unopened.
- F3 (Node.js Learn) is registered at landing level only; the exact pages used for P3.5, P3.6, and P7.2 (async, diagnostics, testing, security) are not yet recorded.
- Book chapters tagged `[TOC]` in the journey come from tables of contents and have not been read by the mentor; verify the exact passage in ChatGPT Project or NotebookLM. Partial reads: S19 ch. 1–2, S20 ch. 4–6, 11, 19, 21–23, S26 ch. 2–3, 16 — remaining cited chapters for these books are still `[TOC]`. Entirely `[TOC]`: S27, S28, S29, S38 — no chapter text has been read from these books.
- OAuth and credential-lifecycle depth for P4.8 is only partly covered by S6 (MCP-specific); RFC 9700 and provider documentation remain to be read.
- No source measures the effect of human-review practices on the quality of AI-generated code; S37 is a small vendor benchmark and S40 and S41 are qualitative vendor and practitioner material.
- No verified ingestion/access-control lifecycle how-to yet for P12.2/P15.4 (permission inheritance, retention, deletion).
- Residual RAG depth gap: chunking, embedding, and reranking tuning beyond the Barnett FP taxonomy.
- Enterprise outcome numbers with independent provenance (narratives exist as vendor-reported leads).

Lessons must name these as gaps rather than cite them as evidence. Scope guard: nothing in these gaps authorizes ML training, model-building, or researcher topics — fill them only with GenAI-application engineering sources (journey rule 11).

## Update procedure

1. Open the publisher's canonical page or the exact artifact being cited.
2. Confirm title, publisher, relevance, and whether the resource is still
   current.
3. Record the date and exact section, chapter, page, or subsection used.
4. Move failed, stale, or weak entries to **References to verify** or **Coverage
   gaps**; do not silently retain them as verified.