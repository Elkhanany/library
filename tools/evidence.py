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
              | recurrence | cns | any
    subtype   HR+/HER2- | HER2+ | HR+/HER2+ | TNBC | HER2-low | BRCA | all
    line      neoadjuvant | adjuvant | post-neoadjuvant | 1L | 2L | 3L+ | any
    phase     2 | 3 | 2/3
    status    reported | ongoing | awaited
    modality  endocrine | cdk4-6 | chemo | her2 | adc | immunotherapy | parp | pi3k-akt
              | surgery | radiation | bone | supportive | other
    weight    practice-defining | supporting | exploratory | any
    topic     substring match on the topic field
    sort      year | acronym | n        (default: status then year)
    cols      comma-separated subset of the column ids below

A table enumerates the record a decision rests on. An exploratory trial is not part
of that record, so `weight=exploratory` is the one filter value that has to be asked
for: a block that says nothing about weight gets everything except the exploratory
trials, and a block that wants them says `weight=exploratory` or `weight=any`. This
is what stops a three-week single-arm window study from setting next to a randomised
phase III trial in the same table with nothing to tell a reader which is which.

Exploratory trials are not hidden. They are in the registry, in Appendix A, and in
the Chapter Stories, which is where a proof of concept earns its place: under the
question it was built to answer, with what its design cannot settle written next to
it. See tools/stories.py.

Usage
    python3 tools/evidence.py --check                 validate every block in every chapter
    python3 tools/evidence.py --render "setting=early subtype=TNBC line=neoadjuvant"
    python3 tools/evidence.py --orphans               registry trials no block picks up
    python3 tools/evidence.py --coverage              per-block match counts
    python3 tools/evidence.py --weights               the evidence-weight axis
    python3 tools/evidence.py --axes                  axes against the source document
    python3 tools/evidence.py --topics                near misses on a topic-filtered table
