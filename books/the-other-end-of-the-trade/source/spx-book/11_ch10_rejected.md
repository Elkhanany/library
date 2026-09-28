# Chapter 10 — Rejected and non-retail
## What NOT to trade and why

> **Core intuition.** A textbook teaches negative space. Most retail trading content focuses on strategies in this chapter — they're vivid, easy to backtest, and frequently traded — but they don't survive evidence-tier evaluation. Knowing what *not* to allocate to is at least as valuable as knowing what to allocate to. Each rejection in this chapter is reasoned, not opinionated.

---

## 10.1 The taxonomy of rejection

There are three reasons to reject a candidate strategy:

1. **Decayed.** The edge was real but has substantially compressed. Trading the historical effect now produces near-zero or negative net returns.
2. **Never robust.** The "edge" was always thin or methodology-specific. The narrative is appealing but the evidence is weak.
3. **Institutional-only.** A real edge that requires infrastructure (data feeds, low-latency execution, cross-margining, large capital) unavailable to retail.

This chapter walks through specific examples in each category. The pattern matters: when you encounter a *new* strategy, you should be able to classify it into one of these buckets if it's not actually allocatable.

---

## 10.2 Pre-FOMC announcement drift (decayed)

### The historical edge
Lucca-Moench (2015, *JF*) found that from 1994-2011, equities earned approximately 49 bps in the 24 hours before scheduled FOMC announcements. The effect was concentrated in stocks with the highest beta — high beta gained 80+ bps, low beta near zero.

Mechanism: pre-announcement uncertainty led to risk-off positioning that mean-reverted as the announcement approached.

### Why it's rejected
**Kurov-Halova-Wolfe-Gilbert (2021, *JFEcon*)** documented that the effect *disappeared* post-2015 due to Fed transparency reforms — specifically, the 2014 introduction of "dot plot" projections and forward guidance practices. Investors received more information between meetings, reducing the announcement-day uncertainty premium.

Realized 2015-2024 pre-FOMC drift: near zero. The mechanism was real; the policy response eliminated it.

### Lesson
Decay risk for institutional/structural overlays is real and can be sudden. The mechanism has to persist for the edge to persist. When the mechanism changes (as Fed transparency practices did), the edge can vanish even with no decay in retail awareness.

### Operational rule
Don't allocate to pre-FOMC drift. Awareness only.

---

## 10.3 S&P 500 inclusion premium (decayed)

### The historical edge
Stocks added to the S&P 500 historically rallied ~7% in the announcement-to-effective window (Shleifer 1986, Harris-Gurel 1986). Mechanism: index funds were forced buyers; arbitrageurs front-ran the inclusion flow.

### Why it's rejected
**Greenwood-Sammon (2024, *JF*)** documented that the inclusion premium has fallen to <1% as of recent decades. Causes:
- Index funds have become smarter about pre-positioning
- Inclusion announcements are integrated into broader market awareness
- Active arbitrageurs have largely eliminated the obvious mispricing

The 7% effect of the 1990s is now 50-100 bps and arguably statistically insignificant.

### Lesson
Mechanism-clear edges can decay almost completely when capital efficiently exploits them. Institutional edges have a half-life that depends on the discoverability of the underlying flow.

### Operational rule
Don't trade S&P inclusion plays. Even if you correctly anticipate an inclusion, the post-inclusion drift is too small to compensate for the risk.

---

## 10.4 Naive single-name earnings short-vol (institutional-only + dangerous retail)

### The narrative
Implied vol typically rises into earnings as traders price in the announcement uncertainty, then falls sharply post-announcement. The "vol crush" creates a window for selling premium. Many retail traders allocate significant capital to systematic earnings short-vol.

### Why it's rejected for retail

**Adams-Neururer (2020, *RFS*) "Volatility Risk Premium and Stock Returns Around Earnings Announcements"** is the key paper. The finding: at the **single-name retail-tradable level, naive earnings short-vol has a NEGATIVE mean despite a positive median.**

In other words: most of the time you make a small amount on the vol crush. Occasionally you lose a large amount when the move exceeds expected (revenue miss, guidance cut, surprise warning). The aggregate distribution has positive median (frequent small gains) and negative mean (rare large losses dominate).

This is the structural shape from Chapter 2, applied at single-name resolution: short-vol is short skew, and at the retail single-name level the skew tax is too large for the premium to compensate.

### Why it works at institutional level

