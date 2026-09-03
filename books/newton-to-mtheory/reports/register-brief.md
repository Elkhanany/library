# Brief: converting a chapter to the plain-language register

You are rewriting **one chapter file in place**. Read these three things before you touch it:

1. `reports/register-sample.md` — the reader's own rewrite of Chapter 2.1 §1. **This is binding.**
   Where anything below disagrees with it, the sample wins. Match its rhythm.
2. `CONVENTIONS.md`, the section *"The plain-language register (the `clear` tag)"* — eleven numbered
   directives.
3. `src/ch1-1.html` and `src/ch1-3.html` — two chapters already converted and passing. Read at least
   a few thousand words of one of them so you have the target voice in your ear.

## The job

Same content, different delivery. Nothing is added, nothing is cut, nothing is corrected. Every
claim, number, hypothesis and derivation step stays exactly as it is. You are re-saying the
connective prose so a rusty-but-strong reader can follow it without re-reading.

The reader is a breast medical oncologist. Strong mathematically, rebuilding physics from scratch.
He reads the "In plain terms" boxes comfortably and finds the main text dense and theatrical.

## Hard invariants — these are checked byte-for-byte by `registercheck.py`

- Every `<div class="eq">…</div>` — **do not touch a single character inside one.**
- Every `<h1> <h2> <h3> <h4>` heading and its numbering.
- Every `<!--SCRIPT-->…<!--/SCRIPT-->` block.
- Every `<figure>` and its `<figcaption>`.
- Every `id=`, every `eqref`/`ref` anchor, every cross-reference target.
- Every ⚑ and ⚠ and what it attaches to.
- **Every `<div class="callout plain">` ("In plain terms") box, verbatim.** These already work.

## Targets — also enforced by `registercheck.py`

| | limit |
|---|---|
| em-dashes | ≤ 1.0 per 1000 prose words |
| semicolons | ≤ 2.5 per 1000 prose words |
| sentences over 35 words | ≤ 14% |
| abrupt equation bridges (≤ 8 words between two displays) | < 3% |
| length | 85–140% of the original |

Em-dashes and semicolons are the main lever. The original runs 8–11 em-dashes per thousand words.
Almost every one of them is a place where two ideas were welded together: **split there.** That
alone gets most of the way.

## The commonest failure, and how to avoid it

**Directive 9, equation bridges.** Never hand the reader a second display equation straight after
the first with nothing said in between. State the *goal* of the next step before taking it:

> "Now that we have the potential energy, our next goal is to isolate the velocity, so differentiate
> both sides."

The algebra being all present is not the same as the thread being followable. This is where the
thread drops.

## Register notes

- Motive before mathematics. *"We want a scalar out of a vector equation, so dot both sides with
  $\vv v$."* Never the operation first.
- Signpost each section in plain English before entering it.
- Pause on what matters: *"Let's look at what that last line is actually saying."*
- Point forward concretely, not ominously. Not *"this will haunt us"* but *"we will need this in
  Chapter 3.4, where the metric stops being constant."*
- Bullets where a two-sided comparison would tangle in prose.
- Everyday anchors only where they are exact. A wrong analogy is worse than none.
- Short paragraphs. Let the page breathe.
- Translate the fine print: when the text hits a caveat, say why it matters rather than stating it
  as a dry rule.
- **"We", "let's" and "you" are allowed here** and this register deliberately overrides the
  second-person-only rule.
- Still forbidden: *obviously, clearly, of course, it turns out that, it can be shown*, and *simply*
  used to wave past work.
- Do **not** hedge to sound collaborative. The fix is subtractive: delete the dash, split the
  sentence. Adding "perhaps" and "one might say" makes it worse.

## HTML hazard

`<` followed by a letter opens a bogus tag and silently deletes text to the next `>`. Inside math use
`\lt` and `\gt`. Never type `$a<b$`.

## First line of the file

The converted file must begin with exactly:

```
<!--REGISTER:clear-->
```

as line 1, before the `<p class="eyebrow">` line.

## When you are done

Run:

```
python3 registercheck.py /tmp/before0/chX-Y.html src/chX-Y.html
```

It must print PASS on every line. If it does not, fix and re-run. Do not report back until it passes.

Then report: the before/after numbers it printed, and anything in the original you believe is a
factual error (do **not** fix it — report it).
