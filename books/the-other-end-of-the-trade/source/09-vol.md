# Section 9 · Vol & Practice
*VIX, 0DTE, and reading the tape.*

This is the chapter where theory meets practice. We've built the mathematical and empirical framework; now we apply it. 9A connects everything in Sections 6-8 to the VIX index — how it's constructed, why it's structurally inverse to SPX, and how vanna feedback drives the violence of VIX spikes. 9B addresses the modern 0DTE phenomenon, with the latest 2024-2025 academic findings showing that 0DTE has, on net, dampened SPX volatility. 9C closes with seven practical heuristics for reading the tape through a dealer-mechanics lens, formalized into a regime classifier.

---

## 9A · VIX: the same mechanism, viewed from above

The VIX is widely called the "fear gauge." That label is qualitatively useful but mathematically imprecise. **The VIX is the model-free 30-day implied volatility of the S&P 500, expressed in annualized percentage points.** The construction starts from a model-free expression for the implied *variance* of the 30-day SPX log-return distribution (a weighted strip of OTM option prices), then takes the square root and scales by 100. So when you see "VIX = 18," that means the model-free 30-day implied annualized vol of SPX is 18% — not 18 units of variance.

This distinction matters because variance and vol move on different scales: a doubling of implied vol (18 → 36) quadruples implied variance (324 → 1,296). The published VIX number is the *vol* scale, which is the one a trader's intuition for "how much can the index move" lives on.

### The construction formula

```
σ²_30d = (2/T) × Σ_i [ΔK_i / K_i²] × e^(rT) × Q(K_i)  − (1/T) × (F/K_0 − 1)²

VIX = 100 × √(σ²_30d)
```

The first line computes the annualized 30-day implied variance from the OTM option strip (where T is the 30-day fraction of a year, K_i is each strike, ΔK_i is the strike spacing, Q(K_i) is the mid quote of the OTM option at K_i, F is the SPX forward, K_0 is the strike immediately below F, and r is the risk-free rate). The second line is the published VIX: take the square root to get vol on the σ scale, then multiply by 100 to express as percentage points.

Every term has a meaning that connects back to dealer hedging through the gamma-theta decomposition of Section 7A.

**The 1/K² weighting is not arbitrary.** It is the coefficient that makes a portfolio of options replicate a variance swap. Demeterfi, Derman, Kamal, and Zou (Goldman Sachs Quantitative Strategies Research Notes, 1999) showed that holding ΔK/K² of each strike across all OTM strikes gives you a position whose P&L is, exactly, total realized variance minus a fixed strike — a variance swap. **VIX is the discrete version of the fair strike of that swap**, scaled and annualized.

The connection to gamma is direct. A delta-hedged option earns ½·Γ·S²·[(ΔS/S)² − σ²·Δt] per interval (Section 7A). Weight this by 1/K² and sum over strikes, and the gammas across strikes combine to give a roughly constant "gamma" exposure per percent move regardless of where spot is — which is the property required for a variance swap. The mathematics is tight: **VIX is, fundamentally, the cost of replicating variance through delta-hedged options.**

### A toy worked example

The formula above is opaque until you compute one. Walk through a stylized six-strike strip end-to-end and you have the chain in hand. The arithmetic is grade-school; the pedagogical value is in seeing every term land somewhere.

**Setup.** SPX = 4,500. 30-day forward F = 4,503. T = 30 / 365 ≈ 0.0822. r = 0.05. K_0 (the strike immediately below F) = 4,500. Six OTM contributions:

| Strike | Type | Mid quote Q(K) | ΔK | (ΔK / K²) × Q |
|---:|:---|---:|---:|---:|
| 4,400 | put | $18 | 50 | 4.65 × 10⁻⁵ |
| 4,450 | put | $32 | 50 | 8.08 × 10⁻⁵ |
| 4,500 | K_0 | $52 | 50 | 1.28 × 10⁻⁴ |
| 4,550 | call | $48 | 50 | 1.16 × 10⁻⁴ |
| 4,600 | call | $30 | 75 | 1.06 × 10⁻⁴ |
| 4,700 | call | $14 | 100 | 6.34 × 10⁻⁵ |

