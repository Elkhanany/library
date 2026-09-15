#!/usr/bin/env python3
"""
Breast Cancer: outline.yaml and markdown chapters into the shape the library builds.

This book is the first in the library whose structure is data rather than a
hand-kept list, and the reason is scale. Ninety-three chapters and seven hundred
and seventy-eight sections cannot be renumbered by hand, and they will be
reordered while it is being written. So the book keeps two source formats the
rest of the library does not have, and this turns them into the two the library
already understands:

    outline.yaml          ->  curriculum.json     structure, display numbers
    chapters/BC-###.md    ->  src/BC-###.html     prose, citations resolved

Everything in outline.yaml carries a permanent id. Nothing in it knows its own
number. `Part VI`, `Chapter 28` and `28.4` are computed here and exist only in
the output, so moving a chapter changes where it reads and nothing else. A
chapter file is named for its id for the life of the book.

    python3 tools/bc.py             regenerate both
    python3 tools/bc.py --check     fail if either is stale, for CI

`src/` is generated for this book, which is a deliberate exception to the rule
that src/ is the only hand-edited tree. The hand-edited files here are
`chapters/*.md` and `outline.yaml`. Editing a fragment in src/ loses the edit on
the next run.
"""
import argparse
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library
import evidence

try:
    import yaml
except ImportError:                                   # pragma: no cover
    sys.exit("bc.py needs pyyaml:  pip install pyyaml")

SLUG = "breast-cancer"
DIR = os.path.join(library.BOOKS, SLUG)

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
         "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"]

# The fenced blocks a chapter may use, and what each renders as. Every one maps
# onto a callout the house stylesheet already defines, so a new block type is a
# line here rather than a new colour in the shared CSS.
FENCES = {
    "interplay": ("interplay", "Interplay"),
    "practice":  ("practice", "In practice"),
    "caution":   ("warn", "Caution"),
}

# The evidence block is not a callout. It carries only a filter, and the rows are
# rendered from trials.yaml at build time so a new readout is entered once in the
# registry and appears in every chapter whose filter matches it. See CONVENTIONS.md.
try:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import evidence as _ev
except Exception:                                        # pragma: no cover
    _ev = None

# The story block is the argument the evidence table is evidence for. It carries
# an ST- or SQ- id rather than a filter, because a story is authored and a table
# is derived. See tools/stories.py.
import stories as _st

# The space before the bracket is eaten with it. A citation is comfortable to
# type as "...mechanism [@ali2020]." and has to set as "...mechanism<sup>1</sup>.",
# hugging the word it qualifies. Every one of the 591 citations in the first
# wave was written with that space, so this is the difference between a
# reference mark and a floating numeral.
CITE_GROUP = re.compile(r"[ \t]*\[(@[A-Za-z0-9_\-]+(?:\s*;\s*@[A-Za-z0-9_\-]+)*)\]")
CITE_KEY = re.compile(r"@([A-Za-z0-9_\-]+)")
TRIAL = re.compile(r"\{\{trial:([A-Za-z0-9_\-]+)\}\}")
TERM = re.compile(r"\[\[term:([A-Za-z0-9_\-]+)\]\]")
XREF = re.compile(r"\[\[((?:BC|BS|PT|APP)-[A-Z0-9]+)\]\]")
MDLINK = re.compile(r"\[([^\]\[]+)\]\((https?://[^)\s]+)\)")
FENCE = re.compile(r"^```([A-Za-z0-9_\-]*)(.*)$")
HEAD = re.compile(r"^(#{2,3})\s+(BS-\d{4})\s*(.*)$")
FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def load():
    """outline, references, trials, glossary — the whole data layer, once."""
    def y(name):
        return yaml.safe_load(library.read(os.path.join(DIR, name)))
    outline = y("outline.yaml")
    refs = y("references.yaml")["refs"]
    trials = y("trials.yaml").get("trials") or {}
    terms = y("glossary.yaml").get("terms") or {}
    stories = y("stories.yaml").get("stories") or {}
    return outline, refs, trials, terms, stories


