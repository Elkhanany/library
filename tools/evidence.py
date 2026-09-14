#!/usr/bin/env python3
"""
evidence.py — render and validate the trial evidence tables.

A chapter declares a table with a fenced block carrying only a filter:

    ```evidence setting=early subtype=HR+/HER2- line=adjuvant
    ```

The block has no body. The table is rendered from trials.yaml at build time, so a
new readout is added ONCE to the registry and appears in every chapter whose
filter matches it. Never paste a trial result into chapter prose that the table
already carries.

Filter keys are ANDed. A value may be a comma-separated list, which is ORed.
`sort` and `cols` are directives, not filters.

    setting   early | metastatic | dcis | prevention | mrd | screening | surveillance
              | recurrence | any
    subtype   HR+/HER2- | HER2+ | HR+/HER2+ | TNBC | HER2-low | BRCA | all
    line      neoadjuvant | adjuvant | post-neoadjuvant | 1L | 2L | 3L+ | any
    phase     2 | 3 | 2/3
    status    reported | ongoing | awaited
    modality  endocrine | cdk4-6 | chemo | her2 | adc | immunotherapy | parp | pi3k-akt
              | surgery | radiation | bone | supportive | other
    topic     substring match on the topic field
    sort      year | acronym | n        (default: status then year)
    cols      comma-separated subset of the column ids below

Usage
    python3 tools/evidence.py --check                 validate every block in every chapter
    python3 tools/evidence.py --render "setting=early subtype=TNBC line=neoadjuvant"
    python3 tools/evidence.py --orphans               registry trials no block picks up
    python3 tools/evidence.py --coverage              per-block match counts
"""
import re, sys, os, argparse

try:
    import yaml
except ImportError:
    sys.exit("evidence.py needs pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "books", "breast-cancer")

VOCAB = {
    "setting": {"early", "metastatic", "dcis", "prevention", "mrd", "screening",
                "surveillance", "recurrence", "any"},
    "subtype": {"HR+/HER2-", "HER2+", "HR+/HER2+", "TNBC", "HER2-low", "BRCA", "all"},
    "line": {"neoadjuvant", "adjuvant", "post-neoadjuvant", "1L", "2L", "3L+", "any"},
    "phase": {"1", "1/2", "2", "2/3", "3"},
    "status": {"reported", "ongoing", "awaited"},
    "modality": {"endocrine", "cdk4-6", "chemo", "her2", "adc", "immunotherapy", "parp",
                 "pi3k-akt", "surgery", "radiation", "bone", "supportive", "other"},
}
DIRECTIVES = {"sort", "cols", "caption"}
COLS = ["acronym", "phase", "n", "population", "arms", "endpoint", "result", "os", "status"]
HEAD = {"acronym": "Trial", "phase": "Ph", "n": "N", "population": "Population",
        "arms": "Experimental vs control",
        "endpoint": "Primary endpoint", "result": "Result", "os": "Overall survival",
        "status": "Status"}
STATUS_ORDER = {"reported": 0, "awaited": 1, "ongoing": 2}


def load():
    t = yaml.safe_load(open(os.path.join(BOOK, "trials.yaml")))["trials"]
    r = yaml.safe_load(open(os.path.join(BOOK, "references.yaml")))["refs"]
    return t, r


def parse_filter(spec):
    f, bad = {}, []
    for tok in spec.split():
        if "=" not in tok:
            bad.append(f"token {tok!r} is not key=value")
            continue
        k, v = tok.split("=", 1)
        if k not in VOCAB and k not in DIRECTIVES and k != "topic":
            bad.append(f"unknown filter key {k!r}")
            continue
        if k in VOCAB:
            for part in v.split(","):
                if part not in VOCAB[k]:
                    bad.append(f"{k}={part!r} is not in the controlled vocabulary {sorted(VOCAB[k])}")
        f[k] = v
    return f, bad


def matches(trial, f):
    for k, v in f.items():
        if k in DIRECTIVES:
            continue
        tv = trial.get(k)
        if tv is None:
            return False
        tv = str(tv)
        if k == "topic":
            if v.lower() not in tv.lower():
                return False
            continue
        wanted = set(v.split(","))
        have = {x.strip() for x in tv.split(",")}
        # An all-comers trial belongs in every subtype table. Wildcarding is deliberately
        # NOT extended to setting, line or modality, where "any" means not applicable and
        # a trial with it should stay out of a specific table.
        if k == "subtype" and ("all" in have or "all" in wanted):
            continue
        if not (wanted & have):
            return False
    return True


def select(trials, f):
    hits = [dict(t, key=k) for k, t in trials.items() if matches(t, f)]
    s = f.get("sort")
    if s == "acronym":
        hits.sort(key=lambda t: t.get("acronym", ""))
    elif s == "n":
        hits.sort(key=lambda t: -(t.get("n") or 0))
    elif s == "year":
        hits.sort(key=lambda t: -(t.get("year") or 0))
    else:
        hits.sort(key=lambda t: (STATUS_ORDER.get(t.get("status", "reported"), 9),
                                 -(t.get("year") or 0), t.get("acronym", "")))
    return hits


def render(hits, f):
    cols = [c.strip() for c in f["cols"].split(",")] if f.get("cols") else COLS
    cols = [c for c in cols if c in COLS]
    present = [c for c in cols if any(t.get(c) not in (None, "") for t in hits)]
    if not present:
        return "_No trial in the registry matches this filter._"
    out = ["| " + " | ".join(HEAD[c] for c in present) + " | Ref |",
           "|" + "---|" * (len(present) + 1)]
    for t in hits:
        cells = []
        for c in present:
            v = t.get(c)
            v = "" if v is None else str(v)
            if c == "acronym":
                v = f"{{{{trial:{t['key']}}}}}"
            cells.append(v.replace("|", "\\|"))
        ref = f"[@{t['primary_ref']}]" if t.get("primary_ref") else ""
        out.append("| " + " | ".join(cells) + f" | {ref} |")
    if f.get("caption"):
        out.append("")
        out.append(f"_{f['caption'].replace('_',' ')}_")
    return "\n".join(out)


BLOCK = re.compile(r"^```evidence[ \t]*([^\n]*)\n(.*?)^```[ \t]*$", re.M | re.S)


def blocks_in(path):
    return [(m.group(1).strip(), m.group(2)) for m in BLOCK.finditer(open(path).read())]


def all_blocks():
    d = os.path.join(BOOK, "chapters")
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".md"):
            for spec, body in blocks_in(os.path.join(d, fn)):
                yield fn[:-3], spec, body


