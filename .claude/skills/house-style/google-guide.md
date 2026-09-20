# The Google guide, as this library implements it

Generated from `tools/stylecheck.py`, which is where the rules live. Edit the
tool, then regenerate this file:

    python3 tools/stylecheck.py --rules       > /tmp/rules
    python3 tools/stylecheck.py --deviations  > /tmp/dev

The canonical guide is at <https://developers.google.com/style>. Every rule
below links to the page it comes from, so a disagreement is settled against the
source. The implementation is taken from the Vale `Google` style package
(<https://github.com/errata-ai/Google>), because the guide's own pages are not
reachable from this environment.

## Levels

`error` is mechanical and unambiguous, and `--fix` applies the ones that can be
corrected without a judgement. `warning` is a real finding that wants a person
to choose the wording. `suggestion` is worth a look and wrong often enough not
to gate anything.

A book may lower or switch off a rule in `PROFILES`, with the reason written
next to it. Two do: the clinical book lowers `future-tense`, because an ongoing
trial has not reported and saying so is the point, and the physics book lowers
`first-person-plural`, because its `we` is the reader and the writer working a
derivation together.

## The rules

```
error      latin                https://developers.google.com/style/abbreviations
                                Write the English. The guide reserves Latin abbreviations for
                                parenthetical use and prefers them spelled out.
error      ordinal              https://developers.google.com/style/numbers
                                Spell out an ordinal in prose.
error      optional-plural      https://developers.google.com/style/plurals-parentheses
                                Do not use a parenthesised plural. Use the plural, or rewrite.
error      exclamation          https://developers.google.com/style/exclamation-points
                                No exclamation points in prose.
error      sentence-spacing     https://developers.google.com/style/sentence-spacing
                                One space after a full stop.
error      heading-period       https://developers.google.com/style/capitalization
                                No full stop at the end of a heading.
error      acronym-periods      https://developers.google.com/style/abbreviations
                                No full stops inside an acronym or initialism.
error      ly-hyphen            https://developers.google.com/style/hyphens
                                An adverb ending in -ly takes no hyphen after it.
error      range-words          https://developers.google.com/style/hyphens
                                Write the range out: 'from 5 to 10', not 'from 5-10'.
error      gender-pronoun       https://developers.google.com/style/pronouns
                                Use 'they', or recast the sentence.
error      gendered-term        https://developers.google.com/style/inclusive-documentation
                                Use the gender-neutral term.
error      slang                https://developers.google.com/style/abbreviations
                                No internet abbreviations.
warning    heading-case         https://developers.google.com/style/capitalization
                                Headings take sentence case.
warning    first-person-plural  https://developers.google.com/style/pronouns
                                Avoid the first person plural. Say who did the thing, or recast so
                                that nobody has to be named.
warning    future-tense         https://developers.google.com/style/tense
                                Prefer the present tense. 'Will' is right only where the sentence is
                                genuinely about the future, such as a trial that has not reported.
warning    excessive-claim      https://developers.google.com/style/excessive-claims
                                An unverifiable claim. Say the thing that can be checked.
warning    timeless             https://developers.google.com/style/timeless-documentation
                                Time-anchored wording dates the page. Say the date, or drop it.
warning    anthropomorphism     https://developers.google.com/style/anthropomorphism
                                A trial does not see or want. Say what its investigators did, or what
                                its data show.
suggestion parenthetical        https://developers.google.com/style/parentheses
                                A long parenthetical. Parentheses tell the reader the words inside
                                them matter less, which is rarely what is meant.
```

## Deliberate deviations from the Google developer documentation style guide

Spelling
  https://developers.google.com/style/spelling
  The guide asks for American spelling. This library is British throughout:
  randomised, tumour, oestrogen, haematological, centre. 4,681 words across
  the four books. Kept because it is consistent, because the clinical book's
  own sources are split between American and British journals, and because
  changing it would edit quoted trial names and endpoint wording.

Second person
  https://developers.google.com/style/person
  The guide asks the writer to address the reader as 'you'. These are
  expository references rather than tutorials. Nobody is being walked
  through a task, so there is no second party to address. First person
  plural is still avoided, which is the half of that rule that does apply.

Contractions
  https://developers.google.com/style/contractions
  The guide prefers 'don't' and 'can't'. The corpus carries 299 contractions
  in a million words, which is to say it does not use them. A clinical
  reference in contractions reads as a blog post about the evidence rather
  than as the evidence.

Em dash spacing
  https://developers.google.com/style/dashes
  The guide asks for an unspaced em dash. The philosophy and physics books
  use the spaced form, 1,504 of them, and that is the house typographic
  convention recorded in the house-style skill. The clinical book takes the
  stricter line and uses no em dash at all, because a dash aside is where a
  hedge goes to hide.

Word list
  https://developers.google.com/style/word-list
  Most of the guide's word list fixes Google product names: 'Container
  Engine' to 'Kubernetes Engine', 'url' to 'URL'. No book here has a product
  in it. The parts that are ordinary English, such as the gendered
  occupation terms, are implemented.

Jargon
  https://developers.google.com/style/jargon
  The guide's jargon list is developer idiom: break-glass, swim lane,
  out-of-the-box. A clinical reference for oncologists is written in the
  register of its field, and explaining what neoadjuvant means to that
  reader is a fault rather than a courtesy. Jargon is governed per book.

```

Spelling
  https://developers.google.com/style/spelling
  The guide asks for American spelling. This library is British throughout:
  randomised, tumour, oestrogen, haematological, centre. 4,681 words across
  the four books. Kept because it is consistent, because the clinical book's
  own sources are split between American and British journals, and because
  changing it would edit quoted trial names and endpoint wording.

Second person
  https://developers.google.com/style/person
  The guide asks the writer to address the reader as 'you'. These are
  expository references rather than tutorials. Nobody is being walked
  through a task, so there is no second party to address. First person
  plural is still avoided, which is the half of that rule that does apply.

Contractions
  https://developers.google.com/style/contractions
  The guide prefers 'don't' and 'can't'. The corpus carries 299 contractions
  in a million words, which is to say it does not use them. A clinical
  reference in contractions reads as a blog post about the evidence rather
  than as the evidence.

Em dash spacing
  https://developers.google.com/style/dashes
  The guide asks for an unspaced em dash. The philosophy and physics books
  use the spaced form, 1,504 of them, and that is the house typographic
  convention recorded in the house-style skill. The clinical book takes the
  stricter line and uses no em dash at all, because a dash aside is where a
  hedge goes to hide.

Word list
  https://developers.google.com/style/word-list
  Most of the guide's word list fixes Google product names: 'Container
  Engine' to 'Kubernetes Engine', 'url' to 'URL'. No book here has a product
  in it. The parts that are ordinary English, such as the gendered
  occupation terms, are implemented.

Jargon
  https://developers.google.com/style/jargon
  The guide's jargon list is developer idiom: break-glass, swim lane,
  out-of-the-box. A clinical reference for oncologists is written in the
  register of its field, and explaining what neoadjuvant means to that
  reader is a fault rather than a courtesy. Jargon is governed per book.

```