"""
import re, sys, os, argparse

try:
    import yaml
except ImportError:
    sys.exit("evidence.py needs pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "books", "breast-cancer")

VOCAB = {
    # cns is a population, not a place in the disease course: entry required
    # brain or leptomeningeal disease. It is its own setting because such a
    # trial otherwise matches every general metastatic filter, and a whole-brain
    # radiotherapy trial has no business in a first-line chemotherapy table. A
    # systemic trial that later reported a CNS subgroup stays metastatic.
    "setting": {"early", "metastatic", "dcis", "prevention", "mrd", "screening",
                "surveillance", "recurrence", "cns", "any"},
    "subtype": {"HR+/HER2-", "HER2+", "HR+/HER2+", "TNBC", "HER2-low", "BRCA", "all"},
    "line": {"neoadjuvant", "adjuvant", "post-neoadjuvant", "1L", "2L", "3L+", "any"},
    # What the trial randomised or tested, not what every arm received. A comma
    # list only when the randomised comparison itself crosses disciplines.
    "discipline": {"medical", "radiation", "surgical", "supportive", "other"},
    # How the publication counts lines, which decides the line tag in hormone
    # receptor-positive disease: endocrine trials count endocrine lines one by
    # one, while chemotherapy and conjugate trials treat the whole endocrine
    # phase as one line and count chemotherapy. CONVENTIONS.md has the rule.
    "line_basis": {"untreated", "endocrine", "chemotherapy", "all", "not-stated"},
    "phase": {"1", "1/2", "2", "2/3", "3"},
    "status": {"reported", "ongoing", "awaited"},
    "modality": {"endocrine", "cdk4-6", "chemo", "her2", "adc", "immunotherapy", "parp",
                 "pi3k-akt", "surgery", "radiation", "bone", "supportive", "other"},
    # How much of a decision the trial's result can carry. Unset means "not
    # exploratory", which is what every trial in the registry was before the axis
    # existed, so adding it changed no table.
    "weight": {"practice-defining", "supporting", "exploratory", "any"},
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
    # The one axis that is not a plain AND. A block that says nothing about weight
    # is asking for the trials a decision rests on, which is everything the registry
    # holds except the ones marked exploratory.
    want_w = f.get("weight")
    if want_w is None:
        if trial.get("weight") == "exploratory":
            return False
    elif want_w != "any":
        if str(trial.get("weight") or "") not in set(want_w.split(",")):
            return False
    for k, v in f.items():
        if k in DIRECTIVES or k == "weight":
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


def blocks_in_text(text):
    """Every evidence block in a piece of markdown, as (filter, body).

    Split out from blocks_in so a caller that has already cut a chapter into
    sections can scan one section at a time and know which section a block sits
    under, which the export needs and the build does not."""
    return [(m.group(1).strip(), m.group(2)) for m in BLOCK.finditer(text)]


def blocks_in(path):
    return blocks_in_text(open(path, encoding="utf-8").read())


def all_blocks():
    d = os.path.join(BOOK, "chapters")
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".md"):
            for spec, body in blocks_in(os.path.join(d, fn)):
                yield fn[:-3], spec, body


# What a registry entry actually holds about what the trial showed. Three
# states, because "has a result" was one flag doing two jobs and got both
# wrong: an ongoing trial with nothing entered read the same as a tabulated
# one, because neither carried `tabulated: false`.
RESULT_STATES = ("tabulated", "extracted", "none")


def result_state(t):
    """tabulated: a result field the evidence tables print.
       extracted : no such field, but the paper's own findings are on the record.
       none      : nothing, which for an ongoing trial is the truth and for a
                   reported one is a gap."""
    if str(t.get("result") or "").strip():
        return "tabulated"
    if str((t.get("digest") or {}).get("results") or "").strip():
        return "extracted"
    return "none"


def _yaml_load(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def cited_in(trials, prose_only=False):
    """Which chapters actually cite each trial. The registry's cited_by is a
    record; this is the fact, read out of the chapter every time it is asked.

    A trial reaches the page three ways and all three count. It can be named in
    prose as a {{trial:}} chip. It can be a row of a rendered evidence table. It
    can be one of the trials a story block names under a question. Only the first
    is literally in the markdown, so counting that alone reports a chapter as
    owing a trial it already carries, which is how this read the book until the
    revamp pass caught it."""
    out = {k: set() for k in trials}
    d = os.path.join(BOOK, "chapters")
    try:
        stories = (_yaml_load(os.path.join(BOOK, "stories.yaml")) or {}).get("stories") or {}
    except Exception:
        stories = {}
    q_trials = {}
    for sid, st in stories.items():
        for q in st.get("questions") or ():
            q_trials[q["id"]] = q.get("trials") or []
            q_trials.setdefault(sid, [])
            q_trials[sid] += q.get("trials") or []
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        cid = fn[:-3]
        text = open(os.path.join(d, fn), encoding="utf-8").read()
        for k in re.findall(r"\{\{trial:([A-Za-z0-9_\-]+)\}\}", text):
            if k in out:
                out[k].add(cid)
        if prose_only:
            continue
        for spec, _body in blocks_in(os.path.join(d, fn)):
            f, bad = parse_filter(spec)
            if bad:
                continue
            for t in select(trials, f):
                out[t["key"]].add(cid)
        for m in re.finditer(r"^```story[ \t]*([^\n]*)\n```[ \t]*$", text, re.M):
            for i in (x.strip() for x in m.group(1).split(",")):
                for k in q_trials.get(i, ()):
                    if k in out:
                        out[k].add(cid)
    return out


def sync_chapters(trials, write=False):
    """Bring each trial's `chapters` list into line with where the book cites it.

    The field is a hand-kept index of which chapters carry a trial, and a
    hand-kept index of four hundred trials across a hundred chapters goes stale
    the first time anything moves. It was 121 entries behind when this was
    written, all in the same direction, which is what a hand-kept index does.

    The fact is cheap to compute and `cited_in` already computes it: prose that
    names the trial, a table that renders it, a story block that places a
    question naming it. The edit is textual, because a YAML round trip
    reformats seventeen thousand lines and buries the change."""
    fact = cited_in(trials)
    path = os.path.join(BOOK, "trials.yaml")
    text = open(path, encoding="utf-8").read()
    changed = []
    for k in sorted(trials):
        want = sorted(fact.get(k) or ())
        m = re.search(r"^  %s:\n((?:    [^\n]*\n|      [^\n]*\n)*)" % re.escape(k),
                      text, re.M)
        if not m:
            continue
        blk = m.group(1)
        c = re.search(r"^    chapters:\n(?:    - [^\n]*\n)*", blk, re.M)
        have = re.findall(r"^    - (\S+)$", c.group(0), re.M) if c else []
        if have == want:
            continue
        changed.append((k, have, want))
        if not write:
            continue
        rows = "".join("    - %s\n" % x for x in want)
        if c:
            nb = blk[:c.start()] + ("    chapters:\n" + rows if want else "") + blk[c.end():]
        else:
            at = len(blk)                       # keys are written alphabetically
            for mm in re.finditer(r"^    ([a-z_]+):", blk, re.M):
                if mm.group(1) > "chapters":
                    at = mm.start()
                    break
            nb = blk[:at] + "    chapters:\n" + rows + blk[at:]
        text = text[:m.start(1)] + nb + text[m.end(1):]
    if write and changed:
        open(path, "w", encoding="utf-8").write(text)
    return changed


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


def topic_tags(trials):
    """The topic= values that behave like tags rather than like prose.

    A tag is appended to the topic as its own trailing clause, so it shows up as
    the last comma-separated token of at least one trial. `extended-endocrine`
    qualifies; `platinum`, which is simply a word in the sentence, does not."""
    tags = set()
    for _ch, spec, _b in all_blocks():
        f, bad = parse_filter(spec)
        v = None if bad else f.get("topic")
        if not v:
            continue
        for t in trials.values():
            parts = [p.strip() for p in str(t.get("topic") or "").split(",")]
            if parts and parts[-1] == v:
                tags.add(v)
                break
    return tags


STOP = set("a an and the of to in for with without versus vs or after before at by on "
           "years year versus standard therapy treatment trial trials patients disease "
           "breast cancer early advanced metastatic adjuvant neoadjuvant further".split())


def words(s):
    return {w for w in re.findall(r"[a-z0-9]+", str(s or "").lower())
            if len(w) > 2 and w not in STOP}


def topics(trials, floor=0.18):
    """Trials that look like they belong to a table whose tag they lack.

    `topic` is read two ways. `topic=platinum` matches the prose, and
    `topic=extended-endocrine` matches a tag someone appended to it. The second
    kind only works if every trial that belongs gets the tag, and nothing
    notices when one does not: the table renders, it is simply short. aTTom was
    missing from the tamoxifen-duration table for exactly this reason, and GIM4
    and SOLE from the extended-endocrine one. Each was still visible in its
    chapter's overview table, so nothing was unreachable and nothing looked
    wrong; the per-question table was just quietly incomplete.

    So this compares each untagged trial that the table's other axes admit
    against the trials already in it, on the words of their topics, and reports
    the ones that read alike. It is a heuristic and says so: a hit is a prompt
    to look, never a finding, and this never fails a build."""
    tags = topic_tags(trials)
    untagged = {k for k, t in trials.items()
                if [p.strip() for p in str(t.get("topic") or "").split(",")][-1] not in tags}

    rows = []
    for ch, spec, _body in all_blocks():
        f, bad = parse_filter(spec)
        if bad or f.get("topic") not in tags:
            continue
        inside = select(trials, f)
        vocab = set().union(*[words(t.get("topic")) for t in inside]) if inside else set()
        if not vocab:
            continue
        have = {t["key"] for t in inside}
        rest = {k: v for k, v in f.items() if k != "topic"}
        near = []
        for t in select(trials, rest):
            if t["key"] in have or t["key"] not in untagged:
                continue
            w = words(t.get("topic"))
            if not w:
                continue
            score = len(w & vocab) / len(w | vocab)
            if score >= floor:
                near.append((score, t["key"], t.get("topic")))
        if near:
            rows.append((ch, f["topic"], len(inside), sorted(near, reverse=True)))

    for ch, topic, n, near in rows:
        print("%s  topic=%-22s %d in the table" % (ch, topic, n))
        for score, k, tp in near:
            print("     %.2f  %-24s %s" % (score, k, (tp or "")[:62]))
    print("\nevidence: %d table(s) with an untagged trial that reads like the rest of it"
          % len(rows))
    print("  A hit either belongs in the table and wants the tag, or belongs elsewhere "
          "and wants its own. Neither is decided here.")
    return 0


# an acronym that is also an ordinary word would match everywhere
COMMON_ACRONYM = {"DATA", "SOLE", "FIRST", "CONFIRM", "TEAM", "FACE", "IDEAL", "SOFT",
                  "TEXT", "NEXT", "PEARL", "MALE", "POSITIVE", "SUCCESS", "MONITOR",
                  "SAFE", "TRAIN", "ADAPT", "ABC", "BEST", "CARE", "EA", "MINDACT",
                  "PLAN", "ICE", "OLD", "YOUNG", "SENOMAC", "ATLAS", "SOUND", "START",
                  "TAILOR"}


def unlinked(trials):
    """Chapters that discuss a trial in plain text and never once link it.

    A trial written as bare text is not cited. It gets no registry link, no
    reference card and no entry in Appendix A from that chapter. BC-820 argued
    KATHERINE, APHINITY and HERA at length and linked none of them.

    A LATER mention in plain text is ordinary prose and the book does it three
    hundred times, so only a chapter that never links the trial at all is
    reported."""
    prose = cited_in(trials, prose_only=True)
    acr = {}
    for k, t in trials.items():
        a = str(t.get("acronym") or "").strip()
        if len(a) >= 3 and a.upper() not in COMMON_ACRONYM:
            acr.setdefault(a, k)
    out = []
    d = os.path.join(BOOK, "chapters")
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        cid = fn[:-3]
        text = open(os.path.join(d, fn), encoding="utf-8").read()
        body = re.sub(r"\{\{trial:[a-z0-9.-]*\}\}", " ", text)
        body = re.sub(r"^---\n.*?\n---\n", "", body, flags=re.S)
        body = re.sub(r"```evidence[^\n]*\n```", " ", body)
        for a, k in acr.items():
            if cid in (prose.get(k) or set()):
                continue
            if re.search(r"(?<![A-Za-z0-9-])%s(?![A-Za-z0-9-])" % re.escape(a), body):
                out.append((cid, k, a))
    return sorted(out)


def gaps(trials):
    """The document says where a trial belongs; the prose says where it is
    actually discussed. Each direction is a different kind of work."""
    cites = cited_in(trials)
    prose = cited_in(trials, prose_only=True)
    unwritten, unlisted = [], []
    for k, t in sorted(trials.items()):
        planned = set(t.get("chapters") or ())
        actual = cites.get(k) or set()
        if planned - actual:
            unwritten.append((k, sorted(planned - actual)))
        # Only a prose mention is an authorial choice. A table picks trials up by
        # filter, so a table match outside the assignment is the filter working,
        # not a chapter quietly annexing a trial.
        extra = (prose.get(k) or set()) - planned
        if extra and planned:
            unlisted.append((k, sorted(extra)))
    print("assigned to a chapter that never cites it: %d" % len(unwritten))
    for k, ch in unwritten[:40]:
        print("   %-26s %s" % (k, ", ".join(ch)))
    if len(unwritten) > 40:
        print("   ... and %d more" % (len(unwritten) - 40))
    print("\nnamed in the prose of a chapter the document does not list: %d" % len(unlisted))
    for k, ch in unlisted[:25]:
        print("   %-26s %s" % (k, ", ".join(ch)))
    if len(unlisted) > 25:
        print("   ... and %d more" % (len(unlisted) - 25))
    return 0



# ---------------------------------------------------------------------------
# The source document as a second opinion on a trial's axes.
#
# `source` on a registry entry records where the pivotal-trials document listed
# the trial: a section, a numbered chapter, a grouping heading. That path is an
# assertion. "Ch. 63 - Neoadjuvant therapy in TNBC" says setting, subtype and
# line; "Platinum" under it says modality. Comparing the two catches a mistyped
# axis, and more usefully catches a trial filed under a heading that does not
# match what it actually studied.
#
# Each entry lists the values that heading admits. A trial disagrees when its
# own value shares nothing with that set. `waive` drops an axis the heading
# deliberately crosses: a cross-subtype chemotherapy foundation listed in an
# HR+ chapter is not an HR+ trial.
SECTION_AXES = {
    "Early nonmetastatic disease": {"setting": ["early", "dcis", "prevention"]},
    "Metastatic disease": {"setting": ["metastatic", "recurrence"]},
    "Brain and leptomeningeal metastases": {"setting": ["cns", "metastatic"]},
}

HRPOS = ["HR+/HER2-", "HR+/HER2+"]
HER2 = ["HER2+", "HR+/HER2+"]
LATER = ["2L", "3L+"]

CHAPTER_AXES = {
    53: {"subtype": HRPOS},
    54: {"subtype": HRPOS, "line": ["adjuvant"], "modality": ["endocrine"]},
    55: {"subtype": HRPOS, "line": ["adjuvant", "post-neoadjuvant"],
         "modality": ["cdk4-6"]},
    56: {"subtype": HRPOS, "line": ["neoadjuvant"]},
    57: {"subtype": HER2},
    58: {"subtype": HER2, "line": ["adjuvant", "post-neoadjuvant"]},
    59: {"subtype": HER2, "line": ["neoadjuvant"], "modality": ["her2"]},
    60: {"subtype": ["HR+/HER2+"]},
    61: {"subtype": ["TNBC"]},
    62: {"subtype": ["TNBC"], "line": ["adjuvant", "post-neoadjuvant"]},
    63: {"subtype": ["TNBC"], "line": ["neoadjuvant"]},
    67: {"subtype": ["HR+/HER2-"]},
    68: {"subtype": ["HR+/HER2-"], "modality": ["endocrine"]},
    69: {"subtype": ["HR+/HER2-"], "modality": ["cdk4-6"]},
    70: {"subtype": ["HR+/HER2-", "HER2-low"]},
    71: {"subtype": HER2},
    72: {"subtype": HER2},
    73: {"subtype": ["HR+/HER2+"]},
    74: {"subtype": ["TNBC"]},
    75: {"subtype": ["TNBC"]},
}

# A grouping heading overrides the chapter where it is more specific, and
# `waive` releases an axis the chapter asserted.
GROUP_AXES = {
    "Genomic assay-guided chemotherapy": {"modality": ["chemo"]},
    "Assay-validation cohorts / chemotherapy foundations (cross-subtype)":
        {"modality": ["chemo"], "waive": ["subtype"]},
    "Tamoxifen foundation": {"modality": ["endocrine"]},
    "AI vs tamoxifen / switching (postmenopausal)": {"modality": ["endocrine"]},
    "Ovarian function suppression (premenopausal)": {"modality": ["endocrine"]},
    "Extended tamoxifen": {"modality": ["endocrine"]},
    "Extended aromatase inhibition": {"modality": ["endocrine"]},
    "Interruption for pregnancy": {"modality": ["endocrine"]},
    "Recent conference report": {},
    # PENELOPE-B is listed here and gave palbociclib for residual disease after
    # neoadjuvant chemotherapy, which the registry calls post-neoadjuvant. The
    # chapter heading is the coarser of the two descriptions, not the truer one.
    "Adjuvant CDK4/6 inhibition": {"modality": ["cdk4-6"],
                                   "line": ["adjuvant", "post-neoadjuvant"]},
    "Neoadjuvant endocrine therapy": {"modality": ["endocrine"], "line": ["neoadjuvant"]},
    # POETIC and ALTERNATE give endocrine therapy before surgery as treatment.
    # WSG-ADAPT HR+/HER2- gives three weeks of it as a response window and then
    # decides adjuvant therapy, so its line is adjuvant and the heading is the
    # coarser description. Both readings are admitted here.
    "Endocrine response-adapted / biomarker": {"modality": ["endocrine"],
                                               "line": ["neoadjuvant", "adjuvant"]},
    "Neoadjuvant CDK4/6 (phase II)": {"modality": ["cdk4-6"], "line": ["neoadjuvant"]},
    "Neoadjuvant checkpoint blockade (phase III)":
        {"modality": ["immunotherapy"], "line": ["neoadjuvant"]},
    "Adjuvant trastuzumab": {"modality": ["her2"], "line": ["adjuvant"]},
    "Adjuvant dual blockade": {"modality": ["her2"], "line": ["adjuvant"]},
    "De-escalation": {"modality": ["her2"], "line": ["adjuvant"]},
    "Trastuzumab duration": {"modality": ["her2"], "line": ["adjuvant"]},
    "Extended adjuvant": {"modality": ["her2"], "line": ["adjuvant"]},
    "Post-neoadjuvant (residual disease)": {"line": ["post-neoadjuvant"]},
    "Foundational trastuzumab / dual blockade": {"modality": ["her2"], "line": ["neoadjuvant"]},
    "Anthracycline omission / de-escalation": {"line": ["neoadjuvant"]},
    "Trials conducted in Asian populations": {"line": ["neoadjuvant"]},
    "Checkpoint blockade (negative)": {"modality": ["immunotherapy"], "line": ["neoadjuvant"]},
    "Recent ADC trial": {"modality": ["adc"], "line": ["neoadjuvant"]},
    "Early triple-positive (HR+/HER2+) disease": {},
    "Early triple-negative disease (overview)": {},
    "Residual disease": {"line": ["post-neoadjuvant"]},
    "Germline BRCA": {"modality": ["parp"], "waive": ["subtype"]},
    "Adjuvant capecitabine / platinum": {"modality": ["chemo"], "line": ["adjuvant"]},
    "Adjuvant checkpoint blockade": {"modality": ["immunotherapy"], "line": ["adjuvant"]},
    "Checkpoint blockade": {"modality": ["immunotherapy"]},
    "Platinum": {"modality": ["chemo"]},
    "Taxane formulation / platform": {"modality": ["chemo"]},
    "Fulvestrant / endocrine sequencing": {"modality": ["endocrine"]},
    "Oral SERDs / receptor degraders": {"modality": ["endocrine"]},
    "ctDNA-guided switching": {"modality": ["endocrine"]},
    "PI3K / AKT / mTOR": {"modality": ["pi3k-akt"]},
    "First line": {"line": ["1L"]},
    "Second line / beyond": {"line": LATER},
    "Second line and beyond (ADCs)": {"modality": ["adc"], "line": LATER},
    "Timing / comparison / sequencing": {"modality": ["cdk4-6"]},
    "Post-CDK4/6i (continuation / switch)": {"modality": ["cdk4-6"], "line": LATER},
    "Antibody-drug conjugates": {"modality": ["adc"]},
    "Chemotherapy foundations (cross-subtype)": {"modality": ["chemo"], "waive": ["subtype"]},
    "PARP inhibitors (gBRCA)": {"modality": ["parp"], "waive": ["subtype"]},
    "PARP inhibitors (gBRCA / HRR)": {"modality": ["parp"], "waive": ["subtype"]},
    "Historical": {"modality": ["her2"]},
    "Continued blockade / alternative antibodies": {"modality": ["her2"]},
    "Tyrosine kinase inhibitors": {"modality": ["her2"]},
    "Endocrine + HER2 blockade": {"modality": ["endocrine", "her2"]},
    "CDK4/6 combinations": {"modality": ["cdk4-6"]},
    "First-line immunotherapy + chemotherapy": {"modality": ["immunotherapy"], "line": ["1L"]},
    "Later-line checkpoint monotherapy": {"modality": ["immunotherapy"], "line": LATER},
    "First-line ADC +/- checkpoint": {"modality": ["adc"], "line": ["1L"]},
    "Later-line ADCs": {"modality": ["adc"], "line": LATER},
    "AKT inhibition (incl. negative confirmatory)": {"modality": ["pi3k-akt"]},
    "Exploratory immunotherapy and radiotherapy": {"modality": ["immunotherapy", "radiation"]},
    "HER2 positive brain metastases and tucatinib":
        {"subtype": HER2, "modality": ["her2"]},
    "HER2 positive brain metastases and antibody drug conjugates":
        {"subtype": HER2, "modality": ["adc"]},
    "HER2 positive brain metastases and other kinase inhibitors":
        {"subtype": HER2, "modality": ["her2"]},
    "HER2 positive brain metastases and antibody combinations":
        {"subtype": HER2, "modality": ["her2"]},
    "HER2 directed therapy for leptomeningeal disease":
        {"subtype": HER2 + ["HER2-low"], "modality": ["her2"]},
    "TNBC and studies spanning breast cancer subtypes": {"waive": ["subtype"]},
    "Hormone receptor positive brain metastases": {"subtype": ["HR+/HER2-"]},
    "Radiotherapy foundations and systemic treatment combinations":
        {"modality": ["radiation"], "waive": ["subtype"]},
    "Leptomeningeal disease and radiotherapy":
        {"modality": ["radiation"], "waive": ["subtype"]},
    "Intrathecal chemotherapy in breast cancer leptomeningeal disease":
        {"modality": ["chemo"], "waive": ["subtype"]},
}


def _norm(s):
    """Headings are typed with en dashes and plus-minus signs; the table is
    written in ASCII so it stays greppable."""
    return (s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")
            .replace("\u00b1", "+/-"))


def expected(path):
    """What one source path says a trial's axes should be, and what it waives."""
    want, waived = {}, set()
    for layer in (SECTION_AXES.get(path.get("section"), {}),
                  CHAPTER_AXES.get(path.get("ch"), {}),
                  GROUP_AXES.get(_norm(path.get("group") or ""), {})):
        waived |= set(layer.get("waive", ()))
        for k, v in layer.items():
            if k != "waive":
                want[k] = v
    for k in waived:
        want.pop(k, None)
    return want


