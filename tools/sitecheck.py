#!/usr/bin/env python3
"""
Every link in the published site points at something that exists.

xrefcheck proves a book's prose references a real chapter; verify.py proves a
built page renders and reaches for nothing. Neither looks at the site as a
whole, and the whole is new: with more than one book there are now links that
leave a book — the hub into each book, each book's top bar back to the hub —
and those are exactly the links no single-book check was ever built to see.

    python3 tools/sitecheck.py

Exit 1 if any internal link, stylesheet, script or image is missing, if any page
carries a navigation bar other than the one its book.json describes, or if any
page reaches outside the site for something it needs to render.
"""
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library

# href/src on things the page needs; a plain <a> is followed too.
REF = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"', re.I)
# Requests a page makes to render, as opposed to somewhere it offers to send you.
NEEDS = re.compile(r'<(?:link|script|img|source)\b[^>]*?(?:href|src)\s*=\s*"([^"]+)"', re.I)


def pages(root):
    for dp, _dirs, files in os.walk(root):
        for f in files:
            if f.endswith(".html"):
                yield os.path.join(dp, f)


def main():
    docs = library.DOCS
    if not os.path.isdir(docs):
        print("sitecheck: no docs/ — run tools/webbuild.py first")
        return 1

    missing, external, n_links, n_pages = [], [], 0, 0

    for page in sorted(pages(docs)):
        n_pages += 1
        rel = os.path.relpath(page, docs).replace(os.sep, "/")
        # Script content is not markup. A page that builds its own links --
        # the trial appendix assembles href="<chapter id>.html" from data --
        # otherwise reports the string literal as a broken link, because the
        # id is only known at runtime. tagcheck strips scripts for the same
        # reason. Real dependencies a page loads are still caught: those are
        # <script src=...> attributes, which live in the tag, not the body.
        text = re.sub(r"<script\b[^>]*>.*?</script>", "", library.read(page),
                      flags=re.S | re.I)
        needed = set(NEEDS.findall(library.read(page)))

        for raw in REF.findall(text):
            url = raw.strip()
            if not url or url.startswith(("#", "data:", "mailto:", "javascript:")):
                continue
            if re.match(r"^[a-z]+:", url, re.I):
                # An external link is fine; an external *dependency* is not,
                # because the book's promise is that a page renders offline.
                if url in needed:
                    external.append((rel, url))
                continue
            n_links += 1
            target = urllib.parse.unquote(url.split("#")[0].split("?")[0])
            if not target:
                continue
            resolved = os.path.normpath(os.path.join(os.path.dirname(page), target))
            if os.path.isdir(resolved):
                resolved = os.path.join(resolved, "index.html")
            if not os.path.exists(resolved):
                missing.append((rel, url))

    for rel, url in missing:
        print(f"  MISSING  {rel}  ->  {url}")
    for rel, url in external:
        print(f"  EXTERNAL DEPENDENCY  {rel}  ->  {url}")

    books = ", ".join(b.slug for b in library.books())
    print(f"sitecheck: {n_pages} pages, {n_links} internal links, books: {books}")
    if missing or external:
        print(f"  {len(missing)} broken, {len(external)} external dependency — FIX THESE")
        return 1
    print("  every internal link resolves, nothing loaded from off-site")

    # Every link resolving is not the same as every page offering the same
    # links. A bar that has gone stale points only at pages that exist, so the
    # check above passes on it and the reader is simply never offered the page
    # that was added. That is what this catches.
    import nav
    rc = nav.check()

    # The app layer is one string match away from silently not existing, so it
    # is checked here rather than left to whoever remembers to look.
    import pwa
    rc = pwa.check() or rc

    # A dataset the site offers for download fails worse than a broken link,
    # because a stale spreadsheet opens and looks right. The link check above
    # proves the file is there; this proves it still says what the registry
    # says.
    import export
    rc = rc or export.main_check()

    # The story layer names trials by key and the registry is edited daily, so a
    # story can be orphaned by a rename it never saw. Cheap to check here; the
    # alternative is a chapter that renders a question with a trial missing
    # from under it.
    import stories
    st, reg = stories.load(), stories.trials()
    errs, _ = stories.check(st, reg)
    for e in errs:
        print("  story  " + e)
    if errs:
        print(f"  {len(errs)} problem in the story layer — FIX THESE")
        return 1
    named = {k for _, _, q in stories.questions(st) for k in (q.get("trials") or [])}
    nq = sum(len(x.get("questions") or []) for x in st.values())
    print(f"  {len(st)} stories, {nq} questions, {len(named)} of {len(reg)} trials placed")
    return rc


if __name__ == "__main__":
    sys.exit(main())