class Model:
    """Everything the converter needs to resolve a permanent id to a place."""

    def __init__(self):
        self.outline, self.refs, self.trials, self.terms, self.stories = load()
        # An old spelling of a key still resolves, so links written before a key
        # was regularised do not rot.
        self.alias = {a: k for k, v in self.refs.items()
                      for a in (v.get("aliases") or [])}
        self.title = {}        # id -> display title
        self.owner = {}        # section id -> chapter id
        self.secnum = {}       # section id -> position within its chapter
        self.chapnum = {}      # chapter id -> flat chapter number
        self.part_of = {}      # chapter id -> (roman, part title)
        self.sections = {}     # chapter id -> [section ids, in order]

        n = 0
        for pi, p in enumerate(self.outline["parts"]):
            self.title[p["id"]] = p["title"]
            for c in p["chapters"]:
                n += 1
                cid = c["id"]
                self.title[cid] = c["title"]
                self.chapnum[cid] = n
                self.part_of[cid] = (ROMAN[pi], p["title"])
                self.sections[cid] = []
                for si, s in enumerate(c.get("sections") or [], 1):
                    if not isinstance(s, dict):
                        # A section written as a bare string, which is how a new
                        # one is meant to be added. Say so, rather than failing
                        # on a string index six frames down.
                        sys.exit("%s: section %r has no id yet. Run: "
                                 "python3 tools/bc.py --mint" % (cid, str(s)[:50]))
                    self.title[s["id"]] = s["title"]
                    self.owner[s["id"]] = cid
                    self.secnum[s["id"]] = si
                    self.sections[cid].append(s["id"])
        for a in self.outline.get("appendices") or []:
            self.title[a["id"]] = a["title"]

    def unverified(self, key):
        """A reference whose identifier is claimed but not yet confirmed.

        Two spellings mean the same thing, because two passes of this book used
        different ones: `verify: true` marks an entry queued for checking, and
        `verified: false` marks one that failed. An entry with neither field is
        one of the originals, carried over already checked."""
        r = self.refs.get(key) or {}
        return r.get("verify") is True or r.get("verified") is False

    def drafted(self, cid):
        """A chapter is written when its markdown exists. The check is against
        the source and not against src/, which this tool is in the middle of
        writing and would answer differently depending on the order."""
        return os.path.exists(os.path.join(DIR, "chapters", cid + ".md"))

    def href(self, tid):
        """Where a permanent id lives in the built book, or None if nowhere yet."""
        if tid.startswith("BC-"):
            return tid + ".html" if self.drafted(tid) else None
        if tid.startswith("BS-"):
            cid = self.owner.get(tid)
            if cid and self.drafted(cid):
                return "%s.html#%s" % (cid, tid)
            return None
        return None            # parts and appendices have no page of their own yet


# ------------------------------------------------------------------ curriculum

def curriculum(m):
    """The library reads this. Display numbers are computed here and nowhere
    else, so nothing in outline.yaml has to know where it sits."""
    # A part's `note` in outline.yaml is an instruction to whoever writes it
    # ("Resist starting at checkpoints"), and the contents page is read by
    # people who are not writing it. So the reader-facing line is the blurb
    # from book.json, which is the same copy the landing page shows, and the
    # note stays where it belongs.
    arc = json.loads(library.read(os.path.join(DIR, "book.json"))).get("arc") or []
    if arc and len(arc) != len(m.outline["parts"]):
        sys.exit("book.json has %d arc entries for %d parts. They are matched by "
                 "position, so they have to agree." % (len(arc), len(m.outline["parts"])))
    parts = []
    for pi, p in enumerate(m.outline["parts"]):
        blurb = arc[pi][2] if arc else (p.get("note") or "")
        parts.append({
            "label": "Part %s · %s" % (ROMAN[pi], p["title"]),
            "subtitle": " ".join(blurb.split()),
            "chapters": [{"num": str(m.chapnum[c["id"]]),
                          "slug": c["id"],
                          "title": c["title"],
                          "math": False}
                         for c in p["chapters"]],
        })
    return json.dumps(parts, indent=1, ensure_ascii=False) + "\n"


