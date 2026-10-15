#!/usr/bin/env python3
"""
Every link in the published site points at something that exists.

xrefcheck proves a book's prose references a real chapter; verify.py proves a
built page renders and reaches for nothing. Neither looks at the site as a
whole, and the whole is new: with more than one book there are now links that
leave a book — the hub into each book, each book's top bar back to the hub —
and those are exactly the links no single-book check was ever built to see.

    python3 tools/sitecheck.py
    python3 tools/sitecheck.py --build <slug>     # the Dropbox build, build/<slug>/

Exit 1 if any internal link, stylesheet, script or image is missing, if any
same-site link names a #fragment its page does not carry, if any page carries
a navigation bar other than the one its book.json describes, if any page
reaches outside the site for something it needs to render, or if a page served
at any address is missing or links relatively.

Two kinds of link a relative resolver used to get wrong or skip:

- A link that starts with library.SITE ('/', the root of the Cloudflare Pages
  domain; '/library/' under GitHub Pages) is where the host serves docs/, so it
  resolves against docs/. Resolved as a file path it pointed at the root of
  the filesystem and was reported missing.
- A link with a #fragment -- contents.html#sec-N, trials.html#t-<key>, the
  Stories page's #SQ- and #r- links, and in-page links like #sec-3 -- names an
  id the target page must carry. Hash routes that hold '=' (#who=, #study=)
  are addresses for a script, not ids, and are skipped. Ids and links built by
  a page's own scripts at runtime are invisible here, as they always were.
  KNOWN_FRAGMENTS lists the ones missing today; it must not grow.

Two pages are served at an address that is not their own, so a relative link
on either resolves against wherever the reader was rather than against docs/,
and every internal link on them must start with library.SITE. offline.html is
what the service worker gives for a page it never stored. 404.html is what
Cloudflare Pages gives, with status 404, for any address that has no file, at
any depth; it must also exist, because without it Pages treats the site as a
single-page app and answers a missing address with the hub and status 200,
which the worker and the book download then store as the page asked for.

--build <slug> runs the same resolver over build/<slug>/*.html, the self-
contained pages make.py writes for Dropbox, ignoring external links. That tree
has no bar, no appendices and index.html for its contents page, so a link that
works on the site can be dead there. KNOWN_BUILD lists today's dead targets
per book; anything else fails.
"""
import html as htmlmod
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
# What a #fragment can land on: any id, or the old <a name>.
IDS = re.compile(r'(?<![-\w])id\s*=\s*"([^"]*)"', re.I)
NAMES = re.compile(r'<a\b[^>]*?(?<![-\w])name\s*=\s*"([^"]*)"', re.I)
SCRIPT = re.compile(r"<script\b[^>]*>.*?</script>", re.S | re.I)

# Fragments that name no id today, measured on the tree wave 0 started from.
# (page, href) -> why. This list must not grow: a new missing fragment fails.
# An entry that resolves again is reported so it can be deleted.
KNOWN_FRAGMENTS = {
    ('the-long-argument/index.html', '#tab-thinkers'):
        "the timeline's 'read these thinkers as a list' skip link; its click "
        "handler switches tabs through data-goto, and no element carries the id",
}

# Dead targets in the Dropbox build, measured on the tree wave 0 started from.
# slug -> {target file relative to build/<slug>/: why}. A missing link whose
# target is listed here is known; any other fails.
KNOWN_BUILD = {
    'breast-cancer': {},
    'newton-to-mtheory': {},
}


# Pages served at an address that is not their own (see the module docstring).
ANYWHERE = ("offline.html", "404.html")


