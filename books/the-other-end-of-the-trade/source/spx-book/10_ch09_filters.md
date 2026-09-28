# Chapter 9 — Regime filters
## VIX term structure, dealer gamma, liquidity, breadth

> **Core intuition.** Filters are *not trades*. They're variables that size other strategies up or down. The "edge" they provide is in the form of avoided losses on existing positions, not direct returns. The classic retail error is treating a filter as a strategy — buying VXX because VIX is in contango, or shorting SPX because dealer gamma is negative. Filters modulate; they don't generate.

---

## 9.1 What filters are

### Definition
A regime filter is a measurable market variable that:
1. Has predictive content about near-term return distribution (mean, vol, skew)
2. Doesn't itself constitute a tradable edge after costs
3. Modulates the sizing of *other* strategies

### Why this distinction matters

Consider VIX term structure. VIX/VIX3M ratio is informative — when it's >1.05, near-term realized vol is meaningfully higher than longer-dated, indicating stress. But:
- *Trading* VIX directly via VXX has lost 99.84% from roll decay since 2009 inception
- *Trading* VIX-targeted strategies (long-vol funds) costs 5-15% annual decay
- *Using* VIX as a filter to halt put-write entries costs nothing and prevents real losses

**Same information, different operational use, very different P&L.**

### The general rule
If you can name a measurement (term structure, gamma, breadth, credit spread) and want to "trade" it, the answer is almost always: don't trade it, use it as a sizing input on something else.

---

## 9.2 VIX term structure

### Core intuition
VIX measures 30-day implied vol on SPX. VIX3M measures 90-day. Their ratio captures the curve. In normal regimes, longer-dated vol is higher (contango, ratio < 1) reflecting demand for longer-dated hedges. In stress, near-term vol spikes and the curve inverts (backwardation, ratio > 1) reflecting acute risk aversion.

### Toy example
- Calm regime: VIX = 14, VIX3M = 17, ratio = 0.82. Contango. Term structure is "normal."
- Stress regime: VIX = 32, VIX3M = 26, ratio = 1.23. Backwardation. Acute risk pricing.

When backwardation develops, near-term vol is elevated *more* than far-term, indicating concentrated short-term concern. Historically, this regime is associated with:
- Sharp short-term moves (both directions)
- Wider option spreads
- Higher correlation across assets
- Increased margin expansion under PM

### Formal object
$$\text{Filter}_t = \frac{\text{VIX}_t}{\text{VIX3M}_t}$$

A common rule:
- Ratio < 1.00 → normal regime
- Ratio 1.00-1.05 → elevated, transitional
- Ratio > 1.05 sustained → stress regime

### Evidence
- Whaley (2009) on VIX as fear gauge — established the contango/backwardation framework
- ProShares "Term Structure" research notes — backtests of using term structure as a filter on equity exposure
- Bloomberg/CBOE practitioner literature — widespread but not academically formalized

### Why it works
The information value comes from the demand-driven nature of VIX prices. When near-term hedging demand spikes (institutional accounts buying short-dated puts), the curve inverts. This demand spike is itself information about institutional risk perception.

### Operational rule (the canonical filter)

**Phased response to backwardation:**

| Trigger | Action |
|---|---|
| VIX/VIX3M > 1.00 for 3 closes | Halt new short-vol entries |
| VIX/VIX3M > 1.05 for 3 closes | Halt all put sales; reduce existing premium-selling sleeve sizing 50% |
| VIX/VIX3M > 1.15 for 3 closes | Close non-essential short-vol; preserve only deep-OTM tails for assignment risk |
| VIX/VIX3M < 1.00 for 5 closes after stress | Begin phased re-entry: 25% of target, then 50%, then 100% over 3 weeks |

Avoid binary on/off triggers — they create whipsaw. Phase changes over multiple days.

### Failure mode
- Sometimes backwardation is brief (single-day liquidity event) and reverses without action being needed
- Other times it persists longer than expected (2008, March 2020 sustained for weeks)
- The rule produces real opportunity cost during false-positive stress signals

### What to do, NOT to do

**Do:**
- Use as a filter to halt new short-vol entries
- Use as a sizing modulator for existing positions
- Use for phased re-entry after stress

**Don't:**
- Buy VXX or VIX futures directly (roll decay, basis effects)
- Treat backwardation as a directional signal on SPX (it correlates with stress, but the post-stress direction is unpredictable)
- Use a single threshold — phase the response

### Misconception box
> **Misconception:** "VIX in backwardation means stocks will fall."
>
> **Correction:** Backwardation indicates *elevated near-term vol*, not directional negative. Many backwardation episodes resolve via mean-reversion *up* (sharp rallies as fear subsides). The signal is about magnitude, not direction. Use it to size, not to direction-bet.

### Self-check
1. Define VIX/VIX3M ratio. What does each level imply?
2. State the phased response rule.
3. Why is buying VXX a bad implementation of this filter?

---

## 9.3 Realized vs implied volatility

### Core intuition
Selling implied vol assumes *future realized vol will be lower*. If realized vol is currently 30% and implied is 22%, selling premium is structurally negative-EV until realized normalizes back below implied.