# -------------------------------------------------------------------- markdown

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def format_ref(key, r):
    """One bibliography line. PubMed when there is a PMID, DOI otherwise, and
    neither when the entry has only a citation."""
    # "Konecny G, et al." already ends in a full stop and most titles do not,
    # so the separator has to look at what it is joining.
    s = ". ".join(b.rstrip(".") for b in (r.get("authors"), r.get("title")) if b)
    tail = []
    if r.get("journal"):
        tail.append("<em>%s</em>" % esc(r["journal"]))
    if r.get("year"):
        tail.append(str(r["year"]))
    if r.get("volume"):
        tail.append(("%s:%s" % (r["volume"], r.get("pages", ""))).rstrip(":"))
    out = esc(s) + (". " + " ".join(tail) if tail else "")
    if r.get("pmid"):
        out += '. <a href="https://pubmed.ncbi.nlm.nih.gov/%s/">PMID&nbsp;%s</a>' % (
            r["pmid"], r["pmid"])
    elif r.get("doi"):
        out += '. <a href="https://doi.org/%s">doi:%s</a>' % (r["doi"], esc(r["doi"]))
    return out


class Chapter:
    """One markdown chapter, on its way to being one HTML fragment."""

    def __init__(self, m, cid):
        self.m = m
        self.cid = cid
        self.order = []        # reference keys, in order of first appearance
        self.seen = {}
        self.errs = []
        self.interplay = []    # (target id, text) — APP-F is built from these

    def fail(self, msg):
        # One line per distinct problem. A key cited ten times in a chapter is
        # one thing to fix, and ten identical lines bury the other nine faults.
        line = "%s: %s" % (self.cid, msg)
        if line not in self.errs:
            self.errs.append(line)

    # ---------------------------------------------------------------- inline
    def cite(self, mo):
        out = []
        for key in CITE_KEY.findall(mo.group(1)):
            k = self.m.alias.get(key, key)
            if k not in self.m.refs:
                self.fail("citation [@%s] is not in references.yaml" % key)
                k = key
            elif self.m.unverified(k):
                # A reference whose identifier has been claimed but not checked
                # against the source. In a clinical book that is worse than a
                # missing citation, because it reads as if someone confirmed it.
                # Resolve the identifier or drop the sentence.
                self.fail("citation [@%s] is not verified. Confirm its identifier "
                          "in references.yaml before it reaches a chapter." % k)
            if k not in self.seen:
                self.order.append(k)
                self.seen[k] = len(self.order)
            out.append('<a href="#r-%s" class="cite">%d</a>' % (k, self.seen[k]))
        return "<sup>" + ",".join(out) + "</sup>"

    def trial(self, mo):
        k = mo.group(1)
        t = self.m.trials.get(k)
        if t is None:
            self.fail("{{trial:%s}} is not in trials.yaml" % k)
            return esc(k)
        bits = [b for b in (("phase %s" % t["phase"]) if t.get("phase") else None,
                            t.get("setting"), t.get("subtitle") or t.get("subtype"),
                            t.get("topic")) if b]
        return '<span class="trial" title="%s">%s</span>' % (
            esc("; ".join(bits)), esc(t.get("acronym", k)))

    def term(self, mo):
        k = mo.group(1)
        g = self.m.terms.get(k)
        if g is None:
            self.fail("[[term:%s]] is not in glossary.yaml" % k)
            return esc(k)
        return '<span class="gloss" title="%s">%s</span>' % (
            esc(g["definition"]), esc(g["term"]))

    def xref(self, mo):
        tid = mo.group(1)
        label = self.m.title.get(tid)
        if label is None:
            self.fail("[[%s]] resolves to nothing in outline.yaml" % tid)
            return esc(tid)
        if tid == self.cid:
            self.fail("[[%s]] points at the chapter it sits in" % tid)
        href = self.m.href(tid)
        if href:
            return '<a href="%s" class="xref">%s</a>' % (href, esc(label))
        # An honest dead end. A link here would 404, and a reader deserves to
        # know the chapter is planned rather than missing.
        return '<span class="xref pending" title="Not written yet">%s</span>' % esc(label)

    def inline(self, t):
        code = []

        def stash(mo):
            code.append(mo.group(1))
            return "\x00%d\x00" % (len(code) - 1)

        t = re.sub(r"`([^`]+)`", stash, t)
        t = esc(t)
        t = CITE_GROUP.sub(self.cite, t)
        t = TRIAL.sub(self.trial, t)
        t = TERM.sub(self.term, t)
        t = XREF.sub(self.xref, t)
        t = MDLINK.sub(lambda mo: '<a href="%s">%s</a>' % (mo.group(2), mo.group(1)), t)
        t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", t)
        t = re.sub(r"\x00(\d+)\x00",
                   lambda mo: "<code>%s</code>" % esc(code[int(mo.group(1))]), t)
        return t

    # ----------------------------------------------------------------- blocks
    def fence(self, kind, arg, body):
        if kind == "html":
            return body
        if kind == "evidence":
            return self.evidence(arg, body)
        if kind == "story":
            return self.story(arg, body)
        if kind not in FENCES:
            self.fail("unknown fenced block '%s'" % kind)
            return ""
        cls, label = FENCES[kind]
        see = ""
        if kind == "interplay":
            mo = re.search(r"target=((?:BC|BS|APP)-[A-Z0-9]+)", arg)
            if not mo:
                self.fail("an interplay block needs target=BC-###")
            else:
                tid = mo.group(1)
                self.interplay.append((tid, " ".join(body.split())))
                if self.m.title.get(tid) is None:
                    self.fail("interplay target %s resolves to nothing" % tid)
                else:
                    see = "<p class=\"ct-see\">See %s</p>" % self.xref(
                        re.match(r"\[\[(.+)\]\]", "[[%s]]" % tid))
        paras = "\n".join("<p>%s</p>" % self.inline(" ".join(p.split()))
                          for p in re.split(r"\n\s*\n", body.strip()) if p.strip())
        return ('<div class="callout %s">\n<span class="ct">%s</span>\n%s\n%s</div>'
                % (cls, label, paras, see))

    def evidence(self, arg, body):
        if body.strip():
            self.fail("an evidence block carries only a filter, not a body")
        if _ev is None:
            self.fail("evidence block needs tools/evidence.py")
            return ""
        f, bad = _ev.parse_filter(arg.strip())
        for b in bad:
            self.fail("evidence filter: %s" % b)
        if bad:
            return ""
        hits = _ev.select(self.m.trials, f)
        if not hits:
            self.fail("evidence filter %r matches no trial" % arg.strip())
            return ""
        md = _ev.render(hits, f)
        rows = [r for r in md.splitlines() if r.startswith("|")]
        cap = [r for r in md.splitlines() if r.startswith("_")]
        head = [c.strip() for c in rows[0].strip("|").split("|")]
        out = ["<div class=\"evidence\"><table class=\"trials\"><thead><tr>"]
        out += ["<th>%s</th>" % esc(h) for h in head]
        out.append("</tr></thead><tbody>")
        for r in rows[2:]:
            cells = [c.strip() for c in r.strip("|").split("|")]
            out.append("<tr>" + "".join(
                "<td>%s</td>" % self.inline(c.replace("\\|", "|")) for c in cells) + "</tr>")
        out.append("</tbody></table>")
        if cap:
            out.append("<p class=\"ct-cap\">%s</p>" % self.inline(cap[0].strip("_")))
        out.append("</div>")
        return "".join(out)

    def story(self, arg, body):
        """```story ST-010``` or ```story SQ-0010,SQ-0020```.

        A story block renders the argument, not the numbers. Each question comes
        out as five labelled moves and the trials that carry it, and every trial
        is the same {{trial:key}} chip a chapter would write by hand, so it
        links into the registry and counts as a citation of that trial."""
        if body.strip():
            self.fail("a story block carries only an id, not a body")
        ids = [i.strip() for i in arg.strip().split(",") if i.strip()]
        if not ids:
            self.fail("a story block needs an ST- or SQ- id")
            return ""
        sid, st, qs = None, None, []
        for i in ids:
            s2, story, got = _st.find(self.m.stories, i)
            if not story:
                self.fail("story block: %s resolves to nothing" % i)
                return ""
            if sid and s2 != sid:
                self.fail("story block: %s is not in %s. One block, one story." % (i, sid))
                return ""
            sid, st = s2, story
            qs += got
        seen = set()
        qs = [q for q in qs if not (q["id"] in seen or seen.add(q["id"]))]
        out = ['<div class="story" id="%s">' % esc(sid if len(ids) == 1 and ids[0] == sid else qs[0]["id"])]
        out.append('<p class="st-where">%s &middot; %s &middot; %s</p>'
                   % (esc(_st.SETTING_LABEL[st["setting"]]), esc(st["subtype"]),
                      esc(st["stage"])))
        out.append('<p class="st-title">%s</p>' % self.inline(st["title"]))
        if st.get("premise") and len(ids) == 1 and ids[0] == sid:
            out.append('<p class="st-premise">%s</p>' % self.inline(st["premise"]))
        for q in qs:
            out.append('<div class="sq" id="%s">' % esc(q["id"]))
            out.append('<p class="sq-ask">%s</p>' % self.inline(q["ask"]))
            out.append("<dl class=\"sq-moves\">")
            for mv in _st.MOVES:
                out.append("<dt>%s</dt><dd>%s</dd>"
                           % (esc(_st.MOVE_LABEL[mv]), self.inline(q[mv])))
            out.append("</dl>")
            out.append('<p class="sq-trials">%s</p>' % " ".join(
                self.trial(re.match(r"\{\{trial:(.+)\}\}", "{{trial:%s}}" % t))
                for t in q.get("trials") or []))
            out.append("</div>")
        out.append("</div>")
        return "".join(out)

    def heading(self, hashes, sid, text):
        want = self.m.title.get(sid)
        if want is None or self.m.owner.get(sid) != self.cid:
            self.fail("%s is not a section of this chapter in outline.yaml" % sid)
            want = text or sid
        elif text and " ".join(text.split()) != " ".join(want.split()):
            self.fail("%s heading says %r, outline.yaml says %r. Fix one."
                      % (sid, text, want))
        if len(hashes) == 2:
            return '<h2 id="%s">%d · %s</h2>' % (
                sid, self.m.secnum.get(sid, 0), self.inline(want))
        return '<h3 id="%s">%s</h3>' % (sid, self.inline(want))

    def body(self, text):
        lines = text.split("\n")
        out, i = [], 0
        while i < len(lines):
            line = lines[i]
            fm = FENCE.match(line)
            if fm:
                kind, arg, buf = fm.group(1), fm.group(2), []
                i += 1
                while i < len(lines) and not lines[i].startswith("```"):
                    buf.append(lines[i])
                    i += 1
                i += 1
                out.append(self.fence(kind, arg, "\n".join(buf)))
                continue
            hm = HEAD.match(line)
            if hm:
                out.append(self.heading(hm.group(1), hm.group(2), hm.group(3)))
                i += 1
                continue
            if line.startswith("#"):
                self.fail("a heading must carry its section id: %r" % line[:60])
                i += 1
                continue
            if not line.strip():
                i += 1
                continue
            if line.startswith(">"):
                buf = []
                while i < len(lines) and lines[i].startswith(">"):
                    buf.append(lines[i].lstrip("> ").rstrip())
                    i += 1
                out.append('<div class="callout brick">\n%s\n</div>' % "\n".join(
                    "<p>%s</p>" % self.inline(" ".join(p.split()))
                    for p in re.split(r"\n\s*\n", "\n".join(buf)) if p.strip()))
                continue
            if line.lstrip().startswith("|"):
                buf = []
                while i < len(lines) and lines[i].lstrip().startswith("|"):
                    buf.append(lines[i].strip())
                    i += 1
                out.append(self.table(buf))
                continue
            lm = re.match(r"^(\s*)([-*]|\d+\.)\s+", line)
            if lm:
                tag = "ul" if lm.group(2) in "-*" else "ol"
                items = []
                while i < len(lines) and re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
                    items.append(re.sub(r"^\s*([-*]|\d+\.)\s+", "", lines[i]))
                    i += 1
                out.append("<%s>\n%s\n</%s>" % (
                    tag, "\n".join("<li>%s</li>" % self.inline(t) for t in items), tag))
                continue
            buf = []
            while (i < len(lines) and lines[i].strip()
                   and not lines[i].startswith(("#", ">", "```"))
                   and not lines[i].lstrip().startswith("|")
                   and not re.match(r"^\s*([-*]|\d+\.)\s+", lines[i])):
                buf.append(lines[i].strip())
                i += 1
            out.append("<p>%s</p>" % self.inline(" ".join(buf)))
        return "\n\n".join(b for b in out if b)

    def table(self, rows):
        cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
        head, rest = cells[0], cells[1:]
        if rest and all(re.fullmatch(r":?-{2,}:?", c or "") for c in rest[0]):
            rest = rest[1:]
        th = "".join("<th>%s</th>" % self.inline(c) for c in head)
        tr = "\n".join("<tr>%s</tr>" % "".join("<td>%s</td>" % self.inline(c)
                                               for c in r) for r in rest)
        return ("<table>\n<thead><tr>%s</tr></thead>\n<tbody>\n%s\n</tbody>\n</table>"
                % (th, tr))

    # ------------------------------------------------------------------ whole
    def render(self, text):
        front = {}
        fm = FRONT.match(text)
        if fm:
            front = yaml.safe_load(fm.group(1)) or {}
            text = text[fm.end():]
        if front.get("id") and front["id"] != self.cid:
            self.fail("front matter id %r does not match the filename" % front["id"])

        title = self.m.title[self.cid]
        if front.get("title") and " ".join(str(front["title"]).split()) != title:
            self.fail("front matter title %r, outline.yaml says %r. Fix one."
                      % (front["title"], title))

        roman, part = self.m.part_of[self.cid]
        head = ['<p class="eyebrow">Part %s · %s · Chapter %d</p>'
                % (roman, esc(part), self.m.chapnum[self.cid]),
                "<h1>%s</h1>" % esc(title)]
        if front.get("subtitle"):
            head.append('<p class="subtitle">%s</p>' % self.inline(str(front["subtitle"])))

        body = self.body(text)

        written = {sid for sid in re.findall(r'<h[23] id="(BS-\d{4})"', body)}
        missing = [s for s in self.m.sections[self.cid] if s not in written]

        tail = []
        if missing:
            # The plan is public rather than silent. A reader can see what this
            # chapter will cover, and so can whoever writes it next.
            tail.append('<div class="callout brick to-come">\n<span class="ct">'
                        'Still to be written</span>\n<ol>\n%s\n</ol>\n</div>'
                        % "\n".join('<li value="%d">%s</li>'
                                    % (self.m.secnum[s], esc(self.m.title[s]))
                                    for s in missing))
        if self.order:
            tail.append('<h2 class="refs-head" id="references">References</h2>')
            # Only the keys that resolved. An unresolved one is already recorded
            # as an error by cite(), and a bare refs[k] here raised KeyError on
            # the first bad key -- before main() could print the error list, so
            # the one tool meant to name a broken citation died instead of
            # reporting it. Nothing is written when errs is non-empty anyway.
            tail.append('<ol class="refs">\n%s\n</ol>' % "\n".join(
                '<li id="r-%s">%s</li>' % (k, format_ref(k, self.m.refs[k]))
                for k in self.order if k in self.m.refs))
        return "\n\n".join(head + [body] + tail) + "\n"


