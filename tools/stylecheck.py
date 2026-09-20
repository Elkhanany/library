#!/usr/bin/env python3
"""
stylecheck.py -- the library's prose against the Google developer documentation
style guide, with this library's deviations from it declared rather than implied.

    python3 tools/stylecheck.py                     every book
    python3 tools/stylecheck.py breast-cancer       one book
    python3 tools/stylecheck.py --level error       only the mechanical rules
    python3 tools/stylecheck.py --fix               apply the safe corrections
    python3 tools/stylecheck.py --deviations        what we do not follow, and why
    python3 tools/stylecheck.py --rules             every rule, with its source

WHY THESE RULES AND NOT THE WHOLE GUIDE

The Google guide is written for developer documentation: API references, CLI
tutorials, product pages. Perhaps two thirds of it is editorial advice that
transfers to any expository prose, and the rest is about code samples, UI
element names and Google Cloud product spellings, which no book here has. What
is implemented below is the transferable part.

The rules themselves are taken from the Vale `Google` style package
(github.com/errata-ai/Google), which is the reference machine implementation of
the guide. Each rule carries the developers.google.com page it comes from, so a
disagreement can be settled against the source rather than against this file.
The guide's own pages are not reachable from this environment, which is the
reason the implementation is cited this precisely.

THREE RULES RUN ONLY ON MARKDOWN

`sentence-spacing`, `exclamation` and `acronym-periods` are marked md_only.
Two books keep their prose inside HTML and JSON, and to read those this tool
blanks the markup, which turns every tag into a run of spaces and makes a
spacing rule meaningless. The other two are worse than meaningless in a physics
book: `n!` is a factorial and `S.P.` is notation. The word-level rules are
unaffected and run everywhere.

WHAT THIS DOES NOT DO

It does not measure sentence architecture. `tools/prosecheck.py` already does
that, against a target measured on this corpus rather than borrowed, and that
target is stricter than anything the Google guide asks for. The two tools are
meant to be run together.

It does not touch the trial registry, reference entries, generated files, code
fences, front matter or TeX. A paper's title is quoted evidence and is never
edited to match a style guide.
"""
import argparse, glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import library

ROOT = library.ROOT

# --------------------------------------------------------------------------
# What we deliberately do not follow.
#
# A style guide adopted without exceptions is a style guide nobody reads twice.
# Each of these is a place where the Google guide and this library disagree,
# the disagreement is deliberate, and the reason is recorded so that a future
# reader can overturn it on the reason rather than on taste.

DEVIATIONS = [
    ("Spelling", "https://developers.google.com/style/spelling",
     "The guide asks for American spelling. This library is British throughout: "
     "randomised, tumour, oestrogen, haematological, centre. 4,681 words across "
     "the four books. Kept because it is consistent, because the clinical book's "
     "own sources are split between American and British journals, and because "
     "changing it would edit quoted trial names and endpoint wording."),
    ("Second person", "https://developers.google.com/style/person",
     "The guide asks the writer to address the reader as 'you'. These are "
     "expository references rather than tutorials. Nobody is being walked "
     "through a task, so there is no second party to address. First person "
     "plural is still avoided, which is the half of that rule that does apply."),
    ("Contractions", "https://developers.google.com/style/contractions",
     "The guide prefers 'don't' and 'can't'. The corpus carries 299 contractions "
     "in a million words, which is to say it does not use them. A clinical "
     "reference in contractions reads as a blog post about the evidence rather "
     "than as the evidence."),
    ("Em dash spacing", "https://developers.google.com/style/dashes",
     "The guide asks for an unspaced em dash. The philosophy and physics books "
     "use the spaced form, 1,504 of them, and that is the house typographic "
     "convention recorded in the house-style skill. The clinical book takes the "
     "stricter line and uses no em dash at all, because a dash aside is where a "
     "hedge goes to hide."),
    ("Word list", "https://developers.google.com/style/word-list",
     "Most of the guide's word list fixes Google product names: 'Container "
     "Engine' to 'Kubernetes Engine', 'url' to 'URL'. No book here has a "
     "product in it. The parts that are ordinary English, such as the gendered "
     "occupation terms, are implemented."),
    ("Jargon", "https://developers.google.com/style/jargon",
     "The guide's jargon list is developer idiom: break-glass, swim lane, "
     "out-of-the-box. A clinical reference for oncologists is written in the "
     "register of its field, and explaining what neoadjuvant means to that "
     "reader is a fault rather than a courtesy. Jargon is governed per book."),
]

