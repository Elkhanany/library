# Section 10 · Tactical Swing
*Applying mechanics to live SPX/SPY trades.*

Everything in the preceding nine sections explained why markets behave the way they do under dealer hedging. This section is the operational counterpart: **how to actually swing-trade SPX/SPY once you know the mechanics**. The central claim of this section is narrow and falsifiable.

> *SPY exhibits conditional short-horizon mean reversion embedded within a longer-run positive equity drift, and that edge weakens or flips in trend-dominant, negative-gamma, or macro-shock regimes. This is not "SPY mean reverts." It is "SPY mean reverts when specific measurable conditions hold."*

The "when" is the entire framework. Strip it out and you have a contrarian heuristic that will work for a year and blow up in the next vol regime. Keep it, and you have a system where most days you do nothing, a handful of days you take a bet that compounds, and the bets you skip are at least as valuable as the bets you take.

The sub-chapters: **10A** is the market markers dashboard — the regime read every swing decision begins with. **10A.5** lays out the conditional mean-reversion thesis and the three-layer hierarchy that frames every trade. **10B** builds the measurement instruments — indicator foundations done correctly, with explicit attention to the multicollinearity trap that ruins most retail indicator stacks. **10C** treats the major pattern types as priors on order flow. **10D** applies the Weinstein 4-stage classification framework. **10E** covers Elder's triple-screen multi-timeframe discipline. **10F** integrates everything into an 8-dimensional composite regime scorecard.

---

## 10A · The market markers dashboard — the regime read before any trade

The conditional mean-reversion thesis in 10A.5 says different markets have different statistical properties. Before you can apply *any* tactical setup — mean reversion, breakout, pullback, premium selling — you need a current read of what regime you're in. This subsection is the operating manual for that read, and because the read precedes every tactical decision, the dashboard sits at the front of Section 10.

**The principle**: every swing decision begins with a four-question check on the dashboard:

1. **What's the trend?** (Is the market in a Stage 2 uptrend, a Stage 4 downtrend, a Stage 1 base, or a Stage 3 distribution?)
2. **What's the volatility regime?** (Compressed? Expanding? Stressed? Normal?)
3. **What's the dealer positioning?** (Positive GEX, negative GEX, near the flip?)
4. **What's the flow signature?** (Bullish premium buying, hedge unwind, defensive positioning?)

If any of these four reads is inconclusive, the right action is usually to **wait**, not to size down on a half-formed thesis. The dashboard's primary function is filtering: it prevents trades on days when the regime is ambiguous.

### 10A.a — Trend and return markers

The first read: where is the market relative to its own structure?

| Marker | Operational use | Typical thresholds |
|---|---|---|
| SPX vs 20D EMA | Short-term trend direction | Above = constructive bias |
| SPX vs 50D SMA | Intermediate-term Stage | Above + rising = Stage 2 |
| SPX vs 200D SMA | Cyclical regime | Above + rising 200D = full Stage 2 |
| 200D slope (5-day delta) | Cyclical strength | Rising > 0 = bull cycle; falling < 0 = bear |
| Rolling 1M/3M/6M/12M returns | Momentum reads at different horizons | Useful for context, not entry signals |
| Distance from MAs (% above/below) | Overextension diagnostic | >3% above 20D = often pulls back; >7% above 50D = stretched |
| % SPX members above 50D / 200D | Breadth confirmation | <40% above 50D in a "rally" = narrow / distribution warning |
| Equal-weight vs cap-weight SPX | Concentration risk | RSP/SPY declining = narrow leadership |
| Sector breadth (sectors above their 50D) | Diffusion | <5 sectors above 50D during SPX rally = caution |

The fastest single read: SPX above rising 20D EMA, above rising 50D SMA, with 200D slope > 0, and >55% of members above their own 50D. If those four conditions hold, you're in a Stage 2 environment where pullback longs and put credit spreads have positive expectancy. If two or more fail, the regime is in transition and tactical positioning should defer to defined-risk structures.

### 10A.b — Fear and volatility markers

VIX is the headline number but it's far from sufficient. The fear/vol dashboard:

| Marker | Reading | Typical thresholds |
|---|---|---|
| VIX (spot) | Current 30-day ATM SPX IV | <14 = complacent; 14-18 = normal; 18-25 = elevated; >25 = stressed |
| VIX percentile (1Y, 3Y) | Where VIX is in its own distribution | <20th = compressed; 50th = normal; >80th = panic |
| VIX9D / VIX / VIX3M | Term structure shape | All ascending = normal contango; VIX > VIX3M = stress backwardation |
| VIX / VIX3M ratio | Stress alarm | >1.0 = backwardation = stress regime |
| VVIX | Vol-of-vol; convexity in vol space | <80 = quiet; >100 = stressed; >130 = panic in vol space |
| SKEW (Cboe) | Tail demand in OTM puts | 130-150 normal; >150 = elevated tail demand |
| SPX realized vol (10D, 30D) | Actual delivered vol | Compare to VIX — IV-RV spread is the variance premium |
| MOVE Index | Treasury vol | >120 sustained = rates regime stress, often precedes equity stress |

The composite signal in 10F formalizes these into a numerical score. For a fast same-day read: **VIX/VIX3M ratio < 1.0 AND VIX percentile < 60th** is sufficient for "normal regime" tactical positioning. Backwardation OR top-quintile VIX both warrant defensive posture.

### 10A.c — Option surface markers

The surface markers determine whether *option-based* expressions are attractive:

| Marker | Reading | Strategy implication |
|---|---|---|
| ATM IV by tenor (1D, 5D, 30D, 90D) | Term structure at the money | Steep ATM curve up = event premium nearby |
| 25-delta risk reversal | Skew (call − put 25Δ IV) | Negative = put-heavy demand; near zero = balanced |
| Put skew (90% put IV − ATM IV) | Downside hedge pricing | Elevated = expensive crash protection |
| Forward IV (between two expirations) | Market's implied vol for the forward window | Computed per 5G formula |
| Expected move (ATM straddle ÷ spot) | Market's pricing of the next N-day move | Used for strike calibration in spreads |
| Implied-Realized spread | IV − recent RV | Positive = variance premium; large positive = vol-selling supportive |
| IV Rank (52-week) | Current IV's percentile in its own 1Y range | High = premium-selling supportive; low = vol-buying supportive |
| Skew slope (25Δ put − 25Δ call) | Asymmetry pricing | Steepening = increasing crash premium |

The two highest-value surface reads: **Implied-Realized spread** (informs whether selling premium has structural edge) and **Forward IV** (informs whether calendars/diagonals make sense for upcoming events).

### 10A.d — Dealer-position markers

The dealer-positioning dashboard maps to Sections 8A-8C:

| Marker | Reading | Operational implication |
|---|---|---|
| Net GEX ($, signed) | Aggregate dealer gamma | Positive = stabilizing; negative = amplifying |
| Distance to gamma flip | How close spot is to the GEX zero level | Within 0.5% = transitional regime; trade carefully |
| Largest call wall (strike + $ size) | Call-side dealer hedge concentration | Above spot = potential resistance; magnet for pinning |
| Largest put wall (strike + $ size) | Put-side dealer hedge concentration | Below spot = potential support |
| Charm magnitude (signed) | Time-decay-driven hedge flow into close | Concentrates in last 30 min, especially OPEX |
| Vanna magnitude (signed) | Vol-change-driven hedge flow | Activates during VIX moves |
| 0DTE volume share of total SPX | Microstructure regime | >55% = retail-saturated; supports Adams et al. (2025) framework |
| OPEX OI concentration at nearby strikes | Pin-risk diagnostic | Heavy concentration = expect pin pressure into close |

The fast read: **GEX sign + distance to flip + nearest large strike**. Three numbers, refreshed pre-market, that tell you whether intraday dynamics are likely dampening (positive GEX, well above flip) or amplifying (negative GEX, near flip).

[INTERACTIVE: future-gex-map]

### 10A.e — Flow markers (the demand side)

What is actually being bought and sold:

| Marker | Reading | Caveats |
|---|---|---|
| SPX put/call ratio (Cboe) | Daily put-volume / call-volume | <0.8 complacent; >1.2 hedging spike |
| Premium bought at ask (call vs put, $) | Aggressor side | Buyer-initiated flow at ask = real demand |
| Block trades (>$1M premium) | Institutional sizing | Single direction = positioning signal |
| Sweeps (orders splitting across exchanges) | Urgency-priced flow | Often institutional; volume-weighted by aggressor |
| OI change overnight | Open vs close in positions | Volume + OI both up = new positioning; volume up + OI flat = closing |
| Bullish vs bearish delta-adjusted premium | Net directional pressure | More signal than raw call/put ratio |
| Dealer-likely side (estimated) | Whether dealers are long or short the flow | Inferred from trade size and chain structure |

Caveat: flow markers are **noisy** and prone to over-interpretation. They confirm or refute a thesis you already have; they should not generate the thesis. "Unusual options activity" alone is not a signal — only when it overlays with fundamentals + technical structure + supportive surface does it become signal.

### 10A.f — Credit, rates, and liquidity markers

Cross-asset confirmation:

| Marker | Reading | Stress threshold |
|---|---|---|
| HY OAS (BAML US HY Master II) | High-yield credit risk premium | >450bps = elevated; >700 = stress |
| IG OAS (BAML US IG Master) | Investment-grade spread | >120bps = unusual |
| CDX HY (5Y) | Credit default swap index, HY | Same direction as HY OAS |
| 2Y10Y Treasury slope | Yield curve shape | Inverted = recession watch |
| Real yields (5Y, 10Y TIPS) | Risk-free real rate | Rising real yields = headwind for risk assets |
| DXY (US Dollar Index) | Cross-currency stress | Rising rapidly = global liquidity tightening |
| USDJPY | Carry-trade stress proxy | Rapid moves in either direction = stress (Aug 2024 lesson) |
| MOVE Index | Treasury vol | >120 sustained = rates regime stress |

The fast cross-asset read: **HY OAS direction + DXY direction + MOVE level**. Rising HY OAS + rising DXY + MOVE > 120 = cross-asset stress, defensive positioning warranted regardless of what SPX is doing on the day.

### 10A.g — Marker → trade family translation

The capstone: how to read the dashboard and select what to do.

| Dashboard state | Regime interpretation | Prefer | Avoid |
|---|---|---|---|
| SPX above rising 50/200D, VIX <16, VIX/VIX3M <0.95, positive GEX above flip, HY OAS <400 | Quiet bull / mean-reverting trend | Pullback longs, put credit spreads, XSP/SPX systematic premium | Long volatility, breakout chasing, OTM puts |
| Compressed (BB width contracted), positive breadth >55%, VIX <14, no event in 14D | Coiled breakout setup | Long shares, call debit spreads, long convexity is cheap | Short vol into the compression unless catalyst maps out |
| Rising VIX, GEX approaching flip from above, HY OAS widening, MOVE >110 | Unstable transition | Reduce size, defined-risk only, increase cash | Naked short premium, leveraged directional |
| VIX/VIX3M >1.0 (backwardation), negative GEX, breadth <40% above 50D, USDJPY moving rapidly | Trend/stress regime | Momentum continuation in direction of weakness, long puts/put spreads, hedges | Mean reversion, dip-buying, short volatility |
| Post-VIX-spike crush, VIX falling from >25, VIX/VIX3M reverting toward 1.0, stabilizing breadth | Repair phase | Vanna/charm unwind longs, put credit spreads at higher IVR, gradual long re-entry | Buying expensive late puts, chasing the spike |
| 0DTE volume >55% of total SPX, ATM IV elevated relative to 30D, sticky range | 0DTE-saturated microstructure | Short-term mean reversion, defined-risk strangles, fade overbought intraday | Holding 0DTE positions through close without management |
| FOMC/CPI/NFP in next 48h, term structure inverted (front IV > back IV) | Pre-event hold | Exit binary risk before event, calendar/diagonal harvesting forward vol | Long convexity into the event (IV crush coming), trading the announcement |