**Cao-Han-Tong-Zhan (2022, *RFS*)** documents a profitable institutional implementation: cross-sectional dispersion-driven short-vol portfolios across 200+ names, with significant short-leg compensation. This requires:
- 200+ name positioning capacity
- Cross-margining for cross-sectional offset
- Risk management infrastructure
- Sophisticated implied-vol surface analytics

Retail can't replicate this at scale. Single-name implementations don't capture the cross-sectional benefit; they just take the negative-mean exposure.

### The reasonable retail variant: calendar spreads on liquid earners

The least-bad retail earnings strategy: long-dated long, short-dated short calendar spreads (selling the inflated front-month vol while keeping back-month exposure). This is:
- Defined-risk
- Limited downside on a miss
- Moderate vol-crush capture

Even this is small-edge. Better used as periodic small bets, not as a sleeve.

### Misconception box
> **Misconception:** "I'll just sell premium on every earnings announcement and capture the average vol crush."
>
> **Correction:** Adams-Neururer 2020 directly contradicts this. At the single-name retail level, the average is *negative*. The visual "wins more often than I lose" feeling is the textbook negative-skew pattern in action.

### Operational rule
- Don't run a systematic single-name earnings short-vol sleeve
- If trading individual names around earnings, prefer calendar spreads to short premium
- Use earnings calendar awareness to *avoid* being caught long premium that decays into a print

---

## 10.5 GEX-level scalping (never robust at retail)

### The narrative
Public GEX models (SqueezeMetrics, SpotGamma, others) identify "call walls" and "put walls" — strikes where dealer gamma exposure is concentrated. Retail traders sell at the call wall, buy at the put wall, expecting dealer hedging to reverse moves at these levels.

### Why it's rejected

Three reasons:

1. **Public GEX models are model-dependent.** Different vendors give different numbers because they make different assumptions about who's long vs short which strikes. The "ground truth" position is unknowable from public data.

2. **Post-2022 0DTE explosion changed structure.** Pre-2022 GEX models assumed monthly/weekly options dominated. With 40%+ of SPX volume now in 0DTE, the models built for the old structure don't necessarily reflect current dealer positioning.

3. **Cboe 2025 study estimates 0DTE MM hedging is ~0.2% of SPX daily liquidity.** This directly contradicts the narrative that dealer flows are dominant intraday. If hedging is 0.2% of liquidity, level effects from hedging are small relative to other drivers.

### What the academic literature actually supports

Garleanu-Pedersen-Poteshman (2009, *RFS*) established that *demand pressure* on options affects prices — this is the theoretical basis for thinking dealer positioning matters. But:
- The effect operates at the *option pricing* level, not the underlying-price level
- Magnitudes are small per unit of demand
- Specific level-trading rules are not validated in the academic literature

### What's valid use

GEX directional sign as a low-confidence regime context (Chapter 9). Negative GEX days tend to have higher realized vol; positive GEX days tend to have compressed realized vol. Use for sizing, not for level trading.

### Misconception box
> **Misconception:** "GEX is the most important new thing in trading. Reading the dealer positioning gives me edge."
>
> **Correction:** Most of the GEX narrative is post-hoc storytelling around price moves. The fundamental data (option open interest by strike) is real, but the inferences drawn from it (dealer net positioning, predicted hedging flows) require assumptions that public models don't validate well. Cboe 2025 directly says the magnitude is small. The narrative is more compelling than the evidence.

### Operational rule
Don't trade GEX levels. Use directional sign as low-confidence regime context only.

---

## 10.6 Systematic iron condors (CNDR-style, empirically rejected)

### The narrative
Iron condors are "defined risk" strategies that profit from range-bound markets. Sell OTM calls AND OTM puts, defining max loss on each side. Markets are usually range-bound, so condors usually win. Many retail "income" strategies are condor-based.

### Why it's rejected

**The CBOE CNDR Index returned approximately 690% from 1986-2024, while SPX TR returned approximately 5,500% over the same period.**

That's an empirical, multi-decade rejection. Systematic condors *underperform massively* over long horizons.

### Why condors fail
- Each leg has negative skew; combining two short legs *doesn't* offset the skew, it adds it
- Condors are vulnerable to *one-sided breaks* — when SPX trends, the OTM call wing or OTM put wing gets blown through, and the "defined risk" max loss triggers
- Tail risk is asymmetric (both wings can be tested in different scenarios)
- Theta accumulates slowly; a few wing breaks per year erase a year of premium

