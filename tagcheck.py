#!/usr/bin/env python3
"""Catch '<' that a browser reads as a tag but the author meant as "less than".

HTML5 opens a tag only when '<' is followed by an ASCII letter, so '$x<2$' is
harmless text and '$x<r$' silently swallows everything up to the next '>' —
which in this book means a lost sentence, a lost problem part, or a lost step
of an argument, with no error anywhere and nothing visibly wrong on the page.

Four such sites shipped in one chapter before this check existed. Run it as
part of every build; it costs milliseconds.
"""
import re, sys, glob
from html.parser import HTMLParser

KNOWN = {
    "a","b","p","i","em","strong","div","span","td","tr","th","table","tbody","thead","caption",
    "ul","ol","li","h1","h2","h3","h4","h5","details","summary","br","hr","code","pre","sup","sub",
    "figure","figcaption","canvas","script","style","small","blockquote","label","input","output",
    "button","select","option","img","svg","path","g","circle","line","rect","text","dl","dt","dd",
}

class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.bad = []
    def handle_starttag(self, tag, attrs):
        if tag not in KNOWN:
            self.bad.append((self.getpos()[0], tag))

def main(paths):
    total = 0
    for f in sorted(paths):
        raw = open(f, encoding="utf-8").read()
        # JavaScript legitimately contains < and >
        t = re.sub(r"<!--SCRIPT-->.*?<!--/SCRIPT-->", "", raw, flags=re.S)
        t = re.sub(r"<script\b.*?</script>", "", t, flags=re.S)
        s = Scan(); s.feed(t)
        if s.bad:
            lines = t.split("\n")
            print(f"{f}:")
            for ln, tag in s.bad:
                print(f"   line {ln}: <{tag}…  ::  {lines[ln-1].strip()[:120]}")
                total += 1
    print(f"tagcheck: {len(list(paths))} files, {total} unescaped '<' "
          + ("— FIX THESE" if total else "— clean"))
    return 1 if total else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or glob.glob("src/ch*.html")))