**Operational pattern**: scan dashboard at pre-market open (8:00-9:00 AM ET); make regime determination; choose strategy family from the table; then apply the conviction score in 12B and the kill rules in 12C. This is a 5-minute discipline that prevents most low-quality trades.

---

## 10A.5 · The conditional mean-reversion thesis

The dashboard in 10A tells you *what regime you're in*. This section is what to do when the dashboard says you're in a mean-reverting regime — when the macro layer green-lights mean reversion as the prior, when structure puts the market at a pullback level, and when gamma positioning makes dampening intraday flow likely. The conditional thesis is not "SPY mean reverts"; it is "SPY mean reverts when measurable conditions hold," and the dashboard's four checks are exactly those measurable conditions.

Mean reversion as a *universal* claim about SPY is empirically false. The classic statistic — the next-bar return conditional on the trailing N-bar return sign — is sometimes positive (momentum), sometimes negative (mean reversion), and the sign depends on the regime. Sorting by VIX level, by GEX sign, by credit-spread direction, the sign flips. A trader who claims "I'm a mean-reversion guy" is implicitly making a regime assumption they may not realize they're making.

The conditional framing avoids that trap. You write down the conditions under which you expect the edge to be positive, you check them, and if any condition fails you don't take the trade. Most days, some condition fails. That's the system working — not a sign that the system is broken.

### The hierarchy: three nested horizons

The framework is hierarchical. Each layer answers a different question, runs on a different clock, and uses different inputs. **A signal at one layer never overrides a contradicting signal at a higher layer.**

**Layer 1 — Macro regime (weeks → months).** Sets the prior. Determines whether mean-reversion edge is positive, weak, or negative. Inputs: equity drift (200-day SMA slope), VIX level and term structure, credit spreads (HY OAS, IG OAS, MOVE index), yield curve (10Y-2Y, 10Y-3M), dollar/FX (DXY, USD/JPY), composite signal score (Section 10F). Default state: positive drift + contango + tight credit = mean-reversion is ON. Inverted curve + widening credit + backwardation = mean-reversion is SUSPENDED.

**Layer 2 — Market structure (2 → 10 days).** Identifies the specific level and pattern context. Inputs: Weinstein stage (Section 10D), location relative to key moving averages (10/21/50/200 EMA), pattern detection (Section 10C), relative strength vs benchmark. Determines whether *this specific setup* is at a location where the macro-regime edge can be expressed cleanly.

**Layer 3 — Dealer gamma and path (intraday → 2 days).** Identifies the immediate execution context. Inputs: net dealer GEX (Section 8A), gamma flip distance, VIX intraday behavior, options skew, time of day. Determines whether *today specifically* is supportive of the trade or whether mechanical flow will work against the position.

**The decision tree:**

```
1. Macro regime supportive (high CompositeSignal, contango, drift positive)?
   If NO → no trade.
   If YES → continue.

2. Structure says BUY (Stage 2 pullback to defined level, pivot intact, RS positive)?
   If NO → no trade.
   If YES → continue.

3. Gamma regime says PATH is acceptable?
   (Positive GEX above flip OR clear setup for amplification trade if below)
   If NO → skip.
   If YES → take the trade.

4. Size for the loss budget (Section 12C), pre-commit invalidation (Section 12C),
   document in journal.
```

Most days, you stop at step 1 or 2. **That's correct.** The framework is designed to filter aggressively; the trades that survive all three gates should be sized larger than the trades that fail any of them.

### Evidence tiering

Not every claim in this framework has the same evidence weight. Tags help reading:

**Tier A** — Peer-reviewed papers, multi-decade replication, official exchange or regulatory data. Examples: equity risk premium (Mehra-Prescott; Dimson-Marsh-Staunton), variance risk premium (Bondarenko; Carr-Wu), Fed meeting week return anomaly (Cieslak-Morse-Vissing-Jorgensen 2019), intraday momentum (Baltussen et al. 2021 JFE), pinning effect (Ni-Pearson-Poteshman 2005).

**Tier B** — Vendor statistics or backtests with credible methodology but no peer review. Examples: SqueezeMetrics GEX models, 0DTE composition data from Cboe, VIX term-structure rules from practitioner research.

