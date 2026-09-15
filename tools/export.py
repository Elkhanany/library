#!/usr/bin/env python3
"""
export.py — the trial registry as a spreadsheet, for reading away from the book.

The registry changes as trials report, and the chapters have to be brought back
into line when they do. That is work done with the evidence in front of you,
often not at a terminal, so this writes the whole of it into one workbook:

    python3 tools/export.py            write books/breast-cancer/src/data/*.xlsx
    python3 tools/export.py --check    fail if the workbook is out of date

Six sheets, and the order is the order you would use them in:

    About            what this is, when the registry was last reviewed, and the
                     rules that govern an edit to the text
    Chapter Stories  one row per clinical question, with its five moves and the
                     trials that carry it. This is the sheet to edit a chapter
                     from, because it says what each group of trials is for.
    Trials           one row per trial, every field the registry holds
    Publications     one row per paper, so a new readout is easy to spot
    Chapters         one row per chapter-and-trial pair, with whether the chapter
                     is meant to discuss it and whether it actually does. This is
                     the worklist: filter it to assigned yes, cited no.
    Evidence tables  every generated table in the book, its filter, and what it
                     currently renders. Read this before writing a number into
                     prose, because a number the table already carries must not
                     be restated.

The workbook is deterministic. It is dated by the registry's own latest review
rather than by the clock, so two exports of the same data are the same bytes and
`--check` means something.
"""
import io
import os
import re
import sys
import json
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library
import evidence
import stories as story
import xlsx

try:
    import yaml
except ImportError:
    sys.exit("export.py needs pyyaml")

BOOK = os.path.join(library.ROOT, "books", "breast-cancer")
OUT = os.path.join(BOOK, "src", "data", "breast-cancer-trials.xlsx")

RULES = [
    "Tables enumerate, prose argues. Never restate in prose a number the table already "
    "carries, unless you are arguing from it and the comparison is the point.",
    "A chapter may not cite an unverified reference. An entry marked verify: true has had "
    "its identifier claimed but not checked, and the build fails on any chapter citing one.",
    "Never rename a reference key or a trial key. Add an alias instead, so links written "
    "against the old spelling keep resolving.",
    "Identifiers are permanent and carry no position. A chapter keeps its BC-### when it "
    "moves, and chapter and section numbers are computed at build time.",
    "Trial results are not written into prose at all. They are entered once in trials.yaml "
    "and appear in every chapter whose evidence filter matches.",
]


def chapters():
    """Display number and title for every chapter, and the part it sits in."""
    cur = json.load(io.open(os.path.join(BOOK, "curriculum.json"), encoding="utf-8"))
    out = {}
    for p in cur:
        for c in p["chapters"]:
            out[c["slug"]] = {"num": c["num"], "title": c["title"], "part": p["label"]}
    return out


def sections():
    o = yaml.safe_load(io.open(os.path.join(BOOK, "outline.yaml"), encoding="utf-8"))
    out = {}
    for p in o["parts"]:
        for c in p.get("chapters") or []:
            for s in c.get("sections") or []:
                if isinstance(s, dict):
                    out[s["id"]] = s.get("title", "")
    return out


def blocks_with_section():
    """Every evidence block, with the section heading standing over it."""
    d = os.path.join(BOOK, "chapters")
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        text = io.open(os.path.join(d, fn), encoding="utf-8").read()
        sec = ""
        for chunk in re.split(r"(?m)^(## BS-\d+.*)$", text):
            m = re.match(r"## (BS-\d+)", chunk)
            if m:
                sec = m.group(1)
                continue
            for spec, _body in evidence.blocks_in_text(chunk):
                yield fn[:-3], sec, spec


def joined(vals, sep="; "):
    return sep.join(str(v) for v in vals if v not in (None, ""))


