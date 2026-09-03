# The review of August 2026

Five agents read Parts 0 to III — twenty-five chapters, 308,000 words, 19,993 typeset
expressions, 187 plain-language passages — and reported independently. Nothing in this
directory was written by the same process that wrote the book.

| Report | Scope | Result |
|---|---|---|
| `math-part0-I.md` | Every derivation in Chapters 0.1–1.4, re-derived in sympy | 0 BLOCKER · 1 MAJOR · 6 MINOR · 7 gaps in the chain |
| `math-part2-III.md` | Every derivation in Chapters 2.1–3.6, including a 50-row convention audit | 0 BLOCKER · 0 MAJOR · 3 MINOR · 3 gaps |
| `language.md` | Voice, terminology, notation, cross-references, callout discipline | 4 BLOCKER · 9 MAJOR · 15 MINOR |
| `plain-terms-arc.md` | All 187 plain-language passages read end to end as one essay | 58 forward promises tracked; 5 uncollected inside Parts 0–III |

Everything they found is applied. The two documents the review produced rather than
corrected — `../PLAN-FORWARD.md` and `../GAPS.md` — sit in the repository root.

## What the mathematics review actually established

Roughly ninety symbolic identities and forty numerical values were re-derived independently
and compared against the text. Agreement was often to the last printed digit: the drag
integral in 1.1 to eleven digits, the Fermat/Snell worked example to fifteen, the pendulum
periods in 1.3 to ten. In Part III the second Bianchi identity returns 1.0e−31 at sixty
decimal digits on a generic Lorentzian four-metric, and ∇^μG_{μν} returns 3.5e−32 against
scales of order 0.1. κ = +8πG/c⁴ follows from the book's own definitions rather than from
recall, and the weak-field sign — the one that would have produced anti-gravity if the
signature had slipped — checks out.

**No result in twenty-five chapters was found to be wrong.** Three printed values and signs
were: a straight-line descent time (0.8406 → 0.8412 s), a cross-term sign in a Christoffel
worked example, and one exponent in a problem solution. All three had correct final answers,
which is exactly why they had survived.

## What the language review found, which was worse

The ⚑ convention — the book's central promise, that a quoted result is always marked as
quoted — was **not applied at all in Chapters 0.1 to 0.7**, which nonetheless import eight
named theorems, several announcing the fact in words. A reader who had learned to scan for
the mark would have read the foundation as fully derived when it was not. That is now fixed
in place, and `GAPS.md` exists so it cannot recur silently.

## The standing rule this produced

An agent that writes a chapter cannot review it. Every part gets an independent pass before
the next part starts, by agents that read the plan and the prose and re-derive the
mathematics from scratch. Three of the errors caught across this build were in *the plan* —
mine, not the book's — which is the pipeline working as intended.
