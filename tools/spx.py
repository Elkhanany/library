#!/usr/bin/env python3
"""
The Other End of the Trade: the dealer-lab curriculum into the shape the library builds.

The book was written as a web app, the Dealer Mechanics Lab, whose Education
surface is twelve markdown files with live React widgets mounted in them by
`[INTERACTIVE: id]` markers. The user of that app calls it "the SPX book". This
turns it into the two formats the library already understands, the way
tools/bc.py does for the clinical book:

    outline.json + source/*.md   ->  curriculum.json   parts, chapters, numbers
    source/*.md + figures/*.html ->  src/<slug>.html   prose, tables, figures

source/ holds the twelve files verbatim, copied from the app's
src/content/education at the commit outline.json records, so a re-import is a
copy and a run of this tool (see --import). The prose is not edited here: a
paragraph arrives with the words it left with, and --verify proves it. What
changes is presentation, into the house's own components:

    # Section N · Title       a part, "Part N · Title" (the app's own labels)
    *italic line*             the part's subtitle, on the contents page
    text before the first ##  "About this part", at the head of its first chapter
    ## 1A · Title — sub       a chapter numbered 1A, with its subtitle
    ### / ####                the chapter's sections and subsections
    > quote                   an aside (callout brick), as in the clinical book
    | table |                 the house data table (.evidence), which scrolls
                              sideways inside itself, labels every cell on a
                              phone, and bleeds into the margin on a wide screen
    ``` block ```             a preformatted formula block
    Section 8A                a link to chapter 8A
    [INTERACTIVE: id]         the figure in figures/<id>.html

figures/ holds one file per widget, rewritten for the library: a figure.fig
with a canvas drawn through NMT.Plot and controls in .ctrls, instead of a React
component. Its script is gathered into the chapter's one <!--SCRIPT--> block
after figures/_lib.js, the helpers every figure shares.

    python3 tools/spx.py             regenerate curriculum.json and src/
    python3 tools/spx.py --check     fail if either is stale, for CI
    python3 tools/spx.py --verify    prove no source word was lost or added
    python3 tools/spx.py --import ../dealer-lab
                                     refresh source/ from a dealer-lab checkout

src/ is generated for this book, as it is for the clinical one. The hand-edited
files are outline.json, figures/, src/_landing.html and, when the app's
curriculum changes, source/ by --import. Editing a chapter fragment in src/
loses the edit on the next run.
"""
import argparse
import html as htmlmod
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library

SLUG = "the-other-end-of-the-trade"
DIR = os.path.join(library.BOOKS, SLUG)
SOURCE = os.path.join(DIR, "source")
FIGS = os.path.join(DIR, "figures")
SRC = os.path.join(DIR, "src")

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
         "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"]

H1 = re.compile(r"^# Section (\d+) · (.+?)\s*$")
FENCE = re.compile(r"^```(\S*)\s*$")
LIST = re.compile(r"^(\s*)([-*]|(\d+)\.)\s+(.*)$")
MARKER = re.compile(r"\[INTERACTIVE:\s*([a-z0-9-]+)[^\]]*\]", re.I)
ALONE = re.compile(r"^\s*\[INTERACTIVE:\s*([a-z0-9-]+)[^\]]*\]\s*$", re.I)
MDLINK = re.compile(r"\[([^\]\[]+)\]\((https?://[^)\s]+)\)")
XREF = re.compile(r"\b(Section|Chapter) (\d+)([A-Z](?:\.\d+)?)?(?![\w.]*\d)")
# A heading that carries its own label ("1. Hedging", "Step 1 — …", "10A.a — …",
# "Example 1: …"). A chapter with one of these keeps its own labels, and the
# house's "N · " numbering is not laid over them.
SELF_LABEL = re.compile(r"^(\d+\.\s|Step \d|Example \d+|\d+[A-Z](?:\.\d+)?\.[a-z]\b)")


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def slugify(text):
    """The app's own anchor for a heading (src/lib/slug.js), so a link into a
    section of the app has the same fragment here."""
    t = str(text).lower()
    t = re.sub(r"[·•—–]", " ", t)
    t = re.sub(r"[^A-Za-z0-9_\s-]", "", t)     # JavaScript's \w is ASCII
    t = re.sub(r"\s+", "-", t.strip())
    return re.sub(r"-+", "-", t) or "sec"