ΔK at internal strikes is half the distance between neighbors; at the boundary strikes (4,400 and 4,700) it's the one-sided distance.

**Step 1 — sum the strike contributions.** Σ (ΔK_i / K_i²) × Q(K_i) ≈ 5.41 × 10⁻⁴.

**Step 2 — scale by 2/T and e^(rT).** 2/T = 24.33. e^(rT) = e^(0.05 × 0.0822) ≈ 1.0041. Product: 24.33 × 1.0041 × 5.41 × 10⁻⁴ ≈ 0.01322.

**Step 3 — subtract the forward correction.** (1/T) × (F/K_0 − 1)² = 12.17 × (4,503/4,500 − 1)² = 12.17 × (6.67 × 10⁻⁴)² ≈ 5.4 × 10⁻⁶. Effectively negligible at this strike spacing, which is why F sitting on top of K_0 is the desirable methodology choice in CBOE's specification.

**Step 4 — combine.** σ²_30d ≈ 0.01322 − 5.4 × 10⁻⁶ ≈ 0.01321.

**Step 5 — square root and rescale.** VIX = 100 × √0.01321 ≈ **11.5**.

The toy strip lands at VIX ≈ 11.5 because the mid-quotes above correspond to an implied vol around 12% — a calm-regime strip. The exact same chain at higher-vol mids (every Q roughly doubled) produces a VIX near 16-17; at typical post-2020 mids (every Q roughly tripled) it lands in the low 20s. **The strip's premium level scales VIX roughly linearly; the geometry of the formula is invariant.** That's the pedagogical payoff of doing this by hand once.

Two caveats. First, real VIX is computed from ~150 strikes weighted continuously per the CBOE methodology, not 6 strikes — what changes is precision, not the qualitative chain. Second, the published VIX uses a near-and-next interpolation across two expirations (this toy uses one). The [INTERACTIVE: vix-strip-builder] widget below lets you vary the strip parameters and watch the index respond.

[INTERACTIVE: vix-strip-builder]

### Why VIX rises asymmetrically when SPX falls

The 1/K² weighting puts disproportionate weight on low-strike options. Combined with the equity skew — OTM puts trade at higher implied vol than OTM calls — a 1% downside move in SPX re-prices the put wing far more than a 1% upside move re-prices the call wing.

**This is why VIX is structurally inverse to SPX**: it isn't "fear" per se, it's the mechanical asymmetry of how variance replication weights the strikes the market is hedged in. The correlation between daily SPX returns and daily VIX changes is approximately −0.80 across decades of data; this is not because fear and stock prices are correlated, but because the math of variance replication requires put-side reweighting that responds asymmetrically to direction.

### VIX futures and the roll

VIX is computed from a strip of SPX options — it is NOT directly tradable. What *is* tradable:

**1. VIX futures**: monthly contracts expiring Wednesday 30 days before SPX OPEX. Settle at the SOQ of VIX computed Friday morning.

**2. VIX ETPs**:
- **VXX** (Barclays): long position in 1st and 2nd VIX futures
- **UVXY** (ProShares): 2× leveraged long VIX futures
- **SVXY** (ProShares): -0.5× inverse VIX futures
- **VIXY** (ProShares): unleveraged long VIX futures

**3. VIX options**: cash-settled options on the VIX index level, with notional based on the index level.

#### Contango and the roll cost

Under normal conditions, the VIX futures curve is in **contango**. Front-month sits below spot VIX; second-month sits above front. The economic reason is the variance risk premium — buyers pay extra for protection over each forward window.

For long-vol ETPs, contango is a **cost**: every month they sell the front (lower price) and buy the second (higher price), locking in a loss. Accumulated drag is approximately **−10% annualized** for VXX. UVXY suffers roughly 2× this drag.

For inverse-vol ETPs, contango is a **benefit**: SVXY profits from the roll. This was the dominant return source for XIV/SVXY pre-2018 — until the eight-month low-vol regime made positioning catastrophically large, triggering Volmageddon.

#### Backwardation

In stress, the curve inverts: front-month trades above second-month. This reverses the roll dynamics:
- Long-vol ETPs profit
- Inverse-vol ETPs lose

