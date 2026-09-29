#!/usr/bin/env python3
"""
The Other End of the Trade: the book's chapters into the shape the library builds.

The book is written here, one markdown file a chapter, in the house markdown
that books/the-other-end-of-the-trade/CONVENTIONS.md describes. It was
rewritten from two sources kept in source/: the Dealer Mechanics Lab's
curriculum (Elkhanany/dealer-lab) and the SPX/XSP Edge Book
(Elkhanany/spx-book). This turns it into the two formats the library already
understands, the way tools/bc.py does for the clinical book:

    outline.json                       ->  curriculum.json   parts, chapters, numbers
    chapters/*.md + glossary/*.json
      + figures/*.html                 ->  src/<slug>.html   prose, maths, callouts, figures
    chapters/*.md                      ->  FIGURE-IDEAS.md   where a new figure would help
    notes/*.md                         ->  QUESTIONS.md      what the rewrite asks the author
                                       ->  CORRECTIONS.md    what it found wrong in the sources

What the markdown becomes:

    ## Heading / ### Heading      a numbered section / a subsection
    \\( ... \\)  and  \\[ ... \\]      inline and display maths, typeset by KaTeX; a display
                                  is a numbered .eq, and {#eq:x} under it names it for [eq:x]
    [eq:5c/bsm]                   the number of display eq:bsm in Chapter 5C, "(5C.4)",
                                  linked to it
    ::: kind Title ... :::        a callout (where, plain, insight, practice, rule, warn,
                                  familiar, recap), "What you need first" (tools), a worked
                                  example (worked), a derivation to open (grind), or
                                  "Check yourself" (check, with ?? questions and !! answers)
    [[term]], [[shown|term]]      a glossary mark: the term, with its definition on a card
    Chapter 5C, Part V            a link to the chapter, or to the part's first chapter
    [FIGURE: id]                  the figure in figures/<id>.html
    [FIGURE IDEA: ...]            nothing on the page; a line in FIGURE-IDEAS.md
    | table |                     the house data table (.evidence)
    > quotation                   an aside (callout brick)
    ``` block ```                 a preformatted block (pre.aligned when its meaning is in
                                  its columns)

    python3 tools/spx.py                 regenerate curriculum.json, src/, FIGURE-IDEAS.md,
                                         QUESTIONS.md and CORRECTIONS.md
    python3 tools/spx.py --draft         the same, with a stub for a chapter not yet written
    python3 tools/spx.py --check         fail if anything generated is stale, for CI
    python3 tools/spx.py --verify        prove every word of the markdown reaches the page
    python3 tools/spx.py --lint 1a 1b    check chapters: markup, maths, glossary, links, figures
    python3 tools/spx.py --facts 1a      numbers and names in a chapter's sources that it lacks
    python3 tools/spx.py --sources 1a    print what a chapter is rewritten from

src/ is generated. The hand-edited files are outline.json, chapters/, glossary/,
notes/, figures/ and src/_landing.html.
"""
import argparse
import html as htmlmod
import json
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library

SLUG = "the-other-end-of-the-trade"
DIR = os.path.join(library.BOOKS, SLUG)
CHAPTERS = os.path.join(DIR, "chapters")
GLOSSARY = os.path.join(DIR, "glossary")
NOTES = os.path.join(DIR, "notes")
FIGS = os.path.join(DIR, "figures")
SRC = os.path.join(DIR, "src")
SOURCE = os.path.join(DIR, "source")
IDEAS = os.path.join(DIR, "FIGURE-IDEAS.md")
QUESTIONS = os.path.join(DIR, "QUESTIONS.md")
CORRECTIONS = os.path.join(DIR, "CORRECTIONS.md")
KATEX = os.path.join(library.VENDOR, "katex", "katex.min.js")

FENCE = re.compile(r"^```(\S*)\s*$")
LIST = re.compile(r"^(\s*)([-*]|(\d+)\.)\s+(.*)$")
FIGURE = re.compile(r"^\s*\[FIGURE:\s*([a-z0-9-]+)\s*\]\s*$")
IDEA = re.compile(r"^\s*\[FIGURE IDEA:", re.I)
OPEN = re.compile(r"^:::\s*([a-z]+)\s*(.*?)\s*$")
CLOSE = re.compile(r"^:::\s*$")
LABEL = re.compile(r"^\s*\{#eq:([a-z0-9-]+)\}\s*$")
MDLINK = re.compile(r"\[([^\]\[]+)\]\((https?://[^)\s]+)\)")
GLOSS = re.compile(r"\[\[([^\]\|]+?)(?:\|([^\]]+?))?\]\]")
EQREF = re.compile(r"\[eq:([a-z0-9-]+)\]")
XEQREF = re.compile(r"\[eq:(\d{1,2}[a-z]|r\d)/([a-z0-9-]+)\]")
XEQ = re.compile("\x01([a-z0-9]+)/([a-z0-9-]+)\x01")
CHREF = re.compile(r"\bChapter (\d{1,2}[A-Z]|R\d)\b")
PARTREF = re.compile(r"\bPart ([IVX]+)\b(?!\s*·)")

# kind: (class, default title, whether a title is required)
CALLOUTS = {
    "where": ("callout where", "Where we are", False),
    "plain": ("callout plain", "In plain terms", False),
    "insight": ("callout insight", "Key idea", False),
    "practice": ("callout practice", "In practice", False),
    "rule": ("callout brick", "Decision rule", False),
    "warn": ("callout warn", None, True),
    "familiar": ("callout familiar", "Familiar ground", False),
    "recap": ("callout brick", "What to carry forward", False),
}
SPECIAL = {"tools": "What you need first", "worked": "Worked example",
           "grind": "The full derivation", "check": "Check yourself"}


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def attr(t):
    return esc(t).replace('"', "&quot;")


def slugify(text):
    t = str(text).lower()
    t = re.sub(r"[·•—–]", " ", t)
    t = re.sub(r"[^A-Za-z0-9_\s-]", "", t)
    t = re.sub(r"\s+", "-", t.strip())
    return re.sub(r"-+", "-", t) or "sec"


def plain(fragment):
    """Visible text of an HTML fragment."""
    return htmlmod.unescape(re.sub(r"<[^>]+>", "", fragment))


# ------------------------------------------------------------------ the outline