# ---------------------------------------------------------------- minting ids

SECTIONS_KEY = re.compile(r"^(\s*)sections:\s*$")
BARE = re.compile(r"^(\s*)-\s+(?!id:)(\S.*?)\s*$")


def mint(dry=False):
    """Give a permanent id to any section written as a bare string.

    Write a new section under the right chapter as

        - Reversion mutations and restored repair

    run this, and it becomes

        - id: BS-6740
          title: Reversion mutations and restored repair

    Ids come from the highest one in use plus ten, so a deleted id is never
    handed out again and a link to it never quietly starts resolving to
    something else. Nothing that already carries an id is touched.

    The rewrite is textual rather than a YAML round trip, because a round trip
    reformats seventy thousand lines and buries the one line that changed.
    """
    path = os.path.join(DIR, "outline.yaml")
    lines = library.read(path).split("\n")
    used = {int(n) for n in re.findall(r"\bBS-(\d{4})\b", "\n".join(lines))}
    nxt = (max(used) if used else 0) + 10

    out, minted, inside, depth = [], [], False, 0
    for line in lines:
        k = SECTIONS_KEY.match(line)
        if k:
            inside, depth = True, len(k.group(1))
            out.append(line)
            continue
        if inside and line.strip():
            ind = len(line) - len(line.lstrip())
            # A YAML sequence may sit at the same indent as the key that owns
            # it, and this file writes them that way, so "indented further" is
            # not the test for still being inside the block. An item at exactly
            # this indent belongs to it; anything shallower, or any key at this
            # indent, has ended it.
            item = line.lstrip().startswith("- ")
            if not ((item and ind == depth) or ind > depth):
                inside = False
        b = BARE.match(line) if inside else None
        if not b:
            out.append(line)
            continue
        pad, title = b.group(1), b.group(2)
        sid = "BS-%04d" % nxt
        nxt += 10
        minted.append((sid, title.strip('"\'')))
        # The scalar is copied through exactly as it was written, so the
        # author's own quoting is what YAML sees and nothing is re-escaped.
        out.append("%s- id: %s" % (pad, sid))
        out.append("%s  title: %s" % (pad, title))

    if not minted:
        print("bc: every section already has an id")
        return 0
    for sid, title in minted:
        print("  %s  %s" % (sid, title[:66]))
    if dry:
        print("bc: %d would be minted. Run without --dry-run." % len(minted))
    else:
        library.write(path, "\n".join(out))
        print("bc: minted %d section id%s" % (len(minted), "s" * (len(minted) != 1)))
    return len(minted)