Backwardation is a reliable stress indicator. VIX/VIX3M ratio crossing 1.0 preceded major SPX drawdowns in nearly every multi-year cycle.

#### Connection to dealer hedging

VIX ETP issuers (Barclays VXX, ProShares UVXY/SVXY) are themselves significant participants in VIX futures. Their daily rebalancing is mechanical and well-understood — the 16:08 EST volume spike on Feb 5, 2018, was the cumulative effect of XIV's forced rebalancing in the closing auction interacting with dealer vol-of-vol hedging.

**Operational implication**: VIX futures and VIX ETPs are NOT the same instrument as the VIX index. The roll structure introduces a multi-percent annualized drag (contango) or boost (backwardation), and futures basis can diverge from spot VIX in stress. Use VIX as a regime indicator; trade VIX futures and options as separate instruments with their own dynamics.

### The vanna feedback during VIX spikes

Recall vanna from Section 5D and 7B: ∂Δ/∂σ. When VIX rises, OTM put deltas become more negative in magnitude. A dealer who is short OTM puts — the dealer of record for most institutional hedging demand — sees their effective long exposure increase. To stay delta-neutral they must sell stock.

Selling stock pushes SPX further down. Further SPX down increases VIX. Further VIX increase deepens put deltas. And around the loop we go. **Vanna is the technical name for the variable that makes VIX-driven sell-offs so violent.**

[INTERACTIVE: vanna-feedback-loop]

The animator demonstrates: at step 0 the dealer is short 1,000 SPX OTM puts (K=4400) against an institutional hedger. Initial delta-hedge: long approximately 410 shares. Spot 4500, VIX 20, IV at this strike 23%. Then spot ticks down 1%; VIX bids up 8%; put delta becomes more negative; dealer must sell more shares; SPX ticks down further; VIX bids up further; loop continues.

> *"Transaction data show a spike in trading volume to 115,862 VIX futures contracts, or roughly one quarter of the entire market, and at highly inflated prices, within one minute at 16:08 [on February 5, 2018]."*
> — BIS Quarterly Review, March 2018

That moment — 16:08 EST on Volmageddon — is the cleanest empirical example of the feedback the animator walks through.

### VIX is one tool in a family

Cboe launched **VIX1D** in April 2023 to measure one-day expected volatility, explicitly because the 30-day VIX no longer captures the short-horizon vol regime driven by 0DTE. VIX1D uses the same model-free variance replication formula but applied to the very-near-dated SPX option strip.

The Cboe VIX family now includes:
- **VIX1D** — 1-day implied volatility (launched April 2023)
- **VIX9D** — 9-day implied volatility
- **VIX** — 30-day (the original, launched 1993; reformulated 2003)
- **VIX3M** — 3-month implied volatility
- **VIX6M** — 6-month implied volatility
- **VIX1Y** — 1-year implied volatility

The relationships between these form the **VIX term structure**. In normal markets, the term structure is in **contango** (short < long), reflecting the variance risk premium — implied vol is bid up further out because more can happen over longer horizons. In stress, it inverts (**backwardation** — short > long): panic concentrates demand into near-dated puts.

The combination of GEX sign and VIX term structure shape is the most common composite signal serious traders use to characterize regime. The standard combinations:

| Net dealer GEX | VIX term structure | Regime |
|---|---|---|
| Strongly positive | Steep contango | **Stable** — premium selling favored |
| Mildly positive | Mild contango | **Normal** — neutral character |
| Near zero | Flat or barely inverted | **Transition** — reduce size |
| Negative | Backwardation | **Stress** — long vol favored, mean-reversion dangerous |
| Deeply negative | Deep backwardation | **Crisis** — defensive only, mechanical strategies suspended |

This 5×regime classification underlies the composite scorecard in Section 10F and the conviction-scoring framework in Section 12B.

---

## 9B · 0DTE: the singularity at the strike

The most consequential shift in modern equity microstructure is the rise of **zero-days-to-expiration options**. From under 5% of SPX volume in 2016, 0DTE reached **62.4% of all SPX volume in August 2025** and **60% in September 2025**, with monthly averages between 56% and 62% across all of 2025. Average daily 0DTE volume hit **2.4 million contracts in August 2025**; total SPX options volume hit a record **4.26 million contracts/day in September 2025**.

