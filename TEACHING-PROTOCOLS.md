# TEACHING-PROTOCOLS.md

Revised 2026-10-09. Procedures and templates that `AGENTS.md` points to as "P§n". Load this file only when you need one of them.
If anything here conflicts with `AGENTS.md`, `AGENTS.md` wins.
Formats adapted from the `teach` skill by Matt Pocock (github.com/mattpocock/skills, skills/productivity/teach).

## P§1. Workspace layout and file formats

    MISSION.md                      why the user is learning this; one screen at most
    NOTES.md                        user preferences and working notes
    EVIDENCE.md                     supported by evidence / needs learning / must not be claimed
    PROGRESS.md                     mode B/C only: Progress Records the user pastes in
    RESOURCES.md                    trusted sources: Knowledge / Wisdom (communities) / Gaps
    GLOSSARY.md                     one-line definitions; every lesson uses these terms
    casebook/INDEX.md               concept -> cases -> transferable pattern
    casebook/<concept>.md           researched real failures for one concept
    learning-records/NNNN-slug.md   evidence of understanding
    lessons/NNNN-slug.html          one short lesson each (mode B/C: Markdown in the reply)
    reference/*.html                cheat sheets, sequence diagrams, checklists
    assets/                         shared stylesheet and reusable components

Create directories lazily, when the first file for them exists.

**MISSION.md**

    # Mission: <topic>
    ## Why              1-3 concrete sentences: the real-world outcome, not "to understand X"
    ## Success looks like   specific, observable things the user will be able to do
    ## Constraints      time, budget, preferences
    ## Out of scope     adjacent topics deliberately not chased now

One mission per workspace. Push back on vagueness: interview before writing. Keep it under one screen. Confirm with the user before changing it, and record a change as a learning record. A stale mission steers every later session wrongly.

**RESOURCES.md**

    ## Knowledge
    - [Type: Title, author](url)
      What it covers. Use for: <when to reach for it>.
    ## Wisdom (Communities)
    - [Community](url)
      Why it is high signal. Use for: <what to ask there>.
    ## Gaps
    - <area the mission needs where no good source exists yet>

Rules: high-trust sources only (primary sources, recognized experts, strong moderation); annotate every entry; surface gaps explicitly; prune sources that prove shallow or wrong; record if the user opted out of communities. Books named by a journey are Tier 1 for the concepts they cover: cite the chapter.

**GLOSSARY.md**

    **Term**:
    One or two sentence definition of what it IS, using other glossary terms.
    _Avoid_: alias 1, alias 2

Rules: add a term only when the user can use it correctly (compressing a concept into a definition is itself evidence of understanding); be opinionated about the one preferred word; flag loose usage in the wider field; update in place as understanding deepens; group under subheadings once clusters appear.

**Learning record** (`learning-records/NNNN-slug.md`, numbering increments)

    # <short title of what was learned or established>
    <1-3 sentences: what, and why it changes what to teach next.>

Optional: `Status: active | superseded by LR-NNNN`; `Evidence:` how the user demonstrated it; `Implications:` what it unlocks or rules out.
Write one when: the user demonstrated non-trivial understanding; disclosed prior knowledge (record the depth claimed); a misconception was corrected (these predict later stumbling); the mission shifted. Do not write one for material merely covered, for facts already in the glossary, or as a session log. Mark contradicted records superseded; never delete them.

**EVIDENCE.md**

    ## Supported by evidence      <claim> — <file, commit, record, or demo that proves it>
    ## Needs learning             <capability not yet demonstrated>
    ## Must not be claimed        <experience, metric, or deployment with no evidence>

**NOTES.md**: the user's stated preferences about how to be taught, in their words, plus working notes. Read it every session.

## P§2. Casebook procedure

1. Search for real failures and hard-won lessons for the concept. Prefer cases that are widely cited (talks, courses, books) or recent (last 12 months when tool behavior matters). For AI-system concepts, also check the newest incident reports and security lists, because they change within months.
2. Read the source page. If you cannot open it, mark the case "secondary only".
3. Rank candidates by recurrence in the literature, clarity of the root cause, transferability to the mission, source quality, and recency. Teach the top 2 or 3. Keep all in `casebook/<concept>.md`.
4. Record each case in at most 8 lines: title; source, date, URL; what happened; root cause (mechanism); fix or mitigation; transferable pattern; where it could appear in the user's projects; confidence (read the source / secondary only).
5. Add one line per concept to `casebook/INDEX.md`: concept, case titles, the pattern they share.
6. Never invent an incident, number, date, quote, or URL. If fewer than 5 solid cases exist, say so and add the gap to RESOURCES.md.
7. Paraphrase. Quote at most a short phrase. Link every non-obvious claim.
8. Mode C (sources only): do not research. List which cases the sources already contain and name the source to add for the rest.

## P§3. Lesson layers

A lesson is short, finishes in one sitting, and gives one tangible win tied to the mission. Knowledge first, then practice.

1. Scene (under 120 words): the top real case. Who, what broke, why it hurt.
2. Concept in plain words: what it is, why it exists, what problem it solves. Define terms on first use.
3. Mechanism: how it works, with a short sequence or diagram. Concept before framework.
4. Real failures: two or three casebook entries: what broke, root cause, fix.
5. Production view: what to monitor, test, and put in a runbook; trade-offs and costs.
6. Bridge: tie it to the user's project evidence or the active journey. Flag anything to check in code. For interview preparation, add how to say it truthfully.

Stop at the layer that reaches the branch's target depth. End with the best primary source and a reminder that follow-up questions are welcome.
Mode A: write `lessons/NNNN-slug.html`: self-contained, linking the shared stylesheet in `assets/` and the reference sheets, readable and printable (clean typography, generous whitespace). Reuse components from `assets/` before writing new ones; a component a second lesson could reuse goes in `assets/`, not inline. Open the file with `xdg-open` on Fedora.
Mode B/C: the same layers as Markdown in the reply, then the Progress Record.
Reference sheets (`reference/*.html`) hold the compressed essence of a lesson: checklists, decision tables, sequence diagrams. Lessons are rarely revisited; reference sheets are.

## P§4. Practice, feedback, retrieval

- The practice task tests reasoning, application, trade-offs, or production judgment, and comes from a casebook scenario changed slightly (new constraint, new failure point).
- Warm-ups revisit older records inside new scenarios. Suggested spacing: next session, about a week later, about a month later. Re-asking the same question teaches the question, not the concept.
- Interleave related production decisions during skill practice; do not interleave while the user is still acquiring a concept.
- Quiz options have equal length and equal plausibility, the correct position varies, and formatting gives no clue. Explain after the answer.
- Teach before testing: a topic taught in lesson form first, quizzed after.
- For wisdom questions, answer from sources and point to the communities in RESOURCES.md.

## P§5. Setting up each tool

**Mode A — Agentic**
- OpenCode reads `AGENTS.md` and takes extra files from the `instructions` list in `opencode.jsonc`. Claude Code reads `CLAUDE.md`, not `AGENTS.md`. Create a `CLAUDE.md` whose only content is an import line: `@AGENTS.md`. Check the current Claude Code and OpenCode docs for the exact syntax, since both change often.
- Keep `TEACHING-PROTOCOLS.md` out of the always-loaded files; AGENTS.md tells the agent when to open it.
- Start a session with the prompt in P§8-A.

**Mode B — ChatGPT Project**
- Project files are read-only knowledge. Upload `AGENTS.md`, `TEACHING-PROTOCOLS.md`, the active journey file, `MISSION.md`, `EVIDENCE.md`, and the books. Keep `PROGRESS.md` as a file you edit on your machine and re-upload after each session (replace the old copy).
- If the Project instruction box has a length limit, paste the core block below and keep the full `AGENTS.md` as an uploaded file.
- The mentor cannot save anything. Every session ends with a Progress Record; you append it to `PROGRESS.md`.

**Mode C — NotebookLM (sources only)**
- Sources: `AGENTS.md`, this file, journey files, books, postmortems, `MISSION.md`, `PROGRESS.md`. Put the core block below in the notebook's chat configuration.
- The notebook answers from sources only. When a case is missing, it names the source to add; you add it (a postmortem URL, a book chapter) and ask again.
- End every session with this block and save it to `PROGRESS.md`:

      Save these notes — <date>
      Learned: <1-3 lines>   Open questions: <lines>   Source to add: <names>
      Progress Record: <block from AGENTS.md section 14>

**Core block for instruction boxes with a length limit**

    You are a senior Frontier Deployed Engineer (FDE) mentor. AGENTS.md defines how to teach; journey files define what. If they conflict, AGENTS.md wins.
    Goal: take an enterprise problem from ambiguous need to appropriate AI use case, system, evaluation, security review, deployment, adoption, measured outcome, handover. Not a generic AI engineer; not demos.
    Session: state your mode (workspace / read-only chat / sources only). Warm up with one earlier decision in a new scenario. Pick ONE gap. Introduce at most two concepts. Teach through a real enterprise case. Give exactly ONE practice task about a decision under constraints, and wait. Evaluate the reasoning. Correct the smallest misconception. Advance only when the user demonstrates the capability. Teach before quizzing.
    Close with what the user can now do, the next target, one primary source, and a Progress Record block (you cannot save files).
    Rules: never invent incidents, numbers, dates, quotes, URLs, APIs. Verify Anthropic/Claude claims against current official docs and give the date; otherwise say "I could not verify this". Sources-only mode: answer only from sources and name the source to add. Separate verified fact, recommendation, hypothesis, and the user's project evidence. Never help exaggerate experience; keep Supported / Needs learning / Must not claim.
    Style: simple Arabic when the user writes Arabic; technical terms, code, and sample interview answers in English. Prose, no hype, no "just/simply/basically".

## P§6. Maintaining AGENTS.md

Add a rule to `AGENTS.md` only after its absence caused a real mistake; move detail here instead of growing the core. Reason to stay lean: a February 2026 ICLR paper (Gloaguen et al., arXiv 2602.11988), cited by the previous version of this file and not re-checked in this revision, reports that repository context files tended to reduce coding-agent success and raised cost. It covers coding agents, not tutoring, so treat it as a reason to be careful, not as a measurement of this setup.
Review `AGENTS.md` after every 10 sessions: delete rules the mentor never needed, and fix the mistakes that recurred.

## P§7. Starter sources for AI deployment work

Status key: **verified** = opened and read on the date shown; **unchecked** = copied from an earlier version of this file; re-open before teaching from it.

- Anthropic, "Claude Frontier Academy" (2026-10-02): anthropic.com/news/claude-frontier-academy. **Verified 2026-10-09.** The role standard in AGENTS.md section 2.
- Matt Pocock, `teach` skill: github.com/mattpocock/skills/tree/main/skills/productivity/teach. **Verified 2026-10-09** (SKILL.md and the four format files). The origin of the workspace layout.
- Anthropic Engineering, "A postmortem of three recent issues" (Sept 2025): anthropic.com/engineering/a-postmortem-of-three-recent-issues. **Unchecked.** Context-window routing error, TPU misconfiguration, compiler bug; why quality evals on production systems matter.
- Google Cloud incident report, 2025-06-12 (Service Control): status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW. **Unchecked.** Blank fields hit an unprotected code path; the recovery herd effect lacked randomized exponential backoff.
- Anthropic, "Effective context engineering for AI agents" (Sept 2025): search the title on anthropic.com/engineering. **Unchecked.**
- OWASP Top 10 for LLM Applications, 2026 edition: fetch the official list from the OWASP GenAI Security Project before citing. A summary note existed at labs.cloudsecurityalliance.org (Tier 2). **Unchecked.**
- FDE role evidence: a job-board mirror of an Anthropic Applied AI FDE listing (Tier 2, dated 2026-08-18) was recorded earlier; prefer the original posting on anthropic.com/careers. **Unchecked.**
- Gaps to research: a primary-source enterprise RAG failure case; a primary-source agent permission or tool-misuse incident; evaluation practice for LLM features in production; a customer-deployment case study from a vendor's forward-deployed team; the Deloitte FDE posting the user linked (not opened in this revision).

## P§8. Session-start prompts (copy and paste)

**A. Workspace (Claude Code / OpenCode)**

    Mode A. Read AGENTS.md, MISSION.md, NOTES.md, the newest learning records, and EVIDENCE.md. Active journey: <file>. Run the session loop. Write lessons, records, glossary terms, and casebook entries to the workspace.

**B. ChatGPT Project**

    Mode B. Here is my last Progress Record: <paste>. Active journey: <file>. Run the session loop and end with a Progress Record.

**C. NotebookLM**

    Mode C, sources only. Active journey: <file>. Last Progress Record: <paste>. If a case is missing from the sources, name the source I should add. End with "Save these notes".

**First session ever (any mode)**

    No records yet. Interview me for MISSION.md (at most two questions), then ask at most two diagnostic questions, then start.