def cited_in(trials):
    """Which chapters actually cite each trial. The registry's cited_by is a
    record; this is the fact, read out of the prose every time it is asked."""
    out = {k: set() for k in trials}
    d = os.path.join(BOOK, "chapters")
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        text = open(os.path.join(d, fn), encoding="utf-8").read()
        for k in re.findall(r"\{\{trial:([A-Za-z0-9_\-]+)\}\}", text):
            if k in out:
                out[k].add(fn[:-3])
    return out


def stale(trials):
    """A publication added after a trial was last reviewed means the prose that
    cites it may now be out of date. This is the worklist: what changed, and
    which chapters to look at.

    A publication with no `added` date was present at the last review. Only the
    intake stamps that field, so the first import cannot flag itself."""
    cites = cited_in(trials)
    rows = []
    for k, t in sorted(trials.items()):
        rev = str(t.get("reviewed") or "")
        fresh = [p for p in (t.get("pubs") or [])
                 if p.get("added") and str(p["added"]) > rev]
        if fresh:
            rows.append((k, rev, fresh, sorted(cites.get(k) or ()),
                         t.get("chapters") or []))
    if not rows:
        print("evidence: nothing new since the last review of any trial")
        return 0
    for k, rev, fresh, cited, chaps in rows:
        print("%s  reviewed %s" % (k, rev or "never"))
        for p in fresh:
            print("    + %-10s %-26s added %s" % (p.get("kind", "?"),
                                                  p.get("ref", "?"), p["added"]))
        where = cited or chaps
        print("    revisit: %s" % (", ".join(where) if where else
                                   "no chapter cites this trial"))
    print("\nevidence: %d trial(s) with new publications since review" % len(rows))
    return 0