Industry-wide, 0DTE was approximately 24% of all US listed options volume by late 2024 and is on track to grow further. This is the largest single shift in options market structure since the SPX weeklies launch in 2005.

The mechanical reason 0DTE matters is what we covered in Section 6E: **Γ ∝ 1/√T**. As T shrinks toward zero, at-the-money gamma diverges. Computing T in years for consistency:

| DTE | T (years) | √T | Γ ratio vs 30-DTE |
|---|---|---|---|
| 30 days | 0.0822 | 0.2867 | 1.0× (baseline) |
| 7 days | 0.0192 | 0.1385 | 2.07× |
| 1 day | 0.00274 | 0.0524 | 5.47× |
| 4 hours | 4.57e-4 | 0.0214 | **13.4×** |
| 30 min | 5.71e-5 | 0.00756 | **37.9×** |
| 5 min | 9.51e-6 | 0.00308 | **93.0×** |

These ratios apply to ATM gamma. For OTM strikes the divergence is faster — gamma compresses into ATM as T shrinks; OTM gamma collapses.

This concentration produces the strange 0DTE consequence: when the dealer is short a slightly-OTM 0DTE call and spot ticks above strike, delta jumps from near zero to near one almost discontinuously. **The dealer must buy a large block of stock at that strike.** When many dealers face this near the same level, you get the "magnet" — price snapping to a strike where hedging flow concentrates.

[INTERACTIVE: gamma-profile-dte]

### The "did 0DTE break the market?" debate

A reasonable concern, given the gamma math above: has 0DTE destabilized markets? The empirical answer — repeatedly confirmed by Cboe's own data, by Dim, Eraker, and Vilkov (2024), and by the Adams et al. (2025) successor paper — is **no, on average it has reduced realized volatility**.

The reasoning is subtle and worth unpacking.

**Cboe's analysis** ("Much Ado About 0DTEs," Mandy Xu, September 2023) found that **net market maker gamma in 0DTE positions has a median value of about +$173 million per percentage point**, with the 25th–75th percentile range from −$1.1 billion to +$2.4 billion. For context, S&P futures trade about $400 billion in daily liquidity. The 0DTE hedging flow is therefore about 0.04% to 0.17% of futures liquidity at the median — **meaningful but not market-moving on a typical day**.

**Dim, Eraker, and Vilkov (2024)** — the academic gold standard on this topic — found:

> *"We find that Market Makers' inventory, as measured by the net gamma of their positions, is on average positive and negatively related to future intraday volatility. Our empirical evidence is consistent with delta-hedging but inconsistent with information-based trading."*

Translation: most 0DTE flow is retail and small institutions *selling* premium (credit spreads, iron condors, cash-secured puts). Dealers *buy* it. The dealers are therefore **long gamma in aggregate in 0DTE**, and their hedging — sell rallies, buy dips — is *stabilizing*. This is the opposite sign from the original SqueezeMetrics convention, and it explains why intraday volatility has compressed even as headline option volume has exploded.

**Adams, Dim, Eraker, Fontaine, Ornthanalai, and Vilkov (2025)** — posted December 3, 2025 — extends this finding causally and identifies the mechanism more precisely. They exploit a natural experiment: Tuesday and Thursday SPXW expirations were not available for trading until April 26 and May 19, 2022 respectively. Using this discontinuity, they show:

> *"The presence of 0DTEs dampens market volatility through a shift in market makers' hedging needs. Importantly, this shift occurs not due to trading 0DTEs on their expiration day but due to positions in longer-dated options accumulated earlier and becoming 0DTEs."*

This is critical: the volatility attenuation effect operates through *longer-dated positions becoming 0DTEs* as time passes, not through 0DTE expiration-day trading. The structural existence of more 0DTE expirations (Mon/Tue/Wed/Thu/Fri now all available) changes the dynamics of dealer hedging across the entire options-life cycle, not just on the day of expiration.

**Brogaard, Han, and Won (2024)** — University of Utah working paper — independently confirmed that 0DTE introduction did not increase market volatility, using event-study methodology around the staggered introduction of Tuesday/Thursday SPXW expirations.

