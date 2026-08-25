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
    # the landing page is a whole document rather than a fragment
    "html","head","body","title","meta","link","section","footer","header","nav","main","article",
}

# Elements this book always closes explicitly. HTML5 lets you omit </p>, </li> and </td>, and the
# parser recovers silently, so an unclosed one renders correctly and no rendered-page audit can see
# it. One had been sitting in Chapter 2.6's §5 grind box since it was written. Counting opens against
# closes is cheap and catches it.
BALANCED = ("p", "div", "details", "summary", "ul", "ol", "li", "table", "tr", "td", "th",
            "figure", "figcaption", "h1", "h2", "h3", "h4", "em", "strong", "b", "i", "a", "span")


class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.bad = []
    def handle_starttag(self, tag, attrs):
        if tag not in KNOWN:
            self.bad.append((self.getpos()[0], tag))


# KaTeX macros here take a fixed number of braced arguments. Written with an
# optional argument — \dv[2]{u}{x} — KaTeX does not error; it takes "[" as the
# first argument and renders something wrong. Six of those were live in Chapter
# 3.7, one inside its boxed central equation, and no check saw them because
# nothing had failed. Use \dvn{2}{u}{x} and \pdvn.
OPTARG = re.compile(r"\\(dv|pdv|abs|norm|ket|bra|avg|vv)\[")


def optargs(t):
    """(line, snippet) for every macro used with an optional argument it has not got."""
    out = []
    for i, line in enumerate(t.split("\n"), 1):
        if OPTARG.search(line):
            out.append((i, line.strip()[:110]))
    return out


def unbalanced(t):
    """(tag, opens, closes) for every element whose counts disagree."""
    out = []
    for tag in BALANCED:
        o = len(re.findall(r"<" + tag + r"(?:\s[^>]*)?>", t))
        c = len(re.findall(r"</" + tag + r">", t))
        if o != c:
            out.append((tag, o, c))
    return out

def main(paths):
    total = unclosed = 0
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
        for tag, o, c in unbalanced(t):
            print(f"{f}:  <{tag}> {o} open / {c} close")
            unclosed += 1
        for ln, snip in optargs(t):
            print(f"{f}:  line {ln}: macro used with an optional argument  ::  {snip}")
            unclosed += 1
    n = len(list(paths))
    print(f"tagcheck: {n} files, {total} unescaped '<', {unclosed} unbalanced element(s) "
          + ("— FIX THESE" if total or unclosed else "— clean"))
    return 1 if (total or unclosed) else 0

if __name__ == "__main__":
    # Every fragment the build assembles, not just the chapters. The ledger carried a
    # stray </table> for six batches — it closed Part II's table after Chapter 2.4, so
    # every row from 2.5 on rendered outside the table — and nothing caught it because
    # this glob said ch*.html. The landing page and the through-line are assembled the
    # same way and were equally unwatched.
    sys.exit(main(sys.argv[1:] or sorted(glob.glob("src/*.html"))))