# --------------------------------------------------------------------------
# The rules.
#
# level  error       mechanical, unambiguous, and safe to correct automatically
#        warning     a real finding that wants a person to choose the wording
#        suggestion  worth a look, and wrong often enough not to gate anything
#
# A rule with `fix` can be applied by --fix. A rule without one never is.

def _swap(pairs, flags=re.I):
    """A substitution rule: find any key, propose its value.

    The keys are regular expressions, so `e\\.g\\.` is what goes into the
    pattern and `e.g.` is what comes back out of a match. The lookup table is
    built on the unescaped form, or every substitution silently proposes an
    empty replacement and --fix quietly does nothing."""
    pat = re.compile(r'(?<![\w-])(?:%s)(?![\w-])'
                     % '|'.join(k for k, _ in pairs), flags)
    table = {k.replace('\\', '').lower(): v for k, v in pairs}

    def find(t):
        return [(m.start(), m.group(0),
                 table.get(m.group(0).lower(), '')) for m in pat.finditer(t)]
    return find


LATIN = [(r'e\.g\.', 'for example'), (r'i\.e\.', 'that is'),
         (r'etc\.', 'and so on'), (r'viz\.', 'namely'),
         (r'cf\.', 'compare'), (r'N\.B\.', 'note')]

GENDERED = [('airman', 'pilot'), ('airmen', 'pilots'),
            ('chairman', 'chair'), ('chairmen', 'chairs'),
            ('manmade', 'artificial'), ('man-made', 'artificial'),
            ('mankind', 'humanity'), ('manpower', 'staff'),
            ('policeman', 'police officer'), ('policemen', 'police officers'),
            ('salesman', 'salesperson'), ('spokesman', 'spokesperson'),
            ('workmanlike', 'skilful'), ('authoress', 'author'),
            ('alumnus', 'graduate'), ('alumni', 'graduates')]

ORDINALS = {'1': 'first', '2': 'second', '3': 'third', '4': 'fourth',
            '5': 'fifth', '6': 'sixth', '7': 'seventh', '8': 'eighth',
            '9': 'ninth', '10': 'tenth'}


def ordinal(t):
    """Only first to tenth.

    The guide says to spell out ordinals, but a 95th centile and a 75th
    percentile are named statistical quantities rather than counting words, and
    nobody writes 'the ninety-fifth centile'. Above ten the numeral is the
    convention in every book here."""
    out = []
    for m in re.finditer(r'\b(\d+)(st|nd|rd|th)\b', t):
        if m.group(1) not in ORDINALS:
            continue
        want = {'1': 'st', '2': 'nd', '3': 'rd'}.get(m.group(1), 'th')
        if m.group(2) != want:
            continue          # '2th' is a typo or a fragment of markup
        after = t[m.end():m.end() + 14].lower()
        if re.match(r'\s*(?:percentile|centile|quantile|quartile)', after):
            continue
        out.append((m.start(), m.group(0), ORDINALS[m.group(1)]))
    return out


def rx(pattern, flags=re.I):
    p = re.compile(pattern, flags)
    return lambda t: [(m.start(), m.group(0), '') for m in p.finditer(t)]


