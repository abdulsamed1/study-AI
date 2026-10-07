# TEACHING-PROTOCOLS.md

Detailed procedures that `AGENTS.md` points to. Load this file only when you need one of them.
If anything here conflicts with `AGENTS.md`, `AGENTS.md` wins.

## 1. Workspace layout and file formats (adapted from the `teach` skill by Matt Pocock)

    MISSION.md                      why the user is learning this; one screen at most
    NOTES.md                        user preferences and working notes
    RESOURCES.md                    trusted sources: Knowledge / Wisdom (communities) / Gaps
    GLOSSARY.md                     one-line definitions; every lesson uses these terms
    casebook/INDEX.md               concept -> famous production problems -> transferable pattern
    casebook/<concept>.md           researched real failures for one concept
    learning-records/NNNN-slug.md   evidence of understanding
    lessons/NNNN-slug.html          one short lesson each (no file access: Markdown in the reply)
    reference/*.html                cheat sheets, sequence diagrams, checklists
    assets/                         shared stylesheet and reusable components

- MISSION.md: Why (1-3 concrete sentences) / Success looks like / Constraints / Out of scope. One mission per
  workspace. Push back on vague missions. Confirm with the user before changing it.
- RESOURCES.md: annotate every entry with what it covers and when to use it. High-trust sources only. Record gaps
  explicitly. Remove sources that prove shallow or wrong.
- Learning record: a title plus 1-3 sentences; optional Status, Evidence, Implications. Mark a contradicted record
  `superseded by LR-NNNN`; never delete it.
- Journey files may name "project sources" (uploaded books, articles). Treat books as Tier 1 for the concepts they
  cover and cite the chapter. Treat user-supplied articles as scenario input and verify them against a primary source.

## 2. Casebook procedure

1. Search for real failures and hard-won lessons for the concept. Prefer cases that are widely cited (talks, courses,
   books) or recent (last 12 months when tool behavior matters). For AI-system concepts, also check the newest
   incident reports and security lists, because they change within months.
2. Read the source page. If you cannot open it, mark the case "secondary only".
3. Rank candidates by recurrence in the literature, clarity of the root cause, transferability to the mission, source
   quality, and recency. Teach the top 2 or 3. Keep all of them in `casebook/<concept>.md`.
4. Record each case in at most 8 lines: title; source, date, URL; what happened; root cause (mechanism); fix or
   mitigation; transferable pattern; where it could appear in the user's projects; confidence (read the source /
   secondary only).
5. Add one line per concept to `casebook/INDEX.md`: concept, case titles, the pattern they share.
6. Never invent an incident, number, date, quote, or URL. If fewer than 5 solid cases exist, say so and add the gap to
   RESOURCES.md.
7. Paraphrase. Quote at most a short phrase, and link every non-obvious claim.

## 3. Lesson layers

A lesson is short, finishes in one sitting, and gives one tangible win tied to the mission. Knowledge first, then
practice. Difficulty is the enemy while acquiring knowledge and the tool while practising.

1. Scene (under 120 words): the top real case. Who, what broke, why it hurt.
2. Concept in plain words: what it is, why it exists, what problem it solves. Define terms on first use.
3. Mechanism: how it works, with a short sequence or diagram. Concept before framework.
4. Real failures: two or three casebook entries: what broke, root cause, fix.
5. Production view: what to monitor, test, and put into a runbook; trade-offs and costs.
6. Bridge: tie it to the user's project evidence or the active journey. Flag anything to check in code. For interview
   preparation, add how to say it truthfully.

Stop at the layer that reaches the branch's target depth. End with the best primary source and a reminder that the user
can ask follow-ups. Workspace mode: write `lessons/NNNN-slug.html` (self-contained, shared stylesheet in `assets/`,
links to reference sheets); reuse `assets/` components first; open the file with `xdg-open` on Fedora.

## 4. Practice, feedback, retrieval

- The practice task tests reasoning, application, trade-offs, or production judgment, and comes from a casebook
  scenario changed slightly (new constraint, new failure point).
- Warm-up questions revisit older records inside new scenarios. This gives spacing and interleaving. Re-asking the
  same question teaches the question, not the concept.
- Quiz options have equal length and no formatting clues. Give the explanation after the answer.
- For wisdom questions (what works in practice, what teams regret), answer from sources and point to the communities
  recorded in RESOURCES.md.

## 5. Sources-only mode (NotebookLM / Gemini Notebook)

- The notebook grounds answers in its sources. Do not add outside facts. If a lesson needs a case that is not in the
  sources, say which source to add (a postmortem URL, a book chapter) instead of improvising.
- Keep lessons in the same layers. Skip file-writing steps; end with a "Save these notes" block.
- Paste the core `AGENTS.md` into the notebook's chat configuration. Add this file, the journey files, books, and
  postmortems as sources.

## 6. Maintaining AGENTS.md

Add a rule to `AGENTS.md` only after its absence caused a real mistake. Move detail here instead of growing the core.
Reason: a February 2026 ICLR paper (Gloaguen et al., arXiv 2602.11988) found that repository context files tended to
reduce coding-agent task success and raised inference cost by over 20%, and concluded that context files should
state only minimal requirements. That study covers coding agents on repository tasks, not tutoring, so treat it as a
reason to stay lean, not as a measurement of this setup.

## 7. Starter sources for AI deployment work (checked 2026-10-06; re-open before teaching from them)

- FDE role evidence (Tier 2, job board mirror, listing dated 2026-08-18): Anthropic Applied AI Forward Deployed Engineer
  https://www.ziprecruiter.de/jobs/579595928-forward-deployed-engineer-bei-anthropic
  Describes embedding with strategic customers and building production applications with Claude models.
- OWASP Top 10 for LLM Applications, 2026 edition (published 2026-08-03). Summary and ranking (Tier 2 research note):
  https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-genai-top10-2026-agent-control-stand/
  Fetch the official list from the OWASP GenAI Security Project before citing. The companion Top 10 for Agentic
  Applications dates from December 2025.
- Anthropic Engineering, "A postmortem of three recent issues" (Sept 2025):
  https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues
  Context-window routing error, TPU misconfiguration, compiler bug; why quality evals on production systems matter.
- Google Cloud incident report, 2025-06-12 (Service Control):
  https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW
  Blank fields hit an unprotected code path; the recovery herd effect lacked randomized exponential backoff.
- Anthropic, "Effective context engineering for AI agents" (Sept 2025). Search the title on anthropic.com/engineering.
  Principles: smallest set of high-signal tokens; retrieve just in time; compaction, notes, sub-agents.
- Gaps to research: a primary-source enterprise RAG failure case; a primary-source agent permission or tool-misuse
  incident; evaluation practice for LLM features in production; a customer-deployment case study from a vendor's
  forward deployed team.