def axes(trials):
    """Where the registry and the source document disagree about a trial."""
    unknown, disagree, untabulated = set(), [], []
    for key, t in sorted(trials.items()):
        paths = t.get("source") or []
        if not paths:
            continue
        for p in paths:
            g = _norm(p.get("group") or "")
            if g and g not in GROUP_AXES and g not in CHAPTER_AXES.values():
                unknown.add(g)
        if t.get("tabulated") is False:
            untabulated.append(key)
            continue
        # A trial listed under two headings is claimed by both, so a value
        # agreeing with either one is agreement, not a disagreement. A path
        # marked xref is a signpost the document left to another chapter, and
        # asserts nothing about the trial.
        paths = [p for p in paths if not p.get("xref")] or paths
        rows = []
        for axis in ("setting", "subtype", "line", "modality"):
            have = {v.strip() for v in str(t.get(axis) or "").split(",") if v.strip()}
            if not have or (axis == "subtype" and "all" in have):
                continue
            allowed, said = set(), False
            for p in paths:
                w = expected(p).get(axis)
                if w:
                    said = True
                    allowed |= set(w)
            if said and not have & allowed:
                rows.append((axis, ",".join(sorted(have)), ", ".join(sorted(allowed))))
        if rows:
            disagree.append((key, t, rows))

    for key, t, rows in disagree:
        where = "; ".join("%s%s" % ("Ch. %d / " % p["ch"] if p.get("ch") else "",
                                    p.get("group") or p.get("section"))
                          for p in t["source"])
        print("%-26s %s" % (key, where))
        for axis, have, want in rows:
            print("    %-9s registry %-28s document implies %s" % (axis, have, want))
    print()
    print("axes: %d trial(s) disagree with the source document" % len(disagree))
    print("      %d listed in the document with no axes yet (tabulated: false)"
          % len(untabulated))
    if unknown:
        print("      %d grouping heading(s) not in the table:" % len(unknown))
        for g in sorted(unknown):
            print("        %s" % g)
    return 0