**Tier C** — Practitioner pattern language requiring operationalization. Examples: VCP detection (Minervini), Cup & Handle pivot rules (O'Neil), Weinstein stage analysis. Real but heuristic; the rigorous formalization is your job.

Always tag in your own notes which tier each claim sits in. The tier doesn't disqualify a claim, but it sets the prior for how heavily to weight it.

### Horizon tagging

Every signal also gets a horizon tag. A macro regime call works on weeks-to-months; a structural pattern works on 2-10 days; a gamma-driven intraday move resolves in hours. **Mixing horizons is the second-most-common failure mode after mixing tiers** — people see a 5-minute breakout and infer a 6-month thesis, or see a 6-month thesis and trade it on a 5-minute chart.

The discipline: state the horizon of every trade idea in writing before entering. If the horizon you stated doesn't match the indicators you're using, fix one or the other before clicking buy.

### What the rest of this section does

- **10B** — Indicator foundations. Build the measurement instruments — RSI, MACD, ATR, ADX, Bollinger Bands, Donchian Channels — with attention to which feature of the data each measures and which combinations represent genuine confluence vs reparameterization.
- **10C** — Pattern library. VCP, Cup & Handle, Bull Flag — pattern detectors with explicit geometric thresholds.
- **10D** — Stage analysis. Weinstein 4-stage classifier and its overlap with GEX regimes.
- **10E** — Multi-timeframe. Elder's triple-screen rule. HTF direction, ITF timing, LTF trigger. Confluence as a discipline against impulse.
- **10F** — Composite signal. Eight-dimensional regime scorecard — volatility, credit, rates, dollar, commodities, global, trend, sentiment — aggregated to a single bias number.

---

The conditional framing avoids that trap. You write down the conditions under which you expect the edge to be positive, you check them, and if any condition fails you don't take the trade. Most days, some condition fails. That's the system working — not a sign that the system is broken.

### The hierarchy: three nested horizons

The framework is hierarchical. Each layer answers a different question, runs on a different clock, and uses different inputs. **A signal at one layer never overrides a contradicting signal at a higher layer.**

**Layer 1 — Macro regime (weeks → months).** Sets the prior. Determines whether mean-reversion edge is positive, weak, or negative. Inputs: equity drift (200-day SMA slope), VIX level and term structure, credit spreads (HY OAS, IG OAS, MOVE index), yield curve (10Y-2Y, 10Y-3M), dollar/FX (DXY, USD/JPY), composite signal score (Section 10F). Default state: positive drift + contango + tight credit = mean-reversion is ON. Inverted curve + widening credit + backwardation = mean-reversion is SUSPENDED.

**Layer 2 — Market structure (2 → 10 days).** Identifies the specific level and pattern context. Inputs: Weinstein stage (Section 10D), location relative to key moving averages (10/21/50/200 EMA), pattern detection (Section 10C), relative strength vs benchmark. Determines whether *this specific setup* is at a location where the macro-regime edge can be expressed cleanly.

**Layer 3 — Dealer gamma and path (intraday → 2 days).** Identifies the immediate execution context. Inputs: net dealer GEX (Section 8A), gamma flip distance, VIX intraday behavior, options skew, time of day. Determines whether *today specifically* is supportive of the trade or whether mechanical flow will work against the position.

**The decision tree:**

```
1. Macro regime supportive (high CompositeSignal, contango, drift positive)?
   If NO → no trade.
   If YES → continue.

2. Structure says BUY (Stage 2 pullback to defined level, pivot intact, RS positive)?
   If NO → no trade.
   If YES → continue.

3. Gamma regime says PATH is acceptable?
   (Positive GEX above flip OR clear setup for amplification trade if below)
   If NO → skip.
   If YES → take the trade.

4. Size for the loss budget (Section 12C), pre-commit invalidation (Section 12C),
   document in journal.
```

Most days, you stop at step 1 or 2. **That's correct.** The framework is designed to filter aggressively; the trades that survive all three gates should be sized larger than the trades that fail any of them.

### Evidence tiering

Not every claim in this framework has the same evidence weight. Tags help reading:

**Tier A** — Peer-reviewed papers, multi-decade replication, official exchange or regulatory data. Examples: equity risk premium (Mehra-Prescott; Dimson-Marsh-Staunton), variance risk premium (Bondarenko; Carr-Wu), Fed meeting week return anomaly (Cieslak-Morse-Vissing-Jorgensen 2019), intraday momentum (Baltussen et al. 2021 JFE), pinning effect (Ni-Pearson-Poteshman 2005).

**Tier B** — Vendor statistics or backtests with credible methodology but no peer review. Examples: SqueezeMetrics GEX models, 0DTE composition data from Cboe, VIX term-structure rules from practitioner research.

**Tier C** — Practitioner pattern language requiring operationalization. Examples: VCP detection (Minervini), Cup & Handle pivot rules (O'Neil), Weinstein stage analysis. Real but heuristic; the rigorous formalization is your job.

Always tag in your own notes which tier each claim sits in. The tier doesn't disqualify a claim, but it sets the prior for how heavily to weight it.

### Horizon tagging

Every signal also gets a horizon tag. A macro regime call works on weeks-to-months; a structural pattern works on 2-10 days; a gamma-driven intraday move resolves in hours. **Mixing horizons is the second-most-common failure mode after mixing tiers** — people see a 5-minute breakout and infer a 6-month thesis, or see a 6-month thesis and trade it on a 5-minute chart.

The discipline: state the horizon of every trade idea in writing before entering. If the horizon you stated doesn't match the indicators you're using, fix one or the other before clicking buy.

### What the rest of this section does

- **10B** — Indicator foundations. Build the measurement instruments — RSI, MACD, ATR, ADX, Bollinger Bands, Donchian Channels — with attention to which feature of the data each measures and which combinations represent genuine confluence vs reparameterization.
- **10C** — Pattern library. VCP, Cup & Handle, Bull Flag — pattern detectors with explicit geometric thresholds.
- **10D** — Stage analysis. Weinstein 4-stage classifier and its overlap with GEX regimes.
- **10E** — Multi-timeframe. Elder's triple-screen rule. HTF direction, ITF timing, LTF trigger. Confluence as a discipline against impulse.
- **10F** — Composite signal. Eight-dimensional regime scorecard — volatility, credit, rates, dollar, commodities, global, trend, sentiment — aggregated to a single bias number.

---

## 10B · Indicator foundations: the measurement instruments

Indicators are **not edges**. They are instruments that measure features of price and volume — trend strength, momentum extreme, volatility regime, range structure. The edge lives in the *framework that combines them*. Picking the right instruments, and knowing what each one measures (and doesn't), is foundational.

The selection below is small and deliberate. Six indicators across three pedagogical functions: momentum extremes (RSI), trend regime (MACD, ADX), volatility regime (ATR, Bollinger), structural levels (Donchian).

### RSI — Relative Strength Index

**Formula:** `RSI = 100 − 100/(1 + RS)` where `RS = avg gain / avg loss over n bars`. Standard parameter: n = 14 (Wilder, 1978).

**Intuition.** Normalizes recent price action to a bounded 0-100 scale. Above 70 is conventionally "overbought," below 30 is "oversold" — but these are calibration points, not signals. The RSI(2) variant by Larry Connors flips the use entirely: extremes below 10 or above 90 on RSI(2) become mean-reversion entry signals in trending markets.

**Dealer mechanic note.** RSI(2) < 10 on a Stage-2 pullback (Section 10D) is a typical gamma-scalping setup — positive-GEX dealers fade the move, and your mean-reversion bet rides their hedging flow.

### MACD — Moving Average Convergence Divergence

**Formula:** `MACD line = EMA(12) − EMA(26)`; `Signal = EMA(9) of MACD line`; `Histogram = MACD − Signal`.

**Intuition.** Captures the change in trend in two ways: the line itself (positive when fast EMA above slow EMA), and the histogram (positive and growing when bullish momentum accelerates).

**Dealer mechanic note.** MACD histogram crossing zero correlates with regime transitions — Stage 1 to 2 or Stage 3 to 4 in Weinstein terms.

### ATR — Average True Range

> **Wilder smoothing** — a specific EMA variant invented by J. Welles Wilder, used in ATR, ADX, RSI, and other Wilder indicators. Standard EMA uses α = 2/(n+1); Wilder smoothing uses α = 1/n.
>
> For n=14: standard EMA α ≈ 0.133 vs Wilder α ≈ 0.0714.
>
> Wilder smoothing is **slower to respond** — effectively equivalent to standard EMA of period 2n−1 (Wilder(14) ≈ EMA(27)). The indicator's documented thresholds (e.g., "ADX > 25 = trend") are calibrated to Wilder smoothing. Do not substitute one for the other.
>
> Python: `pandas.ewm(span=n).mean()` is standard EMA; for Wilder, use `pandas.ewm(alpha=1/n, adjust=False).mean()`.

**Formula:** `TR = max(H−L, |H−PCₜ₋₁|, |L−PCₜ₋₁|)`; `ATR = Wilder-smoothed TR over n bars`.

**Intuition.** Measures the typical bar range — how much the underlying moves in a typical session. Pure volatility instrument. Critical for sizing: position size should be inversely proportional to ATR for consistent risk per trade.

**Dealer mechanic note.** ATR scales with realized vol, which scales with dealer hedging during stress. ATR expansion often signals the dealer-hedging regime is changing before GEX figures update.

### ADX — Average Directional Index

**Formula:** Computed from +DI and −DI (directional movement indicators) over a Wilder-smoothed window, with ADX measuring the strength of the trend regardless of direction.

**Intuition.** Answers "is the underlying trending or chopping?" Values below 20 indicate no trend; 20-25 weak trend; above 25 strong trend; above 40 very strong trend. ADX has no inherent direction.

**Dealer mechanic note.** ADX > 25 corresponds empirically to negative-GEX regimes — where mean-reversion underperforms and trend-following works. ADX < 20 corresponds to positive-GEX, mean-reverting regimes.

### Bollinger Bands

**Formula:** `Middle = SMA(20)`; `Upper/Lower = Middle ± 2σ(20)`; `%B = (Close − Lower)/(Upper − Lower)`; `Bandwidth = (Upper − Lower)/Middle`.

**Intuition.** Dynamic range-channel that adapts to recent volatility. Bandwidth contractions identify low-vol periods (the "Bollinger squeeze") that often precede volatility expansions.

**Dealer mechanic note.** Bandwidth contraction often coincides with positive GEX above the gamma flip — dealers suppressing realized vol below historical levels.

### Donchian Channels

**Formula:** `Upper = highest high over past n bars`; `Lower = lowest low over past n bars`. Standard parameter: n = 20 or n = 55 (Turtle traders).

**Intuition.** Pure breakout signal. Price above the upper Donchian = new n-day high = potential trend initiation. The Turtle Traders famously used 55-day Donchian breakouts as entry signals.

**Dealer mechanic note.** Donchian breakouts often coincide with mechanical institutional rebalancing flow at quarter ends. When dealer net gamma is short going into the breakout, the dealer hedging response amplifies the breakout.

[INTERACTIVE: indicator-lab]

### The multicollinearity trap

A common retail mistake: stacking RSI(2) + IBS + Bollinger %B + Williams %R + Stochastic and calling them "five independent signals confirming the trade."

**They aren't independent.** All five compute the same latent quantity (how stretched is price relative to the recent range). Using them as separate inputs to a decision rule is *double-counting*.

The honest selection is **one indicator per pedagogical function**:
- One momentum-extreme indicator (RSI is the classical choice)
- One trend-strength indicator (ADX)
- One volatility-regime indicator (ATR or Bollinger Bandwidth — but not both)
- One range-structure indicator (Donchian)

Confluence across different measurements is real evidence. Confluence across reparameterizations of the same measurement is noise.

### The 23-indicator menagerie

The full retail menagerie includes Stochastic, ROC, CCI, Williams %R, OBV, MFI, Aroon, Ichimoku Cloud, Parabolic SAR, SuperTrend, KAMA, Choppiness Index, Linear Regression Channel, Keltner Channels, Heikin Ashi candles, Mansfield Relative Strength, and several others. Each has a use case; almost none are essential.

**The retail bias is to add more indicators. The professional bias is to remove them.** If you can't articulate which feature of the data each indicator measures, drop it. If two indicators measure the same feature, drop one. Simpler systems generalize better; complex systems overfit. Same Occam principle as Section 2A applied to technical analysis.

---

## 10C · Pattern library: VCP, Cup & Handle, Bull Flag

Chart patterns are **pre-trade structural priors**. They describe what the tape looks like when a particular kind of accumulation or distribution is happening underneath. Most retail pattern-trading is reductive — "looks like a cup" without checking whether the geometry satisfies the pattern's definition. Pattern detectors operationalize the geometry: explicit thresholds for what counts and what doesn't.

### VCP — Volatility Contraction Pattern (Minervini)

**Definition.** Three or more progressively shallower pullbacks, terminating in a tight pivot. Each subsequent pullback should be smaller than the previous one; the final pivot should have a range less than 5% of price; volume should compress into the pivot.

**Required anchors:** Stage 2 regime (rising 30-bar MA); positive Mansfield relative strength vs benchmark; volume compressing into pivot; final pivot range less than 5% of price.

**What the dealer sees.** VCP is *accumulation visible on the tape*. Volume dries as range narrows because the marginal seller has been absorbed. Dealers short calls into the consolidation see their delta hedges shrink. The breakout is the moment dealers have to chase the move because they're short the call wing into a rising market.

**Why it works (when it does).** Accumulation by institutional investors takes time. They cannot all bid the same price at the same time without moving the market. They place increasingly tighter limit orders as supply dries up. The breakout is the moment the last marginal seller has exited.

**Failure modes.** A VCP that breaks down was probably not accumulating — it was distributing under thin cover. Verify the structural condition (Stage 2, positive RS, supportive macro) before taking the trade.

### Cup & Handle (O'Neil)

**Definition.** A rounding-bottom "cup" lasting weeks to months, followed by a shorter "handle" pullback of typically 3-12 weeks. The handle should not retrace more than 50% of the cup's depth. The breakout buy point is the high of the handle.

**Required anchors:** Cup depth typically 15-35% (deeper cups are riskier); handle on declining volume; Stage 2 or transitioning from Stage 1 to 2.

**What the dealer sees.** The cup represents one complete cycle of institutional position turnover — accumulation, run-up, distribution, re-accumulation. The handle is the final shakeout before the next leg up.

### Bull Flag

**Definition.** A sharp, high-volume impulse move ("flagpole"), followed by a brief consolidation that drifts against the impulse direction on lower volume ("flag"). The flag should last 1-3 weeks for daily-chart flags. Breakout is the high of the flag.

**Required anchors:** Flagpole at least 2-3× recent daily range; flag retracement no more than 38% of flagpole; volume during flag decisively lower than during flagpole.

**What the dealer sees.** The flagpole is often dealer hedging flow itself — a short-gamma dealer being forced to buy as a fundamental catalyst arrives. The flag is the brief period during which the gamma profile re-equilibrates. The breakout is the next wave of demand.

### Why patterns work (when they do)

Patterns are not magic. They are shorthand for institutional order flow that takes time to complete. When patterns fail — and they do, often — it's almost always because the structural condition the pattern was supposed to encode wasn't actually there. The detector's job is to enforce the geometry; your job is to verify the structural condition (Stage 2, positive RS, supportive macro) before taking the trade.

### The structure-vs-noise calibration

Run any pattern detector across hundreds of random tapes (e.g., randomized seed sweep). You'll see that even random tapes occasionally produce something the detector flags. **False positives are the price of operating with a detector at all.** The fix is not a stricter detector — it's the framework: patterns are necessary but not sufficient, and they only earn capital when the higher-layer conditions (regime, stage, RS) confirm.

---

## 10D · Stage analysis: Weinstein's four phases

Stan Weinstein's 4-stage framework, formalized in *Secrets for Profiting in Bull and Bear Markets* (1988), is the most durable operating heuristic in swing trading. It compresses everything an institution does — accumulation, markup, distribution, markdown — into a small finite-state machine.

### The four stages

**Stage 1 — Basing. Neutral. PATIENCE.** Flat 30-bar moving average. Volume drying up. Range-bound price action. Wait for first Stage-2 breakout above the base ceiling — don't anticipate.

**Stage 2 — Markup. Long. BUY PULLBACKS.** Rising 30-bar MA + price above MA + ADX > 18. Where 90% of swing money is made. Pullbacks to the 10-EMA or 21-EMA are gifts. Trail stops below the rising MA.

**Stage 3 — Distribution. Reduce. TIGHTEN STOPS.** Flat MA after an extended advance. Institutions handing off to retail. Reduce sizing; the first close below the rolling MA = exit.

**Stage 4 — Markdown. Short / cash. DON'T BUY DIPS.** Falling 30-bar MA + price below + ADX > 18. Bounces fail at the MA. Wait for the MA to flatten BEFORE looking for re-entry.

### The classifier

The stage classifier uses three inputs:

1. **Slope of the 30-bar SMA**, ATR-normalized for cross-asset comparability
2. **Price relative to the MA** (above or below)
3. **ADX as a trend-strength gate**

Explicit decision rules:

```
slopeNorm = (SMA30[t] − SMA30[t-5]) / 5 / ATR14[t]

Stage 2: slopeNorm > +0.05 AND price > SMA30 AND ADX > 18
Stage 4: slopeNorm < −0.05 AND price < SMA30 AND ADX > 18
Stage 3: |slopeNorm| < 0.05 AND price > SMA30 AND EMA10 slope < 0
Stage 1: |slopeNorm| < 0.05 (otherwise)
```

[INTERACTIVE: stage-classifier]

### Stage × GEX regime — where they overlap

Stage analysis and GEX regime are two views of the same underlying reality. The overlap isn't a coincidence — rising dealer-gamma-supported drift IS what an institutional accumulation looks like on the tape.

| Stage | Typical GEX regime | Path character | Best strategy |
|---|---|---|---|
| **1** | Near zero or modestly positive | Range-bound, low ATR, low ADX | Sell premium (range trades); avoid directional |
| **2** | Positive (above flip) | Trending up with mean-reverting pullbacks to MA | Buy pullbacks; trail stops below rising MA |
| **3** | Compressing toward zero | Widening range, rising ATR, ADX falling | Tighten stops; reduce size; first MA break = exit |
| **4** | Negative (below flip) | Trending down with sharp counter-trend bounces that fail | Don't buy dips; bounces are short opportunities for the brave |

### The transition is the trade

The highest-edge moments are *transitions*, not the middle of stages. Stage 1 → 2 (basing-to-markup) is the breakout. Stage 3 → 4 (distribution-to-markdown) is the breakdown. The middle of Stage 2 is the easiest place to make money; the boundaries of Stage 2 are the most important places to be reading carefully.

The classifier will sometimes flicker between adjacent stages at the boundary — **that's the signal, not the noise.** When a stage classification is unstable across days, the regime is genuinely transitioning, and your sizing should reflect that uncertainty.

---

## 10E · Multi-timeframe confluence (Elder triple-screen)

Dr. Alexander Elder's "triple-screen" rule, formalized in *Trading for a Living* (1993), is the cleanest formalization of multi-timeframe discipline. The idea: at any moment, three timeframes are operative — the higher timeframe (HTF) sets the direction, the intermediate timeframe (ITF) signals the timing, the lower timeframe (LTF) triggers the entry. **All three must agree.**

### The three screens

**HTF — Direction.** Slope of the 30-bar SMA on the higher timeframe (typically weekly for daily swing trading; daily for intraday). Positive slope = bullish bias only. Negative slope = bearish bias only. Flat = no trade.

**ITF — Timing.** MACD histogram on the intermediate timeframe (typically daily for weekly HTF). Cross above zero = bullish window opens. Cross below zero = bullish window closes. Identifies the *moment* within the HTF-allowed direction.

**LTF — Entry.** On the lower timeframe (typically intraday bars), wait for: a pullback to the 21-EMA AND RSI in the 40-65 band. Pullback to MA = location. RSI band = momentum has cooled without breaking. This is the *trigger*.

### Decision tree for screen disagreement

Most of the time the screens disagree. **That is the point.** The decision tree for disagreement is mechanical:

- **HTF flat** → No trade. Wait for direction. Higher screens dominate.
- **HTF up, ITF bear** → No trade. ITF says the bullish window is closed; wait for it to reopen.
- **HTF up, ITF bull, LTF waiting** → Setup. No entry yet. Patient — the LTF will eventually retrace or confirm.
- **HTF up, ITF bull, LTF trigger** → Enter. Risk per Section 12C. Invalidation = close below the 21-EMA on LTF.
- **HTF down (any other state)** → If shorting is in your mandate, mirror the rules. If not, no trade.

### Why the discipline matters

The bias toward action will make you take trades on a single screen. A daily breakout is exciting; you act before checking the weekly. The weekly was rolling over. You bought into distribution disguised as a breakout. **Triple-screen exists specifically to slow you down at the moment you most want to act.** The selectivity from this discipline is worth more than any indicator stack.

[INTERACTIVE: multi-timeframe]

---

## 10F · The composite signal: an eight-dimensional regime scorecard

Any single regime indicator is noisy. The composite-signal framework aggregates **eight orthogonal dimensions** of market state into a single bias number on a −100 (strong bear) to +100 (strong bull) scale. Each dimension averages multiple signals within it; the composite is a weighted average across dimensions.

This is a *tilt indicator*, not an entry trigger. It sets the macro-regime layer of the hierarchy (Section 10A.5, layer 1). It does not replace structure-level invalidation rules. Its purpose is to **suppress trade attempts in adverse regimes and permit them in supportive ones**.

### The eight dimensions

> **Important: weights are heuristic, not empirically optimized.**
>
> The weights below (Volatility 18%, Credit 15%, etc.) reflect practitioner judgment and sensitivity analysis. They are NOT from empirical optimization against a holdout set. Users should:
>
> 1. Treat the composite as a starting framework
> 2. Recompute with their own weights based on walk-forward backtesting
> 3. Recalibrate periodically as regimes shift
>
> The score is most informative as a **directional indicator** ("regime strongly supportive vs weakly supportive vs hostile") rather than as a precise value. Anchor decisions on the regime bucket; treat the numerical score as a confidence indicator.

Each dimension is an independent statement about market state, scored from −1 (most bearish) to +1 (most bullish). The composite recomputes from the weighted average.

**1. Volatility / Fear (weight: 18%).** Inputs: VIX percentile rank against 1-year history, MOVE bond-vol index, SKEW index (third-moment risk). High VIX percentile + high MOVE = stress; both are bearish components. Low VIX percentile with low MOVE = complacency, mildly bullish for mean reversion.

**2. Credit (weight: 15%).** Inputs: High-yield OAS, investment-grade OAS, 1-month delta in spreads. Widening credit = funding stress. Tightening = risk appetite. Credit leads equity by days to weeks at major turns.

**3. Rates (weight: 12%).** Inputs: 10Y-2Y curve (inversion is bearish on a multi-quarter horizon), 5Y breakeven, absolute 10Y level. Curve shape is the dominant input.

**4. Dollar / FX (weight: 10%).** Inputs: DXY 5-day trend, USD/JPY. Rising dollar = risk-off. Falling dollar = risk-on.

**5. Commodities (weight: 8%).** Inputs: WTI level and trend, gold, gold/oil ratio. Gold/oil rising = stress (deflationary). WTI rising = inflation.

**6. Global / Overnight (weight: 10%).** Inputs: EEM (EM equities), EFA (developed ex-US), 5-day return basket. Persistent global weakness leading SPX = bearish; global strength while SPX flat = bullish setup.

**7. Trend (weight: 17%).** Inputs: SPX 200-SMA slope, ADX. The trend filter most retail strategies under-use. Trend up + ADX > 20 = the regime where mean-reversion is most exploitable.

**8. Sentiment (weight: 10%).** Inputs: Advance/decline ratio, put/call ratio, RSI(14) on SPX. Sentiment is contrarian on short horizons (extreme bullish = pullback risk) and aligned on longer horizons (sustained breadth = sustained move).

### How to use the composite

The composite is the macro-layer input to the hierarchy. Specifically:

- **Composite ≥ +40**: Strong bull. New long swing trades permitted at full intended size.
- **Composite +10 to +40**: Bull tilt. Long trades permitted at 70-80% of intended size.
- **Composite −10 to +10**: Neutral. Take only the highest-conviction setups. Size at 50%.
- **Composite −10 to −40**: Bear tilt. Long trades suspended; tactical shorts permitted if in mandate.
- **Composite ≤ −40**: Strong bear. Defensive only. Mechanical foundation sleeves continue; no new tactical positions.

[INTERACTIVE: composite-scorecard]

### The composite vs conviction score (preview)

The composite signal answers "what is the regime?" The conviction score in Section 12B answers "given the regime, should I take this specific trade?" They are complementary. A composite of +50 doesn't earn you the trade — you still need to score E × M × R × X × S. But a composite of −60 zeroes the R factor for most long strategies, regardless of how high the other factors are.

Use the composite to **filter the universe of trades you'll consider**. Use the conviction score to **evaluate the trades that survived the filter**.

---

## 10G · The four core swing archetypes

The framework supports four primary swing setups for index and large-cap single names. Each is a formal pattern with measurable entry conditions, sizing rules, and invalidation criteria. They cover the high-probability operational surface for swing trading on horizons of 2-10 days.

A fifth setup — pre-earnings momentum on single names — is treated separately in 10H because its catalyst dynamics warrant a full subsection.

### Archetype 1 — Trend Pullback / Reclaim

**Edge source.** Mean reversion within a confirmed Stage 2 trend. Positive-GEX dealers fade the pullback by buying at moving-average support, providing mechanical tailwind. Connors' RSI(2) parameterization is **Tier B** (practitioner work published in trade books, not peer-reviewed journals); the underlying short-horizon mean-reversion phenomenon has academic support (Lo and MacKinlay 1990; Jegadeesh 1990 reversal effect), but the specific RSI(2) threshold (<10) and lookback are practitioner-calibrated. Treat as practitioner-grade signal with an academic underlying — not a Tier A result.

**Required regime.**
- Composite signal ≥ +30
- Stage 2 confirmed (30-SMA slope ATR-normalized > +0.05, price > 30-SMA, ADX 20-30)
- Positive net dealer GEX (or above the gamma flip level)
- VIX < 22 (above this, even Stage 2 setups have wider noise distributions)
- VIX term structure in contango (VIX < VIX3M)

**Entry trigger.** Daily close with both:
- RSI(2) < 10 OR IBS < 0.20
- Pullback touches or breaches the 10-EMA or 21-EMA from above

**Execution.** Enter at the open the next trading day if Friday's level holds in pre-market, OR intraday on confirmation of EMA reclaim. Vehicle: XSP for tax efficiency; SPY or QQQ for finer share-level sizing; SPX for size.

**Sizing.** Risk 1-1.5% portfolio per trade — meaning the dollar loss *if the stop is hit*, NOT the notional deployed. Resulting notional is typically 20-100× the dollar risk for equity trades; bounded by premium for long options. Compute: n = risk_budget / (stop_distance × multiplier). Stop = below entry-day low (typically 0.5-1.0% below entry). See 12C for the risk-vs-notional distinction.

**Profit target.** 1.5-2R OR close above prior 5-day high, whichever first.

**Time stop.** 5 trading days. Close regardless of P&L.

**Invalidation.** Close below entry-day low OR 30-SMA slope turns negative (Stage transition).

**Common failure mode.** Setup fires during composite +10 to +30 (mediocre regime); price rolls over rather than bouncing. Mitigation: respect the composite filter strictly.

### Archetype 2 — Compression Breakout

**Edge source.** Range expansion after volatility contraction reflects absorbed supply (Section 10C VCP mechanism). In positive-GEX regimes, dealers short the upside hedge into the breakout, accelerating continuation.

**Required regime.**
- Composite signal ≥ +30
- ADX falling to or below 15-18 (range contraction)
- Volume contracting to 70-90% of 20-day average during base
- VIX < 18
- Positive GEX

**Entry trigger.** Price breaks above range high OR identified VCP pivot, on volume ≥ 130% of 20-day average. Acceptable wider entry: 0.1% above the pivot level (don't chase further).

**Execution.** Enter on the breakout bar with marketable limit. Vehicle: equity directly for cleanest execution, OR bull call spread for defined-risk option expression.

**Sizing.** Risk 1% portfolio (dollar loss if stop hit, not notional deployed; see 12C). Stop = midpoint of the prior range (typically 1-2% below breakout level). Resulting notional often approaches portfolio size for equity expressions; bounded by premium for option expressions.

**Profit target.** Range width above breakout level (a measured-move target) OR 2R, whichever first.

**Time stop.** 8 trading days. If no follow-through within this window, the breakout was likely fake.

**Invalidation.** Close back inside the prior range within 2 sessions; close below midpoint of range.

**Common failure mode.** Fakeout breakouts on weak volume that reverse within 2 days. Mitigation: enforce the volume confirmation rule strictly. A breakout on volume below 100% of average is statistically more often a fakeout than a continuation.

### Archetype 3 — Undercut and Reclaim

**Edge source.** Stop-loss orders cluster below well-known technical levels (200-day MA, prior swing lows). When price breaks the level, those stops trigger, accelerating the decline. When the move fails to follow through and reverses, the shorts that opened on the breakdown are forced to cover. The reclaim above the level signals demand has overwhelmed supply.

**Required regime.**
- Composite signal ≥ +10 (less regime-sensitive than Trend Pullback)
- Index or single-name in Stage 2 or transitioning from Stage 1 to 2
- Well-defined technical level being tested (200-day MA, prior swing low, major round number)

**Entry trigger.** Intraday low penetrates the well-known level; close back above the level by EOD. Confirmation: volume on the reclaim bar > 110% of average.

**Execution.** Enter at next-day open if pre-market holds, OR intraday on confirmation of level holding through the morning session. Vehicle: equity directly for single names; XSP or SPY for index.

**Sizing.** Risk 0.5-1% portfolio per trade (dollar loss if stop hit, not notional deployed; see 12C). Lower than Trend Pullback due to single-name execution friction. Notional often runs 20-50× the dollar risk for clean Mag-7 equity expressions.

**Profit target.** Next overhead resistance level OR 1.5R, whichever first.

**Time stop.** 3 trading days.

**Invalidation.** Close below the undercut low (rejection of the reclaim).

**Common failure mode.** Multiple sequential undercuts where the level becomes a magnet for further declines. Mitigation: if a setup undercuts a major level for a second time within 5 sessions, skip — the level is becoming a ceiling, not a floor.

### Archetype 4 — IBS + RSI Mean Reversion

**Edge source.** Combining intraday positioning (IBS = Internal Bar Strength = (close − low) / (high − low)) with multi-day oscillator (RSI(2)) captures different aspects of selling pressure. IBS reflects today's close relative to today's range; RSI(2) reflects multi-day momentum extreme. The confluence is genuine, not multicollinear.

**Required regime.**
- Composite signal ≥ +20
- Stage 2 confirmed
- Positive GEX above flip
- VIX < 22

**Entry trigger.** Daily close with both:
- IBS < 0.20 (closed in bottom 20% of today's range)
- RSI(2) < 15

**Execution.** Enter at next-day open. Vehicle: QQQ or SPY equity for cleanest execution; XSP if option expression preferred.

**Sizing.** Risk 1% portfolio (dollar loss if stop hit, not notional deployed; see 12C). Tight stop at intraday low (typically 0.5% below entry) means the small per-share risk supports larger position count. With a 0.5% stop and 1% risk, a $300k portfolio can deploy up to ~200% notional in shares — which is leveraged. Verify margin and gap risk before sizing this aggressively.

**Profit target.** First close above entry-day high OR 1R, whichever first. This setup has a high win rate but small per-trade payoff.

**Time stop.** 2 trading days.

**Invalidation.** Close below intraday low of entry day.

**Common failure mode.** Continuation lower if regime is genuinely deteriorating (composite was already weakening). Mitigation: require composite ≥ +20 strictly.

### Why these four archetypes?

The four archetypes cover the conditional swing-trading opportunity surface across three different mechanisms:

| Archetype | Mechanism | Best regime | Typical hold |
|---|---|---|---|
| Trend Pullback | Mean reversion in trend | Strong bull (composite ≥ +30) | 2-5 days |
| Compression Breakout | Range expansion | Strong bull, low VIX | 5-8 days |
| Undercut and Reclaim | Short-cover dynamics | Any positive regime | 2-3 days |
| IBS + RSI | Multi-factor mean reversion | Strong bull, calm | 1-2 days |

Together they capture the high-probability surface for **long swing trades in positive-regime environments**. They do not cover:
- Short trades (require Stage 4 / negative-regime context)
- Long vol trades (require event imminence or extreme low IV)
- Multi-week thesis-driven positions (require fundamental view, not just technical setup)

For those, see Section 10H (pre-earnings, which IS in this surface) and Section 10I (catalyst overlays).

---

## 10H · Pre-earnings momentum swings

> **Evidence tier**: Pre-earnings momentum is **Tier B/C**. Post-earnings drift (PEAD) is Tier A (Bernard and Thomas 1989; Chordia and Shivakumar 2006); the pre-earnings drift conditional on momentum and options flow has mixed evidence.
>
> **The framework's primary edge is exit-before-earnings discipline**, not entry. The disciplined exit converts a binary catalyst gamble into a swing trade with capped downside. Without the exit discipline, this is a single-name event play with strongly negative expected value (Adams and Neururer 2020 documented this for retail through-earnings short-vol).

This subsection is the operational extension of the pre-earnings momentum thesis — the standalone application that connects to the screener work. It deserves its own subsection because the catalyst dynamics, surface effects, and execution friction differ qualitatively from the four trend-following archetypes in 10G.

The central claim: **stocks with constructive pre-earnings setup and momentum-confirming flow can be swung profitably *into* the IV ramp, with the trade closed before the earnings event itself.** This is fundamentally different from "trade through earnings" plays, which are catalyst gambles. The pre-earnings momentum swing captures the structural IV bid plus the pre-event drift, then exits before the binary outcome.

### The two pre-earnings effects

Two empirical phenomena create the operational opportunity:

**1. Pre-earnings IV ramp.** Implied volatility rises in the days leading up to an earnings announcement because options are forward-looking and the event is a known source of large jump risk. The mechanism is well-documented: option implied volatility before earnings is a blend of ambient volatility (normal daily price movement) and event volatility (the anticipated earnings jump). As each trading day passes, the one-day event becomes a larger percentage of the option's remaining life, mathematically pulling up the headline IV. Typical magnitude: ATM IV rises 20-50% in the 5-10 days before earnings, with most of the rise concentrated in the final 3 days. IV typically peaks the day before earnings.

**2. Pre-earnings announcement drift (PEAD prelude).** Stocks that show constructive momentum, positive options flow (call buying outweighing put buying), and tightening IV term structure (forward IV cheap relative to event IV) tend to drift modestly higher in the 1-3 weeks before earnings. The literature on this is less robust than post-earnings drift (which is one of the most replicated findings in finance), but the pre-earnings effect is real and is sharpest in large-cap momentum names with strong analyst-revision flow.

The pre-earnings momentum swing **combines both effects**: ride the underlying drift while the IV ramp inflates the option premium, then exit before the earnings event resolves the IV crush against you.

### The expected move and its uses

For any earnings event, the market prices an "implied move" via the ATM straddle of the first expiration after earnings:

```
Implied move % = (ATM call price + ATM put price) / underlying price × 100%
```

A more accurate version weights the ATM straddle and the first two OTM strangles. ORATS uses this composite expected-move calculation as a standard reference for earnings flow.

**Operational uses of the implied move:**

1. **Position sizing.** If the implied move is ±9%, a position sized to absorb a 5% adverse move will be obliterated by a typical earnings reaction. Size accordingly, or exit before the event.

2. **Historical comparison.** ORATS, Market Chameleon, and similar tools provide trailing 8-quarter median actual moves. If the median historical actual move is 12% and the current implied move is 6%, the market is under-pricing volatility — favors long-vol structures (long straddle, long strangle) if held through. If implied 9% vs historical 6%, market is over-pricing — favors short-vol structures *after* the event (post-event premium selling into the IV crush is a real, separate strategy).

3. **Strike selection.** The implied move boundary is a natural strike for short legs of diagonal/calendar spreads — sell calls or puts at the implied move boundary on the front-month side.

### The pre-earnings momentum setup

**Required conditions (must all be met):**

1. **Stage 2 trend confirmed**: 30-day SMA rising; price above SMA; ADX > 20.
2. **Earnings 3-10 trading days away**. (Sweet spot 5-7 days — enough for the IV ramp to develop without too much risk of catalyst spillover.)
3. **Constructive options flow**: net call buying for at least 5 of the prior 10 trading days (visible via Cboe options flow data, ORATS, Market Chameleon, or similar).
4. **IV term structure showing event premium**: front-month ATM IV > 90-day ATM IV by at least 15 vol points (steep backwardation reflecting the earnings event).
5. **Forward IV not cheap**: if forward IV (computed per 5G) is below 70% of ambient long-dated IV, the market is anticipating significant post-event vol crush — exit-before-earnings discipline is mandatory.
6. **Composite signal ≥ +20**: macro regime supportive.

**Entry trigger.** Once all six conditions are met, enter on the next constructive technical signal:
- Pullback to 21-EMA with RSI(2) < 15 (Trend Pullback overlay)
- VCP pivot breakout (Compression Breakout overlay)
- Higher low confirmed against the prior pullback

The pre-earnings setup is essentially **one of the four base archetypes with a pre-earnings overlay** that justifies sizing up the conviction and a different exit rule.

### Vehicle selection

Three primary vehicles, each with different trade-offs:

**1. Equity (preferred for cleanest expression).** Long shares of the underlying. Pure directional exposure. No options friction. Exit position before earnings — typically at the close on T-1 or the morning of T-day.

**2. Long call spread (defined risk).** Buy ITM/ATM call, sell call at or just above implied move boundary. Captures most of the directional upside while bounded loss. IV exposure is partially hedged (long call has positive vega, short call has negative vega — net positive but small). Exit before earnings.

**3. Diagonal call spread (hybrid directional/vol vehicle — read carefully).** Long back-month ATM/ITM call, short front-month call at implied move boundary. Note this is *not* a pure directional expression: it combines a directional thesis (back-month long call) with a short-vol/short-event leg (front-month short call) that profits from the front-month IV crush after earnings. If you carry the short front leg *through* earnings, you've taken on event risk on the short side — a large favorable gap can drive the short strike deep ITM and create assignment risk. Diagonals belong in the pre-earnings playbook *only* when (a) the surface analysis (forward IV cheap relative to front IV) specifically favors them, and (b) you have a defined plan for closing or rolling the short leg before earnings.

For most retail applications, **equity is the default; long call spread is the option overlay for defined risk in single names**. Diagonals are a *vol-surface* trade that happens to overlap with a directional thesis — treat them as such, not as a "fancier call spread."

### The exit-before-earnings rule

**The defining discipline of the pre-earnings momentum trade is the pre-earnings exit.** The position is closed:

- On equity: at the close on T-1 (the trading day before earnings) at the latest, or the morning of T-day if the morning gap is favorable.
- On long call spreads: at the close on T-1 or earlier if profit target is hit.
- On diagonals: depends on structure — typically T-1 or held through with explicit acknowledgment that you're now in a "trade through" position with different risk.

**Why the discipline matters:**

Post-earnings outcomes are binary at retail scale. The implied move is the market's median expectation; the realized move can be 2-3× the implied move in either direction, with the largest gaps occurring on guidance surprises, not just EPS surprises. **A single bad earnings outcome can wipe out 10-20 successful pre-earnings momentum trades.**

The expected value calculation for "trade through earnings" on single names at retail consistently shows negative or barely-positive EV (Adams-Neururer 2020 documented this). The expected value calculation for "exit before earnings" on the same pre-earnings setup remains positive because you're capturing the IV ramp + drift while declining to absorb the binary risk.

This is the discipline that converts the pre-earnings momentum thesis from a gambling strategy into a swing strategy.

### Worked example: a constructive pre-earnings momentum swing

**Setup.** NVDA at $720, earnings in 6 days. 30-day SMA at $680, rising at +0.15 ATR-normalized slope (strong Stage 2). RSI(14) at 62 (healthy momentum, not extreme). Composite signal +45. Options flow: 7 of last 10 sessions show net call buying. Front-month ATM IV 48%; 90-day ATM IV 32% (16 vol-point spread — confirms event premium).

Forward IV (formula from 5G) for the 76-day window after the front expiration:

```
σ_forward² × (76/365) = (0.32² × 90/365) − (0.48² × 14/365)
                     = 0.02527 − 0.00884
                     = 0.01643
σ_forward² = 0.01643 / 0.2082 = 0.0789
σ_forward ≈ 28.1%
```

Forward IV is about 4 vol points below 90-day IV — modest post-event vol crush priced in. The 16-vol-point front premium captures the event-vol component. The diagonal call spread (long back, short front near the implied move) would harvest this event premium asymmetry.

NVDA pulls back 2.8% over 3 sessions to $700. RSI(2) at 12. Touches 21-EMA at $698. Holds with intraday reclaim.

**Conviction analysis.**
- E = 0.65 (pre-earnings momentum is Tier B with mixed evidence; the trade-before-event approach lifts it relative to "trade through")
- M = 0.80 (IV ramp + PEAD mechanisms both well-documented)
- R = 0.85 (composite +45, Stage 2, all six conditions met)
- X = 0.85 (NVDA options highly liquid, but bid-ask wider than SPX)
- S = 0.80 (sized to be insulated from gap risk because we'll exit before the event)

C = 0.65 × 0.80 × 0.85 × 0.85 × 0.80 = **0.300** (medium-high, take the trade)

**Trade.** Long 200 NVDA shares at $702 (intraday entry on reclaim confirmation).
- Risk: $5,000 portfolio risk → stop at $677 (about 3.5% below entry — wider than normal Trend Pullback to absorb pre-earnings volatility).
- Profit target: not required; primary exit is time-based (T-1 close).

**Outcome.**
Day 1 after entry: NVDA at $710 (+1.1%).
Day 2: $718 (+2.3%). IV ramping aggressively.
Day 3: $725. Stop trail to $710.
Day 4 (T-1 of earnings): NVDA at $733. Close position at $732 at EOD. Profit: $30/share × 200 = $6,000. ~1.2R.

**What we declined:** Earnings come out at $735 in extended hours. Initially the stock pops to $745 (+2%) on the print, then guidance disappoints in the call, and the stock closes the next day at $698 — a 4.9% one-day decline. A trader who held would have lost approximately $7,000 instead of gaining $6,000. The $13,000 swing represents 2.6R of avoided loss.

[INTERACTIVE: pre-earnings-iv-ramp]

### Pre-earnings setup screener — the operational system

For systematic application, a screener filters the universe daily on:

1. **Earnings calendar**: stocks with earnings 3-10 trading days out
2. **Stage filter**: Weinstein Stage 2 confirmed (rising 30-SMA, price above, ADX > 20)
3. **Momentum filter**: RSI(14) in 50-70 range, healthy not extreme
4. **Options flow**: cumulative call-buying signal over prior 5-10 sessions
5. **IV term structure filter**: front-month IV > 90-day IV by 15+ vol points
6. **Liquidity filter**: average option volume > 5,000 contracts on near-dated ATM
7. **Composite filter**: macro regime ≥ +20

Stocks passing all seven filters become candidates. Manual review of each candidate verifies: clean technical pattern; no recent fundamental deterioration; positive analyst flow.

This is the structural skeleton of the screener. The signal-aggregation logic and 100-point composite scoring sit on top of this filter foundation.

### When to skip pre-earnings setups

The most important discipline is recognizing when *not* to take a candidate:

- **Implied move > 10%**: Single-name positions can't be sized cleanly with stops at this magnitude. Use defined-risk options or skip.
- **Stage 3 emergence (rolling 30-SMA flattening)**: The pre-earnings setup requires Stage 2; if it's flattening, the setup is structurally weakening.
- **Composite signal < +20**: Macro doesn't support; defer.
- **Recent guidance cut or analyst downgrades within 2 weeks**: Fundamental flow already negative; skip.
- **Stock has already moved > 8% in the 5 days before setup**: The drift has likely already happened; you're chasing.
- **IV term structure is flat or normal (not steep)**: The event isn't being priced into options — either the market doesn't care, or the catalyst isn't actually material.

The skip discipline is half the system. The most profitable thing about a screener is the candidates it rejects.

---

## 10H.2 · Post-earnings drift / gap-and-go — the PEAD companion playbook

Section 10H covers the *pre-earnings* momentum swing: ride the IV ramp + drift, exit before the event. This subsection covers the **mirror** strategy: enter *after* the event has resolved, capture the post-earnings drift (PEAD).

The strongest empirical edge of the two. While pre-earnings drift is **Tier B/C** evidence (mixed academic support, mostly practitioner), post-earnings drift is one of the most robust anomalies in finance — **Tier A**, repeatedly replicated across decades and markets (Bernard and Thomas 1989; Bernard and Thomas 1990; Chordia and Shivakumar 2006; many subsequent studies). The asymmetry is significant: the post-earnings drift framework has a stronger evidentiary foundation than the pre-earnings momentum thesis, and arguably should be the higher-priority deployment in a swing book.

### The PEAD mechanism

When a company reports earnings:
- The price gaps based on the immediate market reaction.
- Analysts and institutions begin recalibrating their estimates and positions.
- The recalibration takes **weeks to months**, not minutes — institutional flow is slow.
- During this recalibration window, the post-event drift in the same direction as the initial gap is persistent and statistically robust.

The drift is *not* in the immediate post-earnings 30 minutes (that's covered by the gap itself and partial mean-reversion in the opening minutes). The drift unfolds over **5-60 trading days post-event**, particularly for stocks where:
- The earnings surprise was large (analyst expectation gap >5%)
- Revenue beat in the same direction (not just EPS engineering)
- Guidance was raised (or lowered for negative direction)
- Institutional sponsorship is rising (rising relative volume + accumulation signatures)

### The setup

**Required conditions** (after a positive earnings event for long PEAD; mirror for short PEAD):

1. **Quality of the beat**: revenue + EPS + guidance all positive. EPS-only beats with revenue miss or flat guidance often fail to drift.
2. **Gap size and hold**: stock gaps up >5% on the report; opens the next session at or near the post-event level (not gapping back to pre-event range).
3. **Opening range hold**: in the first 30-60 minutes after the open, stock holds above VWAP and the prior day's close.
4. **Volume confirmation**: opening hour volume >2× the 20-day average; sustained heavy volume through midday.
5. **Sector/peer confirmation**: peers in the same industry also up (or at least not down) — sector tailwind reinforces the drift.
6. **No immediate technical blockers**: not running directly into the underside of a 50D or 200D MA from below (which would create supply); not running into a high-volume cluster from the prior 6 months.
7. **IV crush has occurred**: front-month ATM IV has crushed to roughly the 90-day IV level. The event-vol component is out; options are now reasonably priced.

The skip discipline: if the gap is "weak" (only EPS beat, flat or guidance lowered, gap fading in opening hour), the PEAD framework gives no edge. The drift only persists when the fundamental quality is real.

### The structure

The exit-before-earnings problem from 10H is reversed. Here the earnings event is past, IV has crushed, and the option chain is cleaner. Three preferred vehicles:

**1. Equity (default).** Long shares of the underlying. Hold for 5-30 days targeting the drift. Clean directional exposure with no vol overlay. Best for accounts that don't need leverage.

**2. Long call spread (defined-risk leveraged).** Buy a long call slightly OTM or ATM (30-45 DTE); sell a higher-strike call (around the analyst-implied 30-day target, typically 5-10% above spot). Captures the drift with leverage; defined risk. Long call alone is acceptable but uses more capital per unit of exposure than a spread.

**3. Put credit spread below the gap.** Sell a put at the post-gap support level (often the prior consolidation top, now a floor); buy a lower-strike put for defined risk. Captures the drift via theta + delta, with IV crush already locked in. Best when IV is still slightly elevated post-event and the gap is well-supported on the chart.

**Avoid for PEAD**:
- Naked long calls in high-IV-percentile names (vega risk is non-trivial even post-crush)
- Calendars or diagonals (these are pre-event vol-surface trades; post-event, the surface is already collapsed)
- Holding through the *next* earnings event (this is a new binary catalyst that is not part of the PEAD edge)

### Position sizing and time horizon

- **Sizing**: 1-1.5% risk per trade (same as other swing playbooks per 12C)
- **Hold period**: 5-30 trading days. Tail of the drift extends to ~60 days but the bulk of the move occurs in the first 4-6 weeks.
- **Exit triggers**: target reached, stop hit, time stop (60 days max), or fundamental change (analyst downgrade after entry, guidance withdrawal, etc.)
- **Profit-taking discipline**: take half off at +0.75R; trail the remainder. PEAD trades have asymmetric profit distributions — most close near +1-1.5R, but the tail extends to +3-5R when the drift runs.

### Worked example: NVDA post-earnings (illustrative)

NVDA reports earnings after-hours on a Wednesday. Revenue beat by 8%, EPS beat by 12%, guidance raised by 5%. Stock gaps from $720 to $760 in after-hours, opens Thursday at $762.

**Day 1 (Thursday)**: Stock holds above VWAP all day, closes at $768 on 3× average volume. Opening range high $764 holds as intraday support. Sector (semiconductors, SMH ETF) up 2.5%. Front-month IV crushed from 48% to 32% (event premium out). Composite signal supportive.

**Real Value check** (from 12B):
- F = 0.85 (clean beat across all three metrics + raised guidance)
- T = 0.80 (gap held; opening range supportive; above all major MAs)
- O = 0.70 (heavy call buying continues post-event; opening transactions)
- G = 0.75 (post-event GEX positive; call wall at $800)
- V = 0.70 (IV reasonable post-crush; not over-paying)
- X = 0.85 (NVDA liquid)
- S = 0.85 (1% portfolio risk; correlation with existing tech book OK)

RV = 0.85 × 0.80 × 0.70 × 0.75 × 0.70 × 0.85 × 0.85 ≈ 0.20 (borderline, but at the upper end of the borderline range; this is RV's multiplicative-form discipline at work — even with all factors "good," the product compresses).

Reframe: take, but at half size (0.5% risk). Or wait for a tighter pullback within the next 5 sessions to improve T to 0.9+ and V to 0.8+.

**Entry**: Friday morning, NVDA pulls back to $755 in the opening 30 minutes, holds above the $762 opening-range pivot. Long 100 shares at $758. Stop $748 (risk $1,000 = 0.5% of $200k portfolio).

**Exit**: 4 weeks later, NVDA at $815. Trim 50% at $795 (+0.75R per share × 100 = +$3,700). Trail remainder with a 10-day MA stop. Final exit at $815 → another $2,000 on the trailed half. Total +$5,700 on $1,000 risk = +5.7R. Hold period 28 days.

### Failure modes

**1. Buying the gap, not the drift.** Entering at the post-event open at peak euphoria, often near intraday highs. The first 30-60 minutes are noise; entries should be on a pullback to the opening range or VWAP, not on the gap itself.

**2. Holding through the next earnings.** A PEAD trade in a stock reporting again 2 months later carries the next earnings as a binary catalyst. The PEAD edge does not extend through subsequent earnings events. Either exit before the next report or accept that you're now in a different trade.

**3. PEAD on weak beats.** EPS-only beats, missed revenue, or flat-to-lowered guidance: skip. The drift is conditional on fundamental quality, not just the price gap. PEAD is not "buy any post-earnings gap up."

**4. Ignoring sector context.** A positive earnings gap into a sector that's already breaking down (negative sector breadth, peers down) often fails to drift. The PEAD framework requires the broader environment to be at minimum neutral, ideally supportive.

**5. Wrong vehicle for the holding period.** Buying 7-DTE calls on a PEAD thesis with a 30-day expected drift: the theta will destroy the trade before the drift develops. The minimum reasonable expiration is 30-45 DTE; longer is better.

### PEAD vs pre-earnings momentum — when to use which

| Factor | Pre-earnings momentum (10H) | Post-earnings drift (10H.2) |
|---|---|---|
| Evidence tier | Tier B/C (mixed academic support) | Tier A (decades of replication) |
| Holding window | 1-3 weeks before event | 5-30 days after event |
| Exit discipline | Must exit before announcement | Hold through drift, exit on target or stop |
| Vol overlay | IV is ramping (long-vega favorable) | IV has crushed (defined-risk plays cleaner) |
| Vehicle defaults | Equity, long call, long call spread | Equity, long call spread, put credit spread |
| Main failure mode | Holding through earnings (binary) | Buying gap at peak euphoria; holding through next earnings |
| Risk character | Continuous (controllable) | Continuous (controllable) |

The two strategies are complementary, not competing. A well-organized swing book can run both: 10H trades into the event; 10H.2 picks up trades *after* the same event resolves positively. The 10H position is closed at T-1; the same stock may become a 10H.2 candidate at T+1 if the earnings response is strong enough.

---

## 10I · Catalyst event swings — FOMC, CPI, NFP, FDA

Macro-event days operate by a different mechanic than the trend-based archetypes. They're characterized by a **single high-information moment** (the announcement) that resolves uncertainty discretely. The opportunity is in positioning around the path-dependent pre-event and post-event dynamics, not the announcement itself.

The principal events for SPX/SPY/QQQ swing traders:

- **FOMC** (Federal Open Market Committee) — 8 meetings per year, typically Tuesday-Wednesday with announcement at 2:00 PM ET Wednesday; press conference 2:30-3:30 PM ET
- **CPI** (Consumer Price Index) — monthly, typically second week, 8:30 AM ET
- **NFP** (Non-Farm Payrolls / Employment Situation) — monthly, first Friday, 8:30 AM ET
- **Treasury auctions** — particularly 10-year and 30-year auctions during volatile rate periods
- **ECB / BOJ / BOE rate decisions** — overnight events affecting SPX overnight session
- **FDA decisions / clinical readouts** — single-name biotech and pharma catalysts

For each, three operational positions are possible:

### Position 1 — Pre-event vol bid play

Enter long-vol structure 3-5 trading days before the event when IV is elevating into the announcement but the event hasn't been fully priced. Exit before the event.

**Mechanism**: Pre-event IV ramp is structurally similar to single-name earnings IV ramp. Index IV rises into known events (typical magnitude: 1-3 VIX points into FOMC, 2-4 points into NFP/CPI).

**Vehicle**: Long calls or long call spreads if you have directional view; long straddle/strangle if you expect a large move regardless of direction.

**Discipline**: Same as pre-earnings — exit before the announcement to capture the IV bid without absorbing the binary outcome.

### Position 2 — Post-event vanna unwind ramp

The setup pre-discussed in 7B. Enter just before or just after the announcement on confirmation that IV is crushing post-event. Long bias.

**Mechanism**: Vol crushes regardless of direction → dealer-short-puts decay in delta → dealers buy back hedge stock → mechanical ramp lasts 30-90 minutes post-announcement.

**Vehicle**: Long ES futures (overnight session), SPY shares, or SPX/XSP long call spreads with very short DTE (0DTE or 1DTE). The position is intentionally short-duration because the mechanical effect operates within hours.

**Sizing**: Reduced because event-day moves can swamp the mechanical signal. 0.5% portfolio risk max.

**Entry signal**: VIX drops > 2 points within 15 minutes of the announcement (confirms IV crush is occurring). Underlying not breaking the day's intraday low.

**Time stop**: End of the trading session.

### Position 3 — Skip the event entirely

The most common correct action. **The composite signal scorecard treats event proximity as a regime input.** If a major event is within 2 trading days and your existing portfolio carries directional exposure that would be damaged by an adverse outcome, reduce sizing or hedge.

The "skip" discipline applies particularly to:
- Existing swing positions at risk from event volatility
- Multi-day positions where the event falls in the middle of the trade horizon
- High-leverage option positions where the implied move is large relative to position sizing

### Worked example: FOMC week play

**Setup.** FOMC announcement Wednesday at 2 PM ET. Composite signal +40, Stage 2 confirmed. VIX 16 on Friday before; rises to 18 Monday and 20 Tuesday on event-vol bid. SPX 6,000 entering the week.

**Decision tree.**

*Monday morning:* Check active swing positions. Two Trend Pullback positions (long XSP) currently +0.3R. Decision: hold (composite still supportive, but mark mental note to reduce or hedge if VIX > 22 going into Wednesday).

*Tuesday close:* VIX 20.5. Composite +40 holding. No new entries today. Risk of holding through FOMC: implied move on SPX for Wednesday is ±1.2%; position stops are at 0.5% below entry; could blow through. Decision: trim half of one position at the close, accepting the 0.15R cost to reduce gap exposure.

*Wednesday 1:30 PM:* Position remains intact. Pre-announcement VIX 19. Decision: hold remaining position; do not add.

*Wednesday 2:00 PM:* Announcement. Fed leaves rates unchanged with hawkish language. SPX drops 0.5% in 5 minutes, then stabilizes. VIX initially spikes to 22, then drops to 18 within 10 minutes (the vol crush is occurring despite the directional move).

*Wednesday 2:30 PM:* Press conference begins. SPX recovers to flat. VIX drops to 17. Vanna unwind signature confirmed (VIX down 3 points in 30 min).

*Decision:* Add a small position (0.3% risk) sized for the vanna unwind ramp. Long XSP 1DTE call spread, exit by EOD. Confirmation: SPX has reclaimed the morning VWAP; volume is healthy.

*Wednesday 3:45 PM:* SPX up 0.6% on day. Close all positions. Capture: half-trimmed position rallies for partial profit; vanna unwind position closes at 0.4R; original full position unchanged.

**What this demonstrates:** Discrete decision points around the event. Position sizing reductions for the binary risk. Selective opportunity capture on the post-event ramp. **At no point is the trader "trading the announcement" directionally** — the trades are around the event, not on it.

### FDA / clinical event swings (single name)

The single-name biotech catalyst structure operates similarly to FOMC but with vastly larger implied moves. Implied moves for binary clinical readouts can be 30-80%, and the actual outcome is genuinely binary.

**Operational discipline for single-name binary events:**

- Position sizing measured in absolute dollar loss, not percentage of position. A binary clinical outcome can produce a -90% one-day return on the position.
- Defined-risk option structures only. Never naked equity, never short options.
- Position size as if the position is going to zero in your worst-case scenario. If $5,000 at risk on a binary event represents 1% of portfolio, fine. If it represents 10%, the position is unsurvivable in the bad case.
- Pre-event exit usually correct unless the structure was specifically designed for the binary outcome.

The biotech binary trade is a specialized vertical that's outside the scope of the four-archetype framework. It's mentioned here for completeness; treat it as a separate operational specialty if you choose to engage with it.

---

## 10J · Single-name vs index swings — when to use which

The four base archetypes and the pre-earnings overlay apply to both index instruments (SPX/SPY/QQQ) and single-name instruments (Mag-7, momentum stocks, sector leaders). The choice of which to use has consequences for execution friction, position-sizing precision, idiosyncratic risk, and tax treatment.

### When index swings are preferred

**Use SPX/XSP/SPY/QQQ when:**

- Setup is regime-driven (the composite signal favors broad-market action)
- You want to express macro view without single-name idiosyncratic risk
- Tax efficiency matters (XSP/SPX 1256 treatment vs SPY 1099 treatment)
- Execution liquidity is paramount (SPX/XSP have institutional-grade spreads at all strikes)
- You're scaling size (SPX contract multiplier permits efficient large position sizing)

The default for trend-following archetypes (Trend Pullback, Compression Breakout, IBS+RSI) is **XSP for retail traders below $1M account size**, **SPX above that**. The Trend Pullback setup in particular has decades of clean backtest support on SPX/SPY; single-name applications have less robust evidence and more execution friction.

### When single-name swings are preferred

**Use single names (Mag-7, momentum stocks) when:**

- Setup is specifically idiosyncratic (the stock has a unique catalyst, sector tailwind, or company-specific dynamic)
- Pre-earnings momentum applies (only viable on single names with earnings events)
- Relative-strength dynamics matter (a strong stock within a sideways index)
- Single-name dispersion is high (when the index is range-bound but underlying constituents are moving)
- You're explicitly diversifying away from index correlation

Mag-7 names (NVDA, AAPL, GOOGL, MSFT, META, AMZN, TSLA) have institutional-grade options liquidity comparable to SPY — bid-ask spreads, depth, and term-structure availability are all clean. Outside the Mag-7, single-name options execution quality deteriorates noticeably; only the top 30-50 names by options volume have execution clean enough for swing-options strategies.

### The hidden multi-position correlation problem

Single-name positions are often *less diversifying than they appear*. Mag-7 stocks have pairwise correlations of 0.5-0.8 during normal conditions and 0.8-0.95 during stress. A portfolio of NVDA + AAPL + GOOGL long swing positions is fundamentally one large bet on Mag-7 momentum, not three independent bets.

**Operational rule for portfolio-level sizing:** Treat correlated single-name positions as a single position for risk-budget purposes. If your portfolio loss budget is 2% per day for active swing positions, and you have three Mag-7 longs running, each should be sized at 0.67% individual risk — not 2% each.

[INTERACTIVE: mag7-correlation-stress]

(This is the principle worked through in Example 10 of Section 12D.)

### The decision matrix

| Setup type | Default vehicle | Alternative if available |
|---|---|---|
| Trend Pullback (broad regime) | XSP (retail) / SPX (size) | SPY for share-level execution |
| Compression Breakout (broad) | XSP / SPX | SPY |
| Compression Breakout (single name, strong RS) | Mag-7 equity directly | Long call spread for defined risk |
| Undercut and Reclaim (broad) | XSP / SPX | SPY |
| Undercut and Reclaim (single name) | Mag-7 equity directly | Long call spread |
| IBS + RSI Mean Reversion | QQQ shares | SPY shares; XSP options |
| Pre-earnings momentum | Mag-7 equity directly | Long call spread or diagonal |
| Catalyst macro event | XSP / SPX option structure | None (single-name event would be different framework) |

### A note on QQQ

QQQ deserves mention as a hybrid instrument. It's an index ETF (cleaner execution and diversification than single names), but heavily concentrated in Mag-7 (60% of weight in top 10 holdings). For swing-trade purposes, QQQ behaves as "Mag-7 lite" — broad enough to avoid pure single-name idiosyncratic risk, but tech-concentrated enough to capture momentum-driven dispersion when growth leads.

QQQ is the preferred vehicle for:
- IBS + RSI Mean Reversion setups (tech-heavy dispersion creates cleaner mean-reversion signals than broader SPX)
- Compression Breakouts during tech-led regimes
- Setups where you want broad exposure but specifically to growth/tech rather than to value/cyclicals

---

## 10K · DTE selection for swing trades

The expiration date you choose for an options position determines the trade's Greek profile. Wrong DTE for a thesis is a structural mismatch that no execution skill can recover. The framework below operationalizes the choice.

### The DTE decision table

| DTE range | Greek profile | Use case |
|---|---|---|
| **0DTE** | Gamma-dominant, tiny vega, charm-dominant | Intraday convexity plays only. Not appropriate for any 2+ day swing thesis. |
| **1-7 DTE** | High gamma, rapid theta decay, low vega | Tactical event trades (FOMC vanna unwind), short-duration mean reversion. High execution risk; require very high conviction. |
| **8-21 DTE** | Balanced gamma/theta, growing vega | The classic swing-options zone for tactical setups. Trend Pullback option expressions, post-earnings premium selling, vanna-unwind aftermaths. |
| **21-45 DTE** | Lower gamma, lower theta-decay rate per day, meaningful vega | The default swing-options zone. Pre-earnings momentum option overlays, multi-day setups, catalyst-driven positions. |
| **45-90 DTE** | Low gamma, slow theta decay, high vega | Directional thesis with vega exposure. PMCC long legs, diagonal back-month legs. |
| **90-365 DTE** | Very low gamma, minimal theta, very high vega and rho | Strategic positions, hedges, replacement-stock structures. Quarter-plus horizons. |
| **>365 DTE (LEAPS)** | Near-stock delta, minimal theta, extreme vega | Equity replacement strategies. Not "cheap lottery tickets" — the high vega means IV regime change can move the position 30-50% independent of underlying. |

[INTERACTIVE: dte-selection-matrix]

### The matching principle

The cardinal rule: **the DTE should match the thesis horizon, with buffer for adverse path.**

If your thesis is "SPY bounces from the 21-EMA in 2-5 days," using 0DTE options is a structural mismatch — the gamma exposure and theta decay don't match the 5-day horizon. The right vehicle is 14-30 DTE options (which give the thesis time to play out without bleeding to zero through theta).

If your thesis is "NVDA drifts up over 2 weeks into earnings," using 7 DTE options is wrong — earnings is past your expiration, and the theta burn over 14 days at 7 DTE is destructive. The right vehicle is 30-45 DTE options (covers the thesis with buffer).

If your thesis is "tech leads for the next quarter," using 30 DTE options is wrong — too much short-dated gamma noise, too little vega capture for the multi-month horizon. The right vehicle is 90-120 DTE options or LEAPS-based structures.

### Specific DTE choices for each archetype

| Archetype | Optimal DTE | Why |
|---|---|---|
| Trend Pullback | 14-30 DTE if using options; immediate exit if using equity | Hold typically 2-5 days; need buffer for adverse path |
| Compression Breakout | 21-45 DTE | Hold up to 8 days; want meaningful gamma without rapid theta burn |
| Undercut and Reclaim | 14-21 DTE | Hold 2-3 days; tighter DTE OK due to short hold |
| IBS + RSI Mean Reversion | Equity preferred; 7-14 DTE if options | Hold 1-2 days; very short-duration |
| Pre-earnings momentum | Equity preferred; 30-45 DTE if options (expires AFTER earnings) | Trade closes before earnings but vehicle dating must outlast |
| FOMC vanna unwind | 0-1 DTE | Intra-day operation only |
| Macro catalyst hedge | 30-60 DTE | Want vega exposure for IV expansion potential |

### The "expires before exit" trap

A common retail mistake: buying short-DTE options for a swing thesis without verifying that the option's expiration is after the planned exit.

Example: It's Monday. You enter a Trend Pullback setup with a 5-day time stop. You buy options expiring this Friday (4 DTE). On Wednesday, your thesis is playing out but the position needs to hold through Friday's time stop. **But Friday is also expiration day.** You're now forced to either:
- Exit Thursday (one day early, sacrificing potential continuation)
- Roll to next week's expiration (paying premium twice)
- Hold to expiration (taking maximum theta hit on Friday)

The structural fix: choose DTE such that your option expires AT LEAST 2-3 trading days after your latest planned exit. For a 5-day Trend Pullback time stop, that means minimum 8-10 DTE; in practice, 14-21 DTE gives clean buffer.

### Why retail bias is too-short DTE

Retail traders consistently choose shorter DTEs than is optimal for their stated thesis. Two reasons:

1. **Cost.** Shorter DTE options cost less in absolute dollars. A 7 DTE call costs 30-50% less than a 30 DTE call at the same strike. This makes them "feel" more affordable.
2. **Leverage perception.** Shorter DTE options have higher gamma per dollar of premium, which means small moves produce larger percent returns. This is psychologically attractive.

Both reasons confuse leverage with edge. **Cheaper options aren't better options — they're cheaper because they have less time for your thesis to develop and more daily theta cost as a percentage of premium.**

The professional bias is toward longer DTE than feels comfortable, accepting the higher absolute cost in exchange for structural buffer. The asymmetry: paying 30% more for an option that has 3× the time to develop is a fundamentally better risk-adjusted trade than paying less for an option that expires while your thesis is still developing.

---

## 10L · Common swing failure modes and remedies

Across the five swing setups (four trend-based archetypes plus pre-earnings momentum), the same failure modes recur. This subsection catalogs the most common and provides specific remedies.

### Failure mode 1 — Setup creep

**Symptom**: Taking trades that don't meet all the setup's required conditions because "it's close enough" or because slow weeks make you impatient.

**Mechanism**: The framework is designed for selectivity. Each required condition was added because the strategy's edge depends on it. Dropping one condition transforms the setup from "high-probability conditional edge" to "weak directional bet."

**Remedy**:
- Setup card must be physically present (printed, taped, copied) before considering the trade
- Every required condition must be checked and confirmed in writing
- If checking reveals "yeah, that one's not quite there," skip — no exceptions
- Accept that 70-80% of days have no qualifying setup; this is the framework working, not failing

### Failure mode 2 — Holding through the time stop

**Symptom**: Setup's time stop is reached without profit target hit. Position is at small profit or small loss. You hold "to see if it works."

**Mechanism**: Time stops exist because empirical work shows that swing setups that don't pay within their typical horizon have low forward expected value. The probability distribution of "this is a delayed winner" vs "this is a slow loser" is heavily weighted toward the latter.

**Remedy**:
- Time stops are mechanical — close at the specified day's close regardless of P&L
- If you genuinely have a new thesis ("this is becoming a multi-week trade, not a 5-day swing"), close the original position and re-enter with the new framework — never roll the same trade forward without resetting analysis

### Failure mode 3 — Stop migration

**Symptom**: Position is approaching pre-committed stop. You move the stop further "to give it room."

**Mechanism**: Loss aversion (prospect theory). At the stop level, you're psychologically incentivized to avoid the realized loss by deferring it. Stop migration converts small losses into large ones systematically.

**Remedy**:
- Stops, once set, can only be moved toward profit (trailed up on winners), never away from profit
- If you genuinely have new information, close the existing position at market and re-enter with new analysis — don't migrate
- The 25%-PTP / 30-day cool-off rule (Section 12C) is the structural defense for the case where stop migration has happened repeatedly

### Failure mode 4 — Sizing inconsistency

**Symptom**: Larger position size after winning streaks, smaller after losing streaks.

**Mechanism**: Overconfidence after wins; loss aversion after losses. Both push sizing toward the wrong direction (more risk when conditions haven't changed; less risk when nothing about the setup edge has changed).

**Remedy**:
- Position sizing is mechanical: `n ≤ ⌊B_exp / L_max⌋`
- Loss budget `B_exp` is the same percentage of portfolio regardless of recent P&L
- Recent wins do NOT permit larger sizing; recent losses do NOT require smaller sizing
- The only sizing changes that are legitimate: (a) regime-based reductions (composite weakening), (b) drawdown-rule kill switches

### Failure mode 5 — Skipping the exit-before-earnings discipline

**Symptom**: Pre-earnings momentum trade is going well. Earnings approaches. "Just hold through; the momentum is strong."

**Mechanism**: Confirmation bias combined with sunk-cost framing. The position has been profitable; the trader projects continuation through the binary event.

**Remedy**:
- The exit-before-earnings rule is the defining discipline of the pre-earnings momentum trade
- Mechanical close on T-1 at the latest, regardless of how good the trade looks
- Single-name event risk requires defined-risk options (not naked equity) if held through; this is a structurally different trade

### Failure mode 6 — Correlated overconcentration

**Symptom**: Three Mag-7 longs running simultaneously, sized as if independent. Or three Compression Breakouts in growth stocks.

**Mechanism**: The setups are nominally different but the underlying risk factor (Mag-7 momentum, growth-stock dispersion) is the same. Pairwise correlations during stress can hit 0.9+.

**Remedy**:
- Treat correlated positions as one position for risk-budget purposes
- Portfolio-level loss budget bounds the total, not per-trade budget × number of positions
- Cap simultaneous correlated positions: e.g., maximum 2 long Mag-7 swing positions at any time

### Failure mode 7 — Regime obliviousness

**Symptom**: Same setup taken in regime that doesn't support it. Trend Pullback during Stage 3-4 transition. Pre-earnings momentum when composite signal is +5.

**Mechanism**: The technical pattern looks similar regardless of regime. Without explicit regime check, the trader sees only the local geometry.

**Remedy**:
- Composite signal score is layer 1 of the hierarchy — check before any setup-specific analysis
- Each archetype has explicit composite signal threshold (Trend Pullback ≥ +30; Pre-earnings ≥ +20; etc.)
- If composite is below threshold, do not run the rest of the analysis — the answer is no trade

### Failure mode 8 — Indicator stacking (multicollinearity)

**Symptom**: "Five indicators confirm this trade!" — but the five indicators all measure the same thing.

**Mechanism**: RSI(2) + IBS + %B + Williams %R + Stochastic are all measuring "how stretched is price relative to recent range." Their confluence is mathematically guaranteed when the underlying is stretched.

**Remedy**:
- One indicator per pedagogical function (Section 10B)
- If you can't articulate what feature of the data each indicator uniquely measures, drop the duplicates
- Genuine confluence is across different functions (momentum + trend + volatility + volume), not across reparameterizations

### Failure mode 9 — Event/setup horizon mismatch

**Symptom**: Buying 7 DTE options for a 14-day swing thesis. Buying 90 DTE LEAPS for a 3-day pivot trade.

**Mechanism**: Option expiration didn't match thesis horizon. Either expires before thesis develops, or carries unnecessary cost for a fast resolution.

**Remedy**:
- The DTE matching principle (Section 10K)
- Option expiration ≥ thesis horizon + 2-3 trading days buffer

### Failure mode 10 — Trading without a written setup card

**Symptom**: "I see a setup forming." Trade taken without explicit reference to the setup definition.

**Mechanism**: Without external reference, the criteria you're matching against are the criteria you can remember — which become the criteria that conveniently match the current chart.

**Remedy**:
- Setup cards (Section 12E) must be physically referenced before every trade
- Written confirmation: "Conditions A, B, C, D met — entering at $X with stop at $Y, time stop at day Z"
- The act of writing slows the decision by 20-30 seconds — exactly long enough to catch impulse trades

### The meta-failure: assuming discipline will appear in stress

The deepest failure mode is implicit: **assuming that you'll behave more carefully in stress than in calm.** Most retail traders believe this about themselves. The data systematically refutes it.

Discipline only exists when it's binding under stress. It's only binding when it was written down in calm. The setup cards, kill rules, time stops, and pre-committed exits exist as **external constraints on your behavior** — not as suggestions for your behavior.

The professional bias: design the framework so that, even under maximum behavioral stress, the framework defaults you toward the right action. This is what discipline is. It's not strength of will; it's structural design.

> *Most swing-trade failures come not from misreading the setup but from failing to honor the framework's exits, sizing, and skip rules. The setups themselves are the easy part. The discipline to apply them is the entire game.*