def build():
    trials = yaml.safe_load(io.open(os.path.join(BOOK, "trials.yaml"), encoding="utf-8"))["trials"]
    refs = yaml.safe_load(io.open(os.path.join(BOOK, "references.yaml"), encoding="utf-8"))["refs"]
    chap, secs = chapters(), sections()
    cites = evidence.cited_in(trials)

    def chref(cid):
        c = chap.get(cid)
        return "%s %s" % (c["num"], c["title"]) if c else cid

    def where(t):
        out = []
        for s in t.get("source") or []:
            bits = [s.get("section")]
            if s.get("ch"):
                bits.append("Ch. %d" % s["ch"])
            bits.append(s.get("group"))
            out.append(" / ".join(b for b in bits if b) + (" [cross-ref]" if s.get("xref") else ""))
        return joined(out)

    # ------------------------------------------------------- Chapter Stories
    # The argument layer, flattened one row per question. A chapter is edited
    # from this sheet and its numbers come from the Trials sheet, which is the
    # same division of labour the book itself uses.
    st = story.load()
    shead = ["Story", "Setting", "Subtype", "When", "Story title", "Premise",
             "Question id", "Clinical question", "Rationale", "Experiment", "Finding",
             "Limitation", "Next question", "Trials", "Trial keys", "Chapters"]
    srows = []
    for sid, s_ in story.ordered(st):
        for q in s_.get("questions") or []:
            keys = q.get("trials") or []
            srows.append([
                sid, s_["setting"], s_["subtype"], s_["stage"], s_["title"],
                s_.get("premise") or "", q["id"], q["ask"],
                q["rationale"], q["experiment"], q["finding"], q["limitation"], q["next"],
                joined([(trials.get(k) or {}).get("acronym") or k for k in keys], ", "),
                joined(keys, ", "),
                joined([chref(c) for c in (s_.get("chapters") or [])]),
            ])

    # ---------------------------------------------------------------- Trials
    thead = ["Key", "Trial", "Phase", "N", "Setting", "Subtype", "Line", "Modality",
             "Status", "Evidence weight", "Year", "Topic", "Population", "Experimental vs control",
             "Primary endpoint", "Result", "Overall survival", "Read with care",
             "Methods", "Results", "Result taken from", "PMID", "Papers", "NCT",
             "Result state", "Last reviewed", "Chapters it is assigned to",
             "Chapters that cite it", "Listed in the source document under"]
    trows = []
    for k in sorted(trials):
        t = trials[k]
        d = t.get("digest") or {}
        pr = t.get("primary_ref")
        trows.append([
            k, t.get("acronym") or k, t.get("phase"), t.get("n"), t.get("setting"),
            t.get("subtype"), t.get("line"), t.get("modality"), t.get("status"),
            t.get("weight"), t.get("year"), t.get("topic"), t.get("population"), t.get("arms"),
            t.get("endpoint"), t.get("result"), t.get("os"), t.get("note"),
            d.get("methods"), d.get("results"), pr,
            (refs.get(pr) or {}).get("pmid") if pr else None,
            len(t.get("pubs") or []) or None, t.get("nct"),
            evidence.result_state(t),
            str(t["reviewed"]) if t.get("reviewed") else None,
            joined([chref(c) for c in (t.get("chapters") or [])]),
            joined([chref(c) for c in sorted(cites.get(k) or ())]),
            where(t)])

    # ---------------------------------------------------------- Publications
    phead = ["Trial key", "Trial", "Role", "Kind", "Reference", "Year", "Journal",
             "Authors", "Title", "PMID", "DOI", "Added", "Is the tabulated result"]
    prows = []
    for k in sorted(trials):
        t = trials[k]
        for p in t.get("pubs") or []:
            r = refs.get(p.get("ref")) or {}
            prows.append([k, t.get("acronym") or k, p.get("role"), p.get("kind"),
                          p.get("ref"), r.get("year"), r.get("journal"), r.get("authors"),
                          r.get("title"), r.get("pmid"), r.get("doi"),
                          str(p["added"]) if p.get("added") else None,
                          "yes" if p.get("ref") == t.get("primary_ref") else ""])

    # -------------------------------------------------------------- Chapters
    # Which trials each generated table in a chapter actually renders, so the
    # worklist can say whether a trial is already tabulated where it belongs.
    tabled = {}
    for cid, _sec, spec in blocks_with_section():
        f, bad = evidence.parse_filter(spec)
        if bad:
            continue
        for hit in evidence.select(trials, f):
            tabled.setdefault(cid, set()).add(hit["key"])

    chead = ["Part", "Chapter", "Chapter id", "Chapter title", "Trial key", "Trial",
             "Assigned here", "Cited in the prose", "In a table here", "To do",
             "Status", "Result state", "Result"]
    crows = []
    for k in sorted(trials):
        t = trials[k]
        assigned = set(t.get("chapters") or ())
        cited = set(cites.get(k) or ())
        for cid in sorted(assigned | cited, key=lambda c: float(chap[c]["num"])
                          if c in chap and str(chap[c]["num"]).isdigit() else 999):
            c = chap.get(cid)
            a, ct = cid in assigned, cid in cited
            intable = k in (tabled.get(cid) or ())
            # Only what someone has to do goes in this column. A trial the
            # chapter discusses owes nothing, whether or not the source document
            # thought to file it there, so those rows are left blank and the
            # Assigned and Cited columns carry the fact instead.
            if a and not ct:
                todo = "tabulated, not discussed" if intable else "write it in"
            elif ct and not a and assigned:
                todo = "assign it here"
            else:
                todo = ""
            crows.append([c["part"] if c else "", c["num"] if c else "", cid,
                          c["title"] if c else "", k, t.get("acronym") or k,
                          "yes" if a else "", "yes" if ct else "",
                          "yes" if intable else "", todo, t.get("status"),
                          evidence.result_state(t), t.get("result")])

    # ------------------------------------------------------- Evidence tables
    ehead = ["Chapter", "Chapter id", "Chapter title", "Section", "Section title",
             "Filter", "Rows", "Trials in the table"]
    erows = []
    for cid, sec, spec in blocks_with_section():
        f, bad = evidence.parse_filter(spec)
        hits = [] if bad else evidence.select(trials, f)
        c = chap.get(cid)
        shown = re.sub(r"\s*(caption|cols|sort)=\S+", "", spec).strip()
        erows.append([c["num"] if c else "", cid, c["title"] if c else "", sec,
                      secs.get(sec, ""), shown, len(hits),
                      joined([(h.get("acronym") or h["key"]) for h in hits], ", ")])

    # ----------------------------------------------------------------- About
    reviewed = sorted(str(t["reviewed"]) for t in trials.values() if t.get("reviewed"))
    state = {s: sum(1 for t in trials.values() if evidence.result_state(t) == s)
             for s in evidence.RESULT_STATES}
    uncited = sum(1 for k in trials if not cites.get(k))
    ahead = ["Breast Cancer, the trial registry", "A snapshot of the evidence the book stands on"]
    arows = [
        ["Registry last reviewed", reviewed[-1] if reviewed else "never"],
        ["Trials", len(trials)],
        ["Publications", len(prows)],
        ["Trials with a tabulated result", state["tabulated"]],
        ["Trials whose findings are extracted but not tabulated", state["extracted"]],
        ["Trials with no result on the record", state["none"]],
        ["Trials no chapter cites", uncited],
        ["Generated tables in the book", len(erows)],
        ["Chapter Stories", len(st)],
        ["Clinical questions", len(srows)],
        ["", ""],
        ["Source", "books/breast-cancer/trials.yaml"],
        ["Regenerate", "python3 tools/export.py"],
        ["", ""],
        ["The sheets", ""],
        ["Chapter Stories", "One row per clinical question. The hierarchy is setting, subtype "
                            "and when in the course; the deepest level is always a question, and "
                            "each is written in five moves. A story carries no figures, because "
                            "the figures are the registry's job and are two sheets to the right."],
        ["Trials", "One row per trial, every field the registry holds. Methods and Results "
                   "are the paper's own account, with its background and conclusion left out."],
        ["Evidence weight", "practice-defining, supporting or exploratory. A table in the "
                            "book enumerates the record a decision rests on, so an exploratory "
                            "trial is held back from it unless the table asks for one by name. "
                            "It is still in the registry, in the appendix and in the Chapter "
                            "Stories, which is where a proof of concept earns its place."],
        ["Result state", "tabulated means the Result field is filled and the evidence tables "
                         "print it. extracted means the paper's findings are on the record but "
                         "nobody has written the one-line result yet. none means nothing on the "
                         "record says what the trial showed, which for an ongoing trial is the "
                         "truth and for a reported one is a gap."],
        ["Publications", "One row per paper. Sort by Year to find what has reported recently."],
        ["Chapters", "One row per chapter-and-trial pair. Filter to Assigned here = yes and "
                     "Cited in the prose = blank for the chapters that owe a trial a mention."],
        ["Evidence tables", "Every generated table, its filter and what it renders today."],
        ["", ""],
        ["Rules that govern an edit", ""],
    ] + [["", r] for r in RULES]

    W = xlsx.Sheet
    return [
        W("About", ahead, arows, widths=[34, 104], wrap=[1], freeze=False,
          autofilter=False),
        W("Chapter Stories", shead, srows,
          widths=[9, 12, 12, 17, 40, 56, 11, 46, 56, 56, 52, 56, 52, 40, 34, 30],
          wrap=["Story title", "Premise", "Clinical question", "Rationale", "Experiment",
                "Finding", "Limitation", "Next question", "Trials", "Trial keys",
                "Chapters"]),
        W("Trials", thead, trows,
          widths=[18, 22, 6, 8, 12, 16, 15, 18, 10, 17, 7, 34, 44, 44, 26, 52, 40, 40, 56,
                  56, 18, 11, 8, 13, 12, 13, 30, 30, 44],
          wrap=["Topic", "Population", "Experimental vs control", "Primary endpoint",
                "Result", "Overall survival", "Read with care", "Methods", "Results",
                "Chapters it is assigned to", "Chapters that cite it",
                "Listed in the source document under"]),
        W("Publications", phead, prows,
          widths=[18, 22, 24, 12, 22, 7, 26, 30, 70, 11, 30, 11, 12],
          wrap=["Title", "Authors", "Role"]),
        W("Chapters", chead, crows,
          widths=[26, 8, 10, 38, 18, 22, 13, 17, 14, 24, 10, 12, 52],
          wrap=["Chapter title", "Result", "To do"]),
        W("Evidence tables", ehead, erows,
          widths=[8, 10, 38, 10, 40, 56, 6, 80],
          wrap=["Chapter title", "Section title", "Filter", "Trials in the table"]),
    ]


def main_check():
    """The staleness check, callable from another tool. sitecheck runs it, so a
    workbook that no longer matches the registry is caught by the same sweep
    that catches a broken link."""
    old = io.open(OUT, "rb").read() if os.path.exists(OUT) else b""
    if old != xlsx.write(None, build()):
        print("  STALE DATASET  %s — run python3 tools/export.py"
              % os.path.relpath(OUT, library.ROOT))
        return 1
    print("export: the downloadable trial workbook matches the registry")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="fail if the workbook on disk is not what the registry would produce")
    a = ap.parse_args()

    if a.check:
        return main_check()

    sheets = build()
    data = xlsx.write(None, sheets)
    d = os.path.dirname(OUT)
    if not os.path.isdir(d):
        os.makedirs(d)
    io.open(OUT, "wb").write(data)
    print("export: %s (%.0f KB)" % (os.path.relpath(OUT, library.ROOT), len(data) / 1024))
    for s in sheets:
        print("   %-16s %d rows" % (s.name, len(s.rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