class Model:
    def __init__(self):
        self.outline = json.loads(library.read(os.path.join(DIR, "outline.json")))
        self.parts = self.outline["parts"]
        self.chapters, self.by_num, self.by_slug, self.part_first = [], {}, {}, {}
        errs = []
        for p in self.parts:
            for c in p["chapters"]:
                c["part"] = p
                self.chapters.append(c)
                if c["num"] in self.by_num or c["slug"] in self.by_slug:
                    errs.append("outline.json: chapter %s or slug %s is used twice" % (c["num"], c["slug"]))
                self.by_num[c["num"]] = c
                self.by_slug[c["slug"]] = c
            if p["chapters"]:
                self.part_first[p["label"].replace("Part ", "")] = p["chapters"][0]
        if errs:
            sys.exit("\n".join(errs))

    @staticmethod
    def label(p):
        return "%s · %s" % (p["label"], p["title"])

    def path(self, c):
        return os.path.join(CHAPTERS, c["slug"] + ".md")

    def written(self, c):
        return os.path.exists(self.path(c))


# ------------------------------------------------------------------ the sources

class Sources:
    """What a chapter is rewritten from. 'dl:1A' is chapter 1A of the Dealer
    Mechanics Lab as it was imported, mapped by source/dealer-lab/outline.json
    (the first chapter of each of its parts carries the part's introduction);
    'spx:6' is chapter 6 of the Edge Book, 'spx:6.2' its section 6.2, and
    'spx:6/Where this fits' its section of that heading."""

    def __init__(self):
        self.dl = {}
        d = os.path.join(SOURCE, "dealer-lab")
        old = json.loads(library.read(os.path.join(d, "outline.json")))
        for p in old["parts"]:
            text = library.read(os.path.join(d, p["file"]))
            intro, heads, cur, infence = [], {}, None, False
            for line in text.split("\n"):
                if FENCE.match(line):
                    infence = not infence
                if not infence and line.startswith("## "):
                    cur = line[3:].strip()
                    heads[cur] = [line]
                    continue
                (heads[cur] if cur else intro).append(line)
            for i, c in enumerate(p["chapters"]):
                body = []
                if i == 0:
                    body += intro
                for h in c["heads"]:
                    body += heads.get(h, [])
                self.dl[c["num"]] = "\n".join(body).strip() + "\n"
        self.spx = {}
        d = os.path.join(SOURCE, "spx-book")
        for f in sorted(os.listdir(d)):
            m = re.match(r"\d+_ch(\d+)_", f)
            if m:
                self.spx[int(m.group(1))] = library.read(os.path.join(d, f))

    def get(self, ref):
        kind, _, key = ref.partition(":")
        if kind == "dl":
            return self.dl.get(key)
        if kind != "spx":
            return None
        if "/" in key:
            n, head = key.split("/", 1)
            return self._section(int(n), lambda h: h == head)
        if "." in key:
            n = int(key.split(".")[0])
            return self._section(n, lambda h: re.match(re.escape(key) + r"(\s|$)", h) is not None)
        return self.spx.get(int(key))

    def _section(self, n, match):
        text = self.spx.get(n)
        if text is None:
            return None
        out, on, infence = [], False, False
        for line in text.split("\n"):
            if FENCE.match(line):
                infence = not infence
            if not infence and line.startswith("## "):
                on = match(line[3:].strip())
            if on:
                out.append(line)
        return "\n".join(out).strip() + "\n" if out else None


# ------------------------------------------------------------------ glossary

DUPLICATES = []


def glossary():
    """Every entry in glossary/*.json, keyed by the term in lower case."""
    out, errs = {}, []
    if not os.path.isdir(GLOSSARY):
        return out, errs
    for f in sorted(os.listdir(GLOSSARY)):
        if not f.endswith(".json"):
            continue
        try:
            data = json.loads(library.read(os.path.join(GLOSSARY, f)))
        except ValueError as e:
            errs.append("glossary/%s: %s" % (f, e))
            continue
        for term, e in data.items():
            k = term.lower()
            if not isinstance(e, dict) or not e.get("def"):
                errs.append("glossary/%s: %r has no definition" % (f, term))
                continue
            if re.search(r"\[\[|\\\(|\\\[|\$", e["def"]):
                errs.append("glossary/%s: %r: a definition takes no marks or maths" % (f, term))
            if k in out and out[k]["def"] != e["def"]:
                # Writers working in parallel can add the same term. The first
                # file's entry is used; a full build refuses until one is left.
                DUPLICATES.append("glossary: %r is defined in both %s and %s" % (term, out[k]["file"], f))
                continue
            out[k] = {"term": term, "def": e["def"], "chapter": e.get("chapter", ""), "file": f}
    return out, errs


# ------------------------------------------------------------------ figures

class Figures:
    """figures/<id>.html, loaded once. A file is the figure's markup, with
    {{uid}} wherever an id must be unique on the page, followed by one
    <script> whose body is gathered into the chapter's SCRIPT block."""

    HEAD = re.compile(r"\A<!--(.*?)-->\s*", re.S)

    def __init__(self):
        self.cache = {}
        self.lib = None

    def library_js(self):
        if self.lib is None:
            path = os.path.join(FIGS, "_lib.js")
            self.lib = library.read(path) if os.path.exists(path) else ""
        return self.lib

    def get(self, fid):
        if fid not in self.cache:
            path = os.path.join(FIGS, fid + ".html")
            if not os.path.exists(path):
                self.cache[fid] = None
            else:
                raw = library.read(path)
                meta = {}
                m = self.HEAD.match(raw)
                if m:
                    for line in m.group(1).strip().split("\n"):
                        k, _, v = line.partition(":")
                        if v.strip():
                            meta[k.strip()] = v.strip()
                    raw = raw[m.end():]
                sm = re.search(r"<script>\n?(.*?)</script>\s*\Z", raw, re.S)
                script = sm.group(1) if sm else ""
                markup = raw[:sm.start()].rstrip() if sm else raw.rstrip()
                self.cache[fid] = {"id": fid, "markup": markup, "script": script,
                                   "name": meta.get("name", fid)}
        return self.cache[fid]


# ------------------------------------------------------------------ chapters

def aligned(lines):
    """A block whose meaning is in its columns keeps its layout and scrolls
    inside its own box on a narrow screen (book.css, pre.aligned)."""
    body = [l for l in lines if l.strip()]
    return ((len(body) >= 2 and any(re.search(r"\S {3,}\S", l) for l in body))
            or bool(re.search(r"[═│─┌└├]|_{6,}", "\n".join(body))))


def split_row(row):
    """A table row's cells. A pipe splits a cell except when escaped, inside a
    code span, inside maths, inside a glossary mark, or inside parentheses
    (where it is an absolute value)."""
    s = row.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    out, cur, depth, code, math, gl, i = [], [], 0, False, False, False, 0
    while i < len(s):
        ch, two = s[i], s[i:i + 2]
        if two in ("\\(", "\\)"):
            math = two == "\\("
            cur.append(two)
            i += 2
            continue
        if ch == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur.append("|")
            i += 2
            continue
        if two in ("[[", "]]"):
            gl = two == "[["
            cur.append(two)
            i += 2
            continue
        if ch == "`":
            code = not code
        elif not (code or math) and ch == "(":
            depth += 1
        elif not (code or math) and ch == ")" and depth:
            depth -= 1
        elif ch == "|" and not (code or math or gl) and depth == 0:
            out.append("".join(cur).strip())
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    out.append("".join(cur).strip())
    return out


