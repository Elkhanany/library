"""Match gathered papers against the registry and group the unmatched trial reports into candidate trials.

    python3 match.py            # writes ../data/candidates.json and prints a summary

A paper is covered when its PMID is already a reference of a registry trial, when one of its trial
registration numbers (NCT, ISRCTN) is on a registry record, or when a trial name in its title matches a
registry acronym. Uncovered trial reports are grouped by registration number, then by trial name.
"""
import collections, json, os, re, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
LIB = "/home/user/library/books/breast-cancer"

TRIAL_PT = {"Randomized Controlled Trial", "Clinical Trial", "Clinical Trial, Phase I", "Clinical Trial, Phase II",
            "Clinical Trial, Phase III", "Clinical Trial, Phase IV", "Controlled Clinical Trial", "Multicenter Study",
            "Pragmatic Clinical Trial", "Equivalence Trial", "Adaptive Clinical Trial"}
NOT_PRIMARY = {"Review", "Systematic Review", "Meta-Analysis", "Practice Guideline", "Guideline", "Editorial",
               "Comment", "News", "Consensus Development Conference"}
REGID = re.compile(r"\b(NCT\d{8}|ISRCTN\d{8})\b")


def norm(s):
    return re.sub(r"[^A-Z0-9]", "", str(s).upper())


def registry():
    t = yaml.safe_load(open(os.path.join(LIB, "trials.yaml")))["trials"]
    r = yaml.safe_load(open(os.path.join(LIB, "references.yaml")))["refs"]
    pmid2trial, regid2trial, name2trial = {}, {}, {}
    for key, ref in r.items():
        if ref.get("pmid") and ref.get("trial"):
            pmid2trial[str(ref["pmid"])] = ref["trial"]
    for k, v in t.items():
        for p in v.get("pubs") or []:
            pm = (r.get(p.get("ref")) or {}).get("pmid")
            if pm:
                pmid2trial.setdefault(str(pm), k)
        for rid in REGID.findall(json.dumps(v, default=str)):
            regid2trial.setdefault(rid, k)
        for nm in [v.get("acronym"), k]:
            n = norm(nm)
            if len(n) >= 4:
                name2trial.setdefault(n, k)
        # the acronym's first word or bracketed core, e.g. "GeparQuinto / GBG 44" -> GEPARQUINTO, GBG44
        for part in re.split(r"[/(),]", str(v.get("acronym") or "")):
            n = norm(part)
            if len(n) >= 4 and not n.isdigit():
                name2trial.setdefault(n, k)
    allref_pmids = {str(x.get("pmid")) for x in r.values() if x.get("pmid")}
    return t, pmid2trial, regid2trial, name2trial, allref_pmids


NAME_PAT = re.compile(r"\(([A-Za-z][A-Za-z0-9 \-/\.]{2,40})\)|\b([A-Z][A-Za-z]*[-\s]?[A-Z0-9][A-Za-z0-9\-]{1,20})\b")


def names_in(title):
    out = set()
    for m in NAME_PAT.finditer(title):
        s = m.group(1) or m.group(2)
        for piece in re.split(r"[;,]| and ", s):
            n = norm(piece)
            if 4 <= len(n) <= 30 and re.search(r"[A-Z]{2}", n):
                out.add(n)
    return out


def main():
    t, pmid2trial, regid2trial, name2trial, allref = registry()
    papers = [json.loads(l) for l in open(os.path.join(DATA, "papers.jsonl"))]
    stats = collections.Counter()
    uncovered = []
    for p in papers:
        pt = set(p["ptypes"])
        breast = any("Breast" in m for m in p["mesh"]) or "breast" in (p["title"] + p["abstract"]).lower()
        is_trial = bool(pt & TRIAL_PT) and not (pt & NOT_PRIMARY)
        if not is_trial:
            stats["not a trial report"] += 1
            continue
        if not breast:
            stats["not breast"] += 1
            continue
        if p["pmid"] in pmid2trial:
            stats["covered: pmid"] += 1
            continue
        hit = [regid2trial[x] for x in p["nct"] + p["isrctn"] if x in regid2trial]
        if hit:
            stats["covered: registration number"] += 1
            continue
        nm = [name2trial[n] for n in names_in(p["title"]) if n in name2trial]
        if nm:
            stats["covered: trial name"] += 1
            continue
        stats["uncovered"] += 1
        uncovered.append(p)
    groups = collections.OrderedDict()
    for p in sorted(uncovered, key=lambda x: x["year"]):
        ids = p["nct"] + p["isrctn"]
        if ids:
            gk = ids[0]
        else:
            nms = sorted(names_in(p["title"]))
            gk = "name:" + nms[0] if nms else "pmid:" + p["pmid"]
        groups.setdefault(gk, []).append(p)
    # merge name groups into registration-number groups that share a name
    cands = []
    for gk, ps in groups.items():
        src = sorted({s.split(":")[0] for x in ps for s in x["sources"]})
        cands.append({"group": gk, "n_papers": len(ps), "sources": src,
                      "phase3": any("Phase III" in " ".join(x["ptypes"]) or re.search(r"phase (3|III)\b", x["title"] + " " + x["abstract"], re.I) for x in ps),
                      "randomised": any("Randomized Controlled Trial" in x["ptypes"] for x in ps),
                      "papers": [{k: x[k] for k in ("pmid", "year", "journal", "title", "ptypes", "nct", "isrctn", "sources", "doi")} for x in ps]})
    json.dump(cands, open(os.path.join(DATA, "candidates.json"), "w"), indent=1, ensure_ascii=False)
    print("papers:", len(papers))
    for k, v in stats.most_common():
        print("  %-32s %d" % (k, v))
    print("candidate groups:", len(cands))
    by = collections.Counter()
    for c in cands:
        by[("guideline/nccn" if any(s in ("guideline", "nccn") for s in c["sources"]) else "pubmed only",
            "phase3" if c["phase3"] else "other", "rct" if c["randomised"] else "not-rct")] += 1
    for k, v in sorted(by.items()):
        print("  ", k, v)


if __name__ == "__main__":
    main()
