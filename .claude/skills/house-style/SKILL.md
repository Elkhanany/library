---
name: house-style
description: The library's prose style. Use when writing or revising any book text in this repository - chapter prose, philosopher studies, formal-layer commentary, blurbs - and when reviewing a draft for readability. Derived from a measured comparison of the corpus against rewrites, so the numbers in it are observations rather than preferences.
---

# House style

The books in this library are written for an intelligent reader who is not a
specialist. The prose had drifted toward long chained sentences, and this guide
is what fixed it. It is short on purpose: almost all of the improvement came
from **one move**, and a rule nobody can remember is not a rule.

## How this was arrived at

Ten passages were sampled across the corpus to cover different failure modes:
dense history, an attribution chain, a hard idea being introduced, a work
description, an abstract legacy paragraph, a caveat where hedging is the
content, two formal-layer prose fields, and one passage judged among the best in
the book as a control. Each was rewritten for readability by a different model
under instructions to preserve every epistemic marker and add nothing. The
rewrites were then measured against the originals.

The finding was that the rewriter made essentially one change:

| | before | after |
|---|---|---|
| sentences | 41 | 61 (+49%) |
| words | 1,038 | 1,045 (+1%) |
| mean sentence length | 23-41 words | **15-18 words, every passage** |
| longest sentence | 71 words | 33 |
| semicolons joining independent clauses | 6 | 0 |
| epistemic markers lost | - | **0** |
| dates, names, numbers lost | - | **0** |

Words barely moved. Sentence count rose by half. That is the whole pattern.

---

## The one rule

**Do not chain independent clauses. Give each its own sentence.**

A semicolon or an "and" joining two clauses that could each stand alone is the
single construction that made this prose hard. Splitting is nearly free: it cost
1% more words across ten passages and lost nothing.

Before (53 words, one sentence):

> In 1745 Hume lost the chair of Ethics and Pneumatical Philosophy to William
> Cleghorn after charges of scepticism and atheism; in 1752 the logic chair at
> Glasgow was closed to him for the same reasons; in 1755 the General Assembly
> considered censuring him, and the Moderate party of William Robertson and
> Hugh Blair headed it off.

After (three sentences, same facts, same order, same dates):

> In 1745, Hume lost the chair of Ethics and Pneumatical Philosophy to William
> Cleghorn after charges of scepticism and atheism. In 1752, the logic chair at
> Glasgow was closed to him for the same reasons. In 1755, the General Assembly
> considered censuring him, but the Moderate party of William Robertson and Hugh
> Blair headed it off.

**Target: a mean of 15-18 words a sentence, and nothing over about 35.** These
are the numbers the rewrites converged on unprompted, across every passage,
which is why they are here rather than a figure someone liked.

## The exception, and it is a real one

**Lists are not chains. Leave them alone.**

Two of the ten passages came back completely untouched. One was already at 16.9
words a sentence. The other was at 27.7 -- well over target -- and was still not
split, because its long sentences are enumerations rather than narrative:

> Three durable quarrels followed: Popper's indictment of the Republic; the
> analytic recovery of Plato as an arguer whose mistakes can be diagnosed; and
> the Tübingen school's claim that the unwritten doctrines are the true centre.

A colon introducing a series, and semicolons separating items that contain their
own commas, are doing work no full stop can do. The rule is about *clauses that
could stand alone*, not about length.

## What must survive untouched

These are not style. They are the book's standard, and a revision that reads
better because one of them is gone is a failed revision.

- **Every word marking how a claim is known.** *disputed, traditionally dated,
  attributed, reported only by, on his testimony alone, may be, if genuine,
  the conventional birth, a later convention, generally judged.*
- **Reporting verbs at their exact strength.** *reported / called / says /
  credits* mark four different grades of reliability. Flattening them all to
  "says" destroys information.
- **A disagreement stated as a disagreement.** Where two sources conflict, or
  two scholars hold opposite readings, the conflict is the content. Do not
  resolve it to read more smoothly.
- **Every date, name, number, title and scoped qualifier** — *alone, only, on
  balance, for the moods Aristotle accepts, requiring no existential import.*
- **Institutional names in full.** "the chair of Ethics and Pneumatical
  Philosophy" is the actual title. "a chair in moral philosophy" reads better
  and is wrong.

