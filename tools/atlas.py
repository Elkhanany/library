#!/usr/bin/env python3
"""
Build the atlas dataset from The Long Argument's landing page.

The Ages of Thought is a second reading of the same material -- the same
people, the same lines between them -- so its data is derived rather than
retyped. Retyping 117 records to change how they are drawn would be a way of
introducing errors into work that has already been audited.

    python3 tools/atlas.py

Writes books/the-ages-of-thought/src/data/atlas.json and prints what it found.
"""
import html
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library

SRC = os.path.join(library.BOOKS, "the-long-argument", "src", "_landing.html")
OUT = os.path.join(library.BOOKS, "the-ages-of-thought", "src", "data", "atlas.json")
WEIGHTS = os.path.join(library.BOOKS, "the-ages-of-thought", "weights.json")

# How much a thinker moved the argument, banded for the chart's vertical axis.
# The bands are only a coarsening of the same number: they decide how large a
# card is drawn and which stripe it sits in, and nothing else.
BANDS = [(80, 1), (62, 2), (42, 3), (0, 4)]


def band_of(w):
    for lo, b in BANDS:
        if w >= lo:
            return b
    return 4


def block(text, start, end):
    """The source is a hand-written literal, not JSON. Slice it by markers and
    let a tolerant parser do the rest -- a real JS parser here would be a
    dependency for one file that changes once a year."""
    i = text.index(start)
    j = text.index(end, i)
    return text[i + len(start):j]


def span_to(text, i, opener, closer):
    """From the opener at or after i, return the text up to its match."""
    depth, j, instr, esc = 0, i, False, False
    while j < len(text):
        c = text[j]
        if instr:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                instr = False
        elif c == '"':
            instr = True
        elif c == opener:
            depth += 1
        elif c == closer:
            depth -= 1
            if depth == 0:
                return text[i:j]
        j += 1
    raise ValueError("unbalanced %s from %d" % (opener, i))


def people_source(text):
    """P is not one literal. It is `const P = [ ... ]` followed by eight
    `P.push( ... )` calls, one per tradition, and an earlier version of this
    script read only the first and silently produced a book with eighteen
    philosophers in it. Collect every one of them."""
    parts = [span_to(text, text.index("const P = [") + len("const P = "), "[", "]")]
    for m in re.finditer(r"\bP\.push\(", text):
        parts.append(span_to(text, m.end() - 1, "(", ")"))
    return "\n".join(parts)


def js_array_of_objects(src):
    """Parse `{a:1,b:"x"},{...}` into dicts. Handles nested arrays and objects,
    strings with escaped quotes, and unquoted keys. Deliberately narrow: it
    understands exactly the subset this one file is written in."""
    out, i, n = [], 0, len(src)
    while i < n:
        while i < n and src[i] != "{":
            i += 1
        if i >= n:
            break
        depth, j, instr, esc = 0, i, False, False
        while j < n:
            c = src[j]
            if instr:
                if esc:
                    esc = False
                elif c == "\\":
                    esc = True
                elif c == '"':
                    instr = False
            elif c == '"':
                instr = True
            elif c == "{" or c == "[":
                depth += 1
            elif c == "}" or c == "]":
                depth -= 1
                if depth == 0 and c == "}":
                    j += 1
                    break
            j += 1
        out.append(json_ish(src[i:j]))
        i = j
    return out


def json_ish(t):
    """Quote the bare keys, then hand it to the JSON parser.

    Scanned character by character rather than by regex, because the prose in
    these records contains things like `<em>Haecceitas</em>, thisness:` and a
    regex for "identifier before a colon" happily rewrites that into a key,
    corrupting the sentence and then failing to parse. Only text outside a
    string literal is eligible."""
    out, i, n, instr, esc = [], 0, len(t), False, False
    while i < n:
        c = t[i]
        if instr:
            out.append(c)
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                instr = False
            i += 1
            continue
        if c == '"':
            instr = True
            out.append(c)
            i += 1
            continue
        m = re.match(r"([A-Za-z_][A-Za-z0-9_]*)(\s*):", t[i:])
        if m and (not out or out[-1].strip() in ("", "{", ",", "[")
                  or "".join(out).rstrip()[-1:] in "{,"):
            out.append('"%s"%s:' % (m.group(1), m.group(2)))
            i += m.end()
            continue
        out.append(c)
        i += 1
    t = "".join(out)
    t = re.sub(r",(\s*[}\]])", r"\1", t)
    return json.loads(t)