class Chapter:
    """One chapter, on its way to being one HTML fragment."""

    def __init__(self, m, figs, gloss, c):
        self.m, self.figs, self.gloss, self.c = m, figs, gloss, c
        self.errs, self.ids, self.scripts = [], {}, []
        self.fig_uses, self.ideas, self.math, self.eqs, self.eqrefs = {}, [], [], [], []
        self.written = True
        # every display in page order, by its label or None: book.js numbers them all
        self.displays = []
        self.h2 = 0
        self.heading_now = ""

    def fail(self, msg):
        line = "%s: %s" % (self.c["num"], msg)
        if line not in self.errs:
            self.errs.append(line)

    def uid(self, base):
        n = self.ids.get(base, 0) + 1
        self.ids[base] = n
        return base if n == 1 else "%s-%d" % (base, n)

    # ---------------------------------------------------------------- inline
    def chref(self, mo):
        target = self.m.by_num.get(mo.group(1))
        if target is None:
            self.fail("no chapter %s: %r" % (mo.group(1), mo.group(0)))
            return mo.group(0)
        if target is self.c:
            return mo.group(0)
        return '<a class="xref" href="%s.html">%s</a>' % (target["slug"], mo.group(0))

    def partref(self, mo):
        target = self.m.part_first.get(mo.group(1))
        if target is None:
            self.fail("no Part %s" % mo.group(1))
            return mo.group(0)
        if target is self.c:
            return mo.group(0)
        return '<a class="xref" href="%s.html">%s</a>' % (target["slug"], mo.group(0))

    def glossmark(self, mo):
        shown = mo.group(1).strip()
        key = (mo.group(2) or mo.group(1)).strip()
        e = self.gloss.get(key.lower())
        if e is None:
            self.fail("[[%s]] has no glossary entry %r" % (mo.group(0)[2:-2], key))
            return esc(shown)
        return '<span class="gloss" title="%s">%s</span>' % (attr(e["def"]), esc(shown))

    def inline(self, t, links=True):
        stash = []

        def keep(html):
            stash.append(html)
            return "\x00%d\x00" % (len(stash) - 1)

        # code, then maths: nothing inside either is markup
        t = re.sub(r"`([^`]+)`", lambda mo: keep("<code>%s</code>" % esc(mo.group(1))), t)

        def inl(mo):
            body = mo.group(1)
            self.math.append((body, False))
            return keep("\\(%s\\)" % esc(body))
        t = re.sub(r"\\\((.+?)\\\)", inl, t, flags=re.S)
        if "\\(" in t or "\\)" in t:
            self.fail("an unmatched \\( or \\): %r" % t[:80])
        if "\\[" in t or "\\]" in t:
            self.fail("display maths inside a paragraph (put \\[ ... \\] on lines of its own): %r" % t[:80])
        if "\\$" in t:
            self.fail("\\$ outside maths (a price in prose is plain $; \\$ is for inside \\( \\)): %r" % t[:80])
        if re.search(r"\$\s*\\|\$[^$\s]*[_^{]", t):
            self.fail("maths between dollar signs (use \\( and \\)): %r" % t[:80])
        if IDEA.search(t) or re.search(r"\[FIGURE", t):
            self.fail("a [FIGURE ...] marker must be a paragraph of its own: %r" % t[:80])
        t = GLOSS.sub(lambda mo: keep(self.glossmark(mo)), t)

        def eqref(mo):
            self.eqrefs.append(mo.group(1))
            return keep('<a class="eqref" href="#e-%s"></a>' % mo.group(1))
        # another chapter's display: numbered once every chapter is rendered (number_xeqs)
        t = XEQREF.sub(lambda mo: keep('<a class="xref xeq" href="%s.html#e-%s">\x01%s/%s\x01</a>'
                                       % (mo.group(1), mo.group(2), mo.group(1), mo.group(2))), t)
        t = EQREF.sub(eqref, t)
        t = MDLINK.sub(lambda mo: keep('<a href="%s">%s</a>' % (attr(mo.group(2)), esc(mo.group(1)))), t)
        t = esc(t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"(?<![*\w])\*(?!\s)([^*\n]+?)(?<!\s)\*(?![*\w])", r"<em>\1</em>", t)
        if links:
            t = CHREF.sub(self.chref, t)
            t = PARTREF.sub(self.partref, t)
        if "**" in t or re.search(r"(?<![\w*])\*(?=[^\s*])", t):
            self.fail("an asterisk survived emphasis: %r" % plain(t)[:80])
        if "—" in t:
            self.fail("an em dash (use a colon, a comma or a full stop): %r" % plain(t)[:80])
        while "\x00" in t:
            t = re.sub(r"\x00(\d+)\x00", lambda mo: stash[int(mo.group(1))], t)
        return t

    # ---------------------------------------------------------------- blocks
    def figure(self, fid):
        f = self.figs.get(fid)
        if f is None:
            self.fail("[FIGURE: %s] has no figures/%s.html" % (fid, fid))
            return ""
        if fid not in self.c.get("figures", []):
            self.fail("[FIGURE: %s] is not one of this chapter's figures in outline.json" % fid)
        n = self.fig_uses.get(fid, 0) + 1
        self.fig_uses[fid] = n
        u = fid if n == 1 else "%s-%d" % (fid, n)
        markup = f["markup"].replace("{{uid}}", u)
        if f["script"].strip():
            self.scripts.append("/* ---------- %s ---------- */\n%s"
                                % (u, f["script"].replace("{{uid}}", u).strip("\n")))
        return markup

    def table(self, rows):
        """A markdown table as the house data table: the first column pinned,
        every cell named on a phone, sideways scroll inside its own box."""
        cells = [split_row(r) for r in rows]
        head, rest = cells[0], cells[1:]
        align = [""] * len(head)
        if rest and all(re.fullmatch(r":?-{2,}:?", x or "") for x in rest[0]):
            align = ["right" if x.endswith(":") and not x.startswith(":") else
                     "center" if x.startswith(":") and x.endswith(":") else "" for x in rest[0]]
            rest = rest[1:]
        else:
            self.fail("a table without a |---| rule under its header: %r" % rows[0][:60])
        width = len(head)
        for r in rest:
            if len(r) != width:
                self.fail("a table row has %d cells under %d heads: %r" % (len(r), width, "|".join(r)[:60]))
        cls = []
        for j in range(width):
            if j == 0:
                cls.append("c-trial")
                continue
            lens = [len(plain(self.inline(r[j], links=False))) for r in rest if j < len(r)]
            avg = sum(lens) / len(lens) if lens else 0
            cls.append("c-result" if avg >= 45 else "c-endpoint" if avg >= 22
                       else "c-other" if avg >= 10 else "")

        def attrs(j, label=None):
            a = ' class="%s"' % cls[j] if cls[j] else ""
            if label is not None:
                a += ' data-label="%s"' % attr(label)
            if align[j]:
                a += ' style="text-align:%s"' % align[j]
            return a

        labels = [plain(self.inline(h, links=False)) for h in head]
        out = ['<div class="evidence"><div class="ev-scroll"><table class="trials"><thead><tr>']
        out += ["<th%s>%s</th>" % (attrs(j), self.inline(h, links=False)) for j, h in enumerate(head)]
        out.append("</tr></thead><tbody>")
        for r in rest:
            out.append("<tr>" + "".join(
                "<td%s>%s</td>" % (attrs(j, labels[j] if width >= 3 else None), self.inline(r[j]))
                for j in range(min(width, len(r)))) + "</tr>")
        out.append("</tbody></table></div></div>")
        return "".join(out)

    def display(self, body, label):
        self.math.append((body, True))
        self.displays.append(label)
        if label:
            if label in self.eqs:
                self.fail("the label eq:%s is used twice" % label)
            self.eqs.append(label)
            return '<div class="eq" id="e-%s">\n\\[ %s \\]\n</div>' % (label, esc(body.strip()))
        return '<div class="eq">\n\\[ %s \\]\n</div>' % esc(body.strip())

    def callout(self, kind, title, inner):
        if kind in CALLOUTS:
            cls, default, need = CALLOUTS[kind]
            if need and not title:
                self.fail("::: %s needs a title (\"When it fails\", \"Common mistake: ...\")" % kind)
            return '<div class="%s">\n<span class="ct">%s</span>\n%s\n</div>' % (
                cls, self.inline(title or default, links=False), self.blocks(inner))
        if kind == "tools":
            return '<div class="tools"><b>%s</b>\n%s\n</div>' % (
                self.inline(title or SPECIAL["tools"], links=False), self.blocks(inner))
        if kind == "worked":
            head = "Worked example: " + title if title else SPECIAL["worked"]
            return '<div class="worked">\n<span class="ct">%s</span>\n%s\n</div>' % (
                self.inline(head, links=False), self.blocks(inner))
        if kind == "grind":
            return ('<details class="grind"><summary>%s</summary><div class="grind-body">\n%s\n'
                    '</div></details>' % (self.inline(title or SPECIAL["grind"], links=False),
                                          self.blocks(inner)))
        if kind == "check":
            return self.check(title, inner)
        self.fail("no callout of kind %r" % kind)
        return self.blocks(inner)

    def check(self, title, inner):
        qs, cur = [], None
        for line in inner:
            if line.startswith("?? "):
                cur = [[line[3:]], []]
                qs.append(cur)
            elif line.startswith("!! "):
                if cur is None or cur[1]:
                    self.fail("an answer (!!) without its question (??) in ::: check")
                    continue
                cur[1].append(line[3:])
                cur.append(True)
            elif cur is None:
                if line.strip():
                    self.fail("text before the first ?? in ::: check: %r" % line[:60])
            else:
                (cur[1] if len(cur) > 2 else cur[0]).append(line)
        if not qs:
            self.fail("::: check has no ?? questions")
        name = title or SPECIAL["check"]
        self.h2 += 1
        hid = self.uid(slugify(name))
        out = ['<h2 id="%s">%d · %s</h2>' % (hid, self.h2, self.inline(name, links=False)),
               '<div class="problems">']
        for n, q in enumerate(qs, 1):
            if len(q) < 3:
                self.fail("question %d in ::: check has no !! answer" % n)
            out.append('<div class="prob">\n<p class="pnum">Question %d</p>\n%s\n'
                       '<details><summary>Answer</summary><div class="sol">\n%s\n</div></details>\n</div>'
                       % (n, self.blocks(q[0]), self.blocks(q[1])))
        out.append("</div>")
        return "\n".join(out)

    def blocks(self, lines):
        out, i = [], 0
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                i += 1
                continue
            om = OPEN.match(line)
            if om:
                kind, title = om.group(1), om.group(2)
                j, inner = i + 1, []
                while j < len(lines) and not CLOSE.match(lines[j]):
                    if OPEN.match(lines[j]):
                        self.fail("::: %s opens inside ::: %s (callouts do not nest)"
                                  % (OPEN.match(lines[j]).group(1), kind))
                    inner.append(lines[j])
                    j += 1
                if j >= len(lines):
                    self.fail("::: %s is never closed" % kind)
                out.append(self.callout(kind, title, inner))
                i = j + 1
                continue
            if CLOSE.match(line):
                self.fail("a ::: that closes nothing")
                i += 1
                continue
            if FENCE.match(line):
                buf = []
                i += 1
                while i < len(lines) and not FENCE.match(lines[i]):
                    buf.append(lines[i])
                    i += 1
                i += 1
                while buf and not buf[-1].strip():
                    buf.pop()
                out.append("<pre%s>%s</pre>" % (' class="aligned"' if aligned(buf) else "",
                                                esc("\n".join(buf))))
                continue
            if line.lstrip().startswith("\\["):
                buf = [line.lstrip()[2:]]
                while "\\]" not in buf[-1] and i + 1 < len(lines):
                    i += 1
                    buf.append(lines[i])
                body = "\n".join(buf)
                if "\\]" not in body:
                    self.fail("\\[ is never closed")
                body, _, after = body.partition("\\]")
                if after.strip():
                    self.fail("text after \\] on its line: %r" % after.strip()[:40])
                i += 1
                label = None
                j = i
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and LABEL.match(lines[j]):
                    label = LABEL.match(lines[j]).group(1)
                    i = j + 1
                out.append(self.display(body, label))
                continue
            if LABEL.match(line):
                self.fail("{#eq:%s} is not under a display" % LABEL.match(line).group(1))
                i += 1
                continue
            hm = re.match(r"^(#{1,6})\s+(.*)$", line)
            if hm:
                out.append(self.heading(len(hm.group(1)), hm.group(2).strip()))
                i += 1
                continue
            if line.strip() == "---":
                out.append("<hr>")
                i += 1
                continue
            fm = FIGURE.match(line)
            if fm:
                out.append(self.figure(fm.group(1)))
                i += 1
                continue
            if IDEA.match(line):
                buf = []
                while i < len(lines) and lines[i].strip():
                    buf.append(lines[i].strip())
                    i += 1
                text = " ".join(buf)
                if not text.endswith("]"):
                    self.fail("a [FIGURE IDEA: ...] must end its paragraph with ]: %r" % text[:60])
                self.ideas.append((self.heading_now, re.sub(r"^\[FIGURE IDEA:\s*|\]$", "", text, flags=re.I)))
                continue
            if line.startswith(">"):
                buf = []
                while i < len(lines) and lines[i].startswith(">"):
                    buf.append(re.sub(r"^> ?", "", lines[i]))
                    i += 1
                out.append('<div class="callout brick">\n%s\n</div>' % self.blocks(buf))
                continue
            if line.lstrip().startswith("|"):
                buf = []
                while i < len(lines) and lines[i].lstrip().startswith("|"):
                    buf.append(lines[i])
                    i += 1
                out.append(self.table(buf))
                continue
            lm = LIST.match(line)
            if lm:
                ordered = lm.group(3) is not None
                start = int(lm.group(3)) if ordered else 1
                items, loose = [], False
                while i < len(lines):
                    mm = LIST.match(lines[i])
                    if not mm or (mm.group(3) is not None) != ordered:
                        break
                    items.append(mm.group(4).strip())
                    i += 1
                    while (i < len(lines) and lines[i].strip() and not LIST.match(lines[i])
                           and not lines[i].startswith(("#", ">", "|", "```", ":::"))
                           and not lines[i].lstrip().startswith("\\[")):
                        items[-1] += " " + lines[i].strip()
                        i += 1
                    j = i
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j > i and j < len(lines):
                        nm = LIST.match(lines[j])
                        if nm and (nm.group(3) is not None) == ordered:
                            loose = True
                            i = j
                tag = "ol" if ordered else "ul"
                att = ' start="%d"' % start if ordered and start != 1 else ""
                wrap = (lambda s: "<p>%s</p>" % s) if loose else (lambda s: s)
                out.append("<%s%s>\n%s\n</%s>" % (tag, att, "\n".join(
                    "<li>%s</li>" % wrap(self.inline(t)) for t in items), tag))
                continue
            buf = []
            while (i < len(lines) and lines[i].strip() and not FENCE.match(lines[i])
                   and not lines[i].startswith(("#", ">")) and lines[i].strip() != "---"
                   and not lines[i].lstrip().startswith(("|", "\\[")) and not LIST.match(lines[i])
                   and not FIGURE.match(lines[i]) and not IDEA.match(lines[i])
                   and not OPEN.match(lines[i]) and not CLOSE.match(lines[i])
                   and not LABEL.match(lines[i])):
                buf.append(lines[i].strip())
                i += 1
            if buf:
                out.append("<p>%s</p>" % self.inline(" ".join(buf)))
            else:
                self.fail("a line the parser cannot place: %r" % line[:60])
                i += 1
        return "\n\n".join(b for b in out if b)

    def heading(self, hashes, text):
        if hashes == 1:
            self.fail("a # heading: the title comes from outline.json")
        if hashes > 3:
            self.fail("a heading of %d #'s: use ## and ### only" % hashes)
        if re.search(r"[.:]$", text):
            self.fail("a heading ends in punctuation: %r" % text)
        if re.match(r"^\d+(\.\d+)*[.)]?\s", text):
            self.fail("a heading carries its own number (the build numbers sections): %r" % text)
        self.heading_now = text
        hid = self.uid(slugify(text))
        shown = self.inline(text, links=False)
        if hashes <= 2:
            self.h2 += 1
            return '<h2 id="%s">%d · %s</h2>' % (hid, self.h2, shown)
        return '<h3 id="%s">%s</h3>' % (hid, shown)

    # ----------------------------------------------------------------- whole
    def render(self, text):
        c, p = self.c, self.c["part"]
        head = ['<p class="eyebrow">%s · Chapter %s</p>' % (esc(Model.label(p)), esc(c["num"])),
                "<h1>%s</h1>" % esc(c["title"])]
        if c.get("subtitle"):
            head.append('<p class="subtitle">%s</p>' % esc(c["subtitle"]))
        body = self.blocks(text.split("\n")) if text is not None else \
            '<p><em>This chapter is being rewritten.</em></p>'
        for r in self.eqrefs:
            if r not in self.eqs:
                self.fail("[eq:%s] names no display in this chapter" % r)
        for fid in c.get("figures", []):
            if text is not None and fid not in self.fig_uses:
                self.fail("the outline gives this chapter [FIGURE: %s], and it is not placed" % fid)
        out = "\n\n".join(head + [body]) + "\n"
        if self.scripts:
            lib = self.figs.library_js().strip("\n")
            out += "\n<!--SCRIPT-->\n%s\n\n%s\n<!--/SCRIPT-->\n" % (lib, "\n\n".join(self.scripts))
        return out


