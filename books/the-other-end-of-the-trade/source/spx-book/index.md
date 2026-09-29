# The SPX/XSP Edge Book
## A textbook for high-conviction trading decisions

---

## What this book is

This is a **textbook**, not a memo. It is designed to teach you to *reconstruct* the trading framework from first principles, so that when a new edge or strategy appears in your feed, you can evaluate it correctly without relying on this document. The reviewer's framing is the right one:

> A memo says: "Index VRP is real but crash-correlated, trend-following diversifies, FOMC cycle is an overlay, GEX is context."
> A textbook teaches the reader to reconstruct that conclusion from first principles.

Each chapter follows the same teaching template:

1. **Core intuition** — one paragraph, simple language
2. **Toy example** — numbers small enough to reason about mentally
3. **Formal object** — the actual estimand or payoff
4. **Evidence** — what the literature shows
5. **Why it exists** — risk premium, behavioral, institutional, or microstructure
6. **Retail implementation** — how the concept degrades in real life
7. **Failure mode** — when does it break
8. **Decision rule** — what would make this a trade today
9. **Misconception box** — common mental traps
10. **Self-check** — retrieval prompts

This template is consistent across chapters because retrieval and spaced practice work better with predictable structure (Roediger & Karpicke, learning-science literature).

---

## How to read this book

**First pass (the learning arc).** Read Chapters 0–4 end-to-end. These are the primitives and the conviction framework. Don't skip the math — it's deliberately light but recurrent so it becomes instinctive.

**Second pass (the dossiers).** Read Chapters 5–10 as reference. Use the same teaching template across each so you can compare like-with-like.

**Third pass (operational).** Chapters 11–14 are operational: setup cards, allocation, kill criteria, monitoring. Return to these quarterly.

**Glossary and reading list (Chapter 15) are reference material.**

---

## Table of contents

### Part I — Primitives (the foundation)

- **[Chapter 0 — Primitives: distributions, tails, leverage, margin](01_ch00_primitives.md)**
  Return distributions, expected value, variance, skew, kurtosis, drawdown, leverage, margin, path dependency, correlation, tail correlation. The minimum vocabulary needed to read everything that follows.

- **[Chapter 1 — Why edges exist: the four sources](02_ch01_four_sources.md)**
  Compensated risk premia, behavioral frictions, institutional constraints, microstructure. The most common analytical error in trading is conflating these.

- **[Chapter 2 — The Sharpe ratio trap](03_ch02_sharpe_trap.md)**
  Why mean and variance aren't enough. Why short-vol strategies look better than they are. The rigorous framework for evaluating non-Gaussian payoffs.

- **[Chapter 3 — The retail-realism haircut](04_ch03_retail_haircut.md)**
  The four-layer haircut from academic Sharpe to user-account after-tax. Why a 0.8 paper Sharpe routinely becomes 0.25 in your account.

### Part II — The conviction framework

- **[Chapter 4 — High-conviction moves: a formal definition](05_ch04_conviction.md)**
  The conviction score C = E × M × R × X × S. What turns an "interesting trade" into a "high-conviction move." The trade admission checklist.

- **[Chapter 5 — Five-category taxonomy](06_ch05_taxonomy.md)**
  Foundation premia, factor tilts, structural overlays, regime filters, rejected/non-retail. Why this taxonomy determines sizing, persistence, and kill criteria.

### Part III — Edge dossiers

- **[Chapter 6 — Foundation premia: ERP, VRP, trend, carry](07_ch06_foundation_premia.md)**
  The four edges that anchor the portfolio. Each with full teaching template.

- **[Chapter 7 — Equity factor tilts: quality, momentum, value, low-vol](08_ch07_factor_tilts.md)**
  Modest incremental edges with multi-year drawdown patience required.

- **[Chapter 8 — Structural overlays: FOMC, EOQ, OPEX, Halloween](09_ch08_overlays.md)**
  Calendar and flow-based effects that modulate other premia. Not standalone strategies.

- **[Chapter 9 — Regime filters: VIX term structure, dealer gamma, liquidity](10_ch09_filters.md)**
  Variables that size other strategies up and down. Specifically NOT trades.

- **[Chapter 10 — Rejected and non-retail: what NOT to trade](11_ch10_rejected.md)**
  Pre-FOMC drift, S&P inclusion, single-name earnings short-vol, GEX scalping, condors, put-spread+LEAP. Why each is excluded.

### Part IV — Deep dives and operations

- **[Chapter 11 — Worked examples](12_ch11_worked_examples.md)**
  Ten worked examples that walk through reasoning end-to-end. The most valuable chapter for converting concepts into judgment.

- **[Chapter 12 — Setup cards](13_ch12_setup_cards.md)**
  One-page operational cards for every tradeable strategy and every "do-not-trade" pattern. The bridge from concept to execution.

- **[Chapter 13 — The signal-to-trade pipeline](14_ch13_pipeline.md)**
  Observation → interpretation → trade implication → sizing → invalidation. Every move passes through the same grammar.

- **[Chapter 14 — Portfolio framework, kill criteria, revalidation](15_ch14_portfolio_kill.md)**
  Capital allocation, monitoring cadence, behavioral kill criteria, the every-five-years thesis review.

### Reference

- **[Chapter 15 — Glossary, reading list, math summary](16_ch15_reference.md)**
  Vocabulary, primary sources, equation summary card.

---

## A note on humility

The literature is large and contested. Where I state something with high confidence, the underlying evidence is genuinely strong. Where I use hedged language, the uncertainty is real. Use this book as a thinking framework, not as gospel. The next 5 years will produce evidence that updates several rankings here, and the framework itself should be revisited periodically.

The most valuable habit this book imposes: **before allocating to any new "edge," ask which of the four sources it is, and which of the five categories it belongs to.** The answers determine sizing, persistence expectations, and kill criteria. If you can do that reliably, you have absorbed the book.
