#!/usr/bin/env python3
"""
The library: one repository, several books, one build system.

Every tool in tools/ resolves its paths through here rather than assuming it
sits at the repository root, because it no longer does. A book is a directory
under books/ containing book.json — its title, its curriculum, and which
features of the machinery it actually wants. The physics book wants all of
them; a book with no equations in it should not inherit KaTeX, equation
numbering, the Math Ledger or the flag register just because it is a neighbour.

    from library import ROOT, books, book

    for b in books():          # every book in the library, in reading order
        print(b.slug, b.title, len(b.flat))

Paths are absolute so a tool can be run from anywhere:

    python3 tools/webbuild.py
    cd tools && python3 webbuild.py
"""
import io
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = os.path.join(ROOT, "books")
SHARED = os.path.join(ROOT, "shared")
ASSETS = os.path.join(SHARED, "assets")
VENDOR = os.path.join(SHARED, "vendor")
DOCS = os.path.join(ROOT, "docs")

# Reading order of the library itself. A book absent from here still builds; it
# simply sorts after the named ones, so adding a book cannot silently drop it.
ORDER = ["newton-to-mtheory", "the-long-argument"]


def read(path):
    """UTF-8 always. The default encoding is cp1252 on Windows, which cannot
    read a chapter containing ⚑ or −, and that is not a property of the book."""
    with io.open(path, encoding="utf-8") as fh:
        return fh.read()


def write(path, text):
    """UTF-8, and LF regardless of platform. Without newline='' Python rewrites
    every \\n as \\r\\n on Windows, so the same source would build to different
    bytes on different machines and docs/ would churn on every build."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


class Book:
    """One book: where its source lives, what it contains, what it wants built."""

    def __init__(self, slug):
        self.slug = slug
        self.dir = os.path.join(BOOKS, slug)
        cfg = json.loads(read(os.path.join(self.dir, "book.json")))
        self.cfg = cfg
        self.title = cfg["title"]
        self.brand = cfg.get("brand", cfg["title"])
        self.eyebrow = cfg.get("eyebrow", "")
        self.tagline = cfg.get("tagline", "")
        self.thesis = cfg.get("thesis", "")
        self.shell = cfg.get("shell", "full")
        self.features = cfg.get("features", {})
        self.theme = cfg.get("theme", {})

        self.src = os.path.join(self.dir, "src")
        self.reports = os.path.join(self.dir, "reports")
        self.plans = os.path.join(self.dir, "plans")
        self.out = os.path.join(DOCS, slug)

        self.parts = json.loads(read(os.path.join(self.dir, cfg.get("curriculum", "curriculum.json"))))
        # (num, slug, title, part label, is_math) — the shape the build wants.
        self.flat = [
            (c["num"], c["slug"], c["title"], p["label"], bool(c.get("math")))
            for p in self.parts
            for c in p["chapters"]
        ]

    def has(self, feature):
        return bool(self.features.get(feature))

    def chapter_path(self, slug):
        return os.path.join(self.src, slug + ".html")

    def written(self):
        """The chapters that actually exist on disk, in curriculum order."""
        return [f for f in self.flat if os.path.exists(self.chapter_path(f[1]))]

    def __repr__(self):
        return f"<Book {self.slug}: {len(self.written())}/{len(self.flat)} chapters>"


def slugs():
    if not os.path.isdir(BOOKS):
        return []
    found = [d for d in sorted(os.listdir(BOOKS))
             if os.path.exists(os.path.join(BOOKS, d, "book.json"))]
    ranked = [s for s in ORDER if s in found]
    return ranked + [s for s in found if s not in ranked]


def books():
    return [Book(s) for s in slugs()]


def book(slug):
    return Book(slug)


if __name__ == "__main__":
    print(f"library at {ROOT}")
    for b in books():
        feats = ", ".join(k for k, v in b.features.items() if v) or "none"
        print(f"  {b.slug:20s} {len(b.written()):3d}/{len(b.flat):<3d} chapters   {feats}")