def glossary_page(m, gloss, intro_html):
    """R1: every entry, alphabetically, under a heading per letter."""
    groups = {}
    for k in sorted(gloss, key=lambda k: re.sub(r"[^a-z0-9]", "", k)):
        first = re.sub(r"[^a-z0-9]", "", k)[:1].upper() or "#"
        groups.setdefault("0-9" if first.isdigit() else first, []).append(gloss[k])
    out = [intro_html] if intro_html else []
    for letter in sorted(groups):
        out.append('<h2 id="g-%s">%s</h2>' % (letter.lower(), letter))
        for e in groups[letter]:
            where = m.by_num.get(e["chapter"])
            link = (' <a class="xref" href="%s.html">Chapter %s</a>' % (where["slug"], esc(where["num"]))
                    if where else "")
            out.append('<p id="g-%s"><strong>%s.</strong> %s%s</p>'
                       % (slugify(e["term"]), esc(e["term"]), esc(e["def"]), link))
    return "\n\n".join(out)


# ------------------------------------------------------------------ outputs

def curriculum(m, maths):
    parts = []
    for p in m.parts:
        parts.append({
            "label": Model.label(p),
            "subtitle": p["subtitle"],
            "chapters": [{"num": c["num"], "slug": c["slug"], "title": c["title"],
                          "math": bool(maths.get(c["slug"]))} for c in p["chapters"]],
        })
    return json.dumps(parts, indent=1, ensure_ascii=False) + "\n"


