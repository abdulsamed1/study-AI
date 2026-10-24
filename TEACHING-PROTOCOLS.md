# TEACHING-PROTOCOLS.md

Revised 2026-10-22. Templates, procedures, and tool setup that `AGENTS.md` points to as "P§n". Load this file only when you need one of them.
This file holds formats and steps only. Behavioral rules live in `AGENTS.md` and are not repeated here; if the two conflict, `AGENTS.md` wins.
Formats adapted from the `teach` skill by Matt Pocock (github.com/mattpocock/skills, skills/productivity/teach).

## P§1. Workspace layout and file formats

    MISSION.md                      why the user is learning this; one screen at most
    EVIDENCE.md                     supported by evidence / needs learning / must not be claimed
    RESOURCES.md                    verified references / references to verify / coverage gaps
    GLOSSARY.md                     one-line definitions; every lesson uses these terms
    casebook/INDEX.md               concept -> cases -> transferable pattern
    casebook/<concept>.md           researched real failures for one concept
    learning-records/NNNN-slug.md   evidence of understanding
    lessons/NNNN-slug.html          one short lesson each (modes B and C: Markdown in the reply)
    reference/*.html                cheat sheets, sequence diagrams, checklists
    assets/                         shared stylesheet and reusable components

Create directories lazily, when the first file for them exists. In modes B and C these files exist only as uploads or as the user's notes; state lives as described in `AGENTS.md` section 2 and P§6.

**MISSION.md**

    # Mission: <topic>
    ## Why              1-3 concrete sentences: the real-world outcome, not "to understand X"
    ## Success looks like   specific, observable things the user will be able to do
    ## Constraints      time, budget, preferences
    ## Out of scope     adjacent topics deliberately not chased now

One mission per workspace. Push back on vagueness: interview before writing. Keep it under one screen. Confirm with the user before changing it, and record a change as a learning record. A stale mission steers every later session wrongly.

**RESOURCES.md**

The section contract lives in the file itself: `RESOURCES.md` opens with `## How to use this file`, defining the three sections (Verified references / References to verify / Coverage gaps) and the entry rules for each. Keep the template operative there instead of a copy in this file.

Rules: annotate every entry; surface gaps explicitly; prune sources that prove shallow or wrong; record if the user opted out of communities. Source tiers are in `AGENTS.md` section 9; books named by a journey are Tier 1 for the concepts they cover (cite the chapter).

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

The P2.1 baseline is short: one line per assessed dimension with the evidence that supports it. It is an assessment recorded in the three lists, not a separate document; an unassessed dimension is named as unassessed rather than left out.

## P§2. Casebook procedure

1. Search for real failures and hard-won lessons for the concept. Prefer cases that are widely cited (talks, courses, books) or recent (last 3~8 months when tool behavior matters). For AI-system concepts, also check the newest incident reports and security lists, because they change within months.
2. Read the source page. If you cannot open it, mark the case "secondary only".
3. Rank candidates by recurrence in the literature, clarity of the root cause, transferability to the mission, source quality, and recency. Keep all candidates in `casebook/<concept>.md`.
4. Record each case in at most 8 lines: title; source, date, URL; what happened; root cause (mechanism); fix or mitigation; transferable pattern; where it could appear in the user's projects; confidence (read the source / secondary only).
5. Add one line per concept to `casebook/INDEX.md`: concept, case titles, the pattern they share.
6. Paraphrase. Quote at most a short phrase. Link every non-obvious claim.

## P§3. Lesson layers and parts

A lesson unit finishes in one sitting and gives one tangible win tied to the mission. Knowledge first, then practice.

Layers: (1) Scene, under 120 words: the top real case, who, what broke, why it hurt. (2) Concept in plain words: what it is, why it exists, what problem it solves; define terms on first use. (3) Mechanism: how it works, with a short sequence or diagram; concept before framework. (4) Real failures: two or three casebook entries with root cause and fix. (5) Production view: what to monitor, test, and put in a runbook; trade-offs and costs. (6) Bridge: tie it to the user's project evidence or the active journey; flag anything to check in code; for interview preparation, how to say it truthfully.

Parts, one message each (stop at the part that reaches the unit's target depth):

| Part | Layers | Ends with |
|---|---|---|
| 1 | Scene + Concept | one retrieval question |
| 2 | Mechanism | one retrieval question |
| 3 | Real failures | one retrieval question |
| 4 | Production view + Bridge | the practice task |

**Incident-grounded variant (hands-on reliability units).** Keep the four parts and map the eight steps of `AGENTS.md` §8 onto them: Part 1 carries Incident + Evidence (the verified case, the observed symptom, what is still unknown); Part 2 carries Mechanism and the testable hypothesis it supports; Part 3 carries the failure cases and the Harness + Measure design, including what the lab can and cannot reproduce; Part 4 carries Fix + Regression + Transfer and issues the practice task, in which the learner runs the harness, records the baseline, changes one variable, and shows red → green. A part may cite the incident but must not present a simulation as the incident itself. When no verified incident fits, say so and use a clearly labelled synthetic scenario instead of inventing a case.

A part is roughly 400-700 words plus a diagram when useful. The source named for the unit is cited in Part 1 and the best primary source is repeated at the end.
Mode A: also write `lessons/NNNN-slug.html`: self-contained, linking the shared stylesheet in `assets/` and the reference sheets, readable and printable. Reuse `assets/` components before writing new ones. Open the file with `xdg-open` on Fedora.
Modes B and C: Markdown in the reply, one part per message.
Reference sheets (`reference/*.html`) hold the compressed essence of a lesson: checklists, decision tables, sequence diagrams.

## P§5. Practice sources and retrieval schedule

- Build the practice task from a casebook scenario changed slightly (new constraint, new failure point).
- Warm-ups revisit older records inside new scenarios. Suggested spacing: next session, and spaced later sessions across changing scenarios. Re-asking the same question teaches the question, not the concept.
- Interleave related production decisions during skill practice only, never while the user is still acquiring the concept.
- **Defense drill (decision cards).** Pick one decision defense card (`fde-journey-map.md` §3) and escalate without teaching: what was decided and why; what else was possible; what the accepted tradeoff costs; what would make it wrong; the same decision under one changed constraint (for example half the budget, a stricter latency target, or no managed service). The learner answers without an agent and without the card's `owner's explanation` field. Score on the journey's Depth scale and write the result in the standard learning record (P§1), including the card ID, the depth reached, and the first question that exposed a gap.

## P§6. Setting up each tool

Per-tool setup lives here. `AGENTS.md` section 2 defines the modes; this file
only says how to configure each tool.

**Python toolchain (required before P2.1; verify installed, do not assume).**

- Interpreter: Python 3.11 or newer (`python --version`).
- Environment: one virtual environment per project (`python -m venv .venv` or `uv venv`); never install into the system interpreter.
- Dependencies: pinned in a lockfile (`requirements.txt` with hashes, or `uv.lock`/`poetry.lock`); reinstall from the lockfile in CI.
- Runtime validation: Pydantic v2 (`pip install pydantic`); validate at every trust boundary, not deep in domain logic.
- Static checking: mypy or pyright (`mypy --strict` or `pyright`); run in CI; treat new errors as failures.
- Tests: pytest (`pytest -q`); contract and error-path tests use a stub provider, not live calls.
- Verification before teaching P2.1: `python --version`, `pip --version`, `pytest --version`, `mypy --version` (or `pyright --version`), and `python -c "import pydantic; print(pydantic.VERSION)"` all succeed. Record the output in the session record.
- Scope: this toolchain serves Phases 2–17. TypeScript/Node.js tooling (F3, F5) remains the reading context for P7.7–P7.8 and the owned-system labs; it is not a second implementation track.

**Mode A — workspace**
- The workspace agent reads `AGENTS.md` and takes extra files from the `instructions` list in `opencode.jsonc` if the user uses OpenCode. Check the current docs for both, since the syntax changes.
- Keep this file out of the always-loaded list; `AGENTS.md` says when to open it.

**Mode B — chat with files**

*Claude Project*
- Upload the files in the P§9 manifest. Project knowledge holds the files; "Set project instructions" holds the short instruction text (the full rules are in the uploaded file):

      Follow AGENTS.md in the project files exactly. Use TEACHING-PROTOCOLS.md only when AGENTS.md points to it. The active journey file is the one the user names, otherwise ask.

- Project memory is on by default and is scoped to the project; to keep it fully separate, turn off "Use account memory" on the project page. A reply can be kept by adding it to the project sources.
- A redesigned Projects experience (one conversation, parallel cloud threads) is in beta from 2026-09-17; it does not change the setup above.

*ChatGPT Project*
- Upload the files in the P§9 manifest. File limits depend on the plan; check the current limit in OpenAI's help article "Projects in ChatGPT".
- In Project settings, set Memory to Project-only, and enable the account memory settings the article lists. Memory changes can take a few hours to apply. Project memory shows no list, so the mentor confirms recalled state at the start of each session (`AGENTS.md` section 2).
- Project instructions (short, because the full rules are in the uploaded file):

      Follow AGENTS.md in the project files exactly. Use TEACHING-PROTOCOLS.md only when AGENTS.md points to it. The active journey file is the one the user names, otherwise ask.

- Optional, for a reply that must persist verbatim (for example an agreed mission): the response menu offers "Add to project sources", which adds it as a project source.
- For a fact that must not be lost (a mission change, an evidence claim), ask the user once to say "remember this".

**Mode C — chat without files**
- The agent sees only what the user pastes. The user pastes the files in the P§9 manifest that the lesson needs, plus the selected primary sources.
- NotebookLM keeps chat history inside the notebook, but the agent cannot read that history back as state across sessions, so it needs the session-export block below. Generated quizzes, summaries, and audio are practice artifacts, not sources.
- Chat configuration (the same two sentences, adjusted for sources only):

      Follow AGENTS.md among the sources, in mode C. Answer only from the sources and cite them.

### Session export (modes B and C)

Every chat session ends with this block, in every chat mode. It is the only path
for syncing chat-mode progress into the repository.

    Session export — <date>
    Learning record: <what was demonstrated, evidence, next target>    (P§1 format)
    Glossary terms earned: <term — one-line definition>                (P§1 format)
    EVIDENCE changes: <Supported by evidence | Needs learning | Must not be claimed — claim, then the file, commit, record, or demo that proves it>
    RESOURCES changes: <S-ID — status change, or a new lead with its URL and what it would support>
    Next unit: <unit ID and part>

The repository is the source of truth. The workspace agent merges an export in
this order: `learning-records/` file first, then `GLOSSARY.md`, then the three
`EVIDENCE.md` lists, then `RESOURCES.md` (opening the artifact before changing a
status), then the journey ledger. Never apply an export that contradicts the
repository without asking the user which is current.

## P§7. Maintaining AGENTS.md

Add a rule to `AGENTS.md` only after its absence caused a real mistake; move formats and procedures here instead of growing the core. Journey files and this file cite `AGENTS.md` section numbers and never restate its rules; when you notice a repeated rule, delete the copy in the lower-priority file. Reason to stay lean: a February 2026 ICLR paper (Gloaguen et al., arXiv 2602.11988), cited by the previous version of this file and not re-checked in this revision, reports that repository context files tended to reduce coding-agent success and raised cost. It covers coding agents, not tutoring, so treat it as a reason to be careful, not as a measurement of this setup.
Review `AGENTS.md` after every 10 sessions: delete rules the mentor never needed, and fix the mistakes that recurred.

### Baseline alignments

`MISSION.md` is the user's file:
- `MISSION.md` points to both the capability standard in `AGENTS.md` section 1 and the hiring standard in `RESOURCES.md` S1.
- Progress tracking is tool-neutral: the repository is the source of truth, recorded in `EVIDENCE.md` and learning records, with chat modes synchronizing via the session-export block (P§6).

## P§8. External resources and candidate roadmaps

Do not add a static source list to this procedure file. External resources,
candidate sources, and candidate roadmaps belong in `RESOURCES.md` or the
active journey file. Treat those files as inputs to source triage, not as
automatic evidence. Open and verify only the sources needed for the current
lesson, then record their status and the exact section used in `RESOURCES.md`.

## P§9. Source-grounded study-pack procedure

### Source triage

For each source needed by a lesson:

1. Open the publisher's canonical page or the supplied book.
2. Confirm title, publisher, relevance, currency, and URL.
3. Record the date and exact section, chapter, or page in `RESOURCES.md`.
4. Mark it Verified only after those checks; move failed or obsolete entries to
   References to verify or Coverage gaps; never silently retain a stale
   or degraded entry as verified.

### Lesson preparation

Select one usable unit from the active journey. Open only its Verified source
IDs and the specific sections needed for that unit; do not load the entire
library into every lesson. Prepare one realistic scenario, one retrieval
question per part, and one final practice task. Label lesson text as
Source-backed fact, Mentor synthesis, or Practice.

Decide the unit's working mode before preparing the practice task, and record
it with the lesson: (1) the learner writes and debugs the code; (2) the
learner specifies the work and reviews agent-produced code; (3) delegated
implementation combined with a learner-designed experiment and independent
verification. Follow the active journey's rules on human-in-the-loop
engineering and on hand-writing versus review; do not restate them here.

### Tool import and export

The file manifest — what each file is for, when it is loaded, who writes it,
and which modes need it:

| File | Purpose | Loaded when | Written by | Modes |
|---|---|---|---|---|
| `MISSION.md` | why the user is learning this | every session | the user; the mentor drafts it only with the user's confirmation | A, B, C |
| `AGENTS.md` | how to teach | every session | the user | A, B, C |
| `TEACHING-PROTOCOLS.md` | procedures and formats | when a session needs one | the user | A, B, C |
| `fde-journey-map.md` | the canonical FDE journey | every session | the user | A, B, C |
| `production-performance-incident-study-map.md` | the performance branch | when the journey opens it | the user | A, B, C |
| `RESOURCES.md` | canonical source catalog | before teaching, and on every source claim | the user | A, B, C |
| `EVIDENCE.md` | the evidence ledger | every session | the user | A, B, C |
| `GLOSSARY.md` | earned terms | when a term is earned | the user | A, B, C |
| `casebook/` | real failures per concept | when a case is researched | the user | A, B, C |
| `learning-records/` | evidence of understanding | when a record is earned | the user | A, B, C |

The first seven are the minimum set for a lesson. `GLOSSARY.md`, `casebook/`
and `learning-records/` are created as the first file for them exists (P§1).

In a chat tool, use these files as project sources and keep instructions
short: follow `AGENTS.md`, use `TEACHING-PROTOCOLS.md` when referenced, and
cite the uploaded sources. Add the selected primary sources for the current
unit as well. Generated quizzes, summaries, and audio are practice artifacts;
do not promote them to durable learning records until checked against a cited
source.

### Synchronization

Re-check API, product, model, and security sources before teaching current
claims. When a source changes, update its registry row first, then compare
the affected journey tags, lesson citations, and evidence records. Never
silently replace a source or turn a candidate into evidence.

## P§10. Building a branch map (when the journey lacks lesson-level units)

Use when the readiness check in `AGENTS.md` section 4 finds no usable unit.

1. Read the active journey's goal and gates, `MISSION.md`, and the evidence list.
2. Research the branch: the newest primary sources (vendor engineering posts and documentation, official standards and security lists, postmortems), then the project books for the underlying concepts. Open each page you rely on. Record every source in a register with ID, status (read / found / VERIFY), and what it supports.
3. Write the branch in the format used by `fde-journey-map.md`: phases, units with IDs (`P<phase>.<n>`), dependency statements, source tags (`S#` or `F#`), and explicit proof criteria. Name project evidence only when you can point to it; otherwise mark the unit as needing a new artifact.
4. List gaps where no good source exists and add them to `RESOURCES.md`.
5. Show the tree to the user in compact form. After confirmation, teach the first unit. Do not teach during map building.
