#!/usr/bin/env python3
"""Apply a reviewed batch of registry updates to the clinical book: records, references, prose.

    python3 tools/registry_apply.py EDITS.json [--dry]

EDITS.json is a list of verified edits, one per trial, each shaped as

    {"key": "natalee", "verdict": "confirmed" | "corrected" | "rejected",
     "final": {
        "field_changes": [{"field": "os", "old": "...", "new": "...", "source_quote": "..."}],
        "pubs_add":      [{"kind": "survival", "ref": "slamon2026natalee", "role": "6-year OS"}],
        "new_refs_yaml": "  slamon2026natalee:\\n    authors: ...",       # references.yaml entries
        "new_record_yaml": "",                                           # a whole new trial, or empty
        "prose_edits":   [{"file": "chapters/BC-790.md", "quote": "...", "proposed": "..."}],
        "stories_named": ["SQ-0010"]}}

Nothing is guessed. A field is replaced only when the registry still holds the `old` value the
edit was reviewed against; a prose edit only when its quote occurs exactly once; a reference only
when neither its key nor its PMID is already in references.yaml; a record only when its key is new.
Everything else is reported and skipped. A dotted field (`digest.results`) edits one key of a
mapping, and a `new` of null removes the field (`tabulated` once a result is entered). A record whose fields change, and every new record, gets `reviewed` set to --date
(default today). A publication added on its own does not move `reviewed`, so that
`evidence.py --stale` keeps the trial on its worklist until the prose that cites it has been
read; an edit sets `"mark_reviewed": true` once that reading is done. Each story question in
`stories_named` is listed so it can be re-read before its own `reviewed` moves. A question in
`stories_reread` has been re-read, so its `reviewed` is set to --date, after every prose edit.

The registry is edited as text, field by field, so every record keeps the registry's own wrapping
and a diff shows only what changed. Data files are never edited by a prose edit.
"""
import datetime, json, os, re, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "books", "breast-cancer")
REG = os.path.join(BOOK, "trials.yaml")
REFS = os.path.join(BOOK, "references.yaml")
STORIES = os.path.join(BOOK, "stories.yaml")


def block(text, key):
    """The body of one record (or reference): the lines indented under '  key:'."""
    return re.search(r"^  %s:\n((?:    [^\n]*\n)*)" % re.escape(key), text, re.M)


def set_field(text, key, field, value):
    """Replace or insert one top-level field of a record, or remove it when value is None.
    Continuation lines are six-space lines and four-space list items, which is how
    yaml.safe_dump lays out this registry."""
    m = block(text, key)
    if not m:
        return text, "record not found"
    blk = m.group(1)
    f = re.search(r"^    %s:(?:[ \t][^\n]*)?\n(?:(?:      |    - )[^\n]*\n)*" % re.escape(field), blk, re.M)
    if value is None:
        if not f:
            return text, None
        return text[:m.start(1)] + blk[:f.start()] + blk[f.end():] + text[m.end(1):], None
    dumped = yaml.safe_dump({field: value}, allow_unicode=True, width=116, sort_keys=False)
    new = "".join("    " + ln + "\n" for ln in dumped.rstrip("\n").split("\n"))
    if f:
        nb = blk[:f.start()] + new + blk[f.end():]
    else:
        at = len(blk)
        for mm in re.finditer(r"^    ([a-z_]+):", blk, re.M):
            if mm.group(1) > field:
                at = mm.start()
                break
        nb = blk[:at] + new + blk[at:]
    return text[:m.start(1)] + nb + text[m.end(1):], None


def date_question(text, qid, today):
    """Set one story question's `reviewed`. A question is a list item whose keys sit six spaces in."""
    m = re.search(r"^      id: %s\n" % re.escape(qid), text, re.M)
    if not m:
        return text, "no story question %s" % qid
    start = text.rfind("\n    - ", 0, m.start()) + 1
    nxt = re.search(r"^(?!      |        )", text[m.end():], re.M)
    end = m.end() + (nxt.start() if nxt else len(text) - m.end())
    blk, k = re.subn(r"^      reviewed: [^\n]*$", "      reviewed: %s" % today, text[start:end], count=1, flags=re.M)
    if not k:
        return text, "story question %s has no reviewed line" % qid
    return text[:start] + blk + text[end:], None


def current(text, key):
    m = block(text, key)
    return yaml.safe_load("x:\n" + m.group(1))["x"] if m else None


def same(a, b):
    def norm(v):
        if isinstance(v, bool):
            v = "true" if v else "false"          # as YAML writes it, which is what an edit copies
        return " ".join(str(v if v is not None else "").strip("'\"").split())
    return norm(a) == norm(b)


def insert_sorted(text, entry_text, key, pattern):
    """Put a new top-level entry before the first existing key that sorts after it."""
    keys = [(mm.group(1), mm.start()) for mm in re.finditer(pattern, text, re.M)]
    at = next((pos for k, pos in keys if k > key), len(text))
    return text[:at] + entry_text + text[at:]