def plain(fragment):
    """Visible text of an HTML fragment, for data-label and the fidelity pass."""
    return htmlmod.unescape(re.sub(r"<[^>]+>", "", fragment))


# ------------------------------------------------------------------ the source

class Section:
    """One source file: a part of the book."""

    def __init__(self, index, fname):
        self.index = index
        self.fname = fname
        text = library.read(os.path.join(SOURCE, fname))
        lines = text.split("\n")
        m = H1.match(lines[0])
        if not m:
            sys.exit("source/%s: the first line is not '# Section N · Title'" % fname)
        self.number = int(m.group(1))
        if self.number != index + 1:
            sys.exit("source/%s is Section %d but sits at position %d in outline.json"
                     % (fname, self.number, index + 1))
        self.title = m.group(2)
        # The italic line under the title is the part's subtitle.
        i = 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        sub = lines[i].strip() if i < len(lines) else ""
        if not re.fullmatch(r"\*[^*].*\*", sub):
            sys.exit("source/%s: the line under the title is not an italic subtitle" % fname)
        self.subtitle = sub[1:-1].strip()
        i += 1
        # Then the intro, up to the first ## heading; then the ## sections.
        self.intro = []
        self.heads = []          # [(title, [lines])]
        cur = self.intro
        infence = False
        for line in lines[i:]:
            if FENCE.match(line):
                infence = not infence
            if not infence and line.startswith("## "):
                self.heads.append((line[3:].strip(), []))
                cur = self.heads[-1][1]
                continue
            cur.append(line)

    @property
    def label(self):
        return "Part %s · %s" % (ROMAN[self.index], self.title)


# ------------------------------------------------------------------ the model

class Model:
    def __init__(self):
        self.outline = json.loads(library.read(os.path.join(DIR, "outline.json")))
        self.parts = []          # [(Section, [chapter dicts])]
        self.chapters = []       # flat, in reading order
        self.by_num = {}         # "8A" -> chapter
        self.part_first = {}     # 8 -> the part's first chapter
        errs = []
        for pi, p in enumerate(self.outline["parts"]):
            sec = Section(pi, p["file"])
            have = {t: body for t, body in sec.heads}
            used = []
            chs = []
            for c in p["chapters"]:
                c = dict(c)
                bodies = []
                for h in c["heads"]:
                    if h not in have:
                        errs.append("outline.json: %s has no ## heading %r" % (p["file"], h))
                        continue
                    if h in used:
                        errs.append("outline.json: ## %r is used twice" % h)
                    used.append(h)
                    bodies.append((h, have[h]))
                c["bodies"] = bodies
                c["part"] = sec
                self.derive_title(c, errs)
                chs.append(c)
                self.chapters.append(c)
                if c["num"] in self.by_num:
                    errs.append("outline.json: chapter number %s is used twice" % c["num"])
                self.by_num[c["num"]] = c
            for t, _b in sec.heads:
                if t not in used:
                    errs.append("outline.json: ## %r in %s belongs to no chapter" % (t, p["file"]))
            self.parts.append((sec, chs))
            self.part_first[sec.number] = chs[0]
        slugs = [c["slug"] for c in self.chapters]
        if len(set(slugs)) != len(slugs):
            errs.append("outline.json: a chapter slug is used twice")
        if errs:
            for e in errs:
                print("  error  " + e)
            sys.exit("%d problem%s in outline.json" % (len(errs), "s" * (len(errs) != 1)))

    @staticmethod
    def derive_title(c, errs):
        """'1D · Sharpe ratio — return per unit of risk' is chapter 1D, titled
        'Sharpe ratio', with 'Return per unit of risk' as its subtitle. The
        outline may set either for a chapter gathered from several headings."""
        head = c["heads"][0]
        rest = head
        if head.startswith(c["num"] + " · "):
            rest = head[len(c["num"]) + 3:]
        title, sep, sub = rest.partition(" — ")
        if len(c["heads"]) > 1 or "title" in c:
            if "title" not in c:
                errs.append("outline.json: chapter %s gathers several headings and "
                            "needs a title" % c["num"])
            c.setdefault("title", rest)
            c.setdefault("subtitle", "")
            return
        c["title"] = title.strip()
        c["subtitle"] = (sub[:1].upper() + sub[1:]).strip() if sep else ""

    def part_of(self, c):
        return c["part"]