## Add nothing

No invented example, no invented causal link, no filler transition. The test:
**could a fact-checker with the sources verify every sentence?** If a sentence
has become unverifiable, it is new content.

Three small additions slipped into the ten rewrites and all three are worth
recognising, because they are what this failure looks like when it is mild:

- A colon replaced by *"meaning"* — a gloss word carrying no information.
- *"He argues that"* prepended where the original simply asserted.
- *"and"* closing a deliberately open list: *"ready-to-hand, transparent, part
  of a web of purposes"* became *"...transparent, and part of a web of
  purposes."* The original three terms accumulate; the conjunction shuts them.

## The trap, which fired on the first passage

**A paragraph does not begin in isolation.** The one real loss in ten passages
was this opening:

> Against that ran the power of the Kirk.

which became

> The power of the Kirk opposed him.

*"Against that"* pointed back to the previous paragraph and was the section's
only explicit joint between paragraphs. Rewriting the paragraph alone destroyed
it. So: **when revising, read the paragraph before and after.** Anaphora —
*that, this, such, the same* — pointing outside the paragraph is load-bearing
and must be preserved or deliberately replaced with the thing it referred to.

In the same sentence, *"its professors"* became *"university professors"*,
losing which university's. Watch for possessives quietly becoming generic.

## Settled by the comparison

Three questions the earlier analysis could not resolve, now answered by what the
rewriter actually did:

- **The short sentence that ends a paragraph is a keeper, not a mannerism.**
  Every one of them survived, including the pseudo-cleft *"What reached
  Simplicius nine hundred years later was that quotation, not the book."*
- **Attribution goes first, not last.** The passage with seven ancient sources,
  all in leading position, came back verbatim. An earlier rule proposing
  trailing attributions is withdrawn.
- **Em-dash asides are not capped at eight words.** Ten- and thirteen-word dash
  tails survived untouched.

## Mechanical, and separate from all of the above

- Em-dash spacing: use the spaced `&mdash;` form throughout. The corpus is
  currently 279 spaced to 161 unspaced.
- Italicise the first occurrence of a work title or foreign term in each field,
  plain thereafter. This currently drifts inside single paragraphs.
- Prose in `formal.json` cross-references derivation lines by number ("line 6").
  No revision may renumber, merge or drop those lines, or merge two prose fields.
- The data files carry `<em>` tags and HTML entities that rendered text does not
  show. Anything revised outside the JSON must be re-rendered and diffed before
  it goes back in.

## Where this guide does not apply: the formal layer

`formal.json` was measured against the target and deliberately **not** rewritten.
It reads at a mean of 25.1 words a sentence with 59 sentences over 40 words, so
by the numbers it looks like the worst offender in the library. Reading them
says otherwise.

- Most of the long ones are `claim` fields, and a claim is the formal statement
  of one argument's thesis: *"That from 'A belongs to every B' and 'B belongs to
  every C' it follows of necessity that A belongs to every C, in virtue of the
  arrangement of the terms and nothing else."* That is a single proposition. Cut
  it into three sentences and it is no longer the claim; it is three fragments
  of one.
- Most of the rest are enumerations separated by commas rather than semicolons,
  which the mechanical check does not recognise but the guide's own list
  exception covers: *"The order is the order of the quarrel: Anselm's reductio,
  Gaunilo's parody of its schema, Descartes' perfection-based restatement…"*
- The prose fields cross-reference derivation lines by number. Splitting a
  sentence that carries two such references risks separating a line number from
  what it is said to show.

So the 15-18 target is a target for **narrative prose about people**, which is
what it was measured on. It is not a target for the statement of an argument.
`tools/prosecheck.py` counts these as chains and overstates the work
accordingly; treat its formal-layer number as a prompt to look, not a defect
count.

## What this guide does not yet know

It rests on ten passages, one rewriting model, one prompt. It is strong on
sentence architecture because that is what the comparison actually measured, and
silent on vocabulary and paragraph order because the rewriter changed almost
neither. Before treating the 15-18 word target as settled for a new book,
sample that book and check the number holds — a chapter of physics derivation is
not a philosopher's biography, and may not want the same cadence.
