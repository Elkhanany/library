---
name: house-style
description: The library's prose style. Use when writing or revising any book text in this repository - chapter prose, clinical chapters, philosopher studies, formal-layer commentary, blurbs - and when reviewing a draft for readability. The Google developer documentation style guide is the base layer; this file carries the library's own measured rules on top of it, and the places where the two disagree.
---

# House style

Three layers, in this order of authority:

1. **The library's measured rules.** Derived from a controlled rewrite
   comparison on this corpus. Where they are stricter than the base layer, they
   win, because they were measured on these books rather than borrowed.
2. **The [Google developer documentation style guide](https://developers.google.com/style).**
   The base layer for everything the measurement did not cover: abbreviations,
   headings, claims, inclusive language, punctuation, tense.
3. **The declared deviations.** Six places where this library does not follow
   the guide, each with a reason. `python3 tools/stylecheck.py --deviations`
   prints them.

Two commands check a draft, and they check different things:

```bash
python3 tools/prosecheck.py <book>     # sentence architecture, the measured rule
python3 tools/stylecheck.py <book>     # the Google rules, per book
python3 tools/stylecheck.py --fix      # the corrections safe to apply mechanically
```

---

## Layer 1: the one rule

**Do not chain independent clauses. Give each its own sentence.**

This is the whole of what a controlled rewrite of ten passages actually changed.
Ten passages were sampled across the corpus to cover different failure modes,
each rewritten for readability by a different model under instructions to
preserve every epistemic marker and add nothing, then measured:

| | before | after |
|---|---|---|
| sentences | 41 | 61 (+49%) |
| words | 1,038 | 1,045 (+1%) |
| mean sentence length | 23-41 words | **15-18 words, every passage** |
| longest sentence | 71 words | 33 |
| semicolons joining independent clauses | 6 | 0 |
| epistemic markers lost | - | **0** |
| dates, names, numbers lost | - | **0** |

Words barely moved. Sentence count rose by half. Splitting is nearly free: it
cost 1% more words across ten passages and lost nothing.

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
are the numbers the rewrites converged on unprompted, across every passage. The
Google guide has no sentence-length rule at all, so this layer is the stricter
one and it governs.

### The exception, and it is a real one

**Lists are not chains. Leave them alone.**

Two of the ten passages came back completely untouched. One was already at 16.9
words a sentence. The other was at 27.7, well over target, and was still not
split, because its long sentences are enumerations rather than narrative:

> Three durable quarrels followed: Popper's indictment of the Republic; the
> analytic recovery of Plato as an arguer whose mistakes can be diagnosed; and
> the Tübingen school's claim that the unwritten doctrines are the true centre.

A colon introducing a series, and semicolons separating items that contain their
own commas, are doing work no full stop can do. The rule is about *clauses that
could stand alone*, not about length.

## Layer 1: what must survive untouched

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
- **What a number is a number of.** A hazard ratio without its comparison is
  decoration. Give the denominator, or do not imply one. This is a house rule
  rather than a Google one, and it is the rule the clinical book leans on most.

### Add nothing

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

### The trap, which fired on the first passage

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

### Settled by the comparison

- **The short sentence that ends a paragraph is a keeper, not a mannerism.**
  Every one of them survived, including the pseudo-cleft *"What reached
  Simplicius nine hundred years later was that quotation, not the book."*
- **Attribution goes first, not last.** The passage with seven ancient sources,
  all in leading position, came back verbatim. An earlier rule proposing
  trailing attributions is withdrawn.

---

## Layer 2: the Google guide

The full rule list, each with the page it comes from, is in
[google-guide.md](google-guide.md). What follows is what the guide changes about
how these books are written, in the order it will come up.

**Present tense.** Write what a trial *shows*, not what it *will show*. "Will"
is right only where the sentence is genuinely about the future, which in the
clinical book means a trial that has not reported.

**Active voice, where there is an actor.** Say who did the thing. A result
reported in the passive because the patient rather than the investigator is the
subject is correct and stays: *patients were randomised* has no better active
form that is also true.

**Sentence case in headings, and no full stop at the end of one.** The clinical
book is already there: of its 788 headings, `stylecheck.py` flags one, and that
one is a run of proper nouns rather than title case. The physics book has 30 to
look at.

**No first person plural.** No *we*, *us* or *our*. Say who did the thing, or
recast so nobody has to be named. The physics book is the declared exception:
its *we* is the reader and the writer working a derivation together.

**Spell the Latin out.** *for example*, *that is*, *and so on*, *compare*. Place
the comma yourself; this is the one substitution the tool reports and never
applies, because *"X, i.e. Y"* becomes *"X, that is, Y"* and the second comma is
a judgement.

**No unverifiable claim.** Not *seamless*, *state of the art*, *guarantees*. A
bare *best* is fine here and is not flagged: in this corpus every one of its 46
uses is a comparative judgement about evidence, and *best supportive care* is the
name of a trial arm.

**Nothing time-anchored.** *Currently* and *at present* date the page. Give the
date, or drop the word.

**Inclusive language.** No *he/she*, no gendered occupation nouns. `--fix`
applies these.

**Nothing anthropomorphic.** A trial does not see, want or know. Say what its
investigators did, or what its data show.

## Layer 3: where this library departs, and why

Six deviations, printed in full by `stylecheck.py --deviations`. In short:

| | the guide asks | this library | why |
|---|---|---|---|
| Spelling | American | **British** | 4,681 words, consistent; changing it would edit quoted trial names |
| Person | second person, "you" | **third person** | these are references, not tutorials; nobody is being walked through a task |
| Contractions | *don't*, *can't* | **full forms** | 299 contractions in a million words; the corpus does not use them |
| Em dash | unspaced | **spaced, or none** | the house typographic convention, 1,504 of them; the clinical book uses none at all |
| Word list | Google product names | **not applicable** | no book here has a product in it |
| Jargon | avoid field idiom | **per book** | the clinical reader is an oncologist; explaining *neoadjuvant* to them is a fault |

A deviation is overturned by arguing with its reason, not by preferring
something else. If you overturn one, edit `DEVIATIONS` in `tools/stylecheck.py`
and this table together.

---

## Where the layers do not apply

**The formal layer.** `formal.json` was measured against the sentence target and
deliberately **not** rewritten. It reads at a mean of 25.1 words a sentence with
59 sentences over 40 words, so by the numbers it looks like the worst offender in
the library. Reading them says otherwise.

- Most of the long ones are `claim` fields, and a claim is the formal statement
  of one argument's thesis: *"That from 'A belongs to every B' and 'B belongs to
  every C' it follows of necessity that A belongs to every C, in virtue of the
  arrangement of the terms and nothing else."* That is a single proposition. Cut
  it into three sentences and it is no longer the claim; it is three fragments
  of one.
- Most of the rest are enumerations separated by commas rather than semicolons,
  which the guide's own list exception covers.
- The prose fields cross-reference derivation lines by number. Splitting a
  sentence that carries two such references risks separating a line number from
  what it is said to show.

So the 15-18 target is a target for **narrative prose about people**, which is
what it was measured on. It is not a target for the statement of an argument.
`prosecheck.py` counts these as chains and overstates the work accordingly;
treat its formal-layer number as a prompt to look, not a defect count.

**The clinical book's own additions**, in `books/breast-cancer/CONVENTIONS.md`:
tables enumerate and prose argues, a figure appears once, biology is separated
from measurement, and a section is measured against the evidence it renders
rather than a word count. Those are stricter than anything here and they govern
that book.

## Mechanical

- Em-dash spacing: the spaced `&mdash;` form in the physics and philosophy
  books. None at all in the clinical book.
- Italicise the first occurrence of a work title or foreign term in each field,
  plain thereafter. This currently drifts inside single paragraphs.
- Prose in `formal.json` cross-references derivation lines by number ("line 6").
  No revision may renumber, merge or drop those lines, or merge two prose fields.
- The data files carry `<em>` tags and HTML entities that rendered text does not
  show. Anything revised outside the JSON must be re-rendered and diffed before
  it goes back in.

## What this guide does not yet know

Layer 1 rests on ten passages, one rewriting model, one prompt. It is strong on
sentence architecture because that is what the comparison actually measured, and
silent on vocabulary and paragraph order because the rewriter changed almost
neither. Before treating the 15-18 word target as settled for a new book, sample
that book and check the number holds: a chapter of physics derivation is not a
philosopher's biography, and may not want the same cadence.

Layer 2 is a faithful implementation rather than the guide itself.
`developers.google.com` is not reachable from this environment, so the rules
were taken from the [Vale `Google` style package](https://github.com/errata-ai/Google),
which cites the guide page behind each rule. Where a rule here and the guide
disagree, the guide is right.