### Toy example
21-day realized vol on SPX = 32%. VIX (implied) = 22%. Selling puts collects 22% vol of premium but the underlying is moving at 32% vol. The position is structurally underpriced relative to actual movement. This is the "negative VRP" regime.

### Formal object
$$\text{VRP}_t = \text{IV}_t - \text{RV}_{t-21,t}$$

Negative VRP signals an unfavorable regime for premium selling.

### Operational rule
- 21-day realized > implied (negative VRP) → halt new short-vol entries
- 21-day realized > implied + 5 vol points → close existing short-vol if position size requires it
- 21-day realized normalizes to < implied → permit re-entry over 5 sessions

### Failure mode
- Realized can stay elevated for weeks (March 2020 stayed >40% for 6+ weeks)
- Mean reversion timing is unpredictable
- Some "negative VRP" episodes resolve via implied jumping (your puts get worse) rather than realized falling

### Decision rule
Combine with VIX term structure as a layered filter. Both contango AND realized < implied = green light for premium selling. Either condition violated = pause.

---

## 9.4 Liquidity regime

### Core intuition
Funding stress propagates non-linearly. When TED spread (3-month LIBOR - 3-month T-bill, now SOFR-T-bill) widens, banks become reluctant to lend, leveraged players reduce positions, and risk assets sell off in correlated fashion. The MOVE index measures bond market vol; spikes indicate fixed-income stress that often precedes equity stress.

### Toy example
- TED spread normal: 20-30 bps. Banks lend to each other freely.
- TED spread elevated: 100 bps. Funding strain visible, leveraged funds reducing.
- TED spread crisis: 250-400 bps (2008, March 2020). Acute funding stress; everything correlates.

### Formal object
$$\text{Liquidity Filter}_t = \mathbb{1}\{\text{TED} > \tau_1 \text{ OR } \text{MOVE} > \tau_2 \text{ OR } \text{HY OAS} > \tau_3\}$$

Composite indicator: any one of three liquidity stress measures triggers the filter.

### Thresholds (rough)
- TED > 200 bps
- MOVE > 150
- High Yield OAS > 600 bps

These aren't fixed; recalibrate based on rolling history.

### Operational rule
Liquidity stress → reduce all leveraged and short-vol exposure 50%; reduce equity beta 25%; halt new tactical positions until normalization.

### Why this matters specifically for premium-selling
In liquidity events, all premium-selling sleeves correlate to ~1.0 (Chapter 14). The diversification you thought you had between PCS, CC, 0DTE, and condors evaporates because they're all just short-vol with different wrappers. Liquidity filters are the strongest defense against this.

### Failure mode
Liquidity indicators can be late (the equity damage is often done before the credit/funding markets reflect it). Use as a layered filter, not as the only filter.

---

## 9.5 Dealer gamma sign (low confidence)

### Core intuition
Dealers who've sold options must hedge to remain delta-neutral. When they're net long gamma, hedging is *stabilizing* (they sell into rallies, buy into dips). When they're net short gamma, hedging is *destabilizing* (they buy into rallies, sell into dips, amplifying moves).

### Toy example
If dealers net long $10B of gamma, a 1% SPX rally requires them to sell 10B × delta_change. This selling damps the rally — implied volatility falls, range trades develop.

If dealers net short $10B of gamma, the same 1% rally requires them to buy. Buying amplifies the move — implied volatility rises, trends extend.

### Formal object
$$\text{GEX} = \sum_i \Gamma_i \cdot \text{OI}_i \cdot \text{Multiplier}_i \cdot \text{Direction}_i$$

The "Direction" term is the assumption-dependent part — who's long vs short which strikes. Public GEX models (SqueezeMetrics, SpotGamma) make assumptions that may be unreliable.

### Evidence
- Garleanu-Pedersen-Poteshman (2009, *RFS*) "Demand-Based Option Pricing" — established the theoretical link between dealer positioning and option prices
- Practitioner narrative around 2017-2022 around dealer hedging effects
- **Cboe 2025 study** estimates 0DTE market-maker gamma hedging is approximately **0.2% of SPX daily liquidity** — much smaller than retail GEX narratives suggest

### Why this is downgraded from "edge" to "low-confidence filter"

Three reasons:
1. **Public GEX models are model-dependent.** Different vendors give different numbers because they make different assumptions about who's long/short which strikes
2. **Post-2022 0DTE explosion** changed the structure. Pre-2022 GEX models assumed monthly/weekly options were dominant; that's no longer true
3. **Cboe 2025 finding** that 0DTE MM hedging is ~0.2% of liquidity directly contradicts the narrative that dealer flows are dominant intraday

### Operational rule
- Use directional sign (positive vs negative GEX) as a low-confidence regime context only
- Negative GEX environment → expect higher realized vol, wider intraday ranges; consider reducing put-write sizing modestly
- Positive GEX environment → expect compressed realized vol, more pinning; OK to size put-write normally
- **Do not trade specific levels** ("call wall," "put wall")
- **Do not size based on GEX magnitude** (the magnitude is too model-dependent)