RULES = [
    # ---- error: mechanical, and --fix will apply them -------------------
    dict(id='latin', level='error', find=_swap(LATIN),
         msg="Write the English. The guide reserves Latin abbreviations for "
             "parenthetical use and prefers them spelled out.",
         # Reported, never applied. 'X, i.e. Y' becomes 'X, that is, Y', and
         # the second comma is a judgement about the sentence rather than a
         # substitution. A blind swap produces 'that is one that N maps onto'.
         link='https://developers.google.com/style/abbreviations'),
    dict(id='ordinal', level='error', find=ordinal,
         msg="Spell out an ordinal in prose.",
         link='https://developers.google.com/style/numbers', fix=True),
    dict(id='optional-plural', level='error',
         # case-sensitive, lowercase, three letters or more, no internal
         # capital: `F(s)`, `\u03c6(s)` and `measureText(s)` are functions of s,
         # which is most of what `\w+\(s\)` matches in a physics or logic book.
         # ...and not a call to a function whose argument happens to be s
         find=rx(r'(?<![\w(])(?!(?:abs|cos|sin|tan|exp|log|ln|min|max|sum|len|'
                 r'int|str|sqrt|div|mod|arg|lim|det|dim|deg|erf)\()'
                 r'[a-z]{3,}\(s\)', 0),
         msg="Do not use a parenthesised plural. Use the plural, or rewrite.",
         link='https://developers.google.com/style/plurals-parentheses'),
    dict(id='exclamation', level='error', md_only=True, find=rx(r'\w!(?:\s|$)'),
         msg="No exclamation points in prose.",
         link='https://developers.google.com/style/exclamation-points'),
    dict(id='sentence-spacing', level='error', md_only=True,
         find=lambda t: [(m.start(), m.group(0),
                          m.group(1) + ' ' + m.group(2))
                         for m in re.finditer(r'([a-z][.?!])  +([A-Z])', t)],
         msg="One space after a full stop.",
         link='https://developers.google.com/style/sentence-spacing', fix=True),
    dict(id='heading-period', level='error', find=None, scope='heading',
         msg="No full stop at the end of a heading.",
         link='https://developers.google.com/style/capitalization'),
    dict(id='acronym-periods', level='error', md_only=True,
         find=rx(r'\b(?:[A-Z]\.){2,}[A-Z]?\b', 0),
         msg="No full stops inside an acronym or initialism.",
         link='https://developers.google.com/style/abbreviations'),
    dict(id='ly-hyphen', level='error',
         # `early-phase` and `family-based` end in -ly without being adverbs,
         # and they are the commonest hyphenated words in this corpus, so the
         # nouns and adjectives are excluded by name.
         # `early-phase`, `family-based` and Wittgenstein's `fly-bottle` end in
         # -ly without being adverbs, and they are the commonest hyphenated
         # words in this corpus, so the nouns and adjectives are excluded by
         # name.
         find=lambda t: [(m.start(), m.group(0), m.group(0).replace('-', ' ', 1))
                         for m in re.finditer(
                             r'\b(?!(?:ear|on|ho|ug|sil|fami|supp|rep|imp|app|'
                             r'multip|ang|month|dai|year|hour|week|time|cost|'
                             r'qua|assemb|f|p|s|jol|wobb|cudd|love|live|like)ly-)'
                             r'\w+ly-\w+\b', t)],
         msg="An adverb ending in -ly takes no hyphen after it.",
         link='https://developers.google.com/style/hyphens', fix=True),
    dict(id='range-words', level='error',
         find=rx(r'\b(?:from|between)\s+\d+\s*[-–]\s*\d+'),
         msg="Write the range out: 'from 5 to 10', not 'from 5-10'.",
         link='https://developers.google.com/style/hyphens'),
    dict(id='gender-pronoun', level='error',
         find=rx(r'\bhe/she\b|\bs/he\b|\(s\)he\b'),
         msg="Use 'they', or recast the sentence.",
         link='https://developers.google.com/style/pronouns'),
    dict(id='gendered-term', level='error', find=_swap(GENDERED),
         msg="Use the gender-neutral term.",
         link='https://developers.google.com/style/inclusive-documentation',
         fix=True),
    dict(id='slang', level='error',
         # lowercase only: 'bTw' inside a script identifier is not slang
         find=rx(r'\b(?:tl;dr|ymmv|rtfm|imo|imho|fwiw|btw)\b', 0),
         msg="No internet abbreviations.",
         link='https://developers.google.com/style/abbreviations'),

    # ---- warning: a person chooses the wording --------------------------
    dict(id='heading-case', level='warning', find=None, scope='heading',
         msg="Headings take sentence case.",
         link='https://developers.google.com/style/capitalization'),
    dict(id='first-person-plural', level='warning',
         find=rx(r"(?<![\w-])(?:we|we're|we've|us|our|ours|let's)(?![\w-])"),
         msg="Avoid the first person plural. Say who did the thing, or recast "
             "so that nobody has to be named.",
         link='https://developers.google.com/style/pronouns'),
    dict(id='future-tense', level='warning', find=rx(r"(?<![\w-])will(?![\w-])"),
         msg="Prefer the present tense. 'Will' is right only where the sentence "
             "is genuinely about the future, such as a trial that has not "
             "reported.",
         link='https://developers.google.com/style/tense'),
    dict(id='excessive-claim', level='warning',
         # The guide is aiming at marketing superlatives. A bare 'best' is not
         # one: in this corpus all 46 of its uses are comparative judgements
         # about evidence ('the best characterised', 'which drug is best',
         # 'best supportive care', which is the name of a trial arm). Only the
         # claim forms are matched, and 'best' only where it promises.
         find=rx(r"(?<![\w-])(?:best (?:in class|of breed|possible experience)|"
                 r"fastest|simplest|easiest|"
                 r"guarantees?|seamless(?:ly)?|effortless(?:ly)?|"
                 r"cutting[- ]edge|state[- ]of[- ]the[- ]art|world[- ]class)"
                 r"(?![\w-])"),
         msg="An unverifiable claim. Say the thing that can be checked.",
         link='https://developers.google.com/style/excessive-claims'),
    dict(id='timeless', level='warning',
         find=rx(r"(?<![\w-])(?:currently|at present|as of today|nowadays)"
                 r"(?![\w-])"),
         msg="Time-anchored wording dates the page. Say the date, or drop it.",
         link='https://developers.google.com/style/timeless-documentation'),
    dict(id='anthropomorphism', level='warning',
         find=rx(r"\b(?:the (?:trial|study|table|assay|analysis|model|paper)s?)"
                 r"\s+(?:sees|saw|tells|thinks|knows|wants|believes|decides)\b"),
         msg="A trial does not see or want. Say what its investigators did, or "
             "what its data show.",
         link='https://developers.google.com/style/anthropomorphism'),

    # ---- suggestion -----------------------------------------------------
    dict(id='parenthetical', level='suggestion',
         find=rx(r'\([^)]{40,}\)', re.S),
         msg="A long parenthetical. Parentheses tell the reader the words "
             "inside them matter less, which is rarely what is meant.",
         link='https://developers.google.com/style/parentheses'),
]