# ------------------------------------------------------------------ figures

DRAFT = False     # --draft: a missing figure is a placeholder, not an error


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
    """A block whose meaning is in its columns: labels padded to line up, an
    order book drawn as a ladder, a template ruled with box characters. It
    keeps its layout and scrolls inside its own box on a narrow screen, where
    a formula block wraps instead (book.css, pre.aligned)."""
    body = [l for l in lines if l.strip()]
    return ((len(body) >= 2 and any(re.search(r"\S {3,}\S", l) for l in body))
            or bool(re.search(r"[═│─┌└├]|_{6,}", "\n".join(body))))


def split_row(row):
    """A table row's cells. A pipe splits a cell except when escaped, inside a
    code span, or inside parentheses: 8D writes MA(|returns|) in a cell, which
    GFM reads as two cell breaks and the app rendered as a torn row. Inside
    parentheses a pipe is an absolute value, which is what the author meant."""
    s = row.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    out, cur, depth, code, i = [], [], 0, False, 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur.append("|")
            i += 2
            continue
        if ch == "`":
            code = not code
        elif not code and ch == "(":
            depth += 1
        elif not code and ch == ")" and depth:
            depth -= 1
        elif ch == "|" and not code and depth == 0:
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

    def __init__(self, m, figs, c):
        self.m = m
        self.figs = figs
        self.c = c
        self.errs = []
        self.ids = {}
        self.scripts = []
        self.fig_uses = {}      # figure id -> times placed on this page

    def fail(self, msg):
        line = "%s: %s" % (self.c["num"], msg)
        if line not in self.errs:
            self.errs.append(line)

    def uid(self, base):
        """An id not yet used on this page: base, base-2, base-3 ..."""
        n = self.ids.get(base, 0) + 1
        self.ids[base] = n
        return base if n == 1 else "%s-%d" % (base, n)

    # ---------------------------------------------------------------- inline
    def xref(self, mo):
        """'Section 8A' becomes a link to chapter 8A and 'Section 8' one to the
        first chapter of Part 8. 'Section 1256' names no part and is the tax
        code, so it stays text; so does a reference to the page it is on."""
        word, n, lab = mo.group(1), int(mo.group(2)), mo.group(3) or ""
        target = None
        if lab:
            target = self.m.by_num.get("%d%s" % (n, lab))
        elif word == "Section" or word == "Chapter":
            target = self.m.part_first.get(n)
        if target is None or target is self.c:
            return mo.group(0)
        return '<a class="xref" href="%s.html">%s</a>' % (target["slug"], mo.group(0))

    def marker_ref(self, mo):
        """An [INTERACTIVE: id] inside a sentence names the figure rather than
        mounting a second copy of it, which is what the app did."""
        f = self.figs.get(mo.group(1).lower())
        name = f["name"] if f else mo.group(1)
        return '<a href="#fig-%s">%s</a>' % (mo.group(1).lower(), esc(name))

    def inline(self, t, links=True):
        code = []

        def stash(mo):
            code.append(mo.group(1))
            return "\x00%d\x00" % (len(code) - 1)

        t = re.sub(r"`([^`]+)`", stash, t)
        refs = []

        def keep(mo):
            refs.append(mo.group(0))
            return "\x01%d\x01" % (len(refs) - 1)

        t = MARKER.sub(keep, t)
        t = esc(t)
        t = MDLINK.sub(lambda mo: '<a href="%s">%s</a>' % (mo.group(2), mo.group(1)), t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"(?<![*\w])\*(?!\s)([^*\n]+?)(?<!\s)\*(?![*\w])", r"<em>\1</em>", t)
        if links:
            # Not inside a link the source already made.
            parts = re.split(r"(<a\b.*?</a>)", t)
            t = "".join(p if p.startswith("<a") else XREF.sub(self.xref, p) for p in parts)
        t = re.sub(r"\x01(\d+)\x01", lambda mo: self.marker_ref(MARKER.match(refs[int(mo.group(1))])), t)
        t = re.sub(r"\x00(\d+)\x00", lambda mo: "<code>%s</code>" % esc(code[int(mo.group(1))]), t)
        # An asterisk that could have opened emphasis and found no partner. One
        # after a word ("f*", the Kelly fraction) cannot open, and stays text.
        left = plain(re.sub(r"<code>.*?</code>", "", t))
        if "**" in left or re.search(r"(?<![\w*])\*(?=[^\s*])", left):
            self.fail("an asterisk survived emphasis: %r" % left[:80])
        return t

    # ---------------------------------------------------------------- blocks
    def figure(self, fid):
        f = self.figs.get(fid)
        if f is None:
            if DRAFT:
                return ('<figure class="fig" id="fig-%s"><figcaption><b>Figure to come:</b> '
                        '%s</figcaption></figure>' % (fid, fid))
            self.fail("[INTERACTIVE: %s] has no figures/%s.html" % (fid, fid))
            return ""
        n = self.fig_uses.get(fid, 0) + 1
        self.fig_uses[fid] = n
        u = fid if n == 1 else "%s-%d" % (fid, n)
        self.ids["fig-" + u] = 1
        markup = f["markup"].replace("{{uid}}", u)
        if 'id="fig-%s"' % u not in markup:
            self.fail("figures/%s.html: the figure element must carry id=\"fig-{{uid}}\"" % fid)
        if f["script"].strip():
            self.scripts.append("/* ---------- %s ---------- */\n%s"
                                % (u, f["script"].replace("{{uid}}", u).strip("\n")))
        return markup

    def table(self, rows):
        """A markdown table as the house data table (DESIGN.md section 6,
        Evidence tables): sentence-case heads, sans cells, the first column
        pinned, every cell named on a phone, sideways scroll inside its own
        box, and the bleed into the margin on a wide screen. Column floors
        come from how much a column holds, in the vocabulary book.css already
        has, so a column of prose is never twenty characters to the line."""
        cells = [split_row(r) for r in rows]
        head, rest = cells[0], cells[1:]
        align = [""] * len(head)
        if rest and all(re.fullmatch(r":?-{2,}:?", x or "") for x in rest[0]):
            align = ["right" if x.endswith(":") and not x.startswith(":") else
                     "center" if x.startswith(":") and x.endswith(":") else "" for x in rest[0]]
            rest = rest[1:]
        width = len(head)
        for r in rest:
            if len(r) != width:
                self.fail("a table row has %d cells under %d heads: %r" % (len(r), width, "|".join(r)[:60]))
        cls = []
        for j in range(width):
            if j == 0:
                cls.append("c-trial")
                continue
            lens = [len(plain(self.inline(r[j]))) for r in rest if j < len(r)]
            avg = sum(lens) / len(lens) if lens else 0
            cls.append("c-result" if avg >= 45 else "c-endpoint" if avg >= 22
                       else "c-other" if avg >= 10 else "")

        def attrs(j, label=None):
            a = ' class="%s"' % cls[j] if cls[j] else ""
            if label is not None:
                a += ' data-label="%s"' % esc(label).replace('"', "&quot;")
            if align[j]:
                a += ' style="text-align:%s"' % align[j]
            return a

        labels = [plain(self.inline(h, links=False)) for h in head]
        out = ['<div class="evidence"><div class="ev-scroll"><table class="trials"><thead><tr>']
        out += ["<th%s>%s</th>" % (attrs(j), self.inline(h, links=False)) for j, h in enumerate(head)]
        out.append("</tr></thead><tbody>")
        for r in rest:
            out.append("<tr>" + "".join(
                "<td%s>%s</td>" % (attrs(j, labels[j]), self.inline(r[j].replace("\\|", "|")))
                for j in range(min(width, len(r)))) + "</tr>")
        out.append("</tbody></table></div></div>")
        return "".join(out)

    def blocks(self, lines, level_map):
        """Markdown blocks into HTML. level_map maps a count of #'s to the
        tag and numbering it becomes on this page."""
        out, i = [], 0
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                i += 1
                continue
            fm = FENCE.match(line)
            if fm:
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
            hm = re.match(r"^(#{2,6})\s+(.*)$", line)
            if hm:
                out.append(self.heading(len(hm.group(1)), hm.group(2).strip(), level_map))
                i += 1
                continue
            if line.strip() == "---":
                out.append("<hr>")
                i += 1
                continue
            am = ALONE.match(line)
            if am:
                out.append(self.figure(am.group(1).lower()))
                i += 1
                continue
            if line.startswith(">"):
                buf = []
                while i < len(lines) and lines[i].startswith(">"):
                    buf.append(re.sub(r"^> ?", "", lines[i]))
                    i += 1
                out.append('<div class="callout brick">\n%s\n</div>'
                           % self.blocks(buf, {}))
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
                    # continuation lines belong to the item
                    while (i < len(lines) and lines[i].strip() and not LIST.match(lines[i])
                           and not lines[i].startswith(("#", ">", "|", "```"))):
                        items[-1] += " " + lines[i].strip()
                        i += 1
                    # a blank line between two items of the same list keeps it one list
                    j = i
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j > i and j < len(lines):
                        nm = LIST.match(lines[j])
                        if nm and (nm.group(3) is not None) == ordered:
                            loose = True
                            i = j
                tag = "ol" if ordered else "ul"
                attr = ' start="%d"' % start if ordered and start != 1 else ""
                wrap = (lambda s: "<p>%s</p>" % s) if loose else (lambda s: s)
                out.append("<%s%s>\n%s\n</%s>" % (tag, attr, "\n".join(
                    "<li>%s</li>" % wrap(self.inline(t)) for t in items), tag))
                continue
            buf = []
            while (i < len(lines) and lines[i].strip() and not FENCE.match(lines[i])
                   and not lines[i].startswith(("#", ">")) and lines[i].strip() != "---"
                   and not lines[i].lstrip().startswith("|") and not LIST.match(lines[i])
                   and not ALONE.match(lines[i])):
                buf.append(lines[i].strip())
                i += 1
            out.append("<p>%s</p>" % self.inline(" ".join(buf)))
        return "\n\n".join(b for b in out if b)

    def heading(self, hashes, text, level_map):
        spec = level_map.get(hashes)
        if spec is None:
            self.fail("a heading of %d #'s has nowhere to go: %r" % (hashes, text[:60]))
            return "<p><strong>%s</strong></p>" % self.inline(text, links=False)
        tag, counter = spec
        hid = self.uid(slugify(text))
        shown = self.inline(text, links=False)
        if counter is not None:
            counter[0] += 1
            shown = "%d · %s" % (counter[0], shown)
        return '<%s id="%s">%s</%s>' % (tag, hid, shown, tag)

    # ----------------------------------------------------------------- whole
    def render(self):
        c = self.c
        sec = c["part"]
        head = ['<p class="eyebrow">Part %s · %s · Chapter %s</p>'
                % (ROMAN[sec.index], esc(sec.title), esc(c["num"])),
                "<h1>%s</h1>" % self.inline(c["title"], links=False)]
        if c.get("subtitle"):
            head.append('<p class="subtitle">%s</p>' % self.inline(c["subtitle"], links=False))
        body = []
        if self.m.part_first[sec.number] is c and any(l.strip() for l in sec.intro):
            intro = [l for l in sec.intro]
            while intro and not intro[-1].strip():
                intro.pop()
            # The intro ends on the rule that closed it in the source; the
            # rule stays, between the part's preamble and the chapter.
            ends_rule = bool(intro) and intro[-1].strip() == "---"
            if ends_rule:
                intro.pop()
            body.append('<div class="callout where">\n<span class="ct">About this part</span>\n%s\n</div>'
                        % self.blocks(intro, {}))
            if ends_rule:
                body.append("<hr>")
        merged = len(c["bodies"]) > 1
        if merged:
            n = [0]
            for h, lines in c["bodies"]:
                name = h.partition(" — ")[2] or h
                hid = self.uid(slugify(name))
                n[0] += 1
                body.append('<h2 id="%s">%d · %s</h2>' % (hid, n[0], self.inline(name, links=False)))
                body.append(self.blocks(self.trim(lines), {3: ("h3", None), 4: ("h3", None)}))
        else:
            lines = self.trim(c["bodies"][0][1]) if c["bodies"] else []
            heads = [re.sub(r"^#+\s+", "", l) for l in lines if re.match(r"^###\s", l)]
            labelled = any(SELF_LABEL.match(h) for h in heads)
            counter = None if labelled else [0]
            body.append(self.blocks(lines, {3: ("h2", counter), 4: ("h3", None)}))
        out = "\n\n".join(head + [b for b in body if b]) + "\n"
        if self.scripts:
            lib = self.figs.library_js().strip("\n")
            out += "\n<!--SCRIPT-->\n%s\n\n%s\n<!--/SCRIPT-->\n" % (lib, "\n\n".join(self.scripts))
        return out

    @staticmethod
    def trim(lines):
        """A section's lines without the rule that closed it in the source:
        the ---s between ## subsections are the app's chapter breaks, and
        here each of those is a page."""
        lines = list(lines)
        while lines and not lines[-1].strip():
            lines.pop()
        if lines and lines[-1].strip() == "---":
            lines.pop()
        return lines