def gaps(trials):
    """The document says where a trial belongs; the prose says where it is
    actually discussed. Each direction is a different kind of work."""
    cites = cited_in(trials)
    unwritten, unlisted = [], []
    for k, t in sorted(trials.items()):
        planned = set(t.get("chapters") or ())
        actual = cites.get(k) or set()
        if planned - actual:
            unwritten.append((k, sorted(planned - actual)))
        if actual - planned and planned:
            unlisted.append((k, sorted(actual - planned)))
    print("assigned to a chapter that never cites it: %d" % len(unwritten))
    for k, ch in unwritten[:40]:
        print("   %-26s %s" % (k, ", ".join(ch)))
    if len(unwritten) > 40:
        print("   ... and %d more" % (len(unwritten) - 40))
    print("\ncited by a chapter the document does not list: %d" % len(unlisted))
    for k, ch in unlisted[:25]:
        print("   %-26s %s" % (k, ", ".join(ch)))
    if len(unlisted) > 25:
        print("   ... and %d more" % (len(unlisted) - 25))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--render", metavar="FILTER")
    ap.add_argument("--orphans", action="store_true")
    ap.add_argument("--coverage", action="store_true")
    ap.add_argument("--stale", action="store_true",
                    help="trials with a publication newer than their last review, "
                         "and the chapters that cite them")
    ap.add_argument("--gaps", action="store_true",
                    help="where the trial document and the prose disagree about "
                         "which chapters discuss a trial")
    a = ap.parse_args()
    trials, refs = load()

    if a.stale:
        return stale(trials)
    if a.gaps:
        return gaps(trials)

    if a.render:
        f, bad = parse_filter(a.render)
        for b in bad:
            print("filter error:", b, file=sys.stderr)
        hits = select(trials, f)
        print(f"# {len(hits)} trial(s)\n")
        print(render(hits, f))
        return 1 if bad else 0

    if a.orphans:
        seen = set()
        for _, spec, _ in all_blocks():
            f, _bad = parse_filter(spec)
            seen |= {t["key"] for t in select(trials, f)}
        miss = sorted(set(trials) - seen)
        print(f"{len(miss)} of {len(trials)} registry trials are not picked up by any evidence block:")
        for k in miss:
            print(f"  {k:22} {trials[k].get('setting','?'):11} {trials[k].get('subtype','?'):12} "
                  f"{trials[k].get('line','-')}")
        return 0

    if a.coverage:
        for ch, spec, _ in all_blocks():
            f, bad = parse_filter(spec)
            n = len(select(trials, f))
            flag = "  <-- EMPTY" if n == 0 else ("  <-- " + "; ".join(bad) if bad else "")
            print(f"{ch}  {n:3}  {spec}{flag}")
        return 0

    # --check (default)
    errs, nblocks = [], 0
    for ch, spec, body in all_blocks():
        nblocks += 1
        if body.strip():
            errs.append(f"{ch}: evidence block has a body; it must contain only the filter line")
        f, bad = parse_filter(spec)
        for b in bad:
            errs.append(f"{ch}: {b}")
        if not bad and not select(trials, f):
            errs.append(f"{ch}: filter {spec!r} matches no trial")
    # registry integrity
    for k, t in trials.items():
        for key in ("setting", "subtype", "line", "status"):
            v = t.get(key)
            if v is None:
                continue
            for part in str(v).split(","):
                part = part.strip()
                if key in VOCAB and part not in VOCAB[key]:
                    errs.append(f"trials.yaml[{k}].{key}={part!r} not in controlled vocabulary")
        pr = t.get("primary_ref")
        if pr and pr not in refs:
            errs.append(f"trials.yaml[{k}].primary_ref={pr!r} not in references.yaml")

    # Two keys for one trial. Parallel writing waves each minted a record for
    # WSG TP-II, and because both matched the same filters it was listed twice,
    # identically, in three published tables -- which reads as two trials
    # agreeing rather than one trial counted twice. Same primary publication and
    # same enrolment is the signature; nothing else legitimately shares both.
    seen = {}
    for k, t in sorted(trials.items()):
        pr, n = t.get("primary_ref"), t.get("n")
        if not pr or n is None:
            continue
        first = seen.setdefault((pr, n), k)
        if first != k:
            errs.append(f"trials.yaml[{k}] and [{first}] look like the same trial: "
                        f"primary_ref={pr!r}, n={n}. Merge them and keep one key.")

    for e in errs:
        print("ERROR:", e)
    print(f"evidence: {nblocks} blocks, {len(trials)} trials, {len(errs)} problems")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