# ------------------------------------------------------------------- the pass

def trialdata(m):
    """books/breast-cancer/src/data/trials.json -- what the appendix reads.

    Generated, never hand-written, so the appendix cannot disagree with the
    registry the chapters are built from. It carries three things the registry
    alone does not: each publication resolved to a real citation, the chapters
    the trial is assigned to resolved to titles, and the chapters that actually
    cite it, read out of the prose."""
    cites = {}
    cdir = os.path.join(DIR, "chapters")
    for f in sorted(os.listdir(cdir)) if os.path.isdir(cdir) else []:
        if f.endswith(".md"):
            for k in re.findall(r"\{\{trial:([A-Za-z0-9_\-]+)\}\}",
                                library.read(os.path.join(cdir, f))):
                cites.setdefault(k, []).append(f[:-3])

    def chapref(cid):
        return {"id": cid, "num": m.chapnum.get(cid), "title": m.title.get(cid)}

    rows = []
    for key in sorted(m.trials):
        t = m.trials[key]
        pubs = []
        for p in t.get("pubs") or []:
            r = m.refs.get(p.get("ref")) or {}
            pubs.append({k: v for k, v in {
                "role": p.get("role"), "kind": p.get("kind"), "ref": p.get("ref"),
                "year": r.get("year"), "journal": r.get("journal"),
                "authors": r.get("authors"), "title": r.get("title"),
                "pmid": r.get("pmid"), "doi": r.get("doi"),
                "added": str(p["added"]) if p.get("added") else None,
            }.items() if v})
        pubs.sort(key=lambda x: (x.get("year") or 0))
        seen = sorted({c for c in cites.get(key, [])})
        row = {k: v for k, v in {
            "key": key, "acronym": t.get("acronym") or key,
            "phase": t.get("phase"), "n": t.get("n"), "year": t.get("year"),
            "setting": t.get("setting"), "subtype": t.get("subtype"),
            "line": t.get("line"), "modality": t.get("modality"),
            "status": t.get("status"), "weight": t.get("weight"),
            "topic": t.get("topic"),
            "population": t.get("population"), "arms": t.get("arms"),
            "endpoint": t.get("endpoint"), "result": t.get("result"),
            "os": t.get("os"), "nct": t.get("nct"),
            "note": t.get("note"),
            "reviewed": str(t["reviewed"]) if t.get("reviewed") else None,
            "tabulated": False if t.get("tabulated") is False else True,
            "result_state": evidence.result_state(t),
            "pubs": pubs,
            "chapters": [chapref(c) for c in (t.get("chapters") or [])
                         if c in m.chapnum],
            "cited_by": [chapref(c) for c in seen if c in m.chapnum],
        }.items() if v not in (None, "", [], {})}
        rows.append(row)

    parts = [{"label": "Part %s · %s" % (ROMAN[i], p["title"]),
              "chapters": [c["id"] for c in p["chapters"]]}
             for i, p in enumerate(m.outline["parts"])]
    return json.dumps({"trials": rows, "parts": parts},
                      ensure_ascii=False, separators=(",", ":")) + "\n"