def ideas_file(m, ideas):
    out = []
    total = 0
    for c in m.chapters:
        these = ideas.get(c["slug"])
        if not these:
            continue
        out.append("## %s · %s" % (c["num"], c["title"]))
        out.append("")
        for heading, text in these:
            total += 1
            out.append("- %s%s" % ("*%s.* " % heading if heading else "", text))
        out.append("")
    head = ["# Where a new figure would help", "",
            "%d idea%s, collected by `tools/spx.py` from the `[FIGURE IDEA: ...]` markers in "
            "`chapters/*.md`. The markers are not shown in the book: edit them in the chapters, "
            "not here." % (total, "s" * (total != 1)), ""]
    return "\n".join(head + out).rstrip() + "\n"


def notes_section(slug, heading):
    """The body of one "## heading" section of notes/<slug>.md, or ''."""
    path = os.path.join(NOTES, slug + ".md")
    if not os.path.exists(path):
        return ""
    mo = re.search(r"^## %s[ \t]*\n(.*?)(?=^## |\Z)" % re.escape(heading), library.read(path),
                   re.M | re.S)
    return mo.group(1).strip() if mo else ""


def list_items(body):
    """The items of a markdown list, each with the lines that continue it."""
    items = []
    for line in body.split("\n"):
        if line.startswith("- "):
            items.append(line)
        elif items and line.strip() and not line.startswith("#"):
            items[-1] += "\n" + line
    return items


