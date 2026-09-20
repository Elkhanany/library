#!/usr/bin/env python3
"""The three layers agree about which trials the book argues from.

A trial reaches a reader by three separate routes, and each is validated by a
different tool. evidence.py proves the filter on a table is well formed.
stories.py proves a question is written in five moves and names real trials.
bc.py proves a chapter's macros resolve. None of them asks the question that
matters to a reader, which is whether the three routes are telling the same
story about the same trial.

This is that check. It is a reconciliation rather than a validation: almost
nothing it reports is automatically wrong, and the point is that every gap it
finds is either fixed or declared.

    orphans      a registry trial no question names, grouped into families and
                 set against the families stories.yaml declares out of scope
    silent       a trial that reaches the reader by no route at all
    unstoried    a chapter that carries evidence and no story
    spanning     a story whose chapters have been split across parts
    stray        a question rendered in a chapter its own story does not list
    untold       a trial a chapter tabulates that nothing in the book discusses
    stale        a question last read before a trial it names was last read
    contradicted a question saying, in the present tense, that something is not
                 yet known, where the registry holds it

The out-of-scope declaration is the load-bearing part. A library that reports
ninety orphans every run trains its reader to ignore the report. Declaring that
the radiotherapy and DCIS trials are deliberately outside the story layer turns
a standing number into a decision somebody made, with a reason attached, and
leaves the report empty until a NEW gap appears.

A question is the one place in the book that makes a claim about what is NOT
known, and the registry moves under it. "Overall survival is immature" was true
when it was written and is a false sentence the day the trial reports. Two
checks cover that. The date is mechanical and catches drift of any kind. The
wording check is narrow and catches this class directly, including in a question
whose trials were never re-reviewed.

Tense is what separates a defect from a fact. "Overall survival WAS immature at
the primary analysis" is a statement about that analysis and stays true forever.
"Overall survival IS immature" is a claim about now.

    python3 tools/synthcheck.py                 the whole reconciliation
    python3 tools/synthcheck.py --stale         questions the registry has moved under
    python3 tools/synthcheck.py --orphans       just the unstoried trials
    python3 tools/synthcheck.py --families      how every orphan is classified
    python3 tools/synthcheck.py --quiet         errors only, for a build
"""
import argparse, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import evidence as ev
import stories as st

try:
    import yaml
