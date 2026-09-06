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
import html
import io
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = os.path.join(ROOT, "books")
SHARED = os.path.join(ROOT, "shared")
ASSETS = os.path.join(SHARED, "assets")
VENDOR = os.path.join(SHARED, "vendor")
DOCS = os.path.join(ROOT, "docs")

# Reading order of the library itself. A book absent from here still builds; it
# simply sorts after the named ones, so adding a book cannot silently drop it.
ORDER = ["newton-to-mtheory", "the-long-argument"]

# GitHub Pages serves this repo as a PROJECT page, so every published URL carries
# this prefix. It is the only absolute path anywhere in the library. A manifest's
# "id" needs it, because id resolves against the ORIGIN rather than against the
# manifest's own URL; everything else stays document-relative so the tree can be
# moved or previewed from a file:// path. Moving to a custom domain changes this
# one line and nothing else.
SITE = "/library/"


def plain(text):
    """book.json display strings are HTML fragments -- brand is
    "Newton&nbsp;&rarr;&nbsp;M-Theory". A manifest name is plain text, so the
    markup and the non-breaking spaces have to come out."""
    t = html.unescape(re.sub(r"<[^>]+>", "", text or ""))
    return " ".join(t.replace("\u00a0", " ").split())


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
        self.pwa = cfg.get("pwa") or {}   # absent from every book written before the PWA

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

    # ---------- the installable-app face of a book ----------
    # Every one of these falls back to something the book already declares, so a
    # book.json written before any of this existed still produces a complete,
    # correct manifest. A new book only overrides what the derivation gets wrong.

    @property
    def app_name(self):
        return self.pwa.get("name") or plain(self.title)

    @property
    def short_name(self):
        """What iOS writes under the home-screen icon. It elides at roughly
        twelve characters, so this is the one key a new book should set by hand;
        the derivation below is a floor, not an answer."""
        s = self.pwa.get("short_name")
        if s:
            return s
        out = ""
        for w in plain(self.brand or self.title).split():
            cand = (out + " " + w).strip()
            if out and len(cand) > 12:
                break
            out = cand
        return out.rstrip(" \u2192-\u2013\u2014:,") or plain(self.title)[:12]

    @property
    def theme_color(self):
        return self.pwa.get("theme_color") or self.theme.get("paper", "#ffffff")

    @property
    def background_color(self):
        return self.pwa.get("background_color") or self.theme.get("paper", "#ffffff")

    @property
    def icon_spec(self):
        ic = dict(self.pwa.get("icon", {}))
        ic.setdefault("bg", self.theme.get("accent", "#333333"))
        ic.setdefault("fg", self.theme.get("paper", "#ffffff"))
        return ic

    def shortcuts(self):
        """Derived from the book's own features, so a book can never advertise a
        Math Ledger it does not build."""
        if "shortcuts" in self.pwa:
            return self.pwa["shortcuts"]
        out = [{"name": "Continue", "url": "../continue.html?b=" + self.slug},
               {"name": "Chapters", "url": "contents.html"}]
        if self.has("throughline"):
            out.append({"name": "In Plain Terms", "url": "throughline.html"})
        if self.has("ledger"):
            out.append({"name": "Math Ledger", "url": "ledger.html"})
        return out

    def manifest(self, icons):
        # scope is "../" -- the library root -- rather than this book's own
        # directory, because every page carries a "Library" link back to the hub.
        # Scoped to the book, that link would leave the app on iOS and open in a
        # chrome-less in-app browser with none of the app's caches, so moving
        # between books would read as falling out of the app. A library must not
        # do that.
        return {
            "id": SITE + self.slug + "/",
            "name": self.app_name,
            "short_name": self.short_name,
            "description": plain(self.tagline),
            "lang": "en", "dir": "ltr",
            "start_url": "index.html",
            "scope": "../",
            "display": "standalone",
            "display_override": ["standalone"],
            "theme_color": self.theme_color,
            "background_color": self.background_color,
            "categories": self.pwa.get("categories", ["education", "books"]),
            "icons": icons,
            "shortcuts": self.shortcuts(),
        }

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
    # A book absent from ORDER can still place itself with "order" in its
    # book.json, so adding the twentieth book needs no edit to this file.
    rest = sorted((s for s in found if s not in ranked),
                  key=lambda s: (Book(s).cfg.get("order", 10 ** 6), s))
    return ranked + rest


def books():
    return [Book(s) for s in slugs()]


def book(slug):
    return Book(slug)


if __name__ == "__main__":
    print(f"library at {ROOT}")
    for b in books():
        feats = ", ".join(k for k, v in b.features.items() if v) or "none"
        print(f"  {b.slug:20s} {len(b.written()):3d}/{len(b.flat):<3d} chapters   {feats}")