### Decision rule (today)
GEX is a soft input only. If it disagrees with VIX term structure or realized vol filters, ignore it. If it agrees, slight additional confidence. Worth 10-15% of one filter's weight, not its own filter.

### Misconception box
> **Misconception:** "I can sell at the call wall and buy at the put wall."
>
> **Correction:** Specific level rules are not retail edges. Levels shift intraday as positioning changes. The Cboe 2025 finding (0DTE MM hedging ~0.2% of liquidity) directly undermines the magnitude of these effects. Use GEX directional sign as low-confidence context, not as level-trading rules.

### Self-check
1. State the difference between long-gamma and short-gamma dealer positioning.
2. Why is GEX a low-confidence filter?
3. What did Cboe 2025 find about 0DTE MM hedging?

---

## 9.6 Breadth and internals

### Core intuition
Index price can mask deterioration in market internals. When fewer and fewer stocks are participating in a rally, the rally is fragile. When breadth is improving even with index flat, regime is bullish.

### Toy example
SPX at all-time high, but only 30% of stocks above their 50-day MA. The "all-time high" is being driven by a few mega-caps. This is fragile — when the few stocks holding it up rotate, the index falls quickly.

Conversely, SPX flat for 3 months but 65% of stocks above 50-day MA. Beneath the surface, broad participation is improving. This is bullish even though the index doesn't show it yet.

### Formal object
- % stocks above 200-day MA
- % stocks above 50-day MA
- New highs - new lows
- Advance/decline line

### Operational rule
Breadth divergences are warning signs but not direct filters. Use as confirming/disconfirming context for other signals.

- New high in SPX with deteriorating breadth → reduce equity beta 10-15%
- Flat SPX with improving breadth → maintain or slightly increase equity beta

### Failure mode
Breadth can stay weak for months (mega-cap concentration era 2018-2024). The signal often runs ahead of price action by 6-12 months — early-acting on it costs opportunity.

---

## 9.7 Composite filter framework

### Stacking filters

The genuine value comes from stacking multiple filters. Each individual filter has noise; the intersection is where conviction is highest.

**Conditions for full short-vol exposure:**
- VIX/VIX3M < 1.00 ✓
- 21-day realized < implied ✓
- TED < 100 bps ✓
- MOVE < 100 ✓
- HY OAS < 500 bps ✓
- GEX positive (low confidence supplement) ✓

All green = full size. One yellow = reduce 25%. Two or more = reduce 50%+.

This kind of layered filtering is the operational discipline that converts individual filter signals (each with mediocre signal-to-noise) into a portfolio-level regime indicator with much higher confidence.

### What filters together do

**The cumulative impact of well-implemented filters is large.** The biggest single contribution to retail short-vol survival is *not entering* during high-stress regimes. A disciplined filter stack can prevent the GFC-style -33% PUT drawdown by halting new entries before the worst losses.

The cost is opportunity cost during false-positive stress periods — you don't capture some premium that you would have. Empirically this opportunity cost is much smaller than the avoided drawdown benefit.

---

## 9.8 What's NOT a filter

To clarify by negative space, these are NOT filters:

- **Specific GEX levels** ("call wall at 5500"): too model-dependent
- **Single oscillator readings** (RSI at 30): too noisy for sizing decisions
- **Headline news** (CPI print, geopolitical event): unpredictable and reactive
- **Options open interest concentration**: descriptive, not predictive
- **Sentiment indicators** (AAII, Fear & Greed): noisy, contrarian use only

Filters need:
1. Continuous measurement
2. Demonstrated regime predictive value
3. Non-narrative basis

If a "filter" relies on a story to justify use, it's probably not a filter.

---

## 9.9 Misconception box (chapter level)

> **Misconception:** "If a filter has predictive value, I should trade it directly."
>
> **Correction:** Predictive value about *vol* doesn't mean tradable directional edge. VIX has predictive value for stress, but trading VIX (via VXX, UVXY) costs 5-15%/year in roll decay. The information is real; the implementation kills you. Filters modulate other strategies; they're not strategies themselves.

---

## 9.10 Self-check (chapter)

1. State the canonical VIX term-structure filter rule with phased response.
2. Why is GEX downgraded from "edge" to "low-confidence filter"?
3. What three indicators define the liquidity filter?
4. Why does layering filters produce better signal than any single filter?
5. Apply the filter stack to a current market scenario. What sizing does it dictate?
6. Take a "filter" you've considered. Does it meet the three criteria for being an actual filter?

---

## Where this fits

Chapter 6 covered foundation premia. Chapter 7 covered factor tilts. Chapter 8 covered structural overlays. Chapter 9 covers regime filters. Chapter 10 (next) covers what's REJECTED — the strategies you should specifically not trade and why.

The negative space matters as much as the positive. Chapter 10 closes the taxonomy by completing the classification of rejected items.

[← Previous: Chapter 8 — Structural overlays](09_ch08_overlays.md) | [Next: Chapter 10 — Rejected →](11_ch10_rejected.md)
