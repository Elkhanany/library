<div align="center">

<sub>A BUILD-IT-YOURSELF BOOK</sub>

# From Newton to M-Theory

**Special relativity, general relativity, quantum mechanics, quantum field theory,
the Standard Model and string theory — derived, not asserted.**

### [→ Read it online](https://elkhanany.github.io/newton-to-mtheory/)

[Contents](https://elkhanany.github.io/newton-to-mtheory/contents.html) ·
[In Plain Terms](https://elkhanany.github.io/newton-to-mtheory/throughline.html) ·
[Math Ledger](https://elkhanany.github.io/newton-to-mtheory/ledger.html) ·
[Status](STATUS.md) ·
[Conventions](CONVENTIONS.md) ·
[Gaps](GAPS.md)

<sub>28 of 67 chapters · 360,000 words · 22,616 typeset expressions ·
210 plain-language passages · 0 network requests</sub>

</div>

---

> Ask what stays the same when you change your point of view. Whatever survives is real;
> whatever does not was a fact about where you were standing.

Seven subjects, one idea — pick a symmetry, write the most general law invariant under it, then
quantise. Each part is that sentence wearing different clothes.

The book is written for someone who can grasp anything but wants the bricks laid one at a time.
It starts at the definition of a derivative and does not skip.

## The rule

**Nothing appears which has not been built.** There is no "it can be shown that". Where a result
is quoted rather than derived it carries a **⚑**, so the reader always knows what they are
standing on — and every ⚑ in the book is collected in [`GAPS.md`](GAPS.md), ranked by what the gap
costs the reader. Routine algebra folds into collapsible boxes; the reasoning stays on the page.

## Three ways through the same material

They cross-reference each other, so you can move between them at any point.

| | |
|---|---|
| **[Chapters](https://elkhanany.github.io/newton-to-mtheory/contents.html)** | The full derivations, with interactive figures, worked examples, and problems whose solutions unfold when you want them. |
| **[In Plain Terms](https://elkhanany.github.io/newton-to-mtheory/throughline.html)** | Every plain-language passage in the book, collected in order and readable as one continuous essay. No equations anywhere in it. It stands entirely on its own. |
| **[Math Ledger](https://elkhanany.github.io/newton-to-mtheory/ledger.html)** | Every mathematical object: where it was introduced, the question it was invented to answer, and every later chapter that spends it. Follow any symbol back to its origin. |

## Contents

**Part 0 · The Toolkit** — the mathematics, built from scratch

[0.1](https://elkhanany.github.io/newton-to-mtheory/ch0-1.html) What a Derivative Really Is ·
[0.2](https://elkhanany.github.io/newton-to-mtheory/ch0-2.html) Integration and Accumulation ·
[0.3](https://elkhanany.github.io/newton-to-mtheory/ch0-3.html) Series, Approximation, Orders of Magnitude ·
[0.4](https://elkhanany.github.io/newton-to-mtheory/ch0-4.html) Vector Spaces and Linear Maps ·
[0.5](https://elkhanany.github.io/newton-to-mtheory/ch0-5.html) Inner Products, Eigenvectors, and the Spectral Theorem ·
[0.6](https://elkhanany.github.io/newton-to-mtheory/ch0-6.html) Multivariable Calculus ·
[0.7](https://elkhanany.github.io/newton-to-mtheory/ch0-7.html) Fields, Flux, and the Big Theorems ·
[0.8](https://elkhanany.github.io/newton-to-mtheory/ch0-8.html) Differential Equations and the Oscillator ·
[0.9](https://elkhanany.github.io/newton-to-mtheory/ch0-9.html) Fourier, Delta Functions, and Probability

**Part I · The Action Principle**

[1.1](https://elkhanany.github.io/newton-to-mtheory/ch1-1.html) What's Wrong With Forces ·
[1.2](https://elkhanany.github.io/newton-to-mtheory/ch1-2.html) Stationary Action ·
[1.3](https://elkhanany.github.io/newton-to-mtheory/ch1-3.html) Hamilton and Phase Space ·
[1.4](https://elkhanany.github.io/newton-to-mtheory/ch1-4.html) Noether's Theorem

**Part II · Special Relativity**

[2.1](https://elkhanany.github.io/newton-to-mtheory/ch2-1.html) The Crisis of 1900 ·
[2.2](https://elkhanany.github.io/newton-to-mtheory/ch2-2.html) The Lorentz Transformation, Derived ·
[2.3](https://elkhanany.github.io/newton-to-mtheory/ch2-3.html) Minkowski Geometry ·
[2.4](https://elkhanany.github.io/newton-to-mtheory/ch2-4.html) Tensors, Honestly ·
[2.5](https://elkhanany.github.io/newton-to-mtheory/ch2-5.html) Relativistic Dynamics ·
[2.6](https://elkhanany.github.io/newton-to-mtheory/ch2-6.html) Electromagnetism Is Relativity

**Part III · General Relativity** — 6 of 8; 3.7 Schwarzschild and 3.8 Cosmology are next

[3.1](https://elkhanany.github.io/newton-to-mtheory/ch3-1.html) The Equivalence Principle ·
[3.2](https://elkhanany.github.io/newton-to-mtheory/ch3-2.html) Manifolds ·
[3.3](https://elkhanany.github.io/newton-to-mtheory/ch3-3.html) Metric and Connection ·
[3.4](https://elkhanany.github.io/newton-to-mtheory/ch3-4.html) Curvature ·
[3.5](https://elkhanany.github.io/newton-to-mtheory/ch3-5.html) Forms, Lie Derivatives, Killing Vectors ·
[3.6](https://elkhanany.github.io/newton-to-mtheory/ch3-6.html) The Einstein Field Equations

**Parts IV–VII** — quantum mechanics, quantum field theory, the Standard Model, string theory.
Not started. [`PLAN-FORWARD.md`](PLAN-FORWARD.md) is the curriculum.

## Building

```bash
pip install playwright && playwright install chromium
```

```bash
python3 make.py && python3 webbuild.py && python3 verify.py
```

`make.py` → `build/` (self-contained pages; works offline, works in Dropbox).
`webbuild.py` → `docs/` (the website; this is what GitHub Pages serves).
`verify.py` is the audit: no network, no KaTeX errors, no overflow, no dead refs.

Both builds render the mathematics **at build time** in headless Chromium and write the finished
DOM to disk. Nothing is typeset in the reader's browser, so pages paint immediately, work with no
network, and survive being previewed one file at a time by a file-sync client.

`build/` inlines the stylesheet and base64 maths fonts into every page — right for Dropbox, where
each file is opened in isolation and relative paths do not resolve. `docs/` shares one stylesheet
and one set of font files — right for a web server, where the browser caches them once. Same
source, two targets.

`verify.py` is the gate that matters: it opens every built page at desktop and phone widths **with
all network requests blocked**, and fails if any equation did not typeset, any cross-reference did
not resolve, any mathematics overflows its column, or any page tries to reach the internet.

## Publishing

GitHub Pages serves `docs/` on the default branch: **Settings → Pages → Source: Deploy from a
branch → `main` / `/docs`**. The `.nojekyll` file in `docs/` stops Jekyll from eating paths that
begin with an underscore. Publishing a new chapter is then:

```bash
python3 webbuild.py && git add -A && git commit -m "Chapter 3.7" && git push
```

`docs/` is committed deliberately rather than built by an Action: the published site is exactly
the bytes last verified locally, rather than whatever a build server produced, and the repository
has no CI to break.

## Layout

```
src/                  chapter sources — HTML fragments, one per chapter
  _ledger.html        the Math Ledger (hand-maintained)
  _throughline.html   the Through-Line (GENERATED — do not edit)
  _landing.html       the landing-page template
assets/
  book.css            the whole house style
  book.js             theme toggle, KaTeX macros, equation numbering, NMT.Plot
vendor/katex/         KaTeX, vendored so every page works with no network
docs/                 the website — generated by webbuild.py, never edited by hand
build/                the offline copy — generated by make.py, not committed (50 MB of fonts)

build.py              stage 1 — assembles fragments into whole pages
make.py               the offline build   → build/   (self-contained, one file per chapter)
webbuild.py           the website build   → docs/    (shared assets, GitHub Pages)
throughline.py        regenerates src/_throughline.html by extraction
inject_plain.py       inserts "In plain terms" boxes into a chapter, idempotently
verify.py             audits every built page with all network blocked
overflow_check.py     measures real horizontal overflow of typeset maths
```

## Conventions

Binding throughout, and enforced by review:

- Metric signature **(+, −, −, −)**.
- Riemann tensor from `[∇μ, ∇ν] Vρ = R^ρ_σμν V^σ`.
- `G` and `c` kept explicit. No natural units without saying so.
- Every equation numbered at build time; cross-references resolved at build time.
- Every quoted-not-derived step marked ⚑.

[`CONVENTIONS.md`](CONVENTIONS.md) has the full list.

## The documents

| | |
|---|---|
| [`STATUS.md`](STATUS.md) | Where the book stands and how to resume. **Read this first.** |
| [`PLAN.md`](PLAN.md) | The curriculum. Plan of record through Chapter 3.6. |
| [`PLAN-FORWARD.md`](PLAN-FORWARD.md) | The revised curriculum from 3.7 to the end — 59 chapters to 67, with the argument for each addition and, for every piece of mathematics the remaining physics needs, an explicit decision to build it or to flag it. |
| [`GAPS.md`](GAPS.md) | The standing register of what the book has used but not built: every ⚑ in one table, the unstated assumptions that are worse than a ⚑ because the reader cannot see them, the promises not yet collected, and the gaps that will never close. |
| [`CONVENTIONS.md`](CONVENTIONS.md) | Notation, spelling, callout obligations, the ⚑ contract. |
| [`PLAIN-TERMS-PLAN.md`](PLAIN-TERMS-PLAN.md) | The specification the plain-language passages are written against. |
| [`MATHPLAN-3.md`](MATHPLAN-3.md) | The derivation-by-derivation plan Part III was written to, and the model for the ones after it. |
| [`reports/`](reports/) | The August 2026 review — five independent agents over Parts 0–III. `reports/README.md` says what they found. |

## How it is reviewed

An agent that writes a chapter cannot review it. Each part gets an independent pass before the
next part begins: one agent per concern (mathematics, language, narrative), each re-deriving
rather than reading, each reporting to `reports/` rather than editing, so their findings can be
applied in one serialized pass and nothing is silently clobbered.

The August 2026 review found no wrong result in twenty-five chapters — about ninety symbolic
identities and forty numerical values re-derived from scratch and agreed. The material finding was
editorial, and it is why [`GAPS.md`](GAPS.md) now exists: the ⚑ convention had not been applied at
all in Chapters 0.1–0.7, which import eight named theorems and marked none.
