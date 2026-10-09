# Source-Grounded FDE Study Pack Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the existing FDE study path into one source-verified, updateable study pack that works in both ChatGPT Projects and NotebookLM.

**Architecture:** Keep `fde-journey-map.md` outcome-first. Put authority and verification metadata in a new `RESOURCES.md`, behavior in `AGENTS.md`, and procedures/tool import rules in `TEACHING-PROTOCOLS.md`. Use source IDs across the map; do not duplicate curricula for the two tools.

**Tech Stack:** Markdown, existing repository conventions, `curl` for URL checks, `git diff --check`, and small shell checks.

---

## File map

- Create: `/home/abdu/production/study-path/RESOURCES.md` — canonical verified/candidate/gap source registry.
- Modify: `/home/abdu/production/study-path/AGENTS.md` — source-grounding, citation, uncertainty, and tool-neutral teaching contract.
- Modify: `/home/abdu/production/study-path/TEACHING-PROTOCOLS.md` — source triage, import, lesson preparation, retrieval, and export procedures.
- Modify: `/home/abdu/production/study-path/fde-journey-map.md` — replace inline source claims/tags with registry IDs and preserve outcome ordering.
- Validate: the four files above plus the existing mission/evidence files; no new runtime test file is needed.

### Task 1: Build the source registry

**Files:**
- Create: `RESOURCES.md`

- [ ] **Step 1: Define the registry contract**

Create these sections in order:

```markdown
# FDE Study Resources

Updated: 2026-10-09

## How to use this file
## Verified sources
## Candidates — do not cite yet
## Gaps
## Update procedure
```

Under “How to use this file”, state that only verified entries may support
lessons, candidates are research leads, gaps are explicit missing coverage,
books may be cited without reproducing copyrighted text, and changing product
claims require current official documentation.

- [ ] **Step 2: Add at least 21 relevant verified sources**

Add a table with exactly these columns:

```markdown
| ID | Source | Publisher | Type | Coverage | Access | Last verified |
|---|---|---|---|---|---|---|
```

Populate it with at least 21 real, relevant sources across these categories:

- official model/API documentation and courses;
- academic or university tutorials for software, distributed systems, and
  evaluation foundations;
- books for software architecture, distributed systems, AI engineering, and
  agent systems;
- official engineering articles on agents, context, tools, MCP, and evals;
- OWASP security guidance;
- official incident reports and production case studies;
- employer/job-role evidence for FDE expectations.

Every row must include a stable URL or an explicit “book access” description,
one-sentence coverage, access status, and the current verification date. Do not
count a duplicate edition, a generic search result, or an unverified title.

- [ ] **Step 3: Record candidates and gaps without using them as evidence**

Add a short candidate list for sources still needing verification and a gaps
list containing, at minimum, primary RAG guidance and primary statistics for
evaluation. State that journey lessons cannot cite either section.

- [ ] **Step 4: Add the update procedure**

Specify this four-step process:

```markdown
1. Open the publisher's canonical page.
2. Confirm title, publisher, relevance, and URL.
3. Record the date and exact section/chapter used.
4. Move failed or obsolete entries to Candidates or Gaps; do not silently retain them as verified.
```

- [ ] **Step 5: Validate the registry**

Run:

```bash
cd /home/abdu/production/study-path
test "$(grep -cE '^\| S[0-9]+ \|' RESOURCES.md)" -ge 21
! grep -nE 'TODO|TBD|FIXME' RESOURCES.md
git diff --check
```

Expected: the count check succeeds, no placeholder lines are printed, and
`git diff --check` exits successfully.

- [ ] **Step 6: Commit the registry**

```bash
git add RESOURCES.md
git commit -m "docs: add verified FDE resource registry"
```

### Task 2: Tighten the mentor contract

**Files:**
- Modify: `AGENTS.md` in sections 2, 4, 5, and 10-12 as applicable

- [ ] **Step 1: Add the source authority rule**

Add a rule that `RESOURCES.md` is the canonical catalog; lessons may cite only
verified IDs; candidates and gaps are not evidence; every factual lesson claim
must name the source and section/chapter where available. Preserve the
Pocock-inspired loop: diagnose, teach, retrieve, practise, give feedback, then
space and re-test; do not advance because a page was read.

- [ ] **Step 2: Separate fact, synthesis, and practice**

Require lesson text to label:

```markdown
**Source-backed fact:** ...
**Mentor synthesis:** ...
**Practice:** ...
```

Require the mentor to say “I could not verify this” when current official
documentation is unavailable, rather than filling the gap from model memory.

- [ ] **Step 3: Define the shared tool contract**

State that ChatGPT Projects and NotebookLM use the same mission, journey,
registry, and evidence files. ChatGPT uses project instructions plus uploaded
files and treats recalled memory as unverified. NotebookLM uses notebook
citations and treats generated study aids as practice artifacts, not sources.

- [ ] **Step 4: Preserve learning and evidence boundaries**

State that the mentor does not make the user read every source, does not
advance because a topic was mentioned, and never records production claims
that the evidence ledger cannot show.

- [ ] **Step 5: Validate the contract**

Run:

```bash
cd /home/abdu/production/study-path
grep -n "RESOURCES.md\|verified\|NotebookLM\|ChatGPT Project\|I could not verify" AGENTS.md
git diff --check
```

Expected: each required policy concept has at least one matching line and the
diff check succeeds.

- [ ] **Step 6: Commit the contract**

```bash
git add AGENTS.md
git commit -m "docs: define source-grounded mentor contract"
```

### Task 3: Add reusable procedures

**Files:**
- Modify: `TEACHING-PROTOCOLS.md`

- [ ] **Step 1: Add source triage procedure**

Add a procedure that checks a source's canonical page, publisher, date,
coverage, access, and exact lesson section before marking it verified.

- [ ] **Step 2: Add lesson preparation procedure**

Require the mentor to select one journey unit, open only its referenced
verified sources, record exact citations, and prepare one scenario and one
practice task. State that the whole source library is not loaded into every
lesson.

- [ ] **Step 3: Add import/export instructions**

Document the minimum file set for both tools:

```markdown
MISSION.md
AGENTS.md
TEACHING-PROTOCOLS.md
fde-journey-map.md
RESOURCES.md
EVIDENCE.md
```

Document that selected sources are added only when needed, and that generated
notes must be checked against the source before being promoted to durable
learning records.

- [ ] **Step 4: Add update and synchronization procedure**

Require a dated source re-check for API/product/model claims and a manual
comparison before changing the registry, journey tags, or evidence ledger.

- [ ] **Step 5: Validate the procedures**

Run:

```bash
cd /home/abdu/production/study-path
grep -n "source\|NotebookLM\|ChatGPT\|citation\|verified" TEACHING-PROTOCOLS.md
! grep -nE 'TODO|TBD|FIXME' TEACHING-PROTOCOLS.md
git diff --check
```

Expected: the procedure concepts are present, no placeholder lines are
printed, and the diff check succeeds.

- [ ] **Step 6: Commit the procedures**

```bash
git add TEACHING-PROTOCOLS.md
git commit -m "docs: add study-source operating procedures"
```

### Task 4: Wire the journey map to source IDs

**Files:**
- Modify: `fde-journey-map.md`

- [ ] **Step 1: Replace the inline source register**

Replace the map's detailed source register with a short reference to
`RESOURCES.md`, retaining only lesson-to-source ID mappings in the journey.
Do not retain “Read”, “Found”, or “Unchecked” claims in the active map.

- [ ] **Step 2: Resolve current source gaps explicitly**

For every lesson that currently has a source gap, either assign a verified
registry ID or mark the lesson as a source gap that must be resolved before
teaching. Do not invent IDs and do not promote candidates.

- [ ] **Step 3: Preserve the outcome and gate structure**

Keep the existing levels, lesson IDs, priorities, evidence/NO-EVIDENCE labels,
phase gates, and capstone requirements unless a change is required to remove
an unsupported source claim.

- [ ] **Step 4: Check all lesson source IDs**

Run:

```bash
cd /home/abdu/production/study-path
grep -oE 'S[0-9]+' fde-journey-map.md | sort -u > /tmp/fde-map-ids
grep -oE '^\| S[0-9]+' RESOURCES.md | sed -E 's/^\| (S[0-9]+)$/\1/' | sort -u > /tmp/fde-resource-ids
comm -23 /tmp/fde-map-ids /tmp/fde-resource-ids
git diff --check
```

Expected: `comm` prints nothing. Remove the temporary files after the check:

```bash
rm -f /tmp/fde-map-ids /tmp/fde-resource-ids
```

- [ ] **Step 5: Commit the map wiring**

```bash
git add fde-journey-map.md
git commit -m "docs: link FDE journey to verified source IDs"
```

### Task 5: Final pack validation

**Files:**
- Validate: `AGENTS.md`, `TEACHING-PROTOCOLS.md`, `RESOURCES.md`,
  `fde-journey-map.md`, `MISSION.md`, `EVIDENCE.md`

- [ ] **Step 1: Check required files**

```bash
cd /home/abdu/production/study-path
for file in AGENTS.md TEACHING-PROTOCOLS.md RESOURCES.md fde-journey-map.md MISSION.md EVIDENCE.md; do
  test -s "$file"
done
```

Expected: exit code 0.

- [ ] **Step 2: Check source count and prohibited placeholders**

```bash
test "$(grep -cE '^\| S[0-9]+ \|' RESOURCES.md)" -ge 21
! grep -nE 'TODO|TBD|FIXME' AGENTS.md TEACHING-PROTOCOLS.md RESOURCES.md fde-journey-map.md
```

Expected: both commands exit successfully.

- [ ] **Step 3: Check repository diff integrity**

```bash
git diff --check HEAD~4..HEAD
git status --short
```

Expected: no whitespace errors; only the intended documentation commits are
present or the working tree is clean.

- [ ] **Step 4: Record completion**

Update the session learning/evidence state only with what was actually
verified: source registry count, validation commands, and files changed. Do
not claim that the user learned the material or that any capstone capability
was demonstrated.

- [ ] **Step 5: Commit any final corrections**

```bash
git add AGENTS.md TEACHING-PROTOCOLS.md RESOURCES.md fde-journey-map.md
git commit -m "docs: validate FDE study pack"
```
