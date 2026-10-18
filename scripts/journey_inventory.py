#!/usr/bin/env python3
"""Structural validator for fde-journey-map.md.

Read-only: parses the roadmap and checks its structural contract.

  python3 scripts/journey_inventory.py            # human-readable report
  python3 scripts/journey_inventory.py --json     # machine-readable
  python3 scripts/journey_inventory.py --strict    # non-zero exit on violations

Field semantics (see fde-journey-map.md section 3):
  Depends on     hard prerequisite; must appear EARLIER in file order
  Coupled with   non-blocking relationship; may point either direction

Checks: cycles, forward dependencies by FILE ORDER, unknown or missing IDs,
Coupled-with targets, priority/source presence, exactly one primary proof,
ledger == unit list, gate coverage, retrieval-table coverage, oversized units,
[TOC] vs (read) counts, author-name citations that should be S#/F# IDs, and
near-duplicate proof detection (Jaccard) for the D1-D10 overlap audit.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP_PATH = ROOT / "fde-journey-map.md"
RES_PATH = ROOT / "RESOURCES.md"

UNIT_HEAD = re.compile(
    r"^\s*-\s+\*\*(?P<id>P\d+\.\d+[a-z]?)\s*[—–-]\s*(?P<title>.+?)\*\*", re.M)
PRIORITY = re.compile(r"\*\*Priority:\*\*\s*(?P<p>must-have|important|useful)")
DEPENDS = re.compile(r"Depends on:\s*(?P<seg>[^*]{0,300}?)(?:\*\*|\.\s|;|\Z)")
COUPLED = re.compile(r"Coupled with:\s*(?P<seg>[^*]{0,300}?)(?:\*\*|\.\s|;|\Z)")
RANGE = re.compile(r"P(?P<p1>\d+)\.(?P<n1>\d+)(?P<s1>[a-z])?\s*[—–-]\s*P?(?P<p2>\d+)\.(?P<n2>\d+)(?P<s2>[a-z])?")
SINGLE = re.compile(r"\bP(?P<phase>\d+)\.(?P<num>\d+)(?P<sfx>[a-z])?\b")
SOURCE_TAG = re.compile(r"\b([SF])(\d{1,2})\b")
PROOF_FIELD = re.compile(r"\*\*(Proof|Artifact):\*\*")
TOMBSTONE = re.compile(r"merged into|split into", re.I)
INTERNAL_REFS = ("AGENTS.md", "EVIDENCE.md", "RESOURCES.md",
                 "production-performance-incident-study-map.md", "TEACHING-PROTOCOLS.md")
AUTHOR_NAMES = ["Barnett", "Aim Labs", "Seven Failure Points", "Kleppmann",
                "Richards", "Ford", "Newman", "Vitillo", "Burns", "Gorton", "Sadalage",
                "Dehghani", "Dahl", "arXiv"]
STOPWORDS = {"the", "a", "an", "and", "or", "to", "of", "in", "for", "with", "is", "are",
             "that", "this", "it", "on", "by", "from", "at", "as", "one", "not", "be",
             "its", "each", "any", "own", "into", "than", "then", "which", "when", "where"}


def uid(phase: int, num: int, sfx: str | None) -> str:
    return f"P{phase}.{num}{sfx or ''}"


def expand_range(p1: int, n1: int, s1: str | None, p2: int, n2: int, s2: str | None) -> list[str]:
    out: list[str] = []
    letters = ["a", "b", "c", "d", "e"]
    if p1 != p2:
        for ph, lo, hi in ((p1, n1, 99), (p2, 1, n2)):
            for n in range(lo, hi + 1):
                out.append(uid(ph, n, None))
            if s2:
                out.append(uid(p2, n2, s2))
        return out
    if s1 or s2:
        lo = letters.index(s1) if s1 else 0
        hi = letters.index(s2) if s2 else 0
        return [uid(p1, n1, letters[i]) for i in range(lo, hi + 1)]
    return [uid(p1, n, None) for n in range(n1, n2 + 1)]


def parse_ids(seg: str) -> list[str]:
    found: list[str] = []
    rest = seg
    for rm in RANGE.finditer(seg):
        found += expand_range(int(rm.group("p1")), int(rm.group("n1")), rm.group("s1"),
                              int(rm.group("p2")), int(rm.group("n2")), rm.group("s2"))
    rest = RANGE.sub(" ", rest)
    for sm in SINGLE.finditer(rest):
        found.append(uid(int(sm.group("phase")), int(sm.group("num")), sm.group("sfx")))
    return sorted(set(found))


def parse_units(text: str) -> tuple[list[dict], list[dict]]:
    """Return (units in file order, tombstones)."""
    starts = [(m.start(), m.group("id"), m.group("title"))
              for m in re.finditer(r"^\s*-\s+\*\*(?P<id>P\d+\.\d+[a-z]?)\s*[—–-]\s*(?P<title>.+?)\*\*",
                                  text, re.M)]
    units: list[dict] = []
    tombstones: list[dict] = []
    for i, (pos, unit_id, title) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        block = text[pos:end]
        # stop at the next markdown heading so trailing sections are not swallowed
        head_stop = re.search(r"^#{1,6} ", block, re.M)
        if head_stop:
            block = block[:head_stop.start()]
        body = block
        first_line = block.splitlines()[0]
        if TOMBSTONE.search(title) or TOMBSTONE.search(block[:300]):
            tombstones.append({"id": unit_id, "title": title.strip()})
            continue
        pm = PRIORITY.search(body)
        dm = DEPENDS.search(body)
        cm = COUPLED.search(body)
        deps = [] if (dm and dm.group("seg").strip().lower().startswith("none")) else (
            parse_ids(dm.group("seg")) if dm else [])
        coupled = parse_ids(cm.group("seg")) if cm else []
        proofs = PROOF_FIELD.findall(body)
        proof = ""
        pf = PROOF_FIELD.search(body)
        if pf:
            proof = body[pf.start():].strip()
        sources = sorted({f"{m.group(1)}{int(m.group(2))}" for m in SOURCE_TAG.finditer(body)},
                         key=lambda s: (s[0], int(s[1:])))
        head = body.split("**Proof:**")[0].split("**Artifact:**")[0].split("Sources:")[0].split("Source:")[0]
        units.append({
            "id": unit_id,
            "title": title.strip(),
            "priority": pm.group("p") if pm else None,
            "depends_text": dm.group("seg").strip() if dm else None,
            "deps": [d for d in deps if d != unit_id],
            "coupled_text": cm.group("seg").strip() if cm else None,
            "coupled": [c for c in coupled if c != unit_id],
            "proof_fields": len(proofs),
            "proof_kind": proofs[0] if proofs else None,
            "proof_words": len(proof.split()),
            "total_words": len(head.split()) + len(proof.split()),
            "sources": sources,
            "has_source": bool(sources) or any(r in block for r in INTERNAL_REFS),
            "toc": len(re.findall(r"\[TOC\]", block)),
            "read": len(re.findall(r"\(read\)", block)),
            "impl_unit": bool(re.search(r"implementation unit", block, re.I)),
            "names": [n for n in AUTHOR_NAMES if n.lower() in block.lower()],
        })
    return units, tombstones


def find_cycles(deps: dict[str, list[str]]) -> list[list[str]]:
    cycles, state, stack = [], {}, []

    def visit(node: str) -> None:
        state[node] = 1
        stack.append(node)
        for nxt in deps.get(node, []):
            if nxt not in deps:
                continue
            if state.get(nxt, 0) == 0:
                visit(nxt)
            elif state.get(nxt) == 1:
                cycles.append(stack[stack.index(nxt):] + [nxt])
        stack.pop()
        state[node] = 2

    for n in deps:
        if state.get(n, 0) == 0:
            visit(n)
    return cycles


def tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z][a-z\-']+", text.lower())
            if len(w) > 3 and w not in STOPWORDS}


def jaccard(a: set[str], b: set[str]) -> float:
    return len(a & b) / len(a | b) if (a | b) else 0.0


def build_report() -> dict:
    text = MAP_PATH.read_text(encoding="utf-8")
    units, tombstones = parse_units(text)
    order = {u["id"]: i for i, u in enumerate(units)}
    ids = [u["id"] for u in units]
    by_id = {u["id"]: u for u in units}

    # phase numbering continuity
    gaps: list[str] = []
    by_phase: dict[int, list[dict]] = {}
    for u in units:
        ph = int(re.match(r"P(\d+)\.", u["id"]).group(1))
        by_phase.setdefault(ph, []).append(u)
    for ph, us in sorted(by_phase.items()):
        nums = sorted({int(re.search(r"\.(\d+)", u["id"]).group(1)) for u in us})
        for n in nums:
            if n > 1 and n - 1 not in nums:
                gaps.append(f"Phase {ph}: P{ph}.{n} exists but P{ph}.{n - 1} does not")

    cycles = find_cycles({u["id"]: u["deps"] for u in units})

    forward, unknown_dep, coupled_missing = [], [], []
    for u in units:
        for d in u["deps"]:
            if d not in by_id:
                unknown_dep.append(f"{u['id']} -> {d}")
            elif order[d] > order[u["id"]]:
                forward.append({"unit": u["id"], "depends_on": d,
                                "unit_line": order[u["id"]] + 1, "dep_line": order[d] + 1})
        for c in u["coupled"]:
            if c not in by_id:
                coupled_missing.append(f"{u['id']} -> {c}")

    dependents: dict[str, set[str]] = {u["id"]: set() for u in units}
    for u in units:
        for d in u["deps"]:
            if d in dependents:
                dependents[d].add(u["id"])

    ledger = re.search(r"## 8\. Progress ledger template.*?```text\n(.*?)```", text, re.S)
    ledger_ids: list[str] = []
    if ledger:
        ledger_ids = re.findall(r"\bP\d+\.\d+[a-z]?\b", ledger.group(1))

    gates = [{"gate": m.group(1), "name": m.group(2).strip(), "required_proof": m.group(3).strip(),
              "phases": m.group(4).strip()}
             for m in re.finditer(r"^\|\s*\*\*(G\d+)\s*—\s*([^|]+?)\*\*\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|",
                                  text, re.M)]
    gate_phases: set[int] = set()
    for g in gates:
        for n in re.findall(r"(\d+)", g["phases"].replace("Phase", "")):
            gate_phases.add(int(n))
        for a, b in re.findall(r"(\d+)\s*[—–-]\s*(\d+)", g["phases"]):
            gate_phases.update(range(int(a), int(b) + 1))

    retrieval_table = re.search(r"^#{2,6} ?Retrieval table\s*\n([^#]*?)(?:\n#+ |\Z)", text, re.M | re.S)
    retrieval_ids: set[str] = set()
    if retrieval_table:
        retrieval_ids = {x for x in re.findall(r"\bP\d+\.\d+[a-z]?\b", retrieval_table.group(1))}
    must_have = [u["id"] for u in units if u["priority"] == "must-have"]

    res = RES_PATH.read_text(encoding="utf-8")
    registered = (set(re.findall(r"^\|\s*(S\d+)\s*\|", res, re.M))
                  | set(re.findall(r"^\|\s*(F\d+)\s*\|", res, re.M))
                  | set(re.findall(r"^\s*(?:-\s*)?\*\*(S\d+)\s+—", res, re.M))
                  | set(re.findall(r"^\s*-\s*\*\*(F\d+)\b", res, re.M)))
    cited = {s for u in units for s in u["sources"]}

    proofs = {u["id"]: tokens(re.search(r"\*\*(?:Proof|Artifact):\*\*.*", by_id_text(text, u["id"]), re.S).group(0))
              for u in units if by_id_text(text, u["id"])}
    overlap = []
    for i, a in enumerate(units):
        for b in units[i + 1:]:
            ta, tb = proofs.get(a["id"]), proofs.get(b["id"])
            if not ta or not tb or len(ta) < 8 or len(tb) < 8:
                continue
            score = jaccard(ta, tb)
            if score >= 0.55:
                overlap.append({"pair": f"{a['id']}/{b['id']}", "jaccard": round(score, 2)})

    rep: dict = {
        "unit_count": len(units),
        "ids_in_file_order": ids,
        "tombstones": tombstones,
        "phase_numbering_gaps": gaps,
        "duplicate_ids": sorted({i for i in ids if ids.count(i) > 1}),
        "cycles": cycles,
        "forward_dependencies_by_file_order": forward,
        "unknown_dependency_refs": unknown_dep,
        "coupled_with_missing_targets": coupled_missing,
        "units_without_priority": [u["id"] for u in units if not u["priority"]],
        "units_without_source": [u["id"] for u in units if not u["has_source"]],
        "units_without_exactly_one_proof": [f"{u['id']}({u['proof_fields']})" for u in units
                                            if u["proof_fields"] != 1],
        "ledger_missing": [i for i in ids if i not in ledger_ids],
        "ledger_extra": [i for i in ledger_ids if i not in by_id],
        "ledger_duplicates": sorted({i for i in ledger_ids if ledger_ids.count(i) > 1}),
        "phases_without_gate": sorted({int(re.match(r"P(\d+)\.", i).group(1)) for i in ids} - gate_phases),
        "gates": gates,
        "retrieval_table_found": bool(retrieval_table),
        "must_have_units": must_have,
        "must_have_without_retrieval_entry": [i for i in must_have if i not in retrieval_ids],
        "units_with_author_names": [{"id": u["id"], "names": u["names"]}
                                    for u in units if u["names"]],
        "sources_cited_not_registered": sorted(cited - registered),
        "sources_registered_not_cited": sorted(registered - cited,
                                              key=lambda s: (s[0], int(s[1:]))),
        "toc_tag_total": len(re.findall(r"\[TOC\]", text)),
        "toc_tags_in_units": sum(u["toc"] for u in units),
        "read_tag_total": len(re.findall(r"\(read\)", text)),
        "oversized_over_150": [{"id": u["id"], "words": u["total_words"], "labelled": u["impl_unit"]}
                               for u in units if u["total_words"] > 150],
        "oversized_over_200": [{"id": u["id"], "words": u["total_words"]}
                               for u in units if u["total_words"] > 200],
        "proof_overlap_candidates": sorted(overlap, key=lambda x: -x["jaccard"]),
        "dup_audit": dup_audit(text),
        "dependents": {i: sorted(s) for i, s in dependents.items() if s},
        "units": [{k: v for k, v in u.items() if k != "names"} for u in units],
    }
    rep["probe_report"] = probe_report(text, rep)
    return rep


def by_id_text(text: str, unit_id: str) -> str:
    m = re.search(rf"^\s*-\s+\*\*{re.escape(unit_id)}\s*[—–-].*?(?=^\s*-\s+\*\*P\d|^#{1,6} |\Z)",
                  text, re.M | re.S)
    return m.group(0) if m else ""


# Stage 1 findings D1-D10: pairs whose objective or proof overlapped before the
# rewrite. Re-run with --dupes to confirm each no longer fires.
DUP_PAIRS = [
    ("D1", "P2.2", "P3.3"),
    ("D2", "P2.3", "P3.6"),
    ("D2b", "P3.4", "P3.7"),
    ("D4", "P4.5", "P8.3"),
    ("D5", "P5.7", "P9.7"),
    ("D6", "P7.5b", "P10.4"),
    ("D7", "P0.3", "P10.3"),
    ("D8", "P10.2", "P11.6"),
    ("D9", "P6.4", "P16.1"),
]


def dup_audit(text: str) -> list[dict]:
    out = []
    for tag, a, b in DUP_PAIRS:
        ta, tb = by_id_text(text, a), by_id_text(text, b)
        if not ta or not tb:
            out.append({"decision": tag, "pair": f"{a}/{b}", "status": "unit or tombstone missing",
                        "jaccard": None})
            continue
        out.append({"decision": tag, "pair": f"{a}/{b}",
                    "status": "tombstone" if TOMBSTONE.search(ta) or TOMBSTONE.search(tb) else "compared",
                    "jaccard": round(jaccard(tokens(ta), tokens(tb)), 3)})
    return out


def probe_report(text: str, rep: dict) -> list[dict]:
    """Mechanical checks for the approved decisions (D, R, A, E-J)."""
    tomb = {t["id"] for t in rep["tombstones"]}
    unit_map = {u["id"]: by_id_text(text, u["id"]) for u in rep["units"]} if False else {}
    blocks = {}
    for t in re.finditer(r"^\s*-\s+\*\*(?P<id>P\d+\.\d+[a-z]?)\s*[——–-]", text, re.M):
        blocks[t.group("id")] = by_id_text(text, t.group("id"))

    def has(unit: str, needle: str) -> bool:
        return needle.lower() in blocks.get(unit, "").lower()

    def unit_or_tombstone(unit: str, needle: str) -> bool:
        return needle.lower() in text.lower() and (unit in tomb or has(unit, needle))

    probes = []

    def add(name: str, ok: bool, detail: str) -> None:
        probes.append({"probe": name, "result": "pass" if ok else "FAIL", "detail": detail})

    # D1: P3.3 merged into P2.2; P2.2 keeps the trust-boundary proof
    add("D1 P3.3=tombstone", "P3.3" in tomb, str(tomb))
    add("D1 P2.2 unique proof", has("P2.2", "table of valid/invalid fixtures"),
        "fixture table stays only in P2.2")
    add("D11 P3.3 dependents repointed", has("P4.6", "P2.2") and has("P11.3", "P2.2"),
        "P4.6/P11.3 cite P2.2 instead of P3.3")
    # D2: P2.3 reframed; runtime leak evidence stays in P3.6
    add("D2 P3.6 owns leak evidence", has("P3.6", "runtime evidence"), "leak/shutdown evidence in P3.6")
    add("D2 P2.3 contract framing", has("P2.3", "contract") or has("P2.3", "proven by P3.6"),
        "P2.3 refers to P3.6")
    # D3: single home for secrets
    add("D3 P3.4 keeps lockfile/scripts", has("P3.4", "lockfile"), "P3.4 scope narrowed")
    add("D3 P3.7 owns secrets", has("P3.7", "secret"), "P3.7 owns secrets/redaction")
    # D4/D5: boundary sentences
    add("D4 P8.3 references P4.5", has("P8.3", "P4.5"), "P8.3 -> P4.5 boundary")
    add("D5 P9.7 retitled", "backups" not in blocks.get("P9.7", "P9.7").lower() if "P9.7" in blocks else "P9.7" in tomb,
        "title no longer claims backups")
    # F: one failure-matrix template, reuse elsewhere
    add("F template in P6.4", has("P6.4", "containment | recovery | owner"),
        "template defined in P6.4")
    for reuse_unit in ("P8.1", "P9.7", "P16.1", "P10.4c", "P4.8b"):
        add(f"F {reuse_unit} reuse", has(reuse_unit, "reus"), f"{reuse_unit} says reuse + delta")
    # A: coupled-with semantics documented
    add("A Coupled with documented", "Coupled with" in text, "field documented in section 3")
    # E: retrieval table exists
    add("E retrieval table", rep["retrieval_table_found"], "table present in section 3")
    # R2: forward deps converted
    add("R2 P13.5 no Depends on P15.2", not has("P13.5", "Depends on: P15.2"),
        "P15.2 moved to Coupled with")
    add("R2 P13.6 no Depends on P14.1", not has("P13.6", "Depends on: P14.1"),
        "P14.x moved to Coupled with")
    # D10: text dedupe
    n_python = len(re.findall(r"\bPython\b", text))
    add("G/H Python statements <=5", n_python <= 5, f"count={n_python}")
    s22_full = sum(1 for ln in text.splitlines() if re.search(r"2026-10-31|2026-11-30", ln))
    add("H S22 full note once", s22_full <= 1, f"note lines={s22_full}")
    add("I gaps -> RESOURCES pointer", "RESOURCES.md coverage gaps" in text, "section 7 points to RESOURCES.md")
    # J: IDs instead of author names
    names = [c for c in rep["units_with_author_names"]]
    add("J no author-name citations", not names, str(names))
    return probes


def violations(rep: dict) -> list[str]:
    v: list[str] = []
    for key in ("phase_numbering_gaps", "duplicate_ids", "cycles", "unknown_dependency_refs",
                "coupled_with_missing_targets", "units_without_priority", "units_without_source",
                "units_without_exactly_one_proof", "ledger_missing", "ledger_extra",
                "ledger_duplicates", "phases_without_gate", "must_have_without_retrieval_entry",
                "sources_cited_not_registered"):
        if rep[key]:
            v.append(f"{key}: {rep[key]}")
    if rep["forward_dependencies_by_file_order"]:
        v.append(f"forward_dependencies_by_file_order: {rep['forward_dependencies_by_file_order']}")
    if rep["units_with_author_names"]:
        v.append(f"units_with_author_names: {rep['units_with_author_names']}")
    return v


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    rep = build_report()

    if args.json:
        print(json.dumps(rep, indent=2, ensure_ascii=False))
        return 1 if (args.strict and violations(rep)) else 0

    print(f"units={rep['unit_count']}  tombstones={len(rep['tombstones'])}  "
          f"toc_tags={rep['toc_tag_total']} (in units: {rep['toc_tags_in_units']})  "
          f"read_tags={rep['read_tag_total']}")
    print("\n-- units in file order --")
    for u in rep["units"]:
        flags = []
        if u["impl_unit"]:
            flags.append("impl-unit")
        if u["total_words"] > 150:
            flags.append(f"OVERSIZED:{u['total_words']}w")
        if u["coupled"]:
            flags.append("coupled:" + ",".join(u["coupled"]))
        print(f"  {u['id']:8} {str(u['priority']):10} proof={u['proof_fields']} "
              f"src={','.join(u['sources']) or '-':22} toc={u['toc']} read={u['read']} "
              f"{' '.join(flags)}")
    if rep["tombstones"]:
        print("\n-- tombstones --")
        for t in rep["tombstones"]:
            print(f"  {t['id']}: {t['title']}")

    print("\n== VIOLATIONS ==")
    v = violations(rep)
    print("  none" if not v else "")
    for item in v:
        print(f"  {item}")

    print("\n-- info --")
    print(f"  ledger == units: {'OK' if not (rep['ledger_missing'] or rep['ledger_extra']) else 'MISMATCH'}")
    print(f"  retrieval table: {'found' if rep['retrieval_table_found'] else 'MISSING'}; "
          f"must-have without entry: {rep['must_have_without_retrieval_entry'] or 'none'}")
    print(f"  sources registered not cited: {rep['sources_registered_not_cited'] or 'none'}")
    print(f"  sources cited not registered: {rep['sources_cited_not_registered'] or 'none'}")
    print(f"  oversized >150: {[(o['id'], o['words'], o['labelled']) for o in rep['oversized_over_150']] or 'none'}")
    print(f"  oversized >200: {[(o['id'], o['words']) for o in rep['oversized_over_200']] or 'none'}")
    print(f"  proof overlap candidates (jaccard>=0.55): {rep['proof_overlap_candidates'] or 'none'}")
    print("  -- dup audit (Stage 1 decisions D1-D10) --")
    for d in rep["dup_audit"]:
        print(f"    {d['decision']:4} {d['pair']:10} {d['status']:24} jaccard={d['jaccard']}")
    print("  -- decision probes --")
    for p in rep["probe_report"]:
        print(f"    {p['result']:4} {p['probe']}  ({p['detail']})")
    return 1 if (args.strict and v) else 0


if __name__ == "__main__":
    sys.exit(main())