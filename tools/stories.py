#!/usr/bin/env python3
"""
stories.py — the Chapter Stories layer: the argument the trials are evidence for.

The registry answers "what did this trial show". The evidence tables answer
"what else is in this cell". Neither answers the question a chapter actually
opens with, which is "what were we trying to find out, and did we find it out".

A story is that missing layer. It sits at one position in the treatment
landscape, deliberately high up — early or advanced disease, then subtype, then
when in the course — and under that position it holds an ordered list of
CLINICAL QUESTIONS. The question is the deepest level of the hierarchy, not the
drug class, because the drug class does not determine the question: PALOMA-3,
SERENA-4, PADA-1 and SONIA all carry `cdk4-6,endocrine` and ask add, substitute,
select and sequence respectively.

Each question is written in five moves, always in this order:

    rationale    why the idea was worth testing
    experiment   what was actually done to test it
    finding      what came back
    limitation   what the design cannot tell you
    next         the question the finding leaves open

and it names the trials that carry it. A trial may appear under several
questions; that is the point. Nothing here duplicates a trial record, and no
number is repeated from one — a story cites trials by key and the chapter's
evidence table prints the figures.

Data
    books/breast-cancer/stories.yaml

Ids
    ST-###   a story (one position in the landscape)
    SQ-####  a question inside one. Permanent, globally minted, never reordered
             into a different number.

In a chapter
    ```story ST-010
    ```                        the whole story
    ```story SQ-0010,SQ-0020
    ```                        just those questions, in the order written

Usage
    python3 tools/stories.py --check       validate the whole layer
    python3 tools/stories.py --tree        print the hierarchy
    python3 tools/stories.py --orphans     registry trials no question names
    python3 tools/stories.py --axes        questions whose trials disagree with
                                           the position they are filed under
    python3 tools/stories.py --coverage    per-story counts
"""
import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:                                       # pragma: no cover
    sys.exit("stories.py needs pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "books", "breast-cancer")

# The top level is the one the reader already has in their head when they open a
# chapter: is this curable-intent disease or not. `cns` is third because a brain
# metastasis trial answers a question neither of the other two asks.
SETTINGS = ["early", "metastatic", "cns"]
SETTING_LABEL = {"early": "Early disease", "metastatic": "Advanced disease",
                 "cns": "Central nervous system disease"}
SUBTYPES = ["HR+/HER2-", "HER2+", "HR+/HER2+", "TNBC", "BRCA", "all"]

# Where in the course. Kept short on purpose: the user-facing hierarchy is
# meant to stay shallow, and the finer distinctions live in the question.
STAGES = {
    "early": ["neoadjuvant", "adjuvant", "post-neoadjuvant"],
    "metastatic": ["1L", "later", "any"],
    "cns": ["any"],
}
# For --axes: what a story's stage permits a trial's `line` to be.
STAGE_LINES = {
    "neoadjuvant": {"neoadjuvant"},
    "adjuvant": {"adjuvant", "any"},
    "post-neoadjuvant": {"post-neoadjuvant", "adjuvant"},
    "1L": {"1L", "any"},
    "later": {"2L", "3L+", "any"},
    "any": None,
}

MOVES = ["rationale", "experiment", "finding", "limitation", "next"]
MOVE_LABEL = {"rationale": "Rationale", "experiment": "Experiment",
              "finding": "Finding", "limitation": "Limitation",
              "next": "Next question"}

ST_ID = re.compile(r"^ST-\d{3}$")
SQ_ID = re.compile(r"^SQ-\d{4}$")


def load(path=None):
    doc = yaml.safe_load(open(path or os.path.join(BOOK, "stories.yaml"),
                              encoding="utf-8"))
    return doc.get("stories") or {}


def trials():
    return yaml.safe_load(open(os.path.join(BOOK, "trials.yaml"),
                               encoding="utf-8")).get("trials") or {}


def ordered(stories):
    """Stories in reading order: setting, then subtype, then stage — the same
    order the hierarchy is drawn in, so no file position is load-bearing."""
    def k(item):
        sid, s = item
        return (SETTINGS.index(s["setting"]) if s["setting"] in SETTINGS else 99,
                SUBTYPES.index(s["subtype"]) if s["subtype"] in SUBTYPES else 99,
                (STAGES.get(s["setting"]) or []).index(s["stage"])
                if s["stage"] in (STAGES.get(s["setting"]) or []) else 99,
                sid)
    return sorted(stories.items(), key=k)


def questions(stories):
    for sid, s in ordered(stories):
        for q in s.get("questions") or []:
            yield sid, s, q


def find(stories, ident):
    """An ST id, or an SQ id, to (story id, story, [questions])."""
    if ident in stories:
        return ident, stories[ident], list(stories[ident].get("questions") or [])
    for sid, s, q in questions(stories):
        if q.get("id") == ident:
            return sid, s, [q]
    return None, None, []


# ----------------------------------------------------------------- validation

def check(stories, reg):
    errs, warns = [], []
    seen_q = {}
    for sid, s in sorted(stories.items()):
        where = sid
        if not ST_ID.match(sid):
            errs.append("%s: a story id is ST-### " % sid)
        for f in ("setting", "subtype", "stage", "title", "chapters", "questions"):
            if not s.get(f):
                errs.append("%s: no %s" % (where, f))
        if s.get("setting") not in SETTINGS:
            errs.append("%s: setting %r is not one of %s" % (where, s.get("setting"), SETTINGS))
        elif s.get("stage") not in STAGES[s["setting"]]:
            errs.append("%s: stage %r is not one of %s for setting %s"
                        % (where, s.get("stage"), STAGES[s["setting"]], s["setting"]))
        if s.get("subtype") not in SUBTYPES:
            errs.append("%s: subtype %r is not one of %s" % (where, s.get("subtype"), SUBTYPES))
        for q in s.get("questions") or []:
            qid = q.get("id")
            if not qid or not SQ_ID.match(str(qid)):
                errs.append("%s: a question id is SQ-#### , not %r" % (where, qid))
                continue
            if qid in seen_q:
                errs.append("%s: %s is already used in %s" % (where, qid, seen_q[qid]))
            seen_q[qid] = sid
            if not str(q.get("ask") or "").strip().endswith("?"):
                errs.append("%s %s: `ask` is the clinical question and ends in a "
                            "question mark: %r" % (where, qid, q.get("ask")))
            for mv in MOVES:
                if not str(q.get(mv) or "").strip():
                    errs.append("%s %s: no %s" % (where, qid, mv))
            ts = q.get("trials") or []
            if not ts:
                errs.append("%s %s: names no trial" % (where, qid))
            for t in ts:
                if t not in reg:
                    errs.append("%s %s: trial %r is not in the registry" % (where, qid, t))
    return errs, warns


def axes(stories, reg):
    """Where a question's trials disagree with the position it is filed under.

    A disagreement is not automatically wrong — a lobular window study belongs
    in an adjuvant argument, and a story about what to do after CDK4/6
    progression legitimately cites the first-line trial that created the
    situation. It is reported so that the choice is deliberate."""
    rows = []
    for sid, s, q in questions(stories):
        for k in q.get("trials") or []:
            t = reg.get(k)
            if not t:
                continue
            why = []
            if s["setting"] == "cns":
                if t.get("setting") != "cns":
                    why.append("setting %s" % t.get("setting"))
            elif t.get("setting") not in (s["setting"], "any"):
                why.append("setting %s" % t.get("setting"))
            have = {x.strip() for x in str(t.get("subtype") or "").split(",")}
            if s["subtype"] != "all" and "all" not in have and s["subtype"] not in have:
                why.append("subtype %s" % t.get("subtype"))
            want = STAGE_LINES.get(s["stage"])
            if want is not None and str(t.get("line") or "") not in want:
                why.append("line %s" % t.get("line"))
            if why:
                rows.append((sid, q["id"], k, s["setting"], s["subtype"], s["stage"],
                             "; ".join(why)))
    return rows


def orphans(stories, reg):
    named = {k for _, _, q in questions(stories) for k in (q.get("trials") or [])}
    return sorted(set(reg) - named)


# ------------------------------------------------------------------ rendering

def to_markdown(story, qs):
    """A story as plain markdown. bc.py renders its own HTML from the same
    structure; this is what --tree and any non-HTML consumer reads."""
    out = ["### %s" % story["title"]]
    if story.get("premise"):
        out += ["", story["premise"]]
    for q in qs:
        out += ["", "**%s**" % q["ask"]]
        for mv in MOVES:
            out.append("- _%s._ %s" % (MOVE_LABEL[mv], q[mv]))
        out.append("- _Trials._ " + ", ".join("{{trial:%s}}" % t for t in q["trials"]))
    return "\n".join(out)


# ----------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--tree", action="store_true")
    ap.add_argument("--axes", action="store_true")
    ap.add_argument("--orphans", action="store_true")
    ap.add_argument("--coverage", action="store_true")
    ap.add_argument("--render", metavar="ID", help="one ST- or SQ- id as markdown")
    a = ap.parse_args()
    stories, reg = load(), trials()

    if a.render:
        sid, s, qs = find(stories, a.render)
        if not s:
            sys.exit("no story or question %s" % a.render)
        print(to_markdown(s, qs))
        return

    if a.tree:
        last = None
        for sid, s in ordered(stories):
            head = (s["setting"], s["subtype"])
            if head != last:
                print("\n%s · %s" % (SETTING_LABEL[s["setting"]], s["subtype"]))
                last = head
            print("  %s  %s  [%s]" % (sid, s["stage"], s["title"]))
            for q in s.get("questions") or []:
                print("      %s  %s" % (q["id"], q["ask"]))
                print("             %s" % ", ".join(q.get("trials") or []))
        return

    if a.axes:
        rows = axes(stories, reg)
        for r in rows:
            print("  %s %s  %-22s filed under %s/%s/%s but the trial is %s"
                  % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
        print("stories: %d trial placement%s worth a second look"
              % (len(rows), "s" * (len(rows) != 1)))
        return

    if a.orphans:
        o = orphans(stories, reg)
        for k in o:
            print("  %-26s %s" % (k, (reg[k].get("topic") or "")[:70]))
        print("stories: %d of %d registry trials are in no question"
              % (len(o), len(reg)))
        return

    if a.coverage:
        nq = nt = 0
        for sid, s in ordered(stories):
            qs = s.get("questions") or []
            ts = {k for q in qs for k in (q.get("trials") or [])}
            nq += len(qs)
            nt += len(ts)
            print("  %s  %-11s %-10s %-16s %2d questions %3d trials"
                  % (sid, s["setting"], s["subtype"], s["stage"], len(qs), len(ts)))
        print("stories: %d stories, %d questions, %d trial slots"
              % (len(stories), nq, nt))
        return

    errs, warns = check(stories, reg)
    for w in warns:
        print("  warn   " + w)
    for e in errs:
        print("  error  " + e)
    if errs:
        sys.exit("%d problem%s." % (len(errs), "s" * (len(errs) != 1)))
    nq = sum(len(s.get("questions") or []) for s in stories.values())
    named = {k for _, _, q in questions(stories) for k in (q.get("trials") or [])}
    print("stories: %d stories, %d questions, %d of %d registry trials named, 0 problems"
          % (len(stories), nq, len(named), len(reg)))


if __name__ == "__main__":
    main()