BY_ID = {r['id']: r for r in RULES}
LEVELS = ('error', 'warning', 'suggestion')

# Per-book overrides. A book may lower a rule or switch it off, with a reason.
PROFILES = {
    'breast-cancer': {
        # An ongoing trial has not reported, and the whole point of saying so is
        # that it will. The rule stays on as a suggestion so a stray "will show"
        # is still visible.
        'future-tense': 'suggestion',
        # A clinical reference states results in the passive where the patient
        # rather than the investigator is the subject. 19% of its sentences
        # carry a passive and almost all of them are right.
        'parenthetical': 'suggestion',
    },
    'newton-to-mtheory': {
        # This book teaches, and addresses its reader directly 2,358 times. Its
        # 'we' is the reader and writer working a derivation together, which is
        # the one context where the first person plural earns its place.
        'first-person-plural': 'suggestion',
    },
}


# --------------------------------------------------------------------------
# Where the prose is, and what in it is not prose.

def corpus(slug):
    """(label, path_or_None, text) for one book's prose.

    The clinical book writes markdown chapters. The philosophy books keep their
    prose inside src/data/*.json. The physics book hand-writes src/*.html. Only
    the first of those can be corrected in place, which is why the others come
    back with no path."""
    d = os.path.join(ROOT, 'books', slug)
    md = sorted(glob.glob(d + '/chapters/*.md'))
    if md:
        for p in md:
            yield os.path.basename(p), p, open(p, encoding='utf-8').read()
        return
    # Prose inside JSON comes back with no path: correcting it means
    # re-serialising a data file, which is a different job from editing a
    # sentence. Those books are reported on and never written to.
    js = sorted(glob.glob(d + '/src/data/*.json'))
    if js:
        for p in js:
            for path, text in _walk(json.loads(open(p, encoding='utf-8').read()),
                                    os.path.basename(p)):
                yield path, None, text
        return
    # This book hand-writes its chapters as src/*.html, so they are source and
    # can be corrected. Blanking preserves every offset, which is what makes
    # writing back safe.
    for p in sorted(glob.glob(d + '/src/*.html')):
        yield os.path.basename(p), p, open(p, encoding='utf-8').read()


def _walk(obj, path=''):
    if isinstance(obj, str):
        if len(obj) > 60:
            yield path, obj
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _walk(v, '%s[%d]' % (path, i))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from _walk(v, '%s.%s' % (path, k) if path else k)