except ImportError:                                       # pragma: no cover
    sys.exit("synthcheck.py needs pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "books", "breast-cancer")
CH = os.path.join(BOOK, "chapters")

EVIDENCE = re.compile(r"^```evidence([^\n]*)$", re.M)
STORY = re.compile(r"^```story ([^\n]+)$", re.M)
TRIAL = re.compile(r"\{\{trial:([a-z0-9][a-z0-9\-.]*)\}\}")


# ---------------------------------------------------------------- the families
#
# A family is what a reader would call the trial, not what the registry calls
# it. The registry axes are chosen to drive tables, so `setting` separates
# `dcis` from `early` but puts a sentinel node trial and an adjuvant CDK4/6
# trial in the same bucket. Modality separates those two, and neither axis
# alone sorts the orphans the way a person would.
def family(t):
    setting = t.get("setting")
    mods = {m.strip() for m in str(t.get("modality") or "").split(",")}
    if setting == "dcis":
        return "dcis"
    if setting == "prevention":
        return "prevention"
    if setting == "screening":
        return "screening"
    if setting in ("mrd", "surveillance"):
        return "mrd"
    if setting == "cns":
        return "cns"
    if setting == "recurrence":
        return "local-recurrence"
    if mods & {"surgery"}:
        return "surgery"
    if mods & {"radiation"}:
        return "radiotherapy"
    if mods & {"bone", "supportive"}:
        return "supportive"
    if mods & {"endocrine"}:
        return "endocrine"
    if mods & {"chemo"}:
        return "chemotherapy"
    return "other"


def scope(doc):
    """The families stories.yaml declares out of scope, and why.

    Read from the data rather than hard-coded here, because it is an editorial
    decision about this book and not a property of the tool."""
    out = {}
    for row in (doc.get("_scope") or {}).get("out", []) or []:
        out[row["family"]] = row.get("because", "")
    return out


# ----------------------------------------------------------------- the reading
def spine():
    """Chapter to part, and the part titles, in reading order."""
    doc = yaml.safe_load(open(os.path.join(BOOK, "outline.yaml"), encoding="utf-8"))
    part_of, title, order = {}, {}, []
    for i, p in enumerate(doc["parts"], 1):
        title[p["id"]] = (i, p["title"])
        for c in p.get("chapters", []):
            part_of[c["id"]] = p["id"]
            order.append(c["id"])
    return part_of, title, order


def chapters(reg):
    """Per chapter: the trials its tables render, the trials its prose names,
    and the question ids its story blocks place."""
    tabled, prosed, placed = {}, {}, {}
    for fn in sorted(os.listdir(CH)):
        if not fn.endswith(".md"):
            continue
        cid, text = fn[:-3], open(os.path.join(CH, fn), encoding="utf-8").read()
        hits = set()
        for spec in EVIDENCE.findall(text):
            f, bad = ev.parse_filter(spec.strip())
            if bad:                       # evidence.py --check owns that error
                continue
            hits |= {t["key"] for t in ev.select(reg, f)}
        tabled[cid] = hits
        prosed[cid] = set(TRIAL.findall(text))
        placed[cid] = {q.strip() for spec in STORY.findall(text)
                       for q in spec.split(",") if q.strip()}
    return tabled, prosed, placed


# ------------------------------------------------------------------ the checks
def reconcile(reg, sto, doc):
    part_of, ptitle, order = spine()
    tabled, prosed, placed = chapters(reg)
    declared = scope(doc)

    named = {k for _, _, q in st.questions(sto) for k in (q.get("trials") or [])}
    home = {q["id"]: sid for sid, _s, q in st.questions(sto)}

    rep = {"declared": declared, "part_of": part_of, "ptitle": ptitle}

    # orphans, split by whether the family is declared out of scope
    rep["orphans"] = sorted(set(reg) - named)
    rep["fam"] = {k: family(reg[k]) for k in rep["orphans"]}
    rep["undeclared"] = [k for k in rep["orphans"] if rep["fam"][k] not in declared]

    # a trial that reaches the reader by no route at all
    anywhere = set(named)
    for c in tabled:
        anywhere |= tabled[c] | prosed[c]
    rep["silent"] = sorted(set(reg) - anywhere)

    # a chapter that carries evidence and no story
    told = {c for c in placed if placed[c]}
    rep["unstoried"] = [c for c in order
                        if tabled.get(c) and c not in told
                        and c not in {x for s in sto.values() for x in s.get("chapters", [])}]

    # a story whose chapters have been split across parts
    rep["spanning"] = []
    for sid, s in sorted(sto.items()):
        parts = {part_of.get(c) for c in s.get("chapters", []) if c in part_of}
        if len(parts) > 1:
            rep["spanning"].append((sid, sorted(parts, key=lambda p: ptitle.get(p, (99, ""))[0])))

    # a question rendered somewhere its own story does not claim
    rep["stray"] = []
    for cid, qs in placed.items():
        for qid in sorted(qs):
            sid = home.get(qid)
            if sid is None:
                rep["stray"].append((cid, qid, "no such question"))
            elif cid not in sto[sid].get("chapters", []):
                rep["stray"].append((cid, qid, "%s lists %s" %
                                     (sid, ",".join(sto[sid].get("chapters", [])))))

    # a trial a chapter tabulates that neither its prose nor a story there discusses
    rep["untold"] = []
    for cid in order:
        if not tabled.get(cid):
            continue
        here = set(prosed.get(cid, ()))
        for qid in placed.get(cid, ()):
            sid = home.get(qid)
            if sid:
                for _s, _x, q in st.questions({sid: sto[sid]}):
                    if q["id"] == qid:
                        here |= set(q.get("trials") or [])
        missing = sorted(tabled[cid] - here)
        if missing:
            rep["untold"].append((cid, missing))
    rep["stale"], rep["contradicted"] = staleness(reg, sto)
    return rep


# A claim that something is not yet known, written about now rather than about a
# past analysis. The negative lookbehind is the whole check: `was immature at the
# primary analysis` is a fact about that analysis and never expires.
PRESENT = re.compile(
    r"(?<!was )(?<!were )(?<!has been )(?:"
    r"is (?:still )?immature|are (?:still )?immature|"
    r"is not (?:yet )?reported|are not (?:yet )?reported|"
    r"is not (?:yet )?known|remains unknown|remain unknown|"
    r"has not (?:yet )?reported|have not (?:yet )?reported|"
    r"has yet to report|none has reported|is awaited|are awaited"
    r")", re.I)

# What the claim is about, and the registry field that would settle it.
SURVIVAL = re.compile(r"survival", re.I)
# An `os` field that itself reports nothing settles nothing.
EMPTY = re.compile(r"not (?:yet )?reported|no overall survival result|immature|"
                   r"not separately reported|not reached|ongoing", re.I)


def settled(t, field):
    v = str(t.get(field) or "").strip()
    return bool(v) and not EMPTY.search(v)


def staleness(reg, sto):
    """Questions the registry has moved under, by date and by wording.

    The wording check reports at two levels, because a claim of the form
    "overall survival is immature" is a statement about every trial the question
    names, and one trial that has reported falsifies it. A claim of the form
    "the omission trial has not reported" is about one of them, and only that one
    falsifies it. Nothing in the sentence says which was meant.

    So WRONG is every named trial having the datum, where no reading of the
    sentence survives. CHECK is some of them having it, where the universal
    reading is false and the singular reading may not be. The second is read
    rather than fixed, which is the same division numcheck.py draws."""
    stale, contra = [], []
    for sid, _s, q in st.questions(sto):
        named = [k for k in (q.get("trials") or []) if k in reg]
        when = str(q.get("reviewed") or "")
        moved = [k for k in named
                 if reg[k].get("reviewed") and str(reg[k]["reviewed"]) > when]
        if moved:
            stale.append((sid, q["id"], when,
                          max(str(reg[k]["reviewed"]) for k in moved), moved))
        for mv in st.MOVES:
            text = str(q.get(mv) or "")
            for m in PRESENT.finditer(text):
                head = text[max(0, m.start() - 60):m.start()]
                field = "os" if SURVIVAL.search(head + m.group(0)) else "result"
                have = [k for k in named if settled(reg[k], field)]
                if have:
                    contra.append(("WRONG" if len(have) == len(named) else "CHECK",
                                   sid, q["id"], mv, m.group(0), field, have,
                                   " ".join((head + m.group(0)).split())[-95:]))
    return stale, contra


# ----------------------------------------------------------------- the report
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--orphans", action="store_true", help="just the unstoried trials")
    ap.add_argument("--families", action="store_true", help="how every orphan is classified")
    ap.add_argument("--untold", action="store_true", help="just the untold tabulated trials")
    ap.add_argument("--stale", action="store_true",
                    help="questions the registry has moved under")
    ap.add_argument("--quiet", action="store_true", help="errors only")
    a = ap.parse_args()

    reg, _refs = ev.load()
    doc = yaml.safe_load(open(os.path.join(BOOK, "stories.yaml"), encoding="utf-8"))
    sto = doc["stories"]
    r = reconcile(reg, sto, doc)

    if a.families:
        by = {}
        for k in r["orphans"]:
            by.setdefault(r["fam"][k], []).append(k)
        for f in sorted(by, key=lambda x: (-len(by[x]), x)):
            mark = "out of scope" if f in r["declared"] else "IN SCOPE"
            print("%-17s %3d   %s" % (f, len(by[f]), mark))
            for k in sorted(by[f]):
                print("    %-30s %s" % (k, (reg[k].get("topic") or "")[:60]))
        return 0

    if a.orphans:
        for k in r["undeclared"]:
            print("%-30s %-16s %s" % (k, r["fam"][k], (reg[k].get("topic") or "")[:52]))
        print("%d of %d registry trials are in no question; %d of those are in a family "
              "stories.yaml declares out of scope" %
              (len(r["orphans"]), len(reg), len(r["orphans"]) - len(r["undeclared"])))
        return 0

    if a.untold:
        for cid, ks in r["untold"]:
            print("%s  %s" % (cid, " ".join(ks)))
        return 0

    if a.stale:
        for sid, qid, when, moved, ks in r["stale"]:
            print("%s %s  read %s, registry moved %s: %s"
                  % (sid, qid, when, moved, " ".join(ks)))
        for lvl, sid, qid, mv, phrase, field, have, ctx in r["contradicted"]:
            print("%-6s %s %s  %s says %r; %d of its trials have a %s: %s"
                  % (lvl, sid, qid, mv, phrase, len(have), field, " ".join(have)))
        return 0

    wrong = [x for x in r["contradicted"] if x[0] == "WRONG"]
    look = [x for x in r["contradicted"] if x[0] == "CHECK"]
    bad = (len(r["undeclared"]) + len(r["silent"]) + len(r["stray"])
           + len(r["stale"]) + len(wrong))

    if not a.quiet:
        print("synthcheck: %d trials, %d stories, %d questions"
              % (len(reg), len(sto), sum(1 for _ in st.questions(sto))))
        print("  in a question:      %d" % (len(reg) - len(r["orphans"])))
        print("  out of scope:       %d  (%s)"
              % (len(r["orphans"]) - len(r["undeclared"]), ", ".join(sorted(r["declared"]))))

    if r["undeclared"]:
        print("\n%d trial(s) in no question and in no declared out-of-scope family:"
              % len(r["undeclared"]))
        for k in r["undeclared"]:
            print("   %-30s %-16s %s" % (k, r["fam"][k], (reg[k].get("topic") or "")[:50]))
        print("   Either write the question, or declare the family under _scope in "
              "stories.yaml with the reason.")

    if r["silent"]:
        print("\n%d trial(s) reach the reader by no route at all, not a table, not a "
              "story, not a sentence:" % len(r["silent"]))
        for k in r["silent"]:
            print("   %-30s %s" % (k, (reg[k].get("topic") or "")[:60]))

    if wrong:
        print("\n%d question(s) say something is not yet known where EVERY trial "
              "they name has it:" % len(wrong))
        for _l, sid, qid, mv, _p, field, have, ctx in wrong:
            print("   %s %s  `%s`, against the %s of %s" % (sid, qid, mv, field,
                                                            ", ".join(have[:4])))
            print("        ...%s" % ctx)

    if r["stale"]:
        print("\n%d question(s) were last read before a trial they name was:"
              % len(r["stale"]))
        for sid, qid, when, moved, ks in r["stale"]:
            print("   %s %s  read %s, %s reviewed %s"
                  % (sid, qid, when, ", ".join(ks[:4]), moved))
        print("   Re-read each against the registry, then move its `reviewed` date.")

    if look and not a.quiet:
        print("\n%d question(s) say something is not yet known where SOME of the "
              "trials named have it:" % len(look))
        for _l, sid, qid, mv, _p, field, have, ctx in look:
            print("   %s %s  `%s`, %d of %s have a %s"
                  % (sid, qid, mv, len(have), field, field))
            print("        ...%s" % ctx)
        print("   A blanket claim is false here and a claim about one named trial "
              "may not be. Read each.")

    if r["stray"]:
        print("\n%d question(s) rendered where their story does not claim them:" % len(r["stray"]))
        for cid, qid, why in r["stray"]:
            print("   %s renders %s, but %s" % (cid, qid, why))

    if not a.quiet:
        if r["unstoried"]:
            print("\n%d chapter(s) carry an evidence table and no story:" % len(r["unstoried"]))
            for c in r["unstoried"]:
                p = r["part_of"].get(c)
                print("   %-8s part %s" % (c, r["ptitle"].get(p, ("?", "?"))[1][:46]))
        if r["spanning"]:
            print("\n%d story/stories split across parts:" % len(r["spanning"]))
            for sid, parts in r["spanning"]:
                print("   %s  %s" % (sid, " + ".join(
                    "%s" % r["ptitle"].get(p, ("?", p))[1][:34] for p in parts)))
        n = sum(len(x[1]) for x in r["untold"])
        print("\n%d tabulated trial(s) in %d chapter(s) that neither the chapter's prose "
              "nor a story there discusses" % (n, len(r["untold"])))
        print("   (run --untold for the list; a table legitimately carries more than a "
              "chapter argues, so this one is read rather than fixed)")

    print("\nsynthcheck: %s" % ("every trial is either argued or declared out of scope"
                                if not bad else "%d thing(s) to settle" % bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