def corrections_file(m):
    """Every correction the notes record under "Changed": the items that open
    with "Fixed" (the writers') or "Checked:" (the second check's)."""
    out = []
    total = 0
    for c in m.chapters:
        these = [it for it in list_items(notes_section(c["slug"], "Changed"))
                 if re.match(r"- (\*\*)?(Fixed|Checked)\b", it)]
        if not these:
            continue
        total += len(these)
        out += ["## %s · %s" % (c["num"], c["title"]), ""] + these + [""]
    head = ["# What the rewrite corrected", "",
            "%d correction%s to the two sources, collected by `tools/spx.py` from the \"Changed\" "
            "section of `notes/*.md`: the items that open with \"Fixed\" (found while rewriting) or "
            "\"Checked:\" (found by the second check of the maths). Each names the source it "
            "corrects (dl: the Dealer Mechanics Lab, spx: the Edge Book). Edit them in the notes, "
            "not here." % (total, "s" * (total != 1)), ""]
    return "\n".join(head + out).rstrip() + "\n"


def questions_file(m):
    """Each notes file's "Questions for the author", in the book's order."""
    out = []
    total = 0
    for c in m.chapters:
        path = os.path.join(NOTES, c["slug"] + ".md")
        if not os.path.exists(path):
            continue
        mo = re.search(r"^## Questions for the author[ \t]*\n(.*?)(?=^## |\Z)", library.read(path),
                       re.M | re.S)
        body = mo.group(1).strip() if mo else ""
        n = len(re.findall(r"^- ", body, re.M))
        if not n:
            continue
        total += n
        out += ["## %s · %s" % (c["num"], c["title"]), "", body, ""]
    head = ["# Questions for the author", "",
            "%d question%s the rewrite raised, collected by `tools/spx.py` from the \"Questions for "
            "the author\" in `notes/*.md`. Answer them there, or in the chapter, not here."
            % (total, "s" * (total != 1)), ""]
    return "\n".join(head + out).rstrip() + "\n"


def number_xeqs(m, figs, gloss, out, chapters, draft):
    """Give each [eq:<slug>/<label>] the number its display has on its own page,
    rendering any chapter this pass did not."""
    errs = []
    # a chapter this pass rendered as a stub (--draft, --preview) is numbered from its text
    cache = {k: ch for k, ch in chapters.items() if ch.written}

    def target(slug):
        if slug not in cache:
            c = m.by_slug.get(slug)
            ch = None
            if c is not None and m.written(c):
                ch = Chapter(m, figs, gloss, c)
                ch.render(library.read(m.path(c)))
                ch.written = True
            cache[slug] = ch
        return cache[slug]

    for path in sorted(out):
        if "\x01" not in out[path]:
            continue
        where = m.by_slug[os.path.basename(path)[:-5]]["num"]

        def num(mo):
            slug, label = mo.group(1), mo.group(2)
            ch = target(slug)
            if ch is None:
                if not (draft and slug in m.by_slug):
                    errs.append("%s: [eq:%s/%s] names no written chapter" % (where, slug, label))
                return "(?)"
            if label not in ch.displays:
                errs.append("%s: [eq:%s/%s] names no display in Chapter %s"
                            % (where, slug, label, ch.c["num"]))
                return "(?)"
            return "(%s.%d)" % (ch.c["num"], ch.displays.index(label) + 1)
        out[path] = XEQ.sub(num, out[path])
    return errs


def generate(m, draft=False, only=None, preview=None):
    figs = Figures()
    gloss, errs = glossary()
    out, placed, maths, ideas, chapters = {}, {}, {}, {}, {}
    for c in m.chapters:
        if only and c["slug"] not in only:
            continue
        text = library.read(m.path(c)) if m.written(c) else None
        if preview is not None and c["slug"] not in preview:
            text = None
        if text is None and c["slug"] != "r1" and not draft:
            if not only:
                errs.append("%s: chapters/%s.md is not written" % (c["num"], c["slug"]))
            continue
        ch = Chapter(m, figs, gloss, c)
        ch.written = text is not None
        if c["slug"] == "r1":
            intro = ch.blocks(text.split("\n")) if text else ""
            html = ch.render("")
            html = html.rstrip("\n") + "\n\n" + glossary_page(m, gloss, intro) + "\n"
        else:
            html = ch.render(text)
        out[os.path.join(SRC, c["slug"] + ".html")] = html
        chapters[c["slug"]] = ch
        errs += ch.errs
        maths[c["slug"]] = bool(ch.math)
        if ch.ideas:
            ideas[c["slug"]] = ch.ideas
        for fid in ch.fig_uses:
            placed.setdefault(fid, []).append(c["num"])
    errs += number_xeqs(m, figs, gloss, out, chapters, draft or preview is not None)
    if not only:
        errs += DUPLICATES
        out[os.path.join(DIR, "curriculum.json")] = curriculum(m, maths)
        out[IDEAS] = ideas_file(m, ideas)
        out[QUESTIONS] = questions_file(m)
        out[CORRECTIONS] = corrections_file(m)
    return out, errs, placed, chapters


# ------------------------------------------------------------------ checks