def anywhere(docs):
    """(page, problem) for each page in ANYWHERE that is missing, or that has
    an internal link not absolute from library.SITE."""
    bad = []
    for rel in ANYWHERE:
        p = os.path.join(docs, rel)
        if not os.path.exists(p):
            bad.append((rel, None))
            continue
        for raw in REF.findall(SCRIPT.sub("", library.read(p))):
            url = raw.strip()
            if not url or url.startswith(("#", "data:", "mailto:", "javascript:", "//")) \
                    or re.match(r"^[a-z][a-z0-9+.-]*:", url, re.I):
                continue            # in-page, or not a path on this site
            if not url.startswith(library.SITE):
                bad.append((rel, url))
    return bad


def pages(root):
    for dp, _dirs, files in os.walk(root):
        for f in files:
            if f.endswith(".html"):
                yield os.path.join(dp, f)


_ids = {}


def ids_of(path):
    """Every id (and <a name>) a page carries in its markup, scripts excluded."""
    if path not in _ids:
        text = SCRIPT.sub("", library.read(path))
        _ids[path] = ({htmlmod.unescape(x) for x in IDS.findall(text)}
                      | {htmlmod.unescape(x) for x in NAMES.findall(text)})
    return _ids[path]


def resolve(page, url, site_root):
    """(file, fragment) for an internal url. site_root is where library.SITE is
    served from (docs/), or None where there is no site (the Dropbox build): a
    link absolute from library.SITE then resolves to a file that does not
    exist, which is the truth about it on a phone opening a file from Dropbox."""
    path, _, frag = url.partition("#")
    target = urllib.parse.unquote(path.split("?")[0])
    site = library.SITE
    if not target:
        resolved = page
    elif site_root is not None and (target == site.rstrip("/") or target.startswith(site)):
        resolved = os.path.normpath(os.path.join(site_root, target[len(site):]))
    else:
        resolved = os.path.normpath(os.path.join(os.path.dirname(page), target))
    if os.path.isdir(resolved):
        resolved = os.path.join(resolved, "index.html")
    return resolved, htmlmod.unescape(urllib.parse.unquote(frag))


def links(root, site_root, externals):
    """Walk every page under root. Returns (missing, external, frags, n_pages,
    n_links, n_frags): missing files, external dependencies (only when
    externals), and fragments whose page does not carry the id."""
    missing, external, frags = [], [], []
    n_links = n_pages = n_frags = 0
    for page in sorted(pages(root)):
        n_pages += 1
        rel = os.path.relpath(page, root).replace(os.sep, "/")
        # Script content is not markup. A page that builds its own links --
        # the trial appendix assembles href="<chapter id>.html" from data --
        # otherwise reports the string literal as a broken link, because the
        # id is only known at runtime. tagcheck strips scripts for the same
        # reason. Real dependencies a page loads are still caught: those are
        # <script src=...> attributes, which live in the tag, not the body.
        raw_text = library.read(page)
        text = SCRIPT.sub("", raw_text)
        needed = set(NEEDS.findall(raw_text))

        for raw in REF.findall(text):
            url = raw.strip()
            if not url or url.startswith(("data:", "mailto:", "javascript:")):
                continue
            if re.match(r"^[a-z][a-z0-9+.-]*:", url, re.I) or url.startswith("//"):
                # An external link is fine; an external *dependency* is not,
                # because the book's promise is that a page renders offline.
                if externals and url in needed:
                    external.append((rel, url))
                continue
            resolved, frag = resolve(page, url, site_root)
            if not url.startswith("#"):
                n_links += 1
                if not os.path.exists(resolved):
                    missing.append((rel, url))
                    continue
            if not frag or "=" in frag:
                continue            # no fragment, or a hash route for a script
            n_frags += 1
            if os.path.exists(resolved) and resolved.endswith(".html") \
                    and frag not in ids_of(resolved):
                frags.append((rel, url))
    return missing, external, frags, n_pages, n_links, n_frags