def main():
    s = library.read(SRC)

    people = js_array_of_objects(people_source(s))
    eras = js_array_of_objects(block(s, "const ERAS = [", "\n];"))
    # ED is a JSON array once it is wrapped in brackets. An earlier version of
    # this script matched entries with a regex that allowed exactly two or
    # three strings, and thirty-seven of the hundred and eighty-three carry a
    # fourth: a sentence about the edge. Those thirty-seven were dropped
    # without a word, and among them was Plato teaching Aristotle. The notes
    # are the only per-edge prose in the dataset, so they are kept.
    ed_src = block(s, "const ED = [", "\n];")
    edges = []
    for e in json.loads("[" + ed_src + "]"):
        d = {"f": e[0], "t": e[1], "k": e[2] if len(e) > 2 else "read"}
        if len(e) > 3 and e[3]:
            d["note"] = html.unescape(e[3])
        edges.append(d)
    if len(edges) < 180:
        raise SystemExit("atlas: only %d edges parsed; the source has over 180" % len(edges))
    tr = json_ish("{" + block(s, "const TR = {", "\n};") + "}")

    if len(people) != len(set(p["id"] for p in people)):
        raise SystemExit("atlas: duplicate ids in P -- the push blocks overlap")
    if len(people) < 100:
        raise SystemExit("atlas: only %d people parsed; P is split across "
                         "blocks and one of them was missed" % len(people))

    ids = set(p["id"] for p in people)
    dropped = [e for e in edges if e["f"] not in ids or e["t"] not in ids]
    edges = [e for e in edges if e["f"] in ids and e["t"] in ids]

    # An epoch owns whoever died inside it, which puts a philosopher in the age
    # his work belongs to rather than the one he was born into. Plato is
    # classical, not archaic.
    def epoch_of(p):
        y = p.get("d", p.get("fl", p.get("b")))
        for i, e in enumerate(eras):
            if e["a"] <= y < e["b"]:
                return i
        return len(eras) - 1 if y >= eras[-1]["a"] else 0

    # The source writes accented letters as HTML entities, because it is an
    # HTML file. This is a JSON file read by script, so `Ren&eacute; Descartes`
    # would be drawn on a card exactly like that. Decode them, and check first
    # that no field escapes a real angle bracket -- the prose carries literal
    # <em> tags that must survive, and an `&lt;` decoded into `<` would turn
    # a quoted symbol into markup.
    def txt(v):
        if isinstance(v, list):
            return [txt(x) for x in v]
        if isinstance(v, dict):
            return {k: txt(x) for k, x in v.items()}
        if isinstance(v, str):
            if "&lt;" in v or "&gt;" in v:
                raise SystemExit("atlas: %r escapes an angle bracket; decoding "
                                 "it here would create markup" % v[:60])
            return html.unescape(v)
        return v

    weights = json.loads(library.read(WEIGHTS))["weights"]
    ids_here = set(p["id"] for p in people)
    missing = sorted(ids_here - set(weights))
    unknown = sorted(set(weights) - ids_here)
    if missing:
        raise SystemExit("atlas: %d thinker(s) have no weight: %s"
                         % (len(missing), ", ".join(missing[:8])))
    if unknown:
        raise SystemExit("atlas: weights.json names %d id(s) that are not in the "
                         "book: %s" % (len(unknown), ", ".join(unknown[:8])))
    bad = [k for k, v in weights.items() if not isinstance(v, int) or not 0 <= v <= 100]
    if bad:
        raise SystemExit("atlas: weight out of 0-100: %s" % ", ".join(sorted(bad)[:8]))

    out_people = []
    for p in people:
        p = txt(p)
        out_people.append({
            "id": p["id"], "n": p["n"], "b": p["b"], "d": p["d"],
            "cb": p.get("cb", 0), "cd": p.get("cd", 0), "fl": p.get("fl"),
            "ti": p.get("ti", 4), "tr": p["tr"], "sch": p.get("sch", ""),
            "pl": p.get("pl", ""), "one": p.get("one", ""),
            "ideas": p.get("ideas", []), "works": p.get("works", []),
            "q": p.get("q"), "ep": epoch_of(p),
            "w": weights[p["id"]],
        })
    # Rank is the order the slider fills the map in: the heaviest first, and
    # ties broken by who came earlier, so the same drag always shows the same
    # people in the same order.
    by_weight = sorted(out_people, key=lambda p: (-p["w"], p["b"], p["id"]))
    for i, p in enumerate(by_weight):
        p["r"] = i + 1
        p["bd"] = band_of(p["w"])
    out_people.sort(key=lambda p: (p["b"], p["d"]))

    counts = {}
    for p in out_people:
        counts[p["ep"]] = counts.get(p["ep"], 0) + 1

    data = {
        "epochs": [{"a": e["a"], "b": e["b"], "n": e["n"], "d": e["d"],
                    "n_all": counts.get(i, 0)} for i, e in enumerate(eras)],
        "traditions": {k: {"n": library.plain(v["n"]), "full": library.plain(v["full"])}
                       for k, v in tr.items()},
        "people": out_people,
        "edges": edges,
    }
    library.write(OUT, json.dumps(data, ensure_ascii=False, separators=(",", ":")))

    bands = {}
    for p in out_people:
        bands[p["bd"]] = bands.get(p["bd"], 0) + 1
    top = sorted(out_people, key=lambda p: p["r"])[:6]
    six = [p["n"] for p in out_people if p["ti"] == 1]
    kinds = {}
    for e in edges:
        kinds[e["k"]] = kinds.get(e["k"], 0) + 1
    noted = sum(1 for e in edges if e.get("note"))
    print("atlas: %d people, %d edges (%d with a note), %d epochs"
          % (len(out_people), len(edges), noted, len(eras)))
    print("  heaviest: " + ", ".join("%s %d" % (p["n"], p["w"]) for p in top))
    print("  bands: " + " ".join("%d:%d" % (b, bands[b]) for b in sorted(bands)))
    print("  old tier 1: " + ", ".join(six))
    print("  edges: " + ", ".join("%s %d" % (k, v) for k, v in sorted(kinds.items())))
    print("  people per epoch: " + " ".join(str(counts.get(i, 0)) for i in range(len(eras))))
    if dropped:
        print("  DROPPED %d edge(s) naming someone not in P: %s" % (len(dropped), dropped[:4]))
    print("  -> %s (%.0f KB)" % (os.path.relpath(OUT, library.ROOT),
                                 os.path.getsize(OUT) / 1024.0))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
