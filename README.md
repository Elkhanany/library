# From Newton to M-Theory

A build-it-yourself book on modern physics: special relativity, general relativity, quantum
mechanics, quantum field theory, the Standard Model and string theory — **derived, not asserted**.

**Read it:** https://USERNAME.github.io/REPO/

The rule the book is written under is that nothing appears which has not been built. Where a
result is quoted rather than derived it carries a ⚑ so the reader always knows what they are
standing on. Routine algebra folds into collapsible boxes; the reasoning stays on the page.

There are three ways through the same material:

| | |
|---|---|
| **Chapters** | The full derivations, with interactive figures and worked problems. |
| **In Plain Terms** | Every plain-language passage in the book, collected in order and readable as one continuous essay with no mathematics in it. |
| **Math Ledger** | Every mathematical object: where it was introduced, what question it answers, and every later chapter that spends it. |

---

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
build.py              stage 1 — assembles fragments into whole pages
make.py               the offline build   → build/   (self-contained, one file per chapter)
webbuild.py           the website build   → docs/    (shared assets, GitHub Pages)
throughline.py        regenerates src/_throughline.html by extraction
inject_plain.py       inserts "In plain terms" boxes into a chapter, idempotently
verify.py             audits every built page with all network blocked
overflow_check.py     measures real horizontal overflow of typeset maths
```

## Building

```bash
pip install playwright && playwright install chromium

python3 make.py        # → build/   self-contained pages; works offline, works in Dropbox
python3 webbuild.py    # → docs/    the website; this is what GitHub Pages serves
python3 verify.py      # audit: no network, no KaTeX errors, no overflow, no dead refs
```

Both builds render the mathematics **at build time** in headless Chromium and write the finished
DOM to disk. Nothing is typeset in the reader's browser, so pages paint immediately, work with no
network, and survive being previewed one file at a time by a file-sync client.

`build/` inlines the stylesheet and base64 maths fonts into every page — right for Dropbox, where
each file is opened in isolation and relative paths do not resolve. `docs/` shares one stylesheet
and one set of font files — right for a web server, where the browser caches them once. Same
source, two targets.

## Publishing

GitHub Pages serves `docs/` on the default branch: **Settings → Pages → Source: Deploy from a
branch → `main` / `/docs`**. The `.nojekyll` file in `docs/` stops Jekyll from eating paths that
begin with an underscore.

## Conventions

Binding throughout, and enforced by review:

- Metric signature **(+, −, −, −)**.
- Riemann tensor from `[∇μ, ∇ν] Vρ = R^ρ_σμν V^σ`.
- `G` and `c` kept explicit. No natural units without saying so.
- Every equation numbered at build time; cross-references resolved at build time.
- Every quoted-not-derived step marked ⚑.

`CONVENTIONS.md` has the full list.

## The documents

| | |
|---|---|
| `PLAN.md` | The curriculum. Plan of record through Chapter 3.6. |
| `PLAN-FORWARD.md` | The revised curriculum from 3.7 to the end — 59 chapters to 67, with the argument for each addition and, for every piece of mathematics the remaining physics needs, an explicit decision to build it or to flag it. |
| `GAPS.md` | The standing register of what the book has used but not built: every ⚑ in one table, the unstated assumptions that are worse than a ⚑ because the reader cannot see them, the promises not yet collected, and the gaps that will never close. |
| `CONVENTIONS.md` | Notation, spelling, callout obligations, the ⚑ contract. |
| `PLAIN-TERMS-PLAN.md` | The specification the plain-language passages are written against. |
| `MATHPLAN-3.md` | The derivation-by-derivation plan Part III was written to, and the model for the ones after it. |
| `reports/` | The August 2026 review — five independent agents over Parts 0–III. `reports/README.md` says what they found. |

## Reviewing

An agent that writes a chapter cannot review it. Each part gets an independent pass before the next
part begins: one agent per concern (mathematics, language, narrative), each re-deriving rather than
reading, each reporting to `reports/` rather than editing, so their findings can be applied in one
serialized pass and nothing is silently clobbered.