### The deeper lesson
"Defined risk" is an operational property (you know your max loss) but not a P&L property. Systematic condors with explicit max-loss caps still underperform because the wing breaks happen often enough to dominate the theta wins.

### Misconception box
> **Misconception:** "Defined-risk income strategies are safer than naked premium selling."
>
> **Correction:** Defined max loss per trade is NOT the same as defined max loss in aggregate. CNDR's empirical underperformance is overwhelming evidence that systematic condors don't work. The "safety" of defined risk is illusory if the aggregate path includes enough wing breaks to dominate the wins.

### Operational rule
Don't run systematic iron condor strategies. The empirical evidence is decisive.

### Caveat
Discretionary condors at occasional opportunities (extreme implied vol relative to expected move, very specific structure) can sometimes work. But systematic / mechanical condor sleeves are empirically rejected.

---

## 10.7 1-year SPX put-spread + LEAP combination (leverage with extra steps)

### The narrative
"Sell 1-year SPX put spreads to fund LEAP calls. The premium pays for the LEAP exposure. Portfolio margin makes this efficient. The result is a leveraged equity exposure with positive edge from VRP harvest."

This is a popular "edge" framing in retail content, especially among traders with portfolio margin accounts.

### Why it's rejected

The structure is *economically equivalent* to ~1.4× SPX exposure (depending on specific deltas), with worse path properties. Worked example in Chapter 11.

The decomposition:
- Long LEAP call ≈ long SPX with embedded financing cost (50-150 bps annualized leverage drag, per Frazzini-Pedersen 2012, 2022)
- Short put spread ≈ small VRP harvest with bounded loss (-2 to -3 vol points realized after costs)
- Net: long ~1.4× SPX with embedded drag and path-dependent margin requirements

**The simpler alternatives:**
- ES futures: 1.4× exposure with cleaner financing (basis ~SOFR + 10-20 bps)
- Box spread financing + SPY: similar economics, no MTM dependency
- 2× SPX ETF (SSO): expense ratio 0.85% but no LEAP roll, no put-spread management

All three give equivalent or better economic exposure with less operational complexity and better path properties.

### Why the "edge" claim is wrong

The argument: "VRP makes this profitable." But:
- VRP from 1-year put spreads after retail costs is roughly +1-3 vol points net
- Embedded leverage drag in LEAPs is roughly 50-150 bps annualized
- Net "edge" over simple leverage is approximately zero or small
- Path properties are *worse* (margin expansion under stress, force-liquidation risk)

It's leverage, dressed up. Calling it "edge" overstates what it adds.

### Misconception box
> **Misconception:** "The put-spread + LEAP combo gives me equity exposure plus VRP edge."
>
> **Correction:** The VRP component is small (1-3 vol points) and largely consumed by execution costs and the embedded leverage drag in the LEAP. After honest accounting, this structure adds essentially nothing over simple leverage. It's complexity that's been narrativized as edge.

### Operational rule
If you want leveraged equity exposure, use ES futures or 2× ETFs. The put-spread + LEAP structure adds complexity without economic benefit.

### Worked example
See Chapter 11 for a full Greeks/P&L decomposition that demonstrates the economic equivalence.

---

## 10.8 VIX ETPs (catastrophic tails on both sides)

### Long VIX ETPs (VXX, UVXY)

**VXX has lost 99.84% from 2009 inception through 2024.** The losses come from continuous roll decay — VIX is in contango most of the time, meaning the ETP must continuously sell expiring contracts at a lower price than they're buying replacement contracts.

Annual roll decay: 5-15% in normal times, much higher in extended contango periods.

Use as portfolio hedge: the carry cost dominates. You need very specific timing (entering near term-structure inversion, exiting before mean reversion) to net positive after costs. Most retail attempts fail.

### Short VIX ETPs (formerly XIV, SVXY)

**XIV terminated -96% in a single day in February 2018.** SVXY is now de-leveraged but still subject to catastrophic single-day losses in vol shocks.

The "short vol" trade via inverse VIX ETPs has negative skew that's even more extreme than direct put-writing because:
- VIX moves are highly non-linear (a 5-point VIX spike is much more than a 5% SPX move)
- ETP rebalancing forces buying vol after stress (selling at the worst time)
- Termination clauses can wipe positions

### Operational rule
Don't trade VIX ETPs. If you want vol exposure (long or short), use SPX/XSP options directly with explicit position management.