def prose(text, label):
    """Blank out everything that is not prose, keeping every offset.

    Offsets have to survive so that --fix can write back into the original
    file. So each non-prose span is replaced by spaces of the same length
    rather than removed."""
    def blank(m):
        return ' ' * (m.end() - m.start())

    t = text
    if label.endswith('.md'):
        t = re.sub(r'^---\n.*?\n---\n', blank, t, flags=re.S)   # front matter
        t = re.sub(r'```.*?```', blank, t, flags=re.S)          # fenced blocks
        t = re.sub(r'`[^`\n]+`', blank, t)                      # inline code
        t = re.sub(r'\[@[^\]]*\]', blank, t)                    # citations
        t = re.sub(r'\{\{[^}]*\}\}', blank, t)                  # trial chips
        t = re.sub(r'\[\[[^\]]*\]\]', blank, t)                 # cross-refs
        t = re.sub(r'\]\([^)]*\)', blank, t)                    # link targets
    else:
        t = re.sub(r'<script.*?</script>|<style.*?</style>', blank, t, flags=re.S)
        t = re.sub(r'<[^>]+>', blank, t)
        t = re.sub(r'&[a-zA-Z]+;|&#\d+;', blank, t)
    return _mask_tex(t)


def _mask_tex(t):
    """Blank every TeX span, scanning once from the left.

    Two passes, one for `$$` and one for `$`, get the pairing wrong as soon as
    a file mixes them: a `$$` block that the first pass missed leaves two loose
    `$` for the second pass to pair with the wrong neighbours. One scan that
    takes whichever delimiter it meets next keeps the pairing right, which is
    what stopped `\\text{i.e.}` inside a display equation being read as prose.

    `\\(...\\)` and `\\[...\\]` are handled too, for the books that use them."""
    out, i, n = [], 0, len(t)
    while i < n:
        if t.startswith('$$', i):
            j = t.find('$$', i + 2)
            j = n if j < 0 else j + 2
        elif t[i] == '$':
            j = t.find('$', i + 1)
            j = n if j < 0 or j - i > 400 else j + 1
        elif t.startswith('\\[', i):
            j = t.find('\\]', i + 2)
            j = n if j < 0 else j + 2
        elif t.startswith('\\(', i):
            j = t.find('\\)', i + 2)
            j = n if j < 0 else j + 2
        else:
            out.append(t[i])
            i += 1
            continue
        out.append(' ' * (j - i))
        i = j
    return ''.join(out)


def headings(text, label):
    """(offset, text) for each heading, however this book writes one."""
    if label.endswith('.md'):
        for m in re.finditer(r'^(#{1,6})\s+(?:BS-\d+\s+)?(.+?)\s*$', text, re.M):
            yield m.start(2), m.group(2)
    else:
        for m in re.finditer(r'<h[1-6][^>]*>(.*?)</h[1-6]>', text, re.S | re.I):
            yield m.start(1), re.sub(r'<[^>]+>', '', m.group(1)).strip()


# A word that is capitalised for a reason other than title case: an acronym, an
# identifier, anything carrying a digit or an internal capital (HER2-positive,
# CanRisk, Tyrer-Cuzick), or the sentence's own first word.
TITLE_CASE_OK = re.compile(
    r'^(?:[A-Z]{2,}[\w-]*|[\w-]*\d[\w-]*|[A-Z][a-z]*[A-Z][\w-]*|'
    r'[A-Z][a-z]+-[A-Z][\w-]*|I|A|An|The)$')


def heading_findings(text, label, rule):
    out = []
    for off, h in headings(text, label):
        if not h:
            continue
        if rule == 'heading-period' and re.search(r'[a-z0-9]\.\s*$', h):
            out.append((off, h, ''))
        if rule == 'heading-case':
            words = h.split()
            # a heading is title case when most of its non-opening words are
            # capitalised and are not acronyms, identifiers or proper nouns
            # Proper nouns cannot be told from title case by looking, so the
            # bar is deliberately high: three or more ordinary words
            # capitalised, and most of the words in the heading.
            candid = [w for w in words[1:] if not TITLE_CASE_OK.match(w.strip('.,:;'))]
            caps = [w for w in candid if w[:1].isupper()]
            if len(caps) >= 3 and len(candid) and len(caps) >= 0.6 * len(candid):
                out.append((off, h, ''))
    return out


# --------------------------------------------------------------------------

def level_for(slug, rule):
    return PROFILES.get(slug, {}).get(rule['id'], rule['level'])