# ------------------------------------------------------------ line labels
# A heading or caption that names a line of therapy is a claim about the trials
# beneath it, and nothing used to test it. BC-920's section on conjugates was
# titled "Conjugates in second line and beyond" from the day the chapter was
# drafted, while the registry had tagged ASCENT-03, ASCENT-04 and
# TROPION-Breast02 first-line all along and the prose said the class had moved
# earlier. The label came from the class's history rather than from the trials,
# and it outlived them. This reads every such label and checks it against the
# line tags of the trials its tables actually render.
_LINE_TOKENS = [
    (re.compile(r"\bfirst[- ]line\b", re.I), 1),
    (re.compile(r"\bsecond[- ]line\b", re.I), 2),
    (re.compile(r"\bthird[- ]line\b|\blater[- ]lines?\b|\blast line\b", re.I), 3),
]
_OPEN_END = re.compile(r"\b(?:second|third)[- ]line (?:and|or) (?:beyond|later)\b|\bline and beyond\b|"
                       r"\band later\b|\bor later\b|\bafter (?:the )?first (?:line|progression)\b", re.I)
_RANGE = re.compile(r"\bfrom\b.+\bto\b", re.I)
_SOFT = re.compile(r"\bmostly\b|\blargely\b|\bmainly\b|\bpredominantly\b", re.I)
_ORD = {"1L": 1, "2L": 2, "3L+": 3}