The current academic consensus, as of late 2025/early 2026, is that **0DTE has stabilized rather than destabilized SPX intraday markets on average**, while still allowing episodic destabilization when dealer positioning flips negative.

### The same data show 0DTE can be episodically destabilizing

The right tail is real. When net dealer 0DTE gamma flips short on event days (FOMC, CPI, NFP), the small notional combines with the enormous per-contract gamma to generate concentrated flow that can amplify intraday moves. The character of the modern market is therefore "**quiet most days, sharp on event days**" — punctuated equilibria driven by which side of gamma dealers sit on at the moment.

The April 2025 "Liberation Day" tariff-related sell-off and the October 10, 2025 follow-through (which set the single-day options volume record of 110 million contracts) both showed this dynamic. On those days, dealer gamma in 0DTE was likely net short (because retail was buying directional protection rather than selling premium), and the hedging flow amplified the directional move.

### The intraday charm clock

Charm scales with 1/T, and for 0DTE that scaling factor accumulates aggressively through the day. A 0DTE option's delta decays smoothly through the morning, then accelerates dramatically after lunch. By 3:30 PM ET, charm has typically delivered most of its mechanical flow.

This is one reason the **last 30 minutes** of the day — already concentrated for end-of-day rebalancing per Baltussen et al. (2021) — has become even more mechanical in the 0DTE era. The combination of (a) charm-driven dealer rebalancing in 0DTE, (b) end-of-day delta rebalancing of longer-dated dealer positions, and (c) closing-auction mechanical flow from passive funds, all concentrate into the same 30-minute window.

For retail traders, the implication: **the last 30 minutes are not a normal trading window**. Strategies that work in the middle of the day may not work in the close. Strategies that explicitly target the close (MOC orders into rebalancing flow) work differently than strategies that try to fade the close (mean reversion against mechanical flow).

### Cboe's own data on 0DTE composition

Cboe's late 2025 disclosures, via Mandy Xu's monthly volatility digest, show that **retail trading makes up roughly 50-54% of total SPX 0DTE volume** as of mid-2025. The retail share has grown structurally as Robinhood (January 2025) and other retail brokers expanded index options access.

Importantly, retail 0DTE flow is mostly *premium selling* — credit spreads and iron condors — not directional purchases. This is what keeps dealers net long gamma in 0DTE on most days. If retail flow flipped to net premium buying (e.g., during a sustained bull market with retail aggressive call buying), the regime would flip and dealers would become net short gamma in 0DTE — at which point the same product that has been stabilizing markets could become destabilizing.

The character of 0DTE markets, in other words, depends critically on the *direction* of retail demand. The Cboe data show this direction is currently selling premium, which is stabilizing. There is no guarantee it will remain so.

---

## 9C · Reading the tape: practical synthesis

Eleven chapters of theory only matter if they change what you see on a chart. Here is the practical synthesis — the heuristics that follow from everything in Sections 1-8, in declining order of importance — followed by an interactive classifier that turns the heuristics into an explicit decision.

### Seven heuristics, ordered by impact

**1. Check the sign of GEX before strategy selection.** Positive GEX days favor premium selling, mean reversion, and tight stops. Negative GEX days favor directional trades, longer holds, and wider stops. **Strategy selection is the single biggest leverage point** — using mean-reversion in a negative GEX regime is how accounts get blown up. Note that "GEX" from public vendors depends on a sign convention that may not match your product's flow regime; verify before trusting.

**2. Identify the gamma flip level.** The price at which net dealer gamma crosses zero is a regime boundary. Slow approaches to the flip rarely matter. Approaches under stress — VIX rising, breadth deteriorating, news pending — frequently mark the moment when feedback flips sign. SpotGamma's "Volatility Trigger" is their proprietary version of this level; the concept is the important part.

**3. Combine GEX with VIX term structure.** Positive GEX + VIX in contango = stable regime (mean-reversion dominates). Negative GEX + VIX in backwardation = stress regime (momentum dominates). These two signals together capture both the positioning *and* the pricing of risk; either alone is incomplete.

**4. Be aware of charm time-of-day effects.** Charm flows accumulate through the day and compress into the last 30 minutes. Trends into 3:30-4:00 PM ET frequently extend on mechanical rebalancing, especially on OPEX Fridays. The first hour after the open is often noise as overnight charm and vanna unwinds clear.

