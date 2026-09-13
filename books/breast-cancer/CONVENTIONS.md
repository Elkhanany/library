# How this book is written

A reference on breast cancer for practising medical oncologists and for fellows. Fourteen
parts, seventy-nine chapters, six hundred and seventy-three sections. It is the first book in
the library whose structure is data rather than a hand-kept list, because at this size it has
to be.

## The three rules

**1. Identifiers are permanent and carry no position.** `PT-##` for a part, `BC-###` for a
chapter, `BS-####` for a section. A chapter keeps its identifier when it moves between parts.
Filenames, anchors, citations and cross-references all bind to the identifier, so restructuring
the book breaks nothing.

**2. Position is list position.** Move a block in `outline.yaml` to move a node. Insert a block
to insert one. Nothing else in the file changes. `BC-345` would sit between `BC-340` and
`BC-350`, which is what an insertion looks like in practice.

**3. Display numbers are computed at build time.** `Part VI`, `Chapter 28`, and the `4 ·` in
front of a section heading exist only in the output. Nothing in the source knows its own
number.

## Where things live

| File | Role |
|---|---|
| `outline.yaml` | Structure. Parts, chapters, sections, tags, appendices. Hand-edited. |
| `chapters/BC-###.md` | Chapter prose, one file per chapter, named for the identifier. Hand-edited. |
| `references.yaml` | Every citation in the book. Hand-edited or imported. |
| `trials.yaml` | Trial registry. Hand-edited. |
| `glossary.yaml` | Defined terms. Hand-edited. |
| `book.json` | Title, theme, and the reader-facing copy for each part. Hand-edited. |
| `curriculum.json` | What the library builds from. **Generated.** |
| `src/BC-###.html` | Chapter fragments. **Generated.** |
| `src/_landing.html` | The book's front door. Hand-edited. |

`src/` is generated for this book, which is a deliberate exception to the library's rule that
`src/` is the only hand-edited tree. Edit a fragment there and the edit is lost on the next
run. The prose lives in `chapters/`.

## The build

```bash
python3 tools/bc.py            # outline.yaml -> curriculum.json, chapters/*.md -> src/*.html
python3 tools/bc.py --check    # fail if either is stale
python3 tools/webbuild.py      # the whole library -> docs/
```

`bc.py` refuses to write anything if a citation key, cross-reference, trial or glossary term
does not resolve, or if a section heading disagrees with `outline.yaml`. Run it before every
commit. It is cheap and it is the only thing standing between a typo and a dead link in a
published chapter.

## Writing a chapter

Add the file as `chapters/BC-###.md`, named for an identifier that already exists in
`outline.yaml`. Front matter carries the identifier and the title, and both are checked against
the outline:

```markdown
---
id: BC-280
title: "HER2 heterogeneity"
subtitle: "What a heterogeneous report changes, and what it does not."
status: drafted
updated: 2026-09-13
---

## BS-2250 Definitions and thresholds, spatial, clonal, and the ten percent convention

Prose.
```

Every heading carries its section identifier, and the text after it must match the title in
`outline.yaml` exactly. Write the heading as `## BS-2250` alone and the title is filled in from
the outline. Sections you have not written yet are collected into a **Still to be written**
block at the foot of the chapter, so the plan is visible rather than silent.

To add a section, write it as a bare string under the right chapter in `outline.yaml`:

```yaml
    sections:
    - id: BS-2390
      title: What to do with a heterogeneous HER2 report in clinic today
    - Reversion mutations and restored repair
```

then `python3 tools/bc.py --mint`, which turns it into an `{id, title}` pair with a freshly
minted permanent identifier. `--mint --dry-run` reports what it would do and writes nothing.
Identifiers come from the highest one in use plus ten, so a deleted identifier is never handed
out again and an old link never quietly starts resolving to something else. Nothing that
already carries one is touched.

To promote a section to a chapter, move it up a level, give it a free `BC-###`, and record its
old `BS-####` in a `was:` list.

## Citations, trials, cross-references, terms

Four syntaxes, all resolved by `bc.py`, all bound to permanent keys:

```
[@slamon1987]                 one citation
[@slamon1987; @shou2004]      grouped into a single bracket
{{trial:katherine}}           a named trial, from the registry
[[BC-280]]  [[BS-2290]]       a chapter or a section
[[term:her2-low]]             a defined term, from the glossary
```

Never inline a citation. No bare PubMed identifiers, DOIs or author-year strings in prose.
Every one goes through `references.yaml`, where the key is the first author's surname and the
year. **Never rename a key.** Add an alias instead, so links written against the old spelling
keep resolving.

**A chapter may not cite an unverified reference.** An entry marked `verify: true` is one whose
identifier has been claimed but not checked against the source, and `bc.py` fails the build on
any chapter that cites one. This is stricter than it sounds and deliberately so: an unverified
citation is worse than a missing one, because it reads to a clinician as though someone
confirmed it. To add a reference, find the paper on PubMed, confirm the hit is the primary
publication rather than a subgroup analysis or commentary, and record the exact identifier with
`verified: true`. A trial acronym returns many secondary papers, so read the title before
accepting one.

Write a citation with a space before the bracket, the way it is comfortable to type:
`...an adaptive survival mechanism [@ali2020].` The build closes that space, so the mark sets
against the word it qualifies rather than floating off it.

Citations are numbered in order of first appearance within a page, which is the right
convention when each chapter is its own page. Because the key is permanent, reordering chapters
changes the printed numeral and nothing else.

A cross-reference to a chapter that has not been written yet renders as its title, in muted
type, and is deliberately not a link. Naming a thing the book intends to cover is honest.
Sending a reader to a page that does not exist is not.

DARE names two different studies in this literature. They are keyed separately as `dare-ctdna`
and `dare-tbcrc`. **Never merge them.**

## Fenced blocks

```
​```interplay target=BC-350
One paragraph tying this chapter's subject back to the heterogeneity argument.
​```

​```practice
What to do on Monday. Reserved for the sections that are about a decision rather than a
mechanism.
​```

​```caution
A place where the obvious reading of the evidence is wrong.
​```
```

Every disease-focused chapter in Parts VIII, IX and X should carry at least one interplay
block, tying its subject back to Part VI.

## Voice

The library's `house-style` skill governs, and it comes to one rule: **do not chain independent
clauses, give each its own sentence.** On top of that, three things this book asks for:

- No em dashes. Recast the sentence or use a full stop.
- Say what a number is a number *of*. A hazard ratio without its comparison is decoration.
- Separate biology from measurement in every claim. If a statement is about an assay
  threshold, a sampling scheme or a scoring convention, say so. Most of the disagreement in
  this field lives in that gap.

The reader already treats this disease. Do not explain what neoadjuvant means. Do explain why a
convention was chosen, because that is what nobody writes down.