---

## 10.9 What looks like edge but isn't: pattern recognition

When evaluating any candidate strategy, the following are red flags:

| Red flag | What it indicates |
|---|---|
| **Vivid narrative without academic backing** | Storytelling, not edge |
| **Single-decade backtest** | Not robust to regime change |
| **Backtest on "easy" data (mid-quote, no slippage)** | Won't survive retail haircut |
| **Defined-risk wrapping that hides skew** | Skew tax still applies |
| **Strategy that requires constant attention** | Behavioral haircut compounds |
| **Reliance on a specific data vendor's signal** | Model-dependent, not edge |
| **Performance that depends on a recent regime** | Sample-specific, not structural |
| **High-quality content without transparency on costs** | Costs likely dominate |

The textbook rule: **a real edge survives critical evaluation. If it doesn't, it's narrative.**

---

## 10.10 The complete map of rejection

Categorizing the items in this chapter:

| Strategy | Category | Reason |
|---|---|---|
| Pre-FOMC drift | Decayed | Fed transparency reforms (2015) |
| S&P inclusion | Decayed | Index funds got smarter |
| Naive single-name earnings short-vol | Never robust at retail | Negative mean (Adams-Neururer 2020) |
| GEX-level scalping | Never robust | Model-dependent, contradicted by Cboe 2025 |
| Systematic iron condors | Never robust | CNDR empirical underperformance |
| Put-spread + LEAP "edge" | Never robust | Leverage with extra steps |
| VIX ETPs (long) | Catastrophic costs | -99.84% VXX |
| VIX ETPs (short) | Catastrophic tails | -96% XIV in a day |

Each item has at least one specific empirical or academic rejection. None should be allocated to.

---

## 10.11 What this leaves you with

After Chapters 6-10, the universe of allocatable strategies is:

**Foundation premia:**
- ERP (long equity)
- VRP (XSP cash-secured ATM put-write only)
- Trend-following (DBMF or KMLM)
- Cross-asset carry (small allocation if accessible)

**Factor tilts:**
- Quality (QUAL)
- Momentum (MTUM)
- Value (RAFI/AVUV)
- Low-vol (USMV)
- Size + Quality (AVUV)

**Structural overlays (cheap implementation only):**
- FOMC even-week tilt (via equity sizing modulation)
- EOQ rebalancing (very small, with explicit direction)
- Halloween (via annual rebalance timing)

**Regime filters:**
- VIX term structure (canonical, phased)
- Realized vs implied vol
- Liquidity composite
- GEX directional sign (low-confidence supplement)

That's a manageable universe. The reason it's manageable: most of what's marketed as "edge" doesn't survive evaluation. The taxonomy plus the conviction framework filters aggressively.

---

## 10.12 Misconception box (chapter level)

> **Misconception:** "If a popular strategy has lots of practitioners, it must be tradable."
>
> **Correction:** Practitioner popularity is not evidence quality. Many of the strategies in this chapter (GEX scalping, iron condors, VIX ETPs) have huge retail communities. The communities exist because the strategies *feel* tradable — they have specific entries, dramatic narratives, and frequent trades. The empirical evidence is what matters, and the empirical evidence doesn't support these strategies as positive-edge for retail. Don't confuse popularity with validity.

---

## 10.13 Self-check (chapter)

1. Name the three reasons a strategy can be rejected. Give an example of each.
2. Why is naive single-name earnings short-vol negative-mean despite positive median?
3. What's the empirical CNDR vs SPX result? What does it imply about systematic condors?
4. Decompose the put-spread + LEAP combination. Why is the "edge" claim wrong?
5. Why have VIX ETPs (both long and short) been catastrophic for retail?
6. Take a strategy you've considered allocating to. Does it appear in this chapter? If not, why not — what evidence supports it that the rejected strategies lack?

---

## Where this fits

Chapters 6-9 covered the strategies that are allocatable. Chapter 10 covers what to specifically NOT trade. Together they complete the taxonomy.

Chapter 11 is the most important chapter for converting concepts into judgment: ten worked examples that walk through the full reasoning chain end-to-end. Chapters 12-14 give operational specifics (setup cards, signal-to-trade pipeline, kill criteria). Chapter 15 is reference.

[← Previous: Chapter 9 — Filters](10_ch09_filters.md) | [Next: Chapter 11 — Worked examples →](12_ch11_worked_examples.md)