def build_main(slug):
    root = os.path.join(library.ROOT, "build", slug)
    if not os.path.isdir(root):
        print(f"sitecheck --build {slug}: no build/{slug}/ -- run NMT_BOOK={slug} "
              f"python3 tools/make.py first")
        return 1
    missing, _ext, frags, n_pages, n_links, n_frags = links(root, None, False)
    known = KNOWN_BUILD.get(slug, {})
    def target(rel, url):
        resolved, _f = resolve(os.path.join(root, rel), url, None)
        return os.path.relpath(resolved, root).replace(os.sep, "/")
    bad, seen = [], {}
    for rel, url in missing:
        t = target(rel, url)
        if t in known:
            seen[t] = seen.get(t, 0) + 1
        else:
            bad.append((rel, url))
    for rel, url in bad[:40]:
        print(f"  MISSING  {rel}  ->  {url}")
    if len(bad) > 40:
        print(f"  ... and {len(bad) - 40} more")
    for rel, url in frags[:40]:
        print(f"  NO SUCH FRAGMENT  {rel}  ->  {url}")
    if len(frags) > 40:
        print(f"  ... and {len(frags) - 40} more")
    for t, why in sorted(known.items()):
        if t in seen:
            print(f"  known    {seen[t]} link(s) to {t}: {why}")
        else:
            print(f"  NOTE     KNOWN_BUILD['{slug}']['{t}'] no longer occurs; delete it")
    print(f"sitecheck --build {slug}: {n_pages} pages, {n_links} internal links, "
          f"{n_frags} fragments, {len(missing)} missing ({sum(seen.values())} known), "
          f"{len(frags)} missing fragments")
    if bad or frags:
        print(f"  {len(bad)} broken, {len(frags)} missing fragment(s): FIX THESE")
        return 1
    print("  every internal link and fragment in the Dropbox build resolves, "
          "apart from the known targets")
    return 0


def main():
    if "--build" in sys.argv:
        i = sys.argv.index("--build")
        if i + 1 >= len(sys.argv):
            print("usage: sitecheck.py --build <slug>")
            return 2
        return build_main(sys.argv[i + 1])

    docs = library.DOCS
    if not os.path.isdir(docs):
        print("sitecheck: no docs/ — run tools/webbuild.py first")
        return 1

    missing, external, frags, n_pages, n_links, n_frags = links(docs, docs, True)
    new_frags = [(r, u) for r, u in frags if (r, u) not in KNOWN_FRAGMENTS]
    still = {(r, u) for r, u in frags if (r, u) in KNOWN_FRAGMENTS}

    for rel, url in missing:
        print(f"  MISSING  {rel}  ->  {url}")
    for rel, url in external:
        print(f"  EXTERNAL DEPENDENCY  {rel}  ->  {url}")
    for rel, url in new_frags:
        print(f"  NO SUCH FRAGMENT  {rel}  ->  {url}")
    for (rel, url), why in sorted(KNOWN_FRAGMENTS.items()):
        if (rel, url) in still:
            print(f"  known    {rel}  ->  {url}  ({why})")
        else:
            print(f"  NOTE     KNOWN_FRAGMENTS entry {rel} -> {url} now resolves; delete it")
    loose = anywhere(docs)
    for rel, url in loose:
        if url is None:
            print(f"  MISSING  {rel}  (served in place of a page at any address; "
                  f"run python3 tools/pwa.py)")
        else:
            print(f"  RELATIVE  {rel}  ->  {url}  (served at any address, so every "
                  f"link starts with {library.SITE})")

    books = ", ".join(b.slug for b in library.books())
    print(f"sitecheck: {n_pages} pages, {n_links} internal links, {n_frags} fragments, "
          f"books: {books}")
    if missing or external or new_frags or loose:
        print(f"  {len(missing)} broken, {len(external)} external dependency, "
              f"{len(new_frags)} missing fragment(s), {len(loose)} problem(s) on "
              f"the pages served at any address: FIX THESE")
        return 1
    print("  every internal link and fragment resolves, nothing loaded from off-site"
          + (f" ({len(still)} known missing fragment)" if still else ""))
    print(f"  {' and '.join(ANYWHERE)} link only from {library.SITE}, "
          f"so they work at any address")

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