# ------------------------------------------------------------------ outputs

def curriculum(m):
    parts = []
    for sec, chs in m.parts:
        parts.append({
            "label": sec.label,
            "subtitle": sec.subtitle,
            "chapters": [{"num": c["num"], "slug": c["slug"], "title": c["title"], "math": False}
                         for c in chs],
        })
    return json.dumps(parts, indent=1, ensure_ascii=False) + "\n"


def generate(m):
    figs = Figures()
    out = {os.path.join(DIR, "curriculum.json"): curriculum(m)}
    errs = []
    placed = {}
    for c in m.chapters:
        ch = Chapter(m, figs, c)
        out[os.path.join(SRC, c["slug"] + ".html")] = ch.render()
        errs += ch.errs
        for fid in ch.fig_uses:
            placed.setdefault(fid, []).append(c["num"])
    if os.path.isdir(FIGS):
        for f in sorted(os.listdir(FIGS)):
            if f.endswith(".html") and f[:-5] not in placed:
                errs.append("figures/%s is placed by no [INTERACTIVE] marker" % f)
    return out, errs, placed


# ------------------------------------------------------------------ fidelity

def words(text):
    return re.findall(r"[A-Za-z0-9À-ɏͰ-Ͽ$%€£+−×÷≈≤≥∑∏√∂σμΔΓΘ]+", text)


