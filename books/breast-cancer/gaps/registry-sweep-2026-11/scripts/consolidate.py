"""Merge the triage outputs into one list of trials to add, removing duplicates across chunks.

    python3 consolidate.py      # writes ../data/to-add.json and ../data/triage-summary.json

Two "add" entries are the same trial when they share a registration number, a PMID, or a normalised
name. An "add" whose registration number or PMID the registry already holds is dropped as "exists".
"""
import collections, glob, json, os, re
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
TRI = os.path.join(HERE, "..", "triage")
DATA = os.path.join(HERE, "..", "data")
LIB = "/home/user/library/books/breast-cancer"


def norm(s):
    return re.sub(r"[^A-Z0-9]", "", str(s or "").upper())


def main():
    t = yaml.safe_load(open(os.path.join(LIB, "trials.yaml")))["trials"]
    r = yaml.safe_load(open(os.path.join(LIB, "references.yaml")))["refs"]
    reg_ids = set(re.findall(r"\b(?:NCT|ISRCTN)\d{8}\b", json.dumps(t, default=str)))
    reg_pmids = {str(v.get("pmid")) for v in r.values() if v.get("pmid") and v.get("trial")}
    entries, counts = [], collections.Counter()
    pmid_seen = collections.Counter()
    for f in sorted(glob.glob(os.path.join(TRI, "out-*.json"))):
        for e in json.load(open(f)):
            e["_chunk"] = os.path.basename(f)
            counts[e.get("decision")] += 1
            for p in e.get("pmids") or []:
                pmid_seen[p] += 1
            entries.append(e)
    adds = [e for e in entries if e.get("decision") == "add"]
    # union-find over adds
    parent = list(range(len(adds)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    keymap = {}
    for i, e in enumerate(adds):
        keys = set()
        if e.get("nct"):
            keys |= {"id:" + x for x in re.findall(r"(?:NCT|ISRCTN)\d{8}", e["nct"])}
        for p in (e.get("pmids") or []) + (e.get("other_pmids_found") or []) + [e.get("primary_pmid")]:
            if p:
                keys.add("pm:" + str(p))
        n = norm(e.get("name"))
        if len(n) >= 5:
            keys.add("nm:" + n)
        for k in keys:
            if k in keymap:
                parent[find(i)] = find(keymap[k])
            else:
                keymap[k] = i
    merged = collections.defaultdict(list)
    for i in range(len(adds)):
        merged[find(i)].append(adds[i])
    out, dropped = [], []
    for grp in merged.values():
        e = dict(grp[0])
        e["pmids"] = sorted({p for g in grp for p in (g.get("pmids") or [])})
        e["other_pmids_found"] = sorted({p for g in grp for p in (g.get("other_pmids_found") or [])})
        e["names_seen"] = sorted({g.get("name") for g in grp})
        e["guideline_cited"] = any(g.get("guideline_cited") for g in grp)
        e["chunks"] = sorted({g["_chunk"] for g in grp})
        ids = set(re.findall(r"(?:NCT|ISRCTN)\d{8}", " ".join(str(g.get("nct") or "") for g in grp)))
        if ids & reg_ids or (set(e["pmids"]) | set(e["other_pmids_found"]) | {str(e.get("primary_pmid"))}) & reg_pmids:
            dropped.append({"name": e.get("name"), "why": "registry already holds its registration number or PMID"})
            continue
        out.append(e)
    out.sort(key=lambda x: (not x["guideline_cited"], str(x.get("setting")), str(x.get("name"))))
    json.dump(out, open(os.path.join(DATA, "to-add.json"), "w"), indent=1, ensure_ascii=False)
    summary = {"decisions": counts, "add_entries": len(adds), "add_trials_after_merge": len(out),
               "dropped_as_existing": dropped, "pmids_in_more_than_one_entry": [p for p, c in pmid_seen.items() if c > 1]}
    json.dump(summary, open(os.path.join(DATA, "triage-summary.json"), "w"), indent=1, default=list)
    print(json.dumps({k: v for k, v in summary.items() if k != "pmids_in_more_than_one_entry"}, indent=1, default=list)[:3000])
    print("pmids in more than one entry:", len(summary["pmids_in_more_than_one_entry"]))
    by = collections.Counter((x["guideline_cited"], str(x.get("setting")), str(x.get("phase"))) for x in out)
    for k, v in by.most_common(25):
        print("  ", k, v)


if __name__ == "__main__":
    main()