def line_claim(text, names=()):
    """The metastatic lines a heading or caption asserts, as a set of 1-3, or
    None when it names no ordinal line. 'from X to Y' spans the range between,
    'and beyond' opens the top, and 'from diagnosis' starts at the first line.
    A sentence that names a trial is about that trial, as in "INAVO120 is a
    first-line trial and so does not appear in the table", so it is skipped.
    Names match case-sensitively, so the FIRST trial does not swallow the word
    "first"."""
    t = str(text or "").replace("_", " ")
    if names:
        keep = [x for x in re.split(r"(?<=\.)\s+", t)
                if not any(re.search(r"(?<![\w-])%s(?![\w-])" % re.escape(n), x) for n in names)]
        t = " ".join(keep)
    hits = {n for rx, n in _LINE_TOKENS if rx.search(t)}
    if not hits:
        return None
    if re.search(r"\bfrom diagnosis\b", t, re.I):
        hits.add(1)
    if re.search(r"\brefractory\b|\bpretreated\b", t, re.I):
        hits.add(3)
    if _OPEN_END.search(t):
        hits |= set(range(min(hits), 4)) | ({2, 3} if re.search(r"after (?:the )?first", t, re.I) else set())
    if _RANGE.search(t) and len(hits) > 1:
        hits = set(range(min(hits), max(hits) + 1))
    return hits