def source_words(sec_lines):
    """The words a reader of the app sees in some markdown: no markers, no
    markup, no link targets, no table rules. A fenced block is read as it
    stands, since nothing inside one is markup."""
    kept, infence = [], False
    for line in sec_lines:
        if FENCE.match(line):
            infence = not infence
            continue
        if infence:
            kept.append(line)
            continue
        line = MARKER.sub(" ", line)
        line = MDLINK.sub(lambda mo: mo.group(1), line)
        if re.fullmatch(r"\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*", line):
            continue
        line = re.sub(r"^>\s?", "", line)
        line = re.sub(r"^\s*([-*]|\d+\.)\s+", " ", line)
        line = re.sub(r"^#{1,6}\s+", " ", line)
        line = line.replace("**", " ").replace("`", " ")
        line = re.sub(r"(?<![\w*])\*|\*(?![\w*])", " ", line)
        kept.append(line.replace("|", " "))
    return words("\n".join(kept))


def verify(m, out):
    """Every word of the source, in order, is in the book, and nothing is in the
    book's prose that was not in the source, apart from what this tool adds on
    purpose: eyebrows, the 'About this part' kicker, section numbers, the
    chapter number and section names it strips out of a title, and figures."""
    bad = 0
    for sec, chs in m.parts:
        want = []
        for c in chs:
            want += words(" ".join(c["heads"]))
            for _h, lines in c["bodies"]:
                want += source_words(lines)
        intro = source_words(sec.intro)
        got = []
        for c in chs:
            frag = library.read(os.path.join(SRC, c["slug"] + ".html")) if not out else \
                out[os.path.join(SRC, c["slug"] + ".html")]
            frag = re.sub(r"<!--SCRIPT-->.*?<!--/SCRIPT-->", "", frag, flags=re.S)
            frag = re.sub(r'<figure class="fig".*?</figure>', " ", frag, flags=re.S)
            frag = re.sub(r'<a href="#fig-[^"]*">.*?</a>', " ", frag)
            frag = re.sub(r'<p class="eyebrow">.*?</p>', " ", frag)
            frag = re.sub(r'<span class="ct">About this part</span>', " ", frag)
            frag = re.sub(r"(<h[23][^>]*>)\d+ · ", r"\1", frag)
            # the chapter title and subtitle stand for the ## heading
            title = c["heads"][0] if len(c["heads"]) == 1 else " ".join(c["heads"])
            frag = re.sub(r"<h1>.*?</h1>", " %s " % esc(title), frag, count=1)
            frag = re.sub(r'<p class="subtitle">.*?</p>', " ", frag, count=1)
            if len(c["heads"]) > 1:
                for h in c["heads"]:
                    name = h.partition(" — ")[2] or h
                    frag = frag.replace(">%s</h2>" % esc(name), "> </h2>", 1)
            # a cell, an item or a block ends a word; an inline tag does not
            frag = re.sub(r"</?(?:td|th|tr|p|li|h[1-6]|div|pre|table|thead|tbody|ul|ol|hr|br)\b[^>]*>",
                          " ", frag)
            got += words(plain(frag))
        # the intro opens the part's first chapter, after its title
        n_title = len(words(chs[0]["heads"][0] if len(chs[0]["heads"]) == 1 else " ".join(chs[0]["heads"])))
        want = want[:n_title] + intro + want[n_title:]
        if want != got:
            bad += 1
            k = next((i for i, (a, b) in enumerate(zip(want, got)) if a != b), min(len(want), len(got)))
            print("  differs  %s: source %d words, book %d; first difference at word %d"
                  % (sec.fname, len(want), len(got), k))
            print("           source: %s" % " ".join(want[max(0, k - 8):k + 8]))
            print("           book:   %s" % " ".join(got[max(0, k - 8):k + 8]))
    return bad