def findings(slug, want_level=None):
    """Every finding for a book, as (label, path, rule, offset, text, fix)."""
    order = {l: i for i, l in enumerate(LEVELS)}
    cut = order.get(want_level, len(LEVELS))
    for label, path, raw in corpus(slug):
        t = prose(raw, label)
        for rule in RULES:
            lv = level_for(slug, rule)
            if lv == 'off' or order[lv] > cut:
                continue
            if rule.get('md_only') and not label.endswith('.md'):
                continue
            if rule.get('scope') == 'heading':
                hits = heading_findings(raw, label, rule['id'])
            else:
                hits = rule['find'](t)
            for off, found, fix in hits:
                yield label, path, rule, lv, off, found, fix


def apply_fixes(slug):
    """Rewrite the safe corrections, in place, one file at a time.

    Only a rule marked `fix` is applied, only where it proposes a replacement,
    and only in a book whose prose lives in files this tool can write."""
    per_file = {}
    for label, path, rule, lv, off, found, fix in findings(slug, 'error'):
        if not path or not rule.get('fix') or not fix:
            continue
        per_file.setdefault(path, []).append((off, found, fix, rule['id']))
    n = 0
    for path, edits in sorted(per_file.items()):
        text = open(path, encoding='utf-8').read()
        # right to left, so earlier offsets stay valid
        for off, found, fix, rid in sorted(edits, key=lambda e: -e[0]):
            if text[off:off + len(found)] != found:
                continue                      # the file moved under us
            rep = fix
            if found[:1].isupper() and rep[:1].islower():
                rep = rep[:1].upper() + rep[1:]
            text = text[:off] + rep + text[off + len(found):]
            n += 1
        open(path, 'w', encoding='utf-8').write(text)
    return n


def report(slug, want_level):
    counts, examples = {}, {}
    for label, path, rule, lv, off, found, fix in findings(slug, want_level):
        k = (lv, rule['id'])
        counts[k] = counts.get(k, 0) + 1
        examples.setdefault(k, []).append((label, ' '.join(found.split())[:70]))
    if not counts:
        print('%s: clean at level %s' % (slug, want_level or 'suggestion'))
        return 0
    print('%s' % slug)
    total = 0
    for lv in LEVELS:
        rows = sorted((k for k in counts if k[0] == lv), key=lambda k: -counts[k])
        for k in rows:
            total += counts[k]
            r = BY_ID[k[1]]
            print('  %-10s %-20s %5d   %s' % (lv, k[1], counts[k], r['link']))
            for label, ex in examples[k][:2]:
                print('               %-18s %s' % (label[:18], ex))
    return total


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('books', nargs='*')
    ap.add_argument('--level', choices=LEVELS, default=None,
                    help='report this level and everything stricter')
    ap.add_argument('--fix', action='store_true',
                    help='apply the corrections that are safe to make mechanically')
    ap.add_argument('--deviations', action='store_true',
                    help='what this library does not take from the guide, and why')
    ap.add_argument('--rules', action='store_true')
    a = ap.parse_args()

    if a.deviations:
        print('Deliberate deviations from the Google developer documentation '
              'style guide\n')
        for name, link, why in DEVIATIONS:
            print('%s\n  %s' % (name, link))
            for line in re.findall(r'.{1,74}(?:\s|$)', why):
                print('  %s' % line.strip())
            print()
        return 0

    if a.rules:
        for lv in LEVELS:
            for r in RULES:
                if r['level'] != lv:
                    continue
                print('%-10s %-20s %s' % (lv, r['id'], r['link']))
                for line in re.findall(r'.{1,70}(?:\s|$)', r['msg']):
                    print('%32s%s' % ('', line.strip()))
        return 0

    slugs = a.books or [s for s in library.slugs()
                        if os.path.isdir(os.path.join(ROOT, 'books', s))]
    if a.fix:
        total = 0
        for s in slugs:
            n = apply_fixes(s)
            total += n
            if n:
                print('%s: %d correction(s)' % (s, n))
        print('%d correction(s) applied. Re-run without --fix to see what is '
              'left for a person.' % total)
        return 0

    total = 0
    for s in slugs:
        total += report(s, a.level)
        print()
    print('%d finding(s). `--deviations` says what is deliberately not '
          'followed.' % total)
    return 0


if __name__ == '__main__':
    sys.exit(main())