def digestdata(m):
    """books/breast-cancer/src/data/digests.json -- the abstract extracts.

    Methods and results for each trial, taken from the abstract of the paper the
    registry quotes. Separate from trials.json because the appendix needs the
    table to draw and needs a digest only when a reader opens one card, and
    because this file grows with every trial while the table row does not."""
    out = {k: t["digest"] for k, t in sorted(m.trials.items()) if t.get("digest")}
    return json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n"


def storydata(m):
    """books/breast-cancer/src/data/stories.json -- what the Chapter Stories page reads.

    The whole argument layer in one file: every position in the landscape, every
    clinical question under it, the five moves, and each trial resolved far
    enough that the page can draw a chip and link it into the registry without
    loading the registry itself."""
    reg = m.trials
    out = []
    for sid, st in _st.ordered(m.stories):
        qs = []
        for q in st.get("questions") or []:
            ts = []
            for k in q.get("trials") or []:
                t = reg.get(k) or {}
                ts.append({"key": k, "acronym": t.get("acronym") or k,
                           "year": t.get("year"), "phase": t.get("phase"),
                           "status": t.get("status")})
            qs.append({"id": q["id"], "ask": q["ask"],
                       **{mv: q[mv] for mv in _st.MOVES}, "trials": ts})
        out.append({"id": sid, "setting": st["setting"],
                    "setting_label": _st.SETTING_LABEL[st["setting"]],
                    "subtype": st["subtype"], "stage": st["stage"],
                    "title": st["title"], "premise": st.get("premise") or "",
                    "chapters": [{"id": c, "num": m.chapnum.get(c),
                                  "title": m.title.get(c),
                                  "href": m.href(c)}
                                 for c in (st.get("chapters") or [])
                                 if c in m.chapnum],
                    "questions": qs})
    return json.dumps({"stories": out}, ensure_ascii=False,
                      separators=(",", ":")) + "\n"