# ------------------------------------------------------------------ the pass

def do_import(path):
    src = os.path.join(path, "src", "content", "education")
    if not os.path.isdir(src):
        sys.exit("%s is not a dealer-lab checkout: no src/content/education" % path)
    names = sorted(f for f in os.listdir(src) if f.endswith(".md"))
    for f in names:
        shutil.copyfile(os.path.join(src, f), os.path.join(SOURCE, f))
    print("spx: copied %d files into %s" % (len(names), os.path.relpath(SOURCE, library.ROOT)))
    print("     record the commit in outline.json 'origin', then run python3 tools/spx.py")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if anything on disk is out of date")
    ap.add_argument("--verify", action="store_true", help="prove the prose is the source's, word for word")
    ap.add_argument("--draft", action="store_true", help="let a missing figure be a placeholder")
    ap.add_argument("--import", dest="imp", metavar="DEALER_LAB", help="refresh source/ from a checkout")
    args = ap.parse_args()

    if args.imp:
        do_import(args.imp)
        return

    global DRAFT
    DRAFT = args.draft
    m = Model()
    out, errs, placed = generate(m)
    if errs:
        for e in errs:
            print("  error  " + e)
        sys.exit("%d problem%s. Nothing written." % (len(errs), "s" * (len(errs) != 1)))

    if args.verify:
        bad = verify(m, out)
        if bad:
            sys.exit("spx: %d part%s differ from the source" % (bad, "s" * (bad != 1)))
        n = sum(len(source_words(sec.intro)) + sum(len(source_words(l)) for c in chs
                                                     for _h, l in c["bodies"])
                for sec, chs in m.parts)
        print("spx: every one of the source's %s words is in the book, in order, and nothing else"
              % format(n, ","))
        return

    stale = [p for p, text in out.items() if not os.path.exists(p) or library.read(p) != text]
    keep = {os.path.join(SRC, f) for f in ("_landing.html",)}
    orphans = [os.path.join(SRC, f) for f in sorted(os.listdir(SRC))
               if f.endswith(".html") and os.path.join(SRC, f) not in out
               and os.path.join(SRC, f) not in keep]

    if args.check:
        for p in stale + orphans:
            print("  stale  " + os.path.relpath(p, library.ROOT))
        if stale or orphans:
            sys.exit("out of date. Run: python3 tools/spx.py")
        print("spx: curriculum.json and %d chapters are current, with %d figures placed"
              % (len(out) - 1, sum(len(v) for v in placed.values())))
        return

    for p in orphans:
        os.remove(p)
    for p, text in sorted(out.items()):
        library.write(p, text)
    print("spx: %d parts, %d chapters, %d figures placed"
          % (len(m.parts), len(m.chapters), sum(len(v) for v in placed.values())))
    for p in stale:
        print("  wrote  " + os.path.relpath(p, library.ROOT))
    for p in orphans:
        print("  removed " + os.path.relpath(p, library.ROOT))


if __name__ == "__main__":
    main()
