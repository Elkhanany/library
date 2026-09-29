# Chapter 5 — Five-category taxonomy
## How edges fit into a portfolio

> **Core intuition.** Once you know an edge's source (Chapter 1) and have scored its conviction (Chapter 4), you need to know *how* it fits into a portfolio. That's what the five-category taxonomy does. Different categories require different sizing rules, different persistence assumptions, and different kill criteria.

---

## 5.1 Why categories matter

In v1 of this framework, all edges were ranked in a single table. This implied false comparability: ERP and OPEX-week tilt aren't the same kind of object and shouldn't compete for allocation against each other. The five-category taxonomy fixes this by separating *what kind of edge it is* from *how strong the evidence is* from *how much capital it should get*.

The categories:

1. **Foundation premia** — risk premia that anchor the portfolio
2. **Equity factor tilts** — systematic deviations from cap-weight that produce excess returns
3. **Structural / tactical overlays** — calendar or flow-based effects that modulate other premia
4. **Regime filters** — variables that size other strategies; not standalone trades
5. **Rejected or non-retail** — decayed, never-robust, or institutional-only

Each category has a different role and different operational rules.

---

## 5.2 Category A: Foundation premia

### Definition
Compensated risk premia paid for bearing non-diversifiable risk. These should anchor the portfolio.

### Examples
- Equity Risk Premium (ERP) — long equities
- Index Variance Risk Premium (VRP) — selling index volatility
- Trend-following / TSMOM — systematic trend across assets
- Cross-asset Carry — buying high-carry assets

### Source classification
Almost all foundation premia are *risk premia* (Source 1 from Chapter 1). They're the most durable category because the premium exists for structural reasons that don't disappear when capital exploits them.

### Allocation role
Foundation premia anchor the portfolio. Typical aggregate allocation: 60-70% of portfolio risk.

### Sizing principles
- Size based on long-run expectation, not recent performance
- Use stressed-vol assumptions for short-vol foundation sleeves (VRP)
- Assume 35-50% drawdowns will happen and ensure portfolio survives
- Don't reduce allocation during drawdowns — they're the cost of the premium

### Persistence
High. These edges have been documented across centuries and survive in different regulatory environments. ERP has been positive in 35 of 35 markets in the Dimson-Marsh-Staunton database. VRP has been positive in roughly 80% of months for 30+ years. Trend has been positive in every decade since 1880.

### Decay risk
Limited. Premia compress when investor demand for the underlying risk shifts (e.g., higher equity allocations have compressed forward ERP). They don't go to zero.

### Kill criteria (foundation)
Foundation premia don't get "turned off" — they get *sized down* in adverse regimes. Specific kill criteria are in Chapter 14.

---

## 5.3 Category B: Equity factor tilts

### Definition
Systematic deviations from market-cap weighting that have produced positive long-run excess returns within equity markets.

### Examples
- Quality / Profitability (RMW, QMJ) — long high-quality stocks
- Momentum (CSMOM) — long winners, short losers
- Value (HML) — long cheap, short expensive
- Low-volatility / BAB — long low-beta, short high-beta
- Size conditional on quality — long small high-quality

### Source classification
Mixed: mostly *behavioral* (Source 2) with *risk premium* and *institutional* components. Quality is the most risk-premium-flavored; momentum is the most behavioral.

### Allocation role
Tilts within the equity sleeve. Typical aggregate allocation: 15-30% of equity sleeve, expressed via factor ETFs.

### Sizing principles
- Tilt rather than concentrate — don't replace SPX with pure factor ETFs
- Diversify across factors (quality + momentum + low-vol better than any single factor)
- Plan for multi-year drawdowns
- Don't try to time factor rotation

### Persistence
Medium. Behavioral edges decay post-publication (Jensen-Kelly-Pedersen 2023 documented ~47% post-pub decline). Quality has held up best; size and naive value have struggled.

### Decay risk
Real. Some factors have already decayed substantially (size standalone, naive value 2010-2020). Others (quality, momentum) have decayed less but compressed.

### Kill criteria
- 24-month rolling Sharpe < 0 → reduce allocation 50%
- Tracking error to academic factor > 4% annualized → switch vehicle
- Multi-decade drawdowns are tolerable if you're committed to the long-run; don't allocate if you'd panic-exit

---

## 5.4 Category C: Structural / tactical overlays

### Definition
Calendar or flow-based effects that *modulate exposure to other premia* rather than serving as standalone strategies.

### Examples
- Cieslak FOMC even-week cycle — equity premium concentrated in even weeks
- End-of-quarter rebalancing flow — pension rebalancing creates predictable flow
- Halloween / Sell-in-May — seasonal pattern
- OPEX-week tilt — monthly options expiration effects
- Turn-of-month — month-end cash flow timing

### Source classification
Mostly *institutional frictions* (Source 3) and some *behavioral* (Source 2). Halloween is a mystery — it persists but no clean mechanism.

