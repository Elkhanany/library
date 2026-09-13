# Writing kit — read this in full before drafting

You are writing one or more chapters of a breast cancer reference for practising medical
oncologists and fellows. The reader already treats this disease. Do not explain what neoadjuvant
means. Do explain why a convention was chosen, because that is what nobody writes down.

## Where things are

| Path | What |
|---|---|
| `books/breast-cancer/_specs/BC-###.txt` | Your chapter's section list. Heading titles must match EXACTLY. |
| `books/breast-cancer/briefs/PT-XX.md` | The development brief for your part. Carries, Threads, Anchors, Controversy. |
| `books/breast-cancer/outline.yaml` | Structure. Do not edit. |
| `books/breast-cancer/references.yaml` | Every citable reference. See the citation rule below. |
| `books/breast-cancer/trials.yaml` | Every citable trial key. |
| `books/breast-cancer/chapters/BC-280.md` | A finished chapter. Match its register. |
| `books/breast-cancer/chapters/BC-300.md` | A second finished chapter. |

## File format

`books/breast-cancer/chapters/BC-###.md`

```markdown
---
id: BC-280
title: "HER2 heterogeneity"
subtitle: "One clause saying what the chapter settles. Optional but wanted."
status: drafted
updated: 2026-09-13
---

## BS-2250 Definitions and thresholds, spatial, clonal, and the ten percent convention

Prose.
```

The `id` and `title` must match the spec file exactly. Every heading is `## BS-#### ` followed by
the section title copied exactly from the spec. A section you do not write is simply omitted, and
the build collects it into a "Still to be written" block. Omitting is honest. Writing a thin
paragraph to fill a slot is not.

## The four macros

```
[@oleary2018]                 one citation
[@oleary2018; @schiavon2015]  grouped into a single bracket
{{trial:paloma3}}             a trial, from trials.yaml
[[BC-280]]  [[BS-2290]]       a chapter or section cross-reference
[[term:her2-low]]             a glossary term
```

Never inline a citation. No bare PMIDs, DOIs or author-year strings in prose.

## THE CITATION RULE — the most important rule here

**You may cite a key only if it already exists in `references.yaml`, or if you have personally
verified it in this session with the PubMed tool and are returning it in your references patch.**

Never invent a citation key. Never invent a PMID. Never guess a DOI. Never cite a trial key that
is not in `trials.yaml`.

To add a reference:

1. Search PubMed (`mcp__PubMed__search_articles`) for the paper.
2. Confirm the hit is the primary publication, not a subgroup analysis, commentary or review.
   Trial acronyms return many secondary papers. Read the title and abstract before accepting it.
3. Fetch metadata (`mcp__PubMed__get_article_metadata`) to get the exact PMID, DOI, journal,
   year, volume and pages.
4. Add it to your returned patch with `verified: true`.

Key format is first author surname plus year, lowercase, e.g. `oleary2018`, `schiavon2015`.

**If you cannot verify a citation, write the sentence without one, or write the claim in a form
that does not need one.** A mechanism explained without a citation is fine. A number without a
source is not. Never attach a number to an unverified reference.

## Numbers

Say what a number is a number *of*. A hazard ratio without its comparison is decoration. If you
have the denominator, give it. If you do not have the denominator, do not imply one.

If your brief supplies a figure you could not verify against a source, you may still use it only
if you soften it to the level you can support, or you may drop it. Prefer dropping it. This book
will be read by people making treatment decisions.

## Voice — this is enforced

The one rule: **do not chain independent clauses. Give each its own sentence.**

- Mean sentence length 15 to 18 words. Nothing over about 35.
- No em dashes anywhere. Recast or use a full stop.
- Avoid heavy use of semicolons and colons.
- Enumerations are exempt. A colon introducing a series is doing work a full stop cannot.
- Separate biology from measurement in every claim. If a statement is about an assay threshold,
  a sampling scheme or a scoring convention, say so. Most disagreement in this field lives in
  that gap.
- No filler. No "it is important to note". No paragraph that restates the heading.

Length: roughly 120 to 250 words per section. A `major` chapter can run longer. Do not pad.

## Fenced blocks

````
```interplay target=BC-350
One paragraph tying this chapter's subject back to the heterogeneity argument in Part VI.
```

```practice
What to do on Monday. Only for sections about a decision rather than a mechanism.
```

```caution
A place where the obvious reading of the evidence is wrong.
```
````

Every disease-focused chapter in Parts VIII, IX and X carries at least one `interplay` block.
Use `practice` where a section is genuinely about a decision. Use `caution` where the intuitive
reading fails. Do not use all three in every chapter.

## What you return

1. The chapter files, written to `books/breast-cancer/chapters/BC-###.md`.
2. A YAML block in your final message containing ONLY the new references you verified, in
   `references.yaml` entry format, each with `verified: true` and a real PMID or DOI.
3. A short list of any claim you wanted to make but dropped for lack of a verifiable source.

Do not edit `outline.yaml`, `references.yaml`, `trials.yaml` or anything outside `chapters/`.
Return the reference patch in your message. The orchestrator merges it.

## Self-check before you finish

- Every heading matches its spec line exactly.
- Every `[@key]` is either already in references.yaml or in your patch.
- Every `{{trial:key}}` is in trials.yaml.
- Every `[[BC-###]]` and `[[BS-####]]` exists in outline.yaml.
- No em dashes. Search for them.
- No sentence over about 35 words.