def trial_lines(t):
    """The ordinal metastatic lines a record is tagged with, or None when it
    carries none (early disease, or 'any')."""
    got = {_ORD[p.strip()] for p in str(t.get("line") or "").split(",") if p.strip() in _ORD}
    return got or None


def line_labels(trials):
    """(errors, warnings) for every heading or caption whose named line of
    therapy excludes a trial its own tables render. A caption that names the
    trial is taken to have explained it; a label saying 'mostly' warns."""
    errs, warns = [], []
    names = sorted({t.get("acronym") for t in trials.values() if t.get("acronym")}, key=len, reverse=True)
    d = os.path.join(BOOK, "chapters")
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        ch = fn[:-3]
        text = open(os.path.join(d, fn), encoding="utf-8").read()
        sections = re.split(r"(?m)^(?=## )", text)
        for sec in sections:
            head = sec.split("\n", 1)[0].lstrip("# ").strip() if sec.startswith("## ") else ""
            rows = []
            for spec, _body in blocks_in_text(sec):
                f, bad = parse_filter(spec)
                if bad:
                    continue
                hits = select(trials, f)
                rows.extend(hits)
                cap = (f.get("caption") or "").replace("_", " ")
                claim = line_claim(cap, names)
                if claim is None:
                    continue
                for t in hits:
                    tl = trial_lines(t)
                    if tl is None or tl & claim:
                        continue
                    if (t.get("acronym") or "").lower() in cap.lower():
                        continue
                    msg = (f"{ch}: caption says line {sorted(claim)} but renders {t['key']} "
                           f"tagged {t.get('line')}: \"{cap[:90]}\"")
                    (warns if _SOFT.search(cap) else errs).append(msg)
            claim = line_claim(head)
            if claim is None:
                continue
            for t in {r["key"]: r for r in rows}.values():
                tl = trial_lines(t)
                if tl is None or tl & claim:
                    continue
                msg = (f"{ch}: heading \"{head[:70]}\" says line {sorted(claim)} but its tables "
                       f"render {t['key']} tagged {t.get('line')}")
                (warns if _SOFT.search(head) else errs).append(msg)
    return errs, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--lines", action="store_true",
                    help="headings and captions whose named line of therapy excludes a trial they render")
    ap.add_argument("--render", metavar="FILTER")
    ap.add_argument("--orphans", action="store_true")
    ap.add_argument("--coverage", action="store_true")
    ap.add_argument("--weights", action="store_true",
                    help="the evidence-weight axis: how it is filled, and which tables "
                         "are holding exploratory trials back")
    ap.add_argument("--stale", action="store_true",
                    help="trials with a publication newer than their last review, "
                         "and the chapters that cite them")
    ap.add_argument("--axes", action="store_true",
                    help="where a trial's setting, subtype, line or modality "
                         "disagrees with the heading it was listed under")
    ap.add_argument("--topics", action="store_true",
                    help="for each topic-filtered table, the trials that match its "
                         "other axes and miss only the topic")
    ap.add_argument("--unlinked", action="store_true",
                    help="chapters that discuss a trial in plain text and never link it")
    ap.add_argument("--sync-chapters", action="store_true",
                    help="rewrite each trial's `chapters` list from where the book "
                         "cites it, so the hand-kept index cannot drift")
    ap.add_argument("--gaps", action="store_true",
                    help="where the trial document and the prose disagree about "
                         "which chapters discuss a trial")
    a = ap.parse_args()
    trials, refs = load()

    if a.lines:
        errs, warns = line_labels(trials)
        for e in errs:
            print("ERROR:", e)
        for w in warns:
            print("warn: ", w)
        print(f"lines: {len(errs)} label(s) contradicted by the trials they render, {len(warns)} to read")
        return 1 if errs else 0
    if a.stale:
        return stale(trials)
    if a.axes:
        return axes(trials)
    if a.topics:
        return topics(trials)
    if a.unlinked:
        rows = unlinked(trials)
        for cid, k, a2 in rows:
            print("   %-8s %-26s writes %s and never links it" % (cid, k, a2))
        print("evidence: %d chapter/trial pair(s) discussed in plain text and never cited"
              % len(rows))
        return 1 if rows else 0

    if a.sync_chapters:
        rows = sync_chapters(trials, write=True)
        for k, have, want in rows[:30]:
            print("   %-26s %d -> %d  %s" % (k, len(have), len(want),
                                             " ".join(sorted(set(want) - set(have))[:6])))
        if len(rows) > 30:
            print("   ... and %d more" % (len(rows) - 30))
        print("evidence: %d trial(s) had a stale `chapters` list; rewritten from the book"
              % len(rows))
        return 0

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
        # An exploratory trial in no table is not an orphan. It is held back from
        # the tables on purpose and its home is the story layer, so it is counted
        # separately and stories.py --orphans is the report that matters for it.
        expl = [k for k in miss if trials[k].get("weight") == "exploratory"]
        rest = [k for k in miss if trials[k].get("weight") != "exploratory"]
        print(f"{len(rest)} of {len(trials)} registry trials are not picked up by any evidence block:")
        for k in rest:
            print(f"  {k:22} {trials[k].get('setting','?'):11} {trials[k].get('subtype','?'):12} "
                  f"{trials[k].get('line','-')}")
        if expl:
            print(f"\n{len(expl)} more are marked exploratory and are held back from the tables "
                  f"by design. Run: python3 tools/stories.py --orphans")
        return 0

    if a.coverage:
        for ch, spec, _ in all_blocks():
            f, bad = parse_filter(spec)
            n = len(select(trials, f))
            flag = "  <-- EMPTY" if n == 0 else ("  <-- " + "; ".join(bad) if bad else "")
            print(f"{ch}  {n:3}  {spec}{flag}")
        return 0

    if a.weights:
        from collections import Counter
        c = Counter(t.get("weight") or "unset" for t in trials.values())
        for k in ("practice-defining", "supporting", "exploratory", "unset"):
            print(f"  {k:18} {c.get(k, 0):4}")
        held = []
        for ch, spec, _ in all_blocks():
            f, bad = parse_filter(spec)
            if bad or f.get("weight"):
                continue
            wide = dict(f, weight="any")
            extra = [t["key"] for t in select(trials, wide)
                     if t.get("weight") == "exploratory"]
            if extra:
                held.append((ch, len(extra), spec, extra))
        print(f"\n{len(held)} table(s) are holding exploratory trials back:")
        for ch, n, spec, extra in held:
            print(f"  {ch}  +{n:2}  {spec[:76]}")
            print(f"            {', '.join(extra[:8])}{' ...' if len(extra) > 8 else ''}")
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
    ADVANCED = {"metastatic", "cns", "recurrence", "mrd"}
    for k, t in trials.items():
        axes_ = lambda f: {p.strip() for p in str(t.get(f) or "").split(",") if p.strip()}
        if not t.get("discipline"):
            errs.append(f"trials.yaml[{k}] has no discipline; say what the trial tested "
                        f"(medical, radiation, surgical, supportive or other)")
        # Every systemic trial in advanced disease says how it counts lines. The
        # line tag is derived from that, and a tag with no stated basis is how a
        # first-line trial ends up filed under second line.
        if "medical" in axes_("discipline") and axes_("setting") & ADVANCED:
            if not t.get("line_basis"):
                errs.append(f"trials.yaml[{k}] is a systemic trial in advanced disease with no line_basis")
            if not t.get("prior_therapy"):
                errs.append(f"trials.yaml[{k}] is a systemic trial in advanced disease with no prior_therapy")
        if t.get("line_basis") and not axes_("setting") & ADVANCED:
            errs.append(f"trials.yaml[{k}] carries line_basis but no advanced-disease setting")
        if t.get("line_basis") == "untreated" and "1L" not in axes_("line"):
            errs.append(f"trials.yaml[{k}].line_basis is untreated but line={t.get('line')!r} has no 1L")
        if axes_("line") == {"1L"} and t.get("line_basis") not in (None, "untreated"):
            errs.append(f"trials.yaml[{k}] is tagged 1L alone but line_basis={t.get('line_basis')!r}")
        for key in ("setting", "subtype", "line", "status", "discipline", "line_basis"):
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
        # The paper a table quotes is a publication, so it belongs in the
        # publication history. Without this, a trial can show a result with no
        # paper behind it in the appendix, and --stale cannot tell whether
        # anything newer has appeared.
        if pr and pr not in {p.get("ref") for p in (t.get("pubs") or ())}:
            errs.append(f"trials.yaml[{k}].primary_ref={pr!r} is not in its pubs; "
                        f"add it with the role the source gave it")

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

    lerr, _lwarn = line_labels(trials)
    errs.extend(lerr)

    for e in errs:
        print("ERROR:", e)
    print(f"evidence: {nblocks} blocks, {len(trials)} trials, {len(errs)} problems")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