### Allocation role
Overlays on existing positions. Typical aggregate allocation: 10-15% of portfolio risk *as modulation*, not as separate sleeves. They scale equity exposure up or down rather than running separate strategies.

### Sizing principles
- Express via existing instruments (ETF rotation, futures sizing) rather than new strategies
- Don't add transaction costs that eat the small premiums
- Most overlays add 10-30 bps of Sharpe; verify the implementation cost is well below this

### Persistence
Variable. Some (FOMC cycle, EOQ rebalancing) have clear mechanisms and seem persistent. Others (OPEX, Halloween) have empirical patterns but unclear mechanisms; persistence is uncertain.

### Decay risk
Real. Some have already decayed (S&P inclusion went from 7% to <1%). Others (OPEX) may be diluting due to weekly/0DTE options. Track for evidence of decay.

### Kill criteria
- Effect underperforms baseline by > 50% over 4 cycles → suspend
- Implementation costs exceed expected edge → simplify or stop
- Mechanism changes (regulatory, product structure) → reassess

---

## 5.5 Category D: Regime filters

### Definition
Variables used to size up or down exposure to other strategies. **NOT standalone edges.**

### Examples
- VIX term structure (contango/backwardation)
- Realized vs implied volatility
- Liquidity regime (TED spread, MOVE index, credit spreads)
- Dealer gamma sign (low confidence)
- Breadth and internals

### Source classification
These are *informational* signals about regime, not edges to trade. The "edge" they create is in the form of *avoided losses* on other strategies, not direct returns.

### Allocation role
Zero direct allocation. They modulate other allocations.

### Sizing principles
- Define the rule explicitly (e.g., "VIX/VIX3M > 1.05 for 3 days → halt new put sales")
- Phase changes in/out over multiple days to avoid whipsaw
- Don't trade the filter itself (e.g., don't buy VXX because VIX is in contango — VXX has lost 99.84% from roll decay)

### Persistence
High at the *information* level. The fact that VIX backwardates in stress is structural and persistent. Specific level rules may need recalibration.

### Decay risk
Low for the underlying signal; meaningful for specific implementation rules. The filter framework persists; the threshold values may need adjustment.

### Kill criteria
- The rule produces persistent false positives (>50% of "stress" calls have no follow-through) → recalibrate
- The underlying signal becomes unavailable or unreliable → switch source

---

## 5.6 Category E: Rejected or non-retail

### Definition
Either decayed (the edge is gone), never-robust (the evidence was never strong), or institutional-only (real edge but inaccessible to retail).

### Examples
- Pre-FOMC announcement drift — decayed post-2015
- S&P inclusion premium — decayed post-2010
- Naive single-name earnings short-vol — institutional-only and high tail risk
- GEX-level scalping — narrative-driven, not validated post-2022
- Systematic iron condors (CNDR-style) — empirically underperform massively
- 1-year put-spread + LEAP combo — leverage with extra steps, not edge
- VIX-futures roll-yield short (XIV/SVXY) — catastrophic tails

### Why this category matters

Most retail trading content focuses on Category E strategies. They're *vivid* (specific narratives, dramatic claims), *easy to backtest* (because the data is clean), and *frequently traded* (high volume in trading communities). But they don't survive evidence-tier evaluation.

Knowing what NOT to trade is half the battle. A textbook should teach negative space explicitly.

### Allocation role
Zero. These are documented for reference and to inoculate the reader against narrative-driven retail bait.

### Why each is rejected

- **Pre-FOMC drift:** Kurov-Halova-Wolfe-Gilbert (2021) document the effect disappeared after 2015 due to forward guidance reforms.
- **S&P inclusion:** Greenwood-Sammon (2024) document <1% effect post-2010 vs. 7%+ in the 1990s.
- **Naive earnings short-vol:** Adams-Neururer (2020) show negative mean despite positive median; institutional cross-sectional version exists (Cao-Han-Tong-Zhan 2022) but requires 200-name infrastructure.
- **GEX scalping:** Cboe 2025 estimates 0DTE MM hedging is ~0.2% of liquidity; level-trading rules don't validate post-2022.
- **CNDR systematic condors:** ~690% return 1986-2024 vs ~5,500% for SPX TR — empirical underperformance.
- **Put-spread + LEAP:** Chapter 11 worked example shows it's economically equivalent to ~1.4× SPX with worse path properties.
- **VIX ETPs (long or short):** VXX has lost 99.84% from roll decay; XIV terminated -96% in a day in 2018.

### What about partial use?

Some Category E items have legitimate *informational* use even though the trade is rejected:
- GEX directional sign as low-confidence regime context (not specific levels)
- Earnings calendar awareness for risk-management (avoid being caught long premium into a print)
- VIX term structure as a filter (Category D, not as a trade)

But the trades themselves stay rejected. The information is useful; the implementations are not.

---

## 5.7 The category-source matrix

Showing how the five categories map to the four sources:

| Source ↓ / Category → | Foundation | Factor | Overlay | Filter | Rejected |
|---|---|---|---|---|---|
| Risk premium | ERP, VRP, Trend, Carry | (some quality) | | | |
| Behavioral | | Momentum, Value, (some quality) | (some) | | |
| Institutional | | BAB | EOQ rebalance, FOMC cycle | | (S&P inclusion) |
| Microstructure | | | (OPEX, partial) | Dealer gamma sign | GEX scalping |

**Reading the matrix.**
- Risk premia tend to become Foundation sleeves. Most durable.
- Behavioral edges tend to become Factor tilts. Decay risk.
- Institutional frictions tend to become Overlays. Regulatory risk.
- Microstructure tends to be Rejected for retail. Capacity issues.

The mapping isn't deterministic but it's predictive. If you find an edge that's purely microstructure but you're trying to make it a foundation sleeve, you're doing something wrong.

---

## 5.8 Three ranking tables (not one)

In v1, all edges were ranked in a single table. This implied false comparability. In v2 we separated three orthogonal questions, and v3 (this textbook) keeps that separation. The three tables answer:

### Table 1: Evidence quality

What does the academic literature say? Is this T1 (peer-reviewed, replicated, multi-decade), T2 (strong empirical but methodology-sensitive), or T3 (thin or decayed)?

### Table 2: Retail implementation viability

After applying the four-layer haircut from Chapter 3, what's the realistic user-account Sharpe? Is the strategy implementable for a retail account at all?

### Table 3: Crash behavior

How does this strategy behave in 2008, March 2020, 2022? What's the tail beta? Does it diversify the portfolio in stress, or does it correlate with everything else premium-selling?

These three questions have different answers for different strategies. A strategy can be T1 evidence (e.g., index VRP), have OK retail implementation (Sharpe 0.30 user-account), and still be problematic for portfolio construction (tail beta ~1.0 in left tail).

The point of separation: don't optimize for one and ignore the others. Trend has middling Sharpe but uniquely diversifying behavior — its portfolio value is in Table 3, not Table 2.

---

## 5.9 Application: how to use the taxonomy

When evaluating a candidate move:

1. **Source first.** Which of the four sources is this? (Chapter 1)
2. **Category second.** Where in the taxonomy does it fit?
3. **Conviction third.** Score the move (Chapter 4).
4. **Implementation fourth.** What's the right vehicle, sizing, and kill rule for this category?

A foundation premium gets foundation-style implementation: long-term, sized for stress, mechanical execution. An overlay gets overlay-style: ETF rotation or simple sizing modulation, no derivatives unless capital justifies. A filter gets filter-style: don't trade it directly, use it to size other things.

Mixing categories is the most common operational error. Examples:

- Treating GEX scalping (rejected) as a foundation sleeve → systematic capital destruction
- Treating end-of-quarter rebalancing (overlay) as a primary income source → overconfidence in a small effect
- Treating VIX term structure (filter) as a trade via VIX ETPs → catastrophic roll decay
- Treating value (factor) as a market-timing signal rather than a structural tilt → exits during the inevitable drawdown

The taxonomy prevents these mismatches.

---

## 5.10 Misconception box

> **Misconception:** "If I have multiple edges, I can stack them in one sleeve for better Sharpe."
>
> **Correction:** Some edges combine; many don't. Foundation premia (ERP + VRP + Trend) combine well because the underlying risk premia are partially independent. Factor tilts within equity (quality + momentum) combine modestly. But mixing categories — using a regime filter as a trade, or stacking many overlays expecting independence — usually produces correlated bets disguised as diversification. Sleeves should be evaluated as sleeves, with explicit attention to correlation in stress (Table 3 above).

---

## 5.11 Self-check

1. Name the five categories. Which is most durable? Which has the highest decay risk?
2. State the source-category mapping. Why do risk premia usually become foundation sleeves?
3. Why are regime filters not standalone allocations?
4. Take three edges you've encountered in trading content. Classify each by source AND category. Are they consistent (e.g., a microstructure edge in the foundation category would be a red flag)?
5. Why does v3 use three separate ranking tables instead of one?
6. Pick a strategy from Category E (rejected). Articulate why it's rejected — what specific evidence kills it?

---

## Where this fits

Chapter 4 gave us the conviction score (decision rule). Chapter 5 gives us the taxonomy (implementation rule). Chapters 6-10 will populate the taxonomy with specific edges, applying the teaching template to each. Chapter 11 will provide worked examples that integrate everything.

After Chapter 5, you should be able to look at any new "edge" in trading content and:
1. Classify its source (Chapter 1)
2. Score its conviction (Chapter 4)
3. Place it in the taxonomy (Chapter 5)
4. Decide whether and how to allocate

That's the full pipeline. The remaining chapters provide depth, examples, and operational specifics.

[← Previous: Chapter 4 — Conviction](05_ch04_conviction.md) | [Next: Chapter 6 — Foundation premia →](07_ch06_foundation_premia.md)