def katex_errors(exprs):
    """Each expression through KaTeX with throwOnError, as the page's own
    auto-render would typeset it. Returns [(expr, message)]."""
    if not exprs or not os.path.exists(KATEX):
        return []
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump([[e, d] for e, d in exprs], f)
        path = f.name
    js = ("const k=require(%s);const x=require(%s);const bad=[];"
          "for(const [e,d] of x){try{k.renderToString(e,{displayMode:d,throwOnError:true,strict:'ignore'})}"
          "catch(err){bad.push([e,String(err.message||err)])}}console.log(JSON.stringify(bad))"
          % (json.dumps(KATEX), json.dumps(path)))
    try:
        r = subprocess.run(["node", "-e", js], capture_output=True, text=True, timeout=120)
        return json.loads(r.stdout or "[]")
    except (OSError, ValueError, subprocess.SubprocessError) as e:
        return [("", "could not run KaTeX under node: %s" % e)]
    finally:
        os.unlink(path)


def lint(m, slugs):
    out, errs, _placed, chapters = generate(m, only=set(slugs))
    bad = list(errs)
    for s in slugs:
        if s not in m.by_slug:
            bad.append("no chapter with slug %r in outline.json" % s)
            continue
        if s not in chapters:
            bad.append("%s: chapters/%s.md is not written" % (m.by_slug[s]["num"], s))
            continue
        for e, msg in katex_errors(chapters[s].math):
            bad.append("%s: KaTeX cannot typeset %r: %s" % (m.by_slug[s]["num"], e[:70], msg[:120]))
    for e in bad:
        print("  error  " + e)
    for s in slugs:
        ch = chapters.get(s)
        if ch:
            print("  %-4s %d displays, %d inline maths, %d figures, %d figure ideas"
                  % (ch.c["num"], sum(1 for _e, d in ch.math if d), sum(1 for _e, d in ch.math if not d),
                     sum(ch.fig_uses.values()), len(ch.ideas)))
    return len(bad)


STOP = set("""A An And As At But By For From If In Into It Its Of On Or So That The Their Then There These
This Those To When Where Which While With You Your Each Every No Not One Two Three Four Five Six Seven
Eight Nine Ten Step Example Question Answer Part Chapter Section Figure Table Note See Why What How Who
Most Many Some All Both Either Neither Here Now Also Yes Consider Suppose Take Let Use""".split())


def canon_numbers(text):
    """Every number in a text, as digits without grouping commas or signs. In
    maths a grouping comma is written {,} (22{,}500), which is still a comma."""
    t = re.sub(r"\\[a-zA-Z]+|[{}\\]", " ", text.replace("{,}", ","))
    out = set()
    for mo in re.finditer(r"(?<![\w.])\d[\d,]*(?:\.\d+)?|(?<![\w\d])\.\d+", t):
        n = mo.group(0).replace(",", "")
        try:
            out.add(repr(float(n)).rstrip("0").rstrip(".") if "." in n else str(int(n)))
        except ValueError:
            pass
    return out


def facts_of(text):
    """The numbers and names a source passage states."""
    t = re.sub(r"```.*?```", " ", text, flags=re.S)
    t = re.sub(r"\[INTERACTIVE:[^\]]*\]", " ", t)
    t = re.sub(r"^#+ .*$", " ", t, flags=re.M)
    t = re.sub(r"[*_`]", "", t)
    nums = set()
    for n in canon_numbers(t):
        if "." not in n and n.isdigit() and int(n) <= 10:
            continue
        nums.add(n)
    names = set()
    for mo in re.finditer(r"(?<=[a-z,;:(\"] )([A-Z][a-zA-Z&'-]+(?: (?:of |and |& )?[A-Z][a-zA-Z&'-]+)*)", t):
        w = mo.group(1)
        if w.split()[0] not in STOP:
            names.add(w)
    for mo in re.finditer(r"\b[A-Z][A-Z0-9&]{1,}[a-z]?\b", t):
        if not re.fullmatch(r"[IVX]+", mo.group(0)):
            names.add(mo.group(0))
    return nums, names


def overlaps(a, b):
    """Whether two source references share text: equal, or one a section of
    the other ('spx:2' and 'spx:2.3', 'spx:0' and 'spx:0/Where this fits')."""
    return a == b or b.startswith(a + ".") or b.startswith(a + "/") \
        or a.startswith(b + ".") or a.startswith(b + "/")


def facts(m, slug, src):
    c = m.by_slug.get(slug)
    if c is None:
        sys.exit("no chapter %r" % slug)
    missing = 0
    for ref in c["sources"]:
        text = src.get(ref)
        if text is None:
            print("  error  %s: no source %s" % (c["num"], ref))
            missing += 1
            continue
        # A source shared by several chapters is covered by any of them, and by
        # any of their notes; 'spx:2' is shared with a chapter taking 'spx:2.3'.
        sharing = [d for d in m.chapters if m.written(d)
                   and any(overlaps(ref, r) for r in d["sources"])]
        have = " ".join(library.read(m.path(d)) for d in sharing)
        if c["slug"] == "r1":
            # the glossary page indexes the whole book: a term's facts count wherever
            # the book states them, and in its glossary entry
            gl, _e = glossary()
            have += " ".join([library.read(m.path(d)) for d in m.chapters if m.written(d)]
                             + ["%s %s" % (e["term"], e["def"]) for e in gl.values()])
        notes = " ".join(library.read(os.path.join(NOTES, d["slug"] + ".md")) for d in sharing
                         if os.path.exists(os.path.join(NOTES, d["slug"] + ".md")))
        have_nums = canon_numbers(have)
        nums, names = facts_of(text)
        note_nums = canon_numbers(notes)
        lost_n = sorted(n for n in nums if n not in have_nums and n not in note_nums)
        lost_w = sorted(w for w in names if w not in have
                        and not re.search(r"(?<!\w)%s(?!\w)" % re.escape(w), notes))
        if lost_n or lost_w:
            print("  %s  (%s)" % (ref, ", ".join(d["num"] for d in sharing) or "no chapter written"))
            if lost_n:
                print("     numbers: " + ", ".join(lost_n))
            if lost_w:
                print("     names:   " + ", ".join(lost_w))
            missing += len(lost_n) + len(lost_w)
    if not missing:
        print("  %s: every number and name in its sources is in the book or in notes/%s.md" % (c["num"], slug))
    return missing


# ------------------------------------------------------------------ fidelity

def words(text):
    return re.findall(r"[A-Za-z0-9À-ɏͰ-Ͽ$%€£+−×÷≈≤≥∑∏√∂σμΔΓΘ]+", text)