# curriculum.json and the three src/data files: generate()'s outputs that are not
# chapter fragments, so a count of fragments discounts them.
NON_CHAPTER = 4


def generate(m):
    """Everything this tool owns, as {path: bytes-to-be}. Nothing is written
    here, so --check and the real run cannot disagree about the result."""
    out = {os.path.join(DIR, "curriculum.json"): curriculum(m),
           os.path.join(DIR, "src", "data", "trials.json"): trialdata(m),
           os.path.join(DIR, "src", "data", "digests.json"): digestdata(m),
           os.path.join(DIR, "src", "data", "stories.json"): storydata(m)}
    errs = []
    cdir = os.path.join(DIR, "chapters")
    for f in sorted(os.listdir(cdir)) if os.path.isdir(cdir) else []:
        if not f.endswith(".md"):
            continue
        cid = f[:-3]
        if cid not in m.chapnum:
            errs.append("chapters/%s is not a chapter in outline.yaml" % f)
            continue
        ch = Chapter(m, cid)
        out[os.path.join(DIR, "src", cid + ".html")] = ch.render(
            library.read(os.path.join(cdir, f)))
        errs += ch.errs
    return out, errs


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if anything on disk is out of date")
    ap.add_argument("--mint", action="store_true",
                    help="give a permanent id to any section written as a bare string")
    ap.add_argument("--dry-run", action="store_true",
                    help="with --mint, report what would be minted and write nothing")
    args = ap.parse_args()

    if args.mint:
        # Minting rewrites the outline, so it runs before the model is built and
        # the regeneration below then sees the ids it just handed out.
        mint(dry=args.dry_run)
        if args.dry_run:
            return

    m = Model()
    out, errs = generate(m)
    if errs:
        for e in errs:
            print("  error  " + e)
        sys.exit("%d problem%s. Nothing written." % (len(errs), "s" * (len(errs) != 1)))

    stale = [p for p, text in out.items()
             if not os.path.exists(p) or library.read(p) != text]
    # A fragment whose chapter was deleted or renamed is stale in the other
    # direction, and would otherwise sit in src/ being built forever.
    srcdir = os.path.join(DIR, "src")
    orphans = [os.path.join(srcdir, f) for f in sorted(os.listdir(srcdir))
               if f.startswith("BC-") and os.path.join(srcdir, f) not in out]

    if args.check:
        for p in stale + orphans:
            print("  stale  " + os.path.relpath(p, library.ROOT))
        if stale or orphans:
            sys.exit("out of date. Run: python3 tools/bc.py")
        nfrag = len(out) - NON_CHAPTER
        print("bc: curriculum.json, the two data files and %d fragment%s are current"
              % (nfrag, "s" * (nfrag != 1)))
        return

    for p in orphans:
        os.remove(p)
    for p, text in sorted(out.items()):
        library.write(p, text)
    print("bc: %d parts, %d chapters, %d sections, %d drafted"
          % (len(m.outline["parts"]), len(m.chapnum),
             len(m.owner), len(out) - NON_CHAPTER))
    for p in stale:
        print("  wrote  " + os.path.relpath(p, library.ROOT))
    for p in orphans:
        print("  removed " + os.path.relpath(p, library.ROOT))


if __name__ == "__main__":
    main()