**5. Anticipate pre-event vs post-event vanna dynamics.** Vanna sets up before FOMC, CPI, NFP. Implied vol is bid into the event; dealer-short-puts have larger short-stock hedges than they would in calm. **After the event, regardless of direction, IV collapses (vol crush). Short-puts' deltas decay toward zero. Dealers buy back hedge stock.** This is the post-event ramp that happens regardless of outcome. Long-vol going in, short-vol coming out — but only if you can size and time it correctly.

**6. Account for pinning at high-OI strikes near OPEX.** Ni, Pearson, and Poteshman document 16.5 bps return alteration on equity expiration days, with effects concentrated near high-OI strikes. Pinning is real but small — useful as a tiebreaker between alternative outcomes, not as a standalone trade thesis. Pinning is stronger in single stocks than in index, and stronger in lower-liquidity names.

**7. Calibrate your skepticism of GEX commentary.** The empirical effect sizes are tens of basis points per standard deviation, not full percentage points. When commentators describe "massive gamma squeezes" driving 2% moves, they are usually wrong — the move came from news or from another mechanism, with gamma contributing on top. **Hold this prior strongly.**

### The regime classifier

[INTERACTIVE: regime-classifier]

The classifier surfaces a single question — "is today's regime what I'm trading for?" — and gives a structured way to override your defaults when it isn't. The scoring is heuristic, not a backtest. Use it to surface the question, not as a signal in itself. Override freely when context dictates.

### A unified mental model

The S&P 500 on a typical day is the sum of three forces, in roughly decreasing order of magnitude:

**1. Fundamental news and information.** Small in number per day but large in magnitude when they hit. An FOMC decision, a CPI print, a major earnings release, a geopolitical event — these are the things that drive markets in the strict sense.

**2. Mechanical positioning.** Dealer hedging, vol targeting, risk parity rebalancing, options-related flows — large in continuous magnitude but mostly self-cancelling across participants. Most days, force two dominates by volume; force one dominates by directional impact.

**3. Microstructure noise.** Bid-ask bounces, auction imbalances, opportunistic liquidity-seeking. Always present, never the primary mover, but the basis on which higher-frequency strategies operate.

**Most days, force two dominates by volume.** The dealer-hedging story we've built across these eleven chapters is the single largest component of force two. The market is, on most days, a delta-hedging machine reacting to the existing options inventory. Price doesn't move because "buyers stepped up" in some abstract sense — it moves because somebody is mechanically required to transact a specific size at a specific price to remain neutral.

**Understanding who that somebody is and what they're forced to do is the entire game.**

### Where to go next

Three directions of deeper study, in order of practical leverage:

**1. Track your own intraday GEX** (Cboe data, SpotGamma, Tier1Alpha, or your preferred vendor) and overlay it on your SPX or SPY chart for two weeks **before trading on it**. You will see when it works and when it doesn't. The forward-walk is the only way to develop intuition for the framework's effect sizes in your specific timeframe and instrument set.

**2. Read the academic sources directly** — Ni-Pearson-Poteshman (2005), Barbon-Buraschi (2021), Garleanu-Pedersen-Poteshman (2009), Dim-Eraker-Vilkov (2024), Adams et al. (2025), Baltussen-Da-Lammers-Martens (2021), Demeterfi-Derman-Kamal-Zou (1999). The vendor commentary will then read very differently. Vendor frameworks are necessarily simplified for marketing; the academic papers expose the assumptions and limitations.

**3. Backtest the regime-aware version of any of your existing setups.** Conditional on positive vs negative GEX, what's your win rate? The asymmetry is usually larger than you expect, and it persists out-of-sample more reliably than most other technical signals.

### Final thought

> *Every option ever traded created an obligation for someone to transact in the underlying. The market is, in part, the integral of those obligations.*

This is the unified statement of the dealer-mechanics framework. Sections 1-5 built the prerequisites. Sections 6-8 derived and aggregated the mechanism. Section 9 applied it to the current market regime. Sections 10-12 will translate the framework into operational discipline — strategy selection, position sizing, and the rules that keep the framework from being destroyed by behavior.