def md_words(text):
    """The words a reader should see from some house markdown, in order."""
    kept, infence = [], False
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if FENCE.match(line):
            infence = not infence
            i += 1
            continue
        if infence:
            kept.append(line)
            i += 1
            continue
        if IDEA.match(line):
            while i < len(lines) and lines[i].strip():
                i += 1
            continue
        om = OPEN.match(line)
        if om:
            kept.append(om.group(2))
            i += 1
            continue
        if CLOSE.match(line) or LABEL.match(line) or FIGURE.match(line):
            i += 1
            continue
        line = GLOSS.sub(lambda mo: mo.group(1), line)
        line = XEQREF.sub(" ", line)
        line = EQREF.sub(" ", line)
        line = MDLINK.sub(lambda mo: mo.group(1), line)
        if re.fullmatch(r"\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*", line):
            i += 1
            continue
        line = re.sub(r"^(\?\?|!!) ", " ", line)
        line = re.sub(r"^>\s?", "", line)
        line = re.sub(r"^\s*([-*]|\d+\.)\s+", " ", line)
        line = re.sub(r"^#{1,6}\s+", " ", line)
        line = line.replace("**", " ").replace("`", " ")
        line = re.sub(r"(?<![\w*])\*|\*(?![\w*])", " ", line)
        kept.append(line.replace("|", " ").replace("\\|", " "))
        i += 1
    return words("\n".join(kept))


def html_words(frag):
    frag = re.sub(r"<!--SCRIPT-->.*?<!--/SCRIPT-->", "", frag, flags=re.S)
    frag = re.sub(r'<figure class="fig".*?</figure>', " ", frag, flags=re.S)
    frag = re.sub(r'<a class="xref xeq"[^>]*>.*?</a>', " ", frag)
    frag = re.sub(r'<p class="eyebrow">.*?</p>|<h1>.*?</h1>|<p class="subtitle">.*?</p>', " ", frag)
    frag = re.sub(r"(<h2[^>]*>)\d+ · ", r"\1", frag)
    frag = re.sub(r'<p class="pnum">Question \d+</p>|<summary>Answer</summary>', " ", frag)
    defaults = [d for _c, d, _n in CALLOUTS.values() if d] + list(SPECIAL.values())
    for d in defaults:
        frag = frag.replace('<span class="ct">%s</span>' % d, " ").replace("<b>%s</b>" % d, " ")
        frag = frag.replace("<summary>%s</summary>" % d, " ").replace(">%s</h2>" % d, "> </h2>")
    frag = frag.replace('<span class="ct">Worked example: ', '<span class="ct">')
    frag = re.sub(r"</?(?:td|th|tr|p|li|h[1-6]|div|pre|table|thead|tbody|ul|ol|hr|br|details|summary)\b[^>]*>",
                  " ", frag)
    return words(plain(frag))


def verify(m, out):
    bad = 0
    total = 0
    for c in m.chapters:
        if not m.written(c) or c["slug"] == "r1":
            continue
        want = md_words(library.read(m.path(c)))
        got = html_words(out[os.path.join(SRC, c["slug"] + ".html")])
        total += len(want)
        if want != got:
            bad += 1
            k = next((i for i, (a, b) in enumerate(zip(want, got)) if a != b), min(len(want), len(got)))
            print("  differs  %s: markdown %d words, page %d; first difference at word %d"
                  % (c["num"], len(want), len(got), k))
            print("           markdown: %s" % " ".join(want[max(0, k - 8):k + 8]))
            print("           page:     %s" % " ".join(got[max(0, k - 8):k + 8]))
    return bad, total


# ------------------------------------------------------------------ the pass

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if anything generated is out of date")
    ap.add_argument("--verify", action="store_true", help="prove every word of the markdown reaches the page")
    ap.add_argument("--draft", action="store_true", help="a chapter not yet written becomes a stub")
    ap.add_argument("--preview", nargs="+", metavar="SLUG",
                    help="build these chapters and stub every other one (a local preview; not for commit)")
    ap.add_argument("--lint", nargs="+", metavar="SLUG", help="check these chapters")
    ap.add_argument("--facts", nargs="+", metavar="SLUG", help="source numbers and names a chapter lacks")
    ap.add_argument("--sources", metavar="SLUG", help="print what a chapter is rewritten from")
    args = ap.parse_args()
    m = Model()

    if args.sources:
        c = m.by_slug.get(args.sources)
        if c is None:
            sys.exit("no chapter %r" % args.sources)
        src = Sources()
        for ref in c["sources"]:
            text = src.get(ref)
            print("=" * 78)
            print("%s  (for %s · %s)" % (ref, c["num"], c["title"]))
            print("=" * 78)
            print(text if text is not None else "(no such source)")
        return
    if args.facts:
        src = Sources()
        n = sum(facts(m, s, src) for s in args.facts)
        sys.exit(1 if n else 0)
    if args.lint:
        sys.exit(1 if lint(m, args.lint) else 0)

    preview = set(args.preview) if args.preview else None
    out, errs, placed, chapters = generate(m, draft=args.draft or bool(preview), preview=preview)
    if not (args.draft or preview):
        for fid in sorted({c2 for p in m.parts for c in p["chapters"] for c2 in c["figures"]}):
            if fid not in placed:
                errs.append("figures/%s.html is placed by no chapter" % fid)
    if errs:
        for e in errs:
            print("  error  " + e)
        sys.exit("%d problem%s. Nothing written." % (len(errs), "s" * (len(errs) != 1)))

    if args.verify:
        bad, total = verify(m, out)
        if bad:
            sys.exit("spx: %d chapter%s differ from their markdown" % (bad, "s" * (bad != 1)))
        print("spx: every one of the chapters' %s words is on the page, in order, and nothing else"
              % format(total, ","))
        return

    stale = [p for p, text in out.items() if not os.path.exists(p) or library.read(p) != text]
    keep = {os.path.join(SRC, "_landing.html")}
    orphans = [os.path.join(SRC, f) for f in sorted(os.listdir(SRC))
               if f.endswith(".html") and os.path.join(SRC, f) not in out
               and os.path.join(SRC, f) not in keep]
    if args.check:
        for p in stale + orphans:
            print("  stale  " + os.path.relpath(p, library.ROOT))
        if stale or orphans:
            sys.exit("out of date. Run: python3 tools/spx.py")
        print("spx: curriculum.json, FIGURE-IDEAS.md, QUESTIONS.md, CORRECTIONS.md and %d chapters are current, "
              "with %d figures placed"
              % (len(chapters), sum(len(v) for v in placed.values())))
        return
    for p in orphans:
        os.remove(p)
    for p, text in sorted(out.items()):
        library.write(p, text)
    print("spx: %d parts, %d chapters (%d written), %d figures placed"
          % (len(m.parts), len(m.chapters), sum(1 for c in m.chapters if m.written(c)),
             sum(len(v) for v in placed.values())))
    for p in stale:
        print("  wrote  " + os.path.relpath(p, library.ROOT))
    for p in orphans:
        print("  removed " + os.path.relpath(p, library.ROOT))


if __name__ == "__main__":
    main()
