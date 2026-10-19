#!/usr/bin/env python3
"""Extract chapter text from the local epub books/ for source grounding.

Usage:
  python3 scripts/epub_chapters.py list <book-fragment>     # spine order + titles
  python3 scripts/epub_chapters.py toc <book-fragment>       # nav/toc entries
  python3 scripts/epub_chapters.py read <book-fragment> <n>  # plain text of spine item n
"""
from __future__ import annotations

import html
import re
import sys
import zipfile
from pathlib import Path

BOOKS = Path(__file__).resolve().parent.parent / "books"


def find_book(fragment: str) -> Path:
    for p in sorted(BOOKS.glob("*.epub")):
        if fragment.lower() in p.name.lower():
            return p
    raise SystemExit(f"no book matching {fragment!r} in {BOOKS}")


def strip_tags(xhtml: str) -> str:
    xhtml = re.sub(r"<head.*?</head>", " ", xhtml, flags=re.S | re.I)
    xhtml = re.sub(r"<style.*?</style>", " ", xhtml, flags=re.S | re.I)
    xhtml = re.sub(r"<(p|div|br|h[1-6]|li|tr)\b[^>]*>", "\n", xhtml, flags=re.I)
    xhtml = re.sub(r"<[^>]+>", " ", xhtml)
    xhtml = html.unescape(xhtml)
    xhtml = re.sub(r"[ \t\xa0]+", " ", xhtml)
    xhtml = re.sub(r"\n\s*\n\s*\n+", "\n\n", xhtml)
    return xhtml.strip()


def spine_items(zf: zipfile.ZipFile) -> list[str]:
    names = zf.namelist()
    container = next((n for n in names if n.endswith("META-INF/container.xml")), None)
    opf_path = None
    if container:
        c = zf.read(container).decode("utf-8", "ignore")
        m = re.search(r"full-path\s*=\s*[\"']([^\"']+)[\"']", c)
        if m:
            opf_path = m.group(1)
    if not opf_path:
        opf_path = next((n for n in names if n.endswith(".opf")), None)
    if not opf_path:
        return []
    opf = zf.read(opf_path).decode("utf-8", "ignore")
    manifest = dict(re.findall(r"<item\b[^>]*id=[\"']([^\"']+)[\"'][^>]*href=[\"']([^\"']+)[\"']", opf))
    manifest.update({i: h for h, i in re.findall(r"<item\b[^>]*href=[\"']([^\"']+)[\"'][^>]*id=[\"']([^\"']+)[\"']", opf)})
    order = re.findall(r"<itemref\b[^>]*idref=[\"']([^\"']+)[\"']", opf)
    base = opf_path.rsplit("/", 1)[0] if "/" in opf_path else ""
    out = []
    for idref in order:
        href = manifest.get(idref)
        if not href:
            continue
        full = f"{base}/{href}" if base else href
        full = re.sub(r"[^/]+/\.\./", "", full)
        if full in names:
            out.append(full)
    return out


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    cmd, frag = sys.argv[1], sys.argv[2]
    path = find_book(frag)
    with zipfile.ZipFile(path) as zf:
        items = spine_items(zf)
        if cmd == "list":
            for i, item in enumerate(items, 1):
                head = strip_tags(zf.read(item).decode("utf-8", "ignore"))[:120]
                print(f"{i:3} {item}\n    {head}")
        elif cmd == "toc":
            nav = next((n for n in zf.namelist() if re.search(r"(nav|toc)\.x?html$", n, re.I)), None)
            if nav:
                print(strip_tags(zf.read(nav).decode("utf-8", "ignore")))
            else:
                print("no nav item; using spine heads")
        elif cmd == "read":
            idx = int(sys.argv[3])
            item = items[idx - 1]
            print(strip_tags(zf.read(item).decode("utf-8", "ignore")))
        else:
            print(__doc__)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
