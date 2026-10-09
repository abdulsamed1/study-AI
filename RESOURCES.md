# FDE Study Resources

Updated: 2026-10-09

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

Books may be listed as citations even when access is paywalled; do not
reproduce copyrighted text. API, product, model, and security claims require
current official documentation or a dated primary source. Cite the exact
chapter, section, page, or heading used when available.

Books marked **Uploaded in both study tools** are fully supplied by the user in
both NotebookLM and the ChatGPT Project. They may be used as study references
in either tool. Cite the book title, edition, author, and chapter or page; do
not reproduce the book or treat a generated summary as the source.

People, organizations, newsletters, conferences, and communities are discovery
leads only. A durable entry must identify a specific artifact with a canonical
URL, explain its relevance, and record its verification status.

## Verified references

| ID | Source | Publisher | Type | Coverage | Access | Last verified |
|---|---|---|---|---|---|---|
| S1 | [Claude Frontier Academy](https://www.anthropic.com/news/claude-frontier-academy) | Anthropic | Role standard | FDE-style delivery and scenario assessment | Public | 2026-10-09 |
| S2 | [Forward Deployed Engineer, Frontier GenAI](https://apply.deloitte.com/careers/JobDetail/Forward-Deployed-Engineer-Frontier-GenAI/350555) | Deloitte | Job evidence | Role expectations and production GenAI experience | Public listing | 2026-10-09 |
| S3 | [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Anthropic Engineering | Engineering article | Workflows, agents, and composition patterns | Public | 2026-10-09 |
| S4 | [Claude API documentation](https://docs.anthropic.com/en/docs) | Anthropic | Official documentation | Messages, tools, structured output, limits, and model behavior | Public; re-check per lesson | 2026-10-09 |
| S5 | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anthropic Engineering | Engineering article | Context budgets, retrieval, and just-in-time context | Public | 2026-10-09 |
| S6 | [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest) | Model Context Protocol | Specification | Tool and context interoperability, authorization concepts | Public; versioned | 2026-10-09 |
| S7 | [Writing tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Anthropic Engineering | Engineering article | Tool contracts, descriptions, and agent usability | Public | 2026-10-09 |
| S8 | [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | Anthropic Engineering | Engineering article | Multi-agent decomposition, delegation, and cost trade-offs | Public | 2026-10-09 |
| S9 | [A postmortem of three recent issues](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues) | Anthropic Engineering | Postmortem | Reliability failures and operational learning | Public | 2026-10-09 |
| S10 | [Google Cloud Service Control incident](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW) | Google Cloud | Official incident report | Dependency failure, impact, and mitigation | Public | 2026-10-09 |
| S11 | [Building AI-powered products](https://www.oreilly.com/library/view/building-ai-powered/9781098166505/) | O'Reilly | Book | AI engineering product and production foundations | Book access may be paid | 2026-10-09 |
| S12 | [Building Effective AI Agents enterprise guide](https://claude.com/resources/guides/building-effective-ai-agents) | Anthropic | Enterprise guide | Choosing single-agent, workflow, and multi-agent designs | Public | 2026-10-09 |
| S13 | [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Anthropic Engineering | Engineering article | Checkpoints, progress, and long-running agent execution | Public | 2026-10-09 |
| S14 | [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) | Anthropic Engineering | Engineering article | Efficient tool use and MCP code execution | Public | 2026-10-09 |
| S15 | [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Anthropic Engineering | Engineering article | Evaluation design, graders, and regression practice | Public | 2026-10-09 |
| S16 | [OWASP GenAI LLM Top 10](https://genai.owasp.org/llm-top-10/) | OWASP GenAI Security Project | Security guidance | LLM application threats and mitigations | Public; use current edition | 2026-10-09 |
| S17 | [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/initiatives/agentic-security/) | OWASP GenAI Security Project | Security guidance | Agent-specific risks and controls | Public; use current edition | 2026-10-09 |
| S18 | [MIT 6.824 Distributed Systems](https://pdos.csail.mit.edu/6.824/) | MIT | University course | Replication, fault tolerance, and distributed-system reasoning | Public materials | 2026-10-09 |
| S19 | Designing Data-Intensive Applications, 2nd Edition | Martin Kleppmann and Chris Riccomini | Book — Uploaded in both study tools | Data systems, consistency, replication, and stream processing | NotebookLM + ChatGPT Project | 2026-10-09 |
| S20 | Fundamentals of Software Architecture, 2nd Edition | Mark Richards and Neal Ford | Book — Uploaded in both study tools | Architecture trade-offs and decision-making | NotebookLM + ChatGPT Project | 2026-10-09 |
| S21 | [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | OpenAI | Official SDK documentation | Agents, tools, handoffs, guardrails, and tracing | Public; re-check per lesson | 2026-10-09 |
| S22 | [OpenAI evaluations guide](https://platform.openai.com/docs/guides/evals) | OpenAI | Official documentation | Evaluation datasets, graders, and regression workflows | Public; re-check per lesson | 2026-10-09 |
| S23 | [Google Agent Development Kit](https://google.github.io/adk-docs/) | Google | Official SDK documentation | Agent workflows, tools, sessions, and deployment concepts | Public; re-check per lesson | 2026-10-09 |
| S24 | [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | NIST | Government framework | AI risk governance, measurement, and management | Public | 2026-10-09 |
| S25 | [Site Reliability Engineering book](https://sre.google/sre-book/table-of-contents/) | Google | Book | Reliability, monitoring, incident response, and operations | Public online edition | 2026-10-09 |
| S26 | Building Microservices: Designing Fine-Grained Systems | Sam Newman | Book — Uploaded in both study tools | Service boundaries, integration, deployment, and operational trade-offs | NotebookLM + ChatGPT Project | 2026-10-09 |
| S27 | Understanding Distributed Systems, 2nd Edition | Roberto Vitillo | Book — Uploaded in both study tools | Distributed-system fundamentals, failure, consistency, and operations | NotebookLM + ChatGPT Project | 2026-10-09 |
| S28 | Foundations of Scalable Systems | To verify from uploaded title page | Book — Uploaded in both study tools | Scalable-system architecture and operational trade-offs | NotebookLM + ChatGPT Project | 2026-10-09 |
| S29 | Designing Distributed Systems, 2nd Edition | Brendan Burns | Book — Uploaded in both study tools | Patterns and paradigms for scalable, reliable Kubernetes systems | NotebookLM + ChatGPT Project | 2026-10-09 |

## References to verify

These are references supplied for the study path but not yet tied to a checked,
specific artifact. For people and organizations, find the relevant article,
book, course, talk, paper, repository, or documentation page first. Do not cite
the name alone.

- A primary-source enterprise RAG failure with enough technical detail to teach
  retrieval failure mechanisms.
- A first-party customer deployment case study with measurable adoption and
  business outcomes.
- The titles *A Common-Sense Guide to AI Engineering* and *An Illustrated
  Guide to AI Agents*
- The author and canonical publication details for *Foundations of Scalable
  Systems* must be confirmed from its uploaded title page before citation.
- A primary statistics-for-LLM-evaluation tutorial that covers variance,
  sample size, and meaningful comparison.
- People: Andrej Karpathy; Simon Willison; Chip Huyen; Hamel Husain;
  Eugene Yan; Sebastian Raschka; Harrison Chase; Jerry Liu; Jason Liu; Shreya
  Shankar; Lilian Weng; Jeremy Howard; swyx; François Chollet; Logan Kilpatrick;
  Yohei Nakajima; Addy Osmani; James Briggs; Paul Iusztin; Aidan Gomez; Dario
  Amodei; Mira Murati; Alexandr Wang; Aravind Srinivas; Cassie Kozyrkov; Andrej
  Tomašević; Nathan Lambert; Jason Wei; Harrison Kinsley; Sebastian Buck; Vicki
  Boykis; Hamza El-Khatib; Riley Goodside; Omar Sanseviero; Thomas Wolf; Clem
  Delangue; Lewis Tunstall; Maxime Labonne; Jay Alammar; Chris Albon; Rachel
  Thomas; Tim Dettmers; Tri Dao; Percy Liang; Andrej Bauer; Jim Fan; Bo Wang;
  Ethan Mollick; Ethan Perez.
- Organizations and publications: Anthropic Engineering; OpenAI Engineering;
  Google DeepMind; Hugging Face; LangChain; LlamaIndex; Weights & Biases; Modal;
  Replicate; Pinecone; Cohere; Together AI; Latent Space; The Batch; AI
  Engineer World's Fair.

## Coverage gaps

- No verified primary source yet covers the full RAG failure taxonomy required
  by L2.2-L2.3.
- No verified primary source yet provides a practical statistical treatment for
  comparing noisy LLM evaluation results.
- No verified agent tool-misuse incident is currently strong enough for a
  casebook entry.

Lessons must name these as gaps rather than cite them as evidence.

## Update procedure

1. Open the publisher's canonical page.
2. Confirm title, publisher, relevance.
3. Record the date and exact section/chapter used.
4. Move failed or obsolete entries to **References to verify** or **Coverage
   gaps**; do not silently retain them as verified.