def dump_entry(key, value):
    dumped = yaml.safe_dump({key: value}, allow_unicode=True, width=116, sort_keys=True)
    return "".join("  " + ln + "\n" for ln in dumped.rstrip("\n").split("\n"))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv
    today = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--date=")),
                 datetime.date.today().isoformat())
    edits = json.load(open(args[0]))
    reg, refs = open(REG, encoding="utf-8").read(), open(REFS, encoding="utf-8").read()
    ref_data = yaml.safe_load(refs)["refs"]
    pmids = {str(v.get("pmid")): k for k, v in ref_data.items() if v.get("pmid")}
    files, log, bad, stories, reread = {}, [], [], {}, set()
    for e in edits:
        if not e or e.get("verdict") == "rejected":
            continue
        k, f = e["key"], e["final"]
        # references first, so a new record or a pubs entry can name them
        if (f.get("new_refs_yaml") or "").strip():
            for rk, rv in (yaml.safe_load("refs:\n" + f["new_refs_yaml"])["refs"] or {}).items():
                if rk in ref_data:
                    bad.append((k, "reference key %s already exists" % rk)); continue
                if rv.get("pmid") and str(rv["pmid"]) in pmids:
                    bad.append((k, "PMID %s is already %s" % (rv["pmid"], pmids[str(rv["pmid"])]))); continue
                refs = insert_sorted(refs, dump_entry(rk, rv), rk, r"^  ([^ :\n][^:\n]*):\n")
                ref_data[rk] = rv
                if rv.get("pmid"):
                    pmids[str(rv["pmid"])] = rk
                log.append("%-16s + reference %s%s" % (k, rk, " (PMID %s)" % rv["pmid"] if rv.get("pmid") else " (conference)"))
        is_new = bool((f.get("new_record_yaml") or "").strip())
        if is_new:
            for nk, nv in (yaml.safe_load("trials:\n" + f["new_record_yaml"])["trials"] or {}).items():
                if block(reg, nk):
                    bad.append((k, "record %s already exists" % nk)); continue
                for p in nv.get("pubs") or []:
                    if p.get("ref") not in ref_data:
                        bad.append((nk, "pubs names %s, which is not in references.yaml" % p.get("ref")))
                nv.setdefault("reviewed", today)
                reg = insert_sorted(reg, dump_entry(nk, nv), nk, r"^  ([a-z0-9][^:\n]*):\n")
                log.append("%-16s + new record" % nk)
        t = current(reg, k)
        if t is None:
            bad.append((k, "not in the registry")); continue
        changed = is_new or bool(f.get("mark_reviewed"))
        for c in ([] if is_new else f.get("field_changes") or []):
            fld, val = c["field"], c["new"]
            top, _, sub = fld.partition(".")
            if top == "reviewed":
                continue                      # set below, once, from --date
            now = (t.get(top) or {}).get(sub) if sub else t.get(top)
            if c.get("old") not in (None, "", "None") and not same(now, c["old"]):
                bad.append((k, "%s: registry holds %r, the edit was reviewed against %r"
                            % (fld, str(now)[:70], str(c["old"])[:70]))); continue
            if val is not None and top in ("n", "year") and str(val).isdigit():
                val = int(val)
            if sub:
                d = dict(t.get(top) or {}); d[sub] = val; val, fld = d, top
            reg, err = set_field(reg, k, fld, val)
            if err:
                bad.append((k, err)); continue
            t, changed = current(reg, k), True
            log.append("%-16s %s" % (k, c["field"]))
        if f.get("pubs_add") and not is_new:
            pubs, have = list(t.get("pubs") or []), {p.get("ref") for p in t.get("pubs") or []}
            for p in f["pubs_add"]:
                if p["ref"] not in ref_data:
                    bad.append((k, "pub %s has no reference" % p["ref"])); continue
                if p["ref"] in have:
                    continue
                pubs.append({"added": today, "kind": p["kind"], "ref": p["ref"], "role": p["role"]})
                log.append("%-16s + pub %s" % (k, p["ref"]))
            reg, err = set_field(reg, k, "pubs", pubs)
            if err:
                bad.append((k, err))
        if changed and not is_new:
            reg, _ = set_field(reg, k, "reviewed", today)
        for e2 in f.get("prose_edits") or []:
            fn = e2["file"]
            if not fn.startswith("/"):
                fn = os.path.join(ROOT if fn.startswith("books/") else BOOK, fn)
            if os.path.abspath(fn) in (REG, REFS):
                bad.append((k, "a prose edit may not touch a data file: %s" % e2["file"])); continue
            if not os.path.exists(fn):
                bad.append((k, "no such file %s" % e2["file"])); continue
            s = files.setdefault(fn, open(fn, encoding="utf-8").read())
            n = s.count(e2["quote"])
            if n != 1:
                bad.append((k, "%s: quote found %d times: %s" % (os.path.basename(fn), n, e2["quote"][:60]))); continue
            files[fn] = s.replace(e2["quote"], e2["proposed"])
            log.append("%-16s prose %s" % (k, os.path.relpath(fn, BOOK)))
        for q in f.get("stories_named") or []:
            stories.setdefault(q, []).append(k)
        for q in f.get("stories_reread") or []:
            reread.add(q)
    if reread:
        st = files.setdefault(STORIES, open(STORIES, encoding="utf-8").read())
        for q in sorted(reread):
            st, err = date_question(st, q, today)
            if err:
                bad.append(("stories", err))
            else:
                log.append("%-16s reviewed %s" % (q, today))
        files[STORIES] = st
        yaml.safe_load(st)
    yaml.safe_load(reg), yaml.safe_load(refs)        # both must still parse
    for line in log:
        print(line)
    for b in bad:
        print("SKIPPED", *b)
    if stories:
        print("story questions to re-read:", ", ".join("%s (%s)" % (q, "/".join(v)) for q, v in sorted(stories.items())))
    if dry:
        print("dry run: nothing written")
        return 1 if bad else 0
    open(REG, "w", encoding="utf-8").write(reg)
    open(REFS, "w", encoding="utf-8").write(refs)
    for fn, s in files.items():
        open(fn, "w", encoding="utf-8").write(s)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
