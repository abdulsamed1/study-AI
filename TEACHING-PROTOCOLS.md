# TEACHING-PROTOCOLS.md

Revised 2026-10-09. Templates, procedures, and tool setup that `AGENTS.md` points to as "P§n". Load this file only when you need one of them.
This file holds formats and steps only. Behavioral rules live in `AGENTS.md` and are not repeated here; if the two conflict, `AGENTS.md` wins.
Formats adapted from the `teach` skill by Matt Pocock (github.com/mattpocock/skills, skills/productivity/teach).

## P§1. Workspace layout and file formats

    MISSION.md                      why the user is learning this; one screen at most
    NOTES.md                        user preferences and working notes
    EVIDENCE.md                     supported by evidence / needs learning / must not be claimed
    RESOURCES.md                    verified references / references to verify / coverage gaps
    GLOSSARY.md                     one-line definitions; every lesson uses these terms
    casebook/INDEX.md               concept -> cases -> transferable pattern
    casebook/<concept>.md           researched real failures for one concept
    learning-records/NNNN-slug.md   evidence of understanding
    lessons/NNNN-slug.html          one short lesson each (modes B/C: Markdown in the reply)
    reference/*.html                cheat sheets, sequence diagrams, checklists
    assets/                         shared stylesheet and reusable components

Create directories lazily, when the first file for them exists. In mode B these files exist only as uploads or as the user's notes; state lives as described in `AGENTS.md` section 3.

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
    ## Coverage gaps
    - <area the mission needs where no good source exists yet>

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

**NOTES.md**: the user's stated preferences about how to be taught, in their words, plus working notes. Read it every session.

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

A part is roughly 400-700 words plus a diagram when useful. The source named for the unit is cited in Part 1 and the best primary source is repeated at the end.
Mode A: also write `lessons/NNNN-slug.html`: self-contained, linking the shared stylesheet in `assets/` and the reference sheets, readable and printable. Reuse `assets/` components before writing new ones. Open the file with `xdg-open` on Fedora.
Mode B: Markdown in the reply, one part per message.
Reference sheets (`reference/*.html`) hold the compressed essence of a lesson: checklists, decision tables, sequence diagrams.

## P§4. Dynamic research-driven teaching policy

- Preserve the instructional framework while generating each lecture dynamically around the current learning objective and the learner's demonstrated knowledge, gaps, and goals.
- Reuse a static lecture or use case only when it remains accurate, relevant, and pedagogically useful; do not depend on a fixed lecture for every session.
- When web search is available, use it selectively for current tools, APIs, production implementations, failure analyses, benchmarks, or new practitioner techniques that materially improve the lesson.
- If web search is unavailable, state the limitation clearly and avoid claiming source verification you did not perform.
- Use sources in this order: official technical documentation and engineering blogs; technical publications and reproducible implementations; recognized practitioners and research groups; community discussions used cautiously.
- Integrate the external material into the lesson by connecting it to the problem, system design, trade-offs, failure modes, and a practice challenge. Separate documented facts from source-supported claims and from the mentor's interpretation.
- Keep lectures coherent and practical: prefer a few highly relevant sources over a long list of links or names.

## P§5. Practice sources and retrieval schedule

- Build the practice task from a casebook scenario changed slightly (new constraint, new failure point).
- Warm-ups revisit older records inside new scenarios. Suggested spacing: next session, about a week later, about a month later. Re-asking the same question teaches the question, not the concept.
- Interleave related production decisions during skill practice only, never while the user is still acquiring the concept.
- **Defense drill (decision cards).** Pick one decision defense card (`fde-journey-map.md` §3) and escalate without teaching: what was decided and why; what else was possible; what the accepted tradeoff costs; what would make it wrong; the same decision under one changed constraint (for example half the budget, a stricter latency target, or no managed service). The learner answers without an agent and without the card's `owner's explanation` field. Score on the journey's Depth scale and write the result in the standard learning record (§1), including the card ID, the depth reached, and the first question that exposed a gap.

## P§6. Setting up each tool


**(mode B)**
- Upload `AGENTS.md`, this file, the journey files, `MISSION.md` and `EVIDENCE.md` once, and the books. File limits depend on the plan; check the current limit in OpenAI's help article "Projects in ChatGPT".
- In Project settings, set Memory to Project-only, and enable the account memory settings the article lists. Memory changes can take a few hours to apply. Project memory shows no list, so the mentor confirms recalled state at the start of each session (`AGENTS.md` section 3).
- Project instructions (short, because the full rules are in the uploaded file):

      Follow AGENTS.md in the project files exactly. Use TEACHING-PROTOCOLS.md only when AGENTS.md points to it. The active journey file is the one the user names, otherwise ask.

- Optional, for a reply that must persist verbatim (for example an agreed mission): the response menu offers "Save to project", which adds it as a project source.

- Sources: `AGENTS.md`, this file, the journey files, books, postmortems, `MISSION.md`, `EVIDENCE.md`, and your saved notes.
- Chat configuration (the same two sentences, adjusted for sources only):

      Follow AGENTS.md among the sources, in mode C. Answer only from the sources and cite them.

- NotebookLM keeps no memory of earlier chats. End each session with this block and save it as a note or source:

      Save these notes — <date>
      Learned: <1-3 lines>   Open questions: <lines>   Source to add: <names>
      Record: <what was demonstrated, evidence, next target>

**Workspace (mode A)**
- agentic reads `AGENTS.md` and takes extra files from the `instructions` list in `opencode.jsonc` if the user use OPENCODE. Check the current docs for both, since the syntax changes.
- Keep this file out of the always-loaded list; `AGENTS.md` says when to open it.

## P§7. Maintaining AGENTS.md

Add a rule to `AGENTS.md` only after its absence caused a real mistake; move formats and procedures here instead of growing the core. Journey files and this file cite `AGENTS.md` section numbers and never restate its rules; when you notice a repeated rule, delete the copy in the lower-priority file. Reason to stay lean: a February 2026 ICLR paper (Gloaguen et al., arXiv 2602.11988), cited by the previous version of this file and not re-checked in this revision, reports that repository context files tended to reduce coding-agent success and raised cost. It covers coding agents, not tutoring, so treat it as a reason to be careful, not as a measurement of this setup.
Review `AGENTS.md` after every 10 sessions: delete rules the mentor never needed, and fix the mistakes that recurred.

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
2. Confirm title, publisher, relevance, and URL.
3. Record the date and exact section, chapter, or page in `RESOURCES.md`.
4. Mark it Verified only after those checks; move failed or obsolete entries to
   References to verify or Coverage gaps.

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

The minimum shared file set is:

    MISSION.md
    AGENTS.md
    TEACHING-PROTOCOLS.md
    fde-journey-map.md
    RESOURCES.md
    EVIDENCE.md

In ChatGPT Projects, use the files as project sources and keep instructions
short: follow `AGENTS.md`, use `TEACHING-PROTOCOLS.md` when referenced, and
cite the uploaded sources. In NotebookLM, add the same files as sources, add
the selected primary sources for the current unit, and require notebook
citations. Generated quizzes, summaries, and audio are practice artifacts; do
not promote them to durable learning records until checked against a cited
source.

### Synchronization

Re-check API, product, model, and security sources before teaching current
claims. When a source changes, update its registry row first, then compare
the affected journey tags, lesson citations, and evidence records. Never
silently replace a source or turn a candidate into evidence.

## P§10. Building a branch map (when the journey lacks lesson-level units)

Use when the readiness check in `AGENTS.md` section 5 finds no usable unit.

1. Read the active journey's goal and gates, `MISSION.md`, and the evidence list.
2. Research the branch: the newest primary sources (vendor engineering posts and documentation, official standards and security lists, postmortems), then the project books for the underlying concepts. Open each page you rely on. Record every source in a register with ID, status (read / found / VERIFY), and what it supports.
3. Write the branch in the format used by `fde-journey-map.md`: phases, units with IDs (`P<phase>.<n>`), dependency statements, source tags (`S#` or `F#`), and explicit proof criteria. Name project evidence only when you can point to it; otherwise mark the unit as needing a new artifact.
4. List gaps where no good source exists and add them to `RESOURCES.md`.
5. Show the tree to the user in compact form. After confirmation, teach the first unit. Do not teach during map building.
