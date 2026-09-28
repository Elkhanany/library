# Section 6 · Dealer Mechanics
*Who's on the other side and what they're forced to do.*

Every option you've ever traded had someone on the other side. Not a mysterious "the market" — a specific business, with specific obligations and specific behaviors. The mechanical decisions that business is forced to make, second by second, collectively constitute one of the largest non-fundamental forces acting on the S&P 500 on any given day with no news.

This section builds that picture from absolute zero. It assumes you know what an option is and what "buy low, sell high" means — Sections 1 through 5 provide that — and nothing more. By the end, you will understand, formally, why VIX rising forces SPX selling, why 0DTE has changed the intraday character of the market, what GEX actually measures, and where the conventional GEX framework breaks. Math appears when it earns its place, and every formula is followed by what it means in plain English.

The arc:

- **6A** — Preface and roadmap
- **6B** — The trade: who is actually on the other side of your option order
- **6C** — Greek inheritance: what exposures the dealer has just acquired
- **6D** — Delta hedging: how the dealer mechanically neutralizes the directional risk
- **6E** — The gamma engine: why the hedge doesn't stay neutralized, and why this drives the entire mechanism

Chapters 7-9 then derive the formal mathematics (7), aggregate the per-position dynamics across the market (8), and apply the framework to VIX, 0DTE, and reading the tape (9).

---

## 6A · What you'll learn and why

Much of what circulates on social media and retail trading platforms about "dealer flows" and "gamma squeezes" is qualitatively right but quantitatively overstated. The academic literature gives effect sizes in tens of basis points, not full percentage points. Where I cite numbers in this section and what follows, they come from peer-reviewed work or directly from Cboe's own data. Where industry sources disagree with academia, I flag it. The goal is calibration — knowing not just *that* dealer hedging matters but *how much* it matters and *when*.

A few epistemic notes that apply throughout:

> **Dealer hedging is a real and quantifiable force.** It moves markets in measurable, statistically significant ways. It is not magic.
>
> **The effect sizes are modest on typical days.** Most days, dealer hedging accounts for tens of basis points of intraday move at most. The dominant force is news and information flow.
>
> **The effect sizes can be large on stress days.** When the conditions described in Section 8C coexist — negative-gamma dealer positioning, mechanical rule-based hedging demand, degraded market depth — the linear framework can break and effects can be measured in full percentage points or more.
>
> **GEX is positioning, not outcome.** It tells you what dealers would do given a move; it does not tell you whether a move will happen. Don't conflate the two.

With those caveats in place, the chapters that follow are some of the most important framework material in this book.

---

## 6B · The trade: who is on the other side?

Begin with the simplest possible scene. You decide to buy one SPY call option, strike $600, expiring in 30 days. You click "buy" in your broker. A millisecond later, you own the contract. Somewhere, a market maker now has the opposite of what you have — they are short a call. Who are they, and why did they take the other side?

### The market maker is not betting against you

**This is the most important sentence in this entire section.** A market maker is not a speculator on the other side of your trade. They have no view on whether SPY will go up or down. Their entire business is to quote a bid (the price they'll buy at) and an offer (the price they'll sell at) simultaneously, and capture the spread between them.

The math is brutally simple. Suppose the call has a "fair value" of $5.00. The market maker quotes a bid of $4.95 and an offer of $5.05. You hit the offer at $5.05. The market maker simultaneously stands ready to buy the same contract back at $4.95 from someone else. If they round-trip the contract, they pocket $0.10. Times one hundred shares per contract, times a hundred contracts a second, times every option in every name — the franchise emerges from scale, not from being right about direction.

> *"By taking the market risk to trade in this fashion, market makers can earn a 'spread' between the bid and the ask. In today's highly competitive and efficient markets, the bid-ask spread is often much less than one percent of the price of a security."*
> — Citadel Securities

In US listed options, this business is dominated by a small number of firms. As discussed in Section 3B with current 2025-2026 data:

- **Citadel Securities** — approximately 35% of all US-listed retail equities and options volume
- **Susquehanna International Group (SIG)** — historically dominant in options market-making
- **Wolverine Trading** — institutional and options franchise
- **Virtu Financial** — second-largest retail wholesaler historically
- **Jane Street** — dominant ETF market-maker, $39.6 billion 2025 net trading revenue
- **Hudson River Trading** — ~20% of US cash equities (entered retail in 2022)
- **Optiver, IMC, DRW** — additional institutional liquidity providers

The Big Three options wholesalers (Citadel, SIG, Wolverine) together execute roughly 85% of retail options order flow. Alongside them sit the dominant institutional liquidity providers (Jane Street, Optiver, IMC, DRW). Jane Street's revenue figures alone — $20.5 billion in 2024 followed by $39.6 billion in 2025 — tell you how thick the layer of intermediation is between you and any counterparty with an actual directional view.

### The problem the dealer just created for themselves

Back to our trade. You bought a call. The dealer sold it. The dealer is now **short a call**. If SPY rallies, they lose money. If SPY falls, they make money. They have a directional exposure they did not want and are not paid to hold.

Carrying this exposure overnight is unthinkable. Consider the math: the spread the dealer captured might be ten cents per contract. A 1% move in SPY against their position on a delta of 0.50 produces a loss many multiples of that spread. They would lose months of franchise profit on a single bad afternoon. So they immediately, mechanically, neutralize the directional exposure. This neutralization is called **delta hedging**, and it is the engine that drives nearly everything that follows in this document.

### The lifecycle of one trade, end to end

Walk through what actually happens when you click "buy" on a single SPY $600 call. The chain is mechanical, fast, and almost entirely invisible to you.

**T + 0ms — You.** Click "buy" in your broker app at the NBBO offer of $3.05. Order is a marketable limit at $3.05 for 1 contract.

**T + 1-3ms — Your broker.** Routing engine decides which venue to send to. For SPY (equity option), almost always a wholesaler — Citadel Securities, Susquehanna, or Wolverine. SPX/XSP (index options) route directly to Cboe instead.

**T + 3-5ms — Wholesaler.** Receives the order. Their internal matching engine checks the principal book. They have inventory to sell the call at $3.03. They fill you at the NBBO ($3.05) — "price improvement" of $0.00 from the NBBO offer, but $0.02 better than their internal sub-mid mark. Their reported execution beats the SIP NBBO; their actual edge is the $0.02 spread.

**T + 5-10ms — Wholesaler.** Now short 1 SPY $600 call. Their risk system computes delta = 0.58 at current spot. They are short 58 share-equivalents. The risk system fires an aggregated hedge order — typically batched with hundreds of other simultaneous flows — for SPY shares.

**T + 10-50ms — Wholesaler.** Buys 58 SPY shares (or proportionally less if internalizable against opposite flow). The hedge typically executes at or inside the NBBO via either internalization, a lit exchange, or an ATS. The aggregate principal book is now delta-flat with respect to this trade.

**T + 1 day — OCC.** Trade settles. You have 1 long call (no shares delivered until exercise/expiry). The wholesaler has the offsetting short position registered at OCC. Counterparty risk is now between you and OCC, not between you and the wholesaler.

**Throughout life — Wholesaler.** Continuously delta-hedges as spot moves. Gamma, vanna, charm all feed in. P&L over the life of the trade depends on whether realized vol on the hedge path exceeded the IV implicit in the $3.05 fill. This is the gamma-theta math from Section 5C.

**Expiry — OCC / You / Wholesaler.** If expired worthless: you lose the premium, wholesaler keeps it (minus hedge P&L). If expired ITM: cash settles (SPX/XSP) or physical settles (SPY shares change hands).

### The franchise math at scale

One trade looks negligible — $0.02 of edge on a 1-contract order is $2. But the volume is enormous. Citadel Securities discloses executing roughly 35% of all US retail equity and options volume. On a typical day, that's billions of share-equivalents and tens of millions of options contracts running through their book. The 2025 total US options market traded approximately 13.8 billion contracts; if Citadel handled 35% of retail (and a smaller but still substantial fraction of institutional flow), their annual options volume is in the billions of contracts.

The arithmetic is dispiriting if you imagine taking the other side, and gratifying if you're the wholesaler:

```
Franchise revenue (simplified):
Revenue = Σ (edge per contract) × (contracts) − hedge slippage − tech & comp
```

With per-contract edges in the $0.50-$2.00 range across the retail options book and hundreds of millions of contracts annually, the franchise produces multi-billion-dollar revenues consistently. Jane Street's $20.5 billion (2024) and $39.6 billion (2025) net trading revenues are not aberrations. They are the asymptotic profile of a high-volume, low-per-trade-edge franchise that executes at scale.

### Risk capital vs alpha capital

Two kinds of capital are at work in any market-making operation. Understanding the distinction clarifies what dealers care about and what they don't.

**Risk capital** is the collateral the dealer must post against open positions. It covers the worst-case loss they could incur before they can unwind. Post-2008 regulation (Basel III, Dodd-Frank, EMIR) made this binding via stress tests. A modern dealer's biggest operational constraint is not "how much can we make per trade" — it is "how much capital does each book consume per unit of expected revenue."

**Alpha capital** is what the firm uses to take active directional or relative-value bets — outright views the desk has. Market makers technically run negligible alpha capital relative to their risk capital; they are nominally directionally flat. In practice, every dealer book has small residual exposures (skew, term, basis, correlation) that they choose to carry rather than hedge perfectly. These residuals are where the real "edge" of a well-run dealer book lives — and where the franchise can lose money in stress.

The relevance to retail: when you read "Citadel Securities lost $3 billion in March 2020," it almost certainly refers to the residual book, not the spread franchise. The spread franchise compounds quietly through every regime. The residual book is what produces the headline losses (and headline gains in benign years).

### Capacity constraints — why the dealer takes your trade

One question retail traders rarely ask: why is the dealer willing to take the other side of your trade specifically? Aren't they worried you might know something?

The honest answer: in aggregate, retail flow is informationally uninformed. A wholesaler internalizing $50 billion of monthly retail flow doesn't worry that the median order knows tomorrow's news. They worry about the tails — the rare retail order that's informed (insider activity, leaked earnings data). Those orders are flagged and routed to lit exchanges rather than internalized, because routing them externally transfers the adverse-selection risk to whichever venue takes them.

For institutional flow, the calculation is different. A hedge fund placing a $200 million SPX options trade is presumed informed; the wholesaler will quote wider (or refuse) and route through the order book directly. This is why "institutional spreads" on large index options trades are often 10-30 bps wider than the SIP NBBO that retail sees.

The structural lesson: **retail order flow is profitable to wholesalers because it is uninformed in aggregate**. The wholesaler is paid not for taking risk against a smart counterparty (they're not — they hedge immediately) but for providing immediacy and capturing spread against the noise that retail order flow represents in aggregate.

### A quick orientation to what follows

Every chapter from here forward is, in some sense, about how the dealer neutralizes the exposure they did not ask for, and what their neutralizing transactions do to the market. The arc:

- **Chapter 6C** — what exposure they actually inherited (the Greeks)
- **Chapter 6D** — how they neutralize the first-order risk (delta hedge)
- **Chapter 6E** — why the hedge doesn't stay neutralized (gamma)
- **Chapter 7** — the mathematical guarantee that the hedge is the only consistent strategy
- **Chapter 8 onward** — what happens when millions of these books interact

---

## 6C · The Greek inheritance

When the dealer sold you the call, they inherited a bundle of sensitivities. The option's value will change when the spot price moves, when implied volatility moves, when time passes, and when interest rates change. Each of these sensitivities has a name — a Greek letter, covered in Section 5C — and each must eventually be managed.

We start with the most important one. **Delta** is the partial derivative of the option's value with respect to spot. In plain language: if the underlying moves up by one dollar, the option moves up by delta dollars. For a call, delta lives between 0 and 1. For a put, between −1 and 0. Deep ITM options behave almost identically to holding the underlying (delta near ±1); deep OTM options barely react at all (delta near 0); ATM sits near ±0.5.

### Unpacking the Black-Scholes delta formula

The Black-Scholes call delta is:

```
Δ_call = e^(-qT) × N(d1)
where d1 = [ln(S/K) + (r − q + ½σ²) × T] / (σ × √T)
```

Let me unpack this piece by piece, because the structure repeats across every Greek in this document.

**N(·)** is the cumulative distribution function of the standard normal. It takes a number on the real line and returns a probability between 0 and 1.

**d1** is a standardized measure of "how in-the-money is this option, relative to the volatility it will see over the remaining time?" Specifically:

- **ln(S/K)** — the log-moneyness. Positive when spot is above strike (ITM for a call), negative when below (OTM), zero exactly at-the-money.
- **(r − q + ½σ²) × T** — adjusts for the risk-free rate (the forward should be higher than spot), the dividend yield (reduces the forward), and the convexity correction (½σ² accounts for the fact that the lognormal distribution's mean is shifted upward relative to the median in log space).
- **σ × √T** in the denominator — normalizes the log-moneyness by the standard deviation of log-returns over T years.

So d1 tells you, in z-score units, how strongly the option is positioned to finish in-the-money. Feeding that into N(·) gives a probability-like number. Multiplying by e^(-qT) adjusts for the dividend yield foregone by holding the option rather than the stock itself.

The result — delta — is the dividend-discounted **hedge ratio**: the number of shares per contract required to neutralize the option's first-order spot exposure. The Black-Scholes call price is C = S·e^(-qT)·N(d₁) − K·e^(-rT)·N(d₂). The two N(·) terms are different probabilities under different measures. **N(d₂) is the standard risk-neutral probability of finishing in-the-money.** Call delta = e^(-qT) × N(d₁) is the share-equivalent hedge ratio under the share-numeraire measure — close to but not equal to the ITM probability, with the gap growing as σ√T grows.

### Reading delta as a hedge ratio (not quite a probability)

A 0.30-delta call *behaves as* 30 shares of the underlying per 100-share contract — that's the operative meaning, and it's what dealer hedging is based on. The informal "30% chance of being ITM" interpretation is approximately right for short-dated near-money options but technically wrong: the actual ITM probability is N(d₂), which is N(d₁) − σ√T-ish smaller. For 30-day 30-delta options at 20% IV, the gap is about 3 percentage points; at 60% IV and 90 days, the gap can exceed 10. When you hear "I'm selling 25-delta puts," interpret it as "25-share-equivalent hedge ratio," not as "25% probability of assignment."

For dealer-mechanics purposes, the share-equivalent interpretation is the operative one. A dealer who is short 1,000 contracts of a 0.30-delta call is short 1,000 × 100 × 0.30 = 30,000 share-equivalents — they behave as if short 30,000 shares of the underlying. To neutralize this, they buy 30,000 shares. Section 6D covers the mechanics.

### The d1 geometry

A useful visualization: d1 is just a z-score, and the area under the standard normal density to the left of d1 is N(d1), which is delta (modulo the dividend factor).

[INTERACTIVE: d1-bell-curve]

A subtle but useful fact: the +½σ² term inside d1 is what makes high-vol options drift higher in delta even when at-the-money. This is the convexity correction — it accounts for log-normal asymmetry: even with zero spot move, high vol means more upside than downside in dollar terms (because the lognormal distribution is right-skewed by construction).

### The other Greeks the dealer also inherited

The call the dealer just sold also has a gamma, theta, vega, and rho. The dealer is short all of them in some sign convention:

- **Short delta** — to be discussed and hedged in 6D
- **Short gamma** — the dealer is on the unfavorable side of gamma (their delta moves against them). To be discussed in 6E.
- **Long theta** — the dealer collects theta as time passes. This is the compensation for accepting negative gamma.
- **Short vega** — the dealer loses money if IV rises (the option becomes more valuable to the customer holding it). Vega is more expensive to hedge dynamically; most dealers manage vega in aggregate across their book rather than hedging each position.
- **Short rho** — usually negligible for short-dated options

The asymmetry that drives all subsequent mechanics: the dealer can hedge delta easily and cheaply (just buy/sell shares of the underlying). They cannot hedge gamma cheaply except by acquiring offsetting options positions. Most dealer books are not gamma-hedged in the literal sense — they carry net gamma exposure and manage it through dynamic delta re-hedging. This is the structural setup for everything in 6E onward.

---

## 6D · Delta hedging — the mechanical neutralization

The dealer is short your one call. Their delta exposure is −Δ, where Δ is the call's delta. If we scale up: a dealer who has sold a hundred 0.50-delta calls is short:

```
100 contracts × 100 shares-per-contract × 0.50 delta = 5,000 share-equivalents
```

They behave as if they're short five thousand shares of the underlying.

The fix is mechanical. They go into the market and buy 5,000 shares of the underlying. Their book is now:

```
Position: short 100 calls + long 5,000 shares
Net delta: −5,000 + 5,000 = 0
```

They are flat. They have, at this instant, no directional exposure. The hedge has done its job.

[INTERACTIVE: delta-hedge-calc]

### Why this neutralization is local, not global

Here is the catch that every dealer has known since 1973 and that drives everything in the next eight chapters of this document. **The hedge is only correct at the current spot.** The moment spot moves, the option's delta changes — that change is gamma — and the existing share position is no longer the right hedge. The dealer must re-hedge. Then spot moves again. They must re-hedge again. This continuous re-hedging is, in idealized continuous time, exactly what makes Black-Scholes pricing work mathematically.

In practice, dealers don't re-hedge continuously. They re-hedge at discrete intervals — often whenever the residual delta exceeds some threshold, or at fixed time grids, or driven by market events.

### The hedging error variance

The choice of when to re-hedge introduces a residual risk. Suppose the dealer re-hedges at intervals of Δt apart. Between hedges, the option's value drifts according to its full Greek profile while the share hedge is static. The hedging error over the interval has variance approximately:

```
Var(hedging error per interval) ≈ ½ × Γ² × S⁴ × σ⁴ × (Δt)²
```

This expression encodes a key insight: **the more frequently you re-hedge, the smaller the noise**, but the more transaction costs you pay. There is an optimal frequency that depends on the relative magnitudes of gamma, volatility, and spread costs. For institutional dealers with very low transaction costs, the optimal frequency is high — every few seconds or even faster. For retail-scale operations with higher costs, the optimal frequency is lower.

For our purposes, the key point is that **dealers re-hedge continuously enough that the aggregate hedge flow is observable in the market**. The continuous-time idealization is good enough to predict where flow will appear: when spot moves through high-OI strikes, the dealer book's net delta shifts, and re-hedging activity appears in the underlying market.

### The 30 minutes that matter most: Baltussen et al. (2021)

The single most important empirical paper on dealer hedging at intraday horizons is **Baltussen, Da, Lammers & Martens (2021)**, "Hedging Demand and Market Intraday Momentum," *Journal of Financial Economics*, Volume 142, Issue 1, October 2021, pages 377-403.

Using intraday returns on over 60 futures contracts globally (equities, bonds, commodities, currencies) between 1974 and 2020, they document a robust "intraday momentum" pattern: **the return during the last 30 minutes before the market close is positively predicted by the return during the rest of the day (from previous close to the last 30 minutes)**. The predictive power is economically and statistically highly significant, and reverts over the next several days.

> *"Hedging short gamma exposure requires trading in the direction of price movements, thereby creating price momentum. Using intraday returns on over 60 futures on equities, bonds, commodities, and currencies between 1974 and 2020, we find strong market intraday momentum everywhere."*
> — Baltussen, Da, Lammers & Martens (2021), JFE

Their mechanism explanation: dealers rebalance toward close to limit overnight residual exposure. When dealers are aggregate net short gamma (typical historically), their re-hedging trades go *in the direction of* price moves — selling more as the price falls, buying more as the price rises. This creates intraday momentum that concentrates in the final 30 minutes.

The effect sizes are economically meaningful. The authors estimate that the predictive power of morning return on closing return generates Sharpe ratios in the 0.5-1.0 range for simple intraday momentum strategies — strong by intraday standards, though insufficient to support strategy deployment after transaction costs.

The mechanism extends beyond options. Leveraged ETFs (LETFs and inverse ETFs) also generate short-gamma hedging needs as their target leverage drifts during the day; they rebalance toward close in the same direction as the day's move. Variance swaps, risk parity portfolios, and vol-targeting funds all conduct similar end-of-day rebalancing in the same direction as the recent move. All of these hedging activities contribute to the documented intraday momentum.

This is why the close is often the most mechanical part of the day and why moves into 4 pm ET frequently extend rather than reverse. **The last 30 minutes are different**, and Baltussen et al. document the difference quantitatively across decades and markets.

### Re-hedging in practice: how often, what threshold

Different dealer business models re-hedge at different frequencies:

- **Equity wholesalers** (Citadel Securities, etc.) — re-hedge essentially continuously via aggregated order flow. Their hedging is interleaved with their market-making and is largely invisible as discrete flow.
- **Options market-makers** on Cboe — re-hedge at threshold breaches. Common thresholds: when residual delta exceeds 5-10% of the original position size, or when spot has moved 0.25-0.50% from the last hedge level.
- **Structured product desks** — re-hedge less frequently, often hourly or even less. They run larger residual deltas and accept the variance because their books are larger and the per-trade cost is higher.

The aggregate effect across the dealer ecosystem is that hedge flow scales with realized volatility. On calm days, hedging is small. On volatile days, hedging is large. This is the structural reason why volatility itself becomes self-reinforcing during stress regimes — Section 8B returns to this with the formal feedback model.

---

## 6E · Gamma — the engine of forced flow

Gamma is the partial derivative of delta with respect to spot. It is the second derivative of the option price with respect to spot. Pronouncing those words and *understanding what gamma actually does* are different things, so let me show you rather than tell you.

### The Black-Scholes gamma formula

```
Γ = e^(-qT) × φ(d1) / (S × σ × √T)
```

where φ(·) is the standard normal density function (the bell-curve height, not the CDF area). Three things to notice:

**First**, gamma is the same for a call and the corresponding put with the same strike — put-call parity guarantees it.

**Second**, gamma is maximized at-the-money: φ(d1) is the bell-curve density, which peaks when its argument is zero, which happens approximately when spot equals strike.

**Third**, and this is the explosive observation, **gamma is proportional to 1/√T**. As time to expiration shrinks toward zero, ATM gamma diverges to infinity. This is not a mathematical curiosity. It is the dominant feature of modern intraday microstructure, because 0DTE options live exactly in this regime.

### The dealer chases delta

The dealer who has sold 1,000 ATM calls at strike $100 with 30 days to expiry initially hedges by buying shares equal to their net short delta. As spot moves, delta changes — and the existing share position becomes wrong. The dealer must rebalance.

[INTERACTIVE: gamma-hedge-sim]

**The dealer is short gamma. Their forced trades go in the same direction as the price move.** They buy as price rises and sell as it falls. This is the destabilizing pattern that dominates negative-GEX regimes at the market level: every dollar of move generates more flow in the direction of the move, which generates more move. The feedback loop is what makes Volmageddon, March 2020, and individual gamma squeezes like GME possible. It also explains why such episodes feel so "violent" — they're not violent because of news but because of mechanical positive feedback.

The opposite case — the dealer **long gamma**, buying dips and selling rallies — is what stabilizes most days in modern markets and what gives positive-GEX regimes their characteristic mean-reverting feel. We'll see in Section 9B that current 0DTE market structure has dealers in aggregate *long* gamma most days (because retail is selling and dealers are buying), which is partly why intraday SPX volatility has compressed even as headline option volume has exploded.

### The long-gamma mirror, worked out

Mirror the short-gamma example above, sign-reversed, at SPX scale so it lines up with the $46k per-contract baseline used in the rest of this section.

Suppose a dealer is *long* 1,000 SPX 6,000 calls with 30 DTE, IV 18%. Per-call ATM delta ≈ 0.52. Total delta exposure from the calls: 1,000 × 100 × 0.52 = +52,000 share-equivalents long. To neutralize, the dealer hedges by going **short 52,000 share-equivalents** of SPX (futures, basket, or ETF).

Now spot ticks up 1% to 6,060. With Γ ≈ 0.0013 per dollar of spot, the per-call delta moves by 0.0013 × 60 ≈ 0.078 — from 0.52 to roughly 0.60. New total long delta from the calls: 1,000 × 100 × 0.60 = +60,000 share-equivalents. To stay flat, the dealer's hedge must grow to short 60,000. They were short 52,000. **They sell 8,000 more shares**.

Spot rising → dealer sells more → presses the rally back toward equilibrium. The opposite holds on a down-move: spot to 5,940 takes delta from 0.52 to 0.44, the dealer's required short hedge shrinks from 52,000 to 44,000, and the dealer **buys** 8,000 shares to close part of the short. Spot falling → dealer buys → absorbs the fall.

**The pattern reverses the short-gamma case at every step.** Where the short-gamma dealer's forced trades reinforce the price move (sell into dumps, buy into rallies), the long-gamma dealer's forced trades fade it. Same 8,000-share rebalance per 1% move, opposite sign. This is the structural source of the stabilizing dynamic in positive-GEX regimes — not because someone is "providing liquidity" with judgment, but because the math of delta-hedging requires the opposite-direction trade when the dealer's gamma is the other sign.

**Bridge to Section 8A.** Long gamma damps; short gamma amplifies. The aggregate dealer book in any given product is a *sum* of both signs across all dealers, strikes, and expirations. When that sum is positive (dealers net long gamma), the market behaves like the long-gamma case writ large; when negative, like the short-gamma case. The aggregation in 8A is doing exactly this — collapsing thousands of individual long- and short-gamma positions into a single signed scalar that classifies the prevailing regime.

### Dollar gamma: the unit that matters

Raw gamma is in units of "delta per dollar of spot move," which is a hard number to interpret across stocks of different prices. The standardized unit dealers actually care about is **dollar gamma per 1% move**:

```
$Γ_1% = Γ × S² × 0.01
```

Why this form? A 1% move in price is ΔS = 0.01 × S. The dealer's delta changes by Γ × ΔS = 0.01 × Γ × S per share. To hedge, they transact that many shares per share of original exposure. The dollar value of that flow is (0.01 × Γ × S) × S = 0.01 × Γ × S² per share, or scaling by contracts, 0.01 × Γ × S² × OI × 100. Dropping the 100 (a constant convention), you get the formula above — the canonical "$Γ per 1%" used in every GEX model from SqueezeMetrics onward.

For a typical ATM SPX option at spot 6,000 with 30 days to expiry and 18% IV, single-contract dollar gamma per 1% move is approximately **$46,000** (Γ ≈ 0.0013 per dollar of spot; per 1%: 0.0013 × 6000² × 0.01 ≈ $464/share × 100 share multiplier = $46,400). For SPY at $600 spot: approximately **$460 per contract per 1%** (same Γ, 100× smaller notional).

[INTERACTIVE: dollar-gamma-units-lab]

Aggregate dealer dollar gamma across the listed SPX book typically ranges from $20B to $100B per 1% move on a normal day. This is the scale of mechanical hedging flow potentially sitting in dealer inventory — meaning a 1% move in SPX could generate tens of billions of dollars of forced rebalancing, depending on the sign of dealer net gamma.

This is what Section 8A formalizes into the GEX metric and what Section 8B shows can drive market regime characterization. The dollar gamma magnitude tells you the *potential size* of mechanical flow. The sign tells you the *direction*. Together they characterize the dealer-hedging engine that drives the modern intraday market.

### The mechanism's predictions

If the framework so far is correct, several predictions follow:

1. **Intraday momentum should be observable in markets dominated by short-gamma dealer positioning.** ✓ Baltussen et al. (2021) document this across 60+ futures markets.

2. **Intraday mean reversion should be observable in markets dominated by long-gamma dealer positioning.** ✓ Modern SPX intraday character has compressed measurably since 0DTE growth, consistent with the Cboe and Dim-Eraker-Vilkov finding that 0DTE dealer positioning is net long-gamma on average.

3. **Volatility should be self-reinforcing in short-gamma regimes.** ✓ Volmageddon and March 2020 case studies in Section 8C document exactly this.

4. **The transition between regimes — the "gamma flip" — should be marked by visible character change.** ✓ Practitioner experience and academic literature both confirm this, though precise identification of the flip level is contested across vendor methodologies.

The framework is empirically supported, but not in a "gamma squeeze accounts for everything" sense — in a "gamma hedging accounts for measurable tens-of-basis-points effects, with occasional larger episodes during stress" sense. Section 8 quantifies this; Section 9 applies it; Section 12 sizes for it.

---

## 6F · The hedging frequency vs cost tradeoff

Everything in 6E assumed *continuous* hedging — the dealer is, at every instant, delta-flat. Real dealers don't rebalance continuously. They cross the bid-ask each time, and the friction is not free. The real optimization a dealer faces is **how often to re-hedge**: often enough to keep gamma exposure controlled, but not so often that spread cost devours the variance they were trying to capture (long gamma) or accept (short gamma).

### The rebalance threshold

Practitioners parameterize discrete hedging by a **rebalance threshold** — a delta-equivalent or basis-point move from the last hedged level that triggers a fresh rebalance. Examples: "rebalance when net delta drifts more than 5,000 share-equivalents," or "rebalance after every 25 bps move in SPX." Tighter threshold → more frequent rebalances → tighter gamma control → higher spread cost. The tradeoff is monotone in each direction; the question is where the *net* optimum sits.

### Stylized arithmetic — long-gamma scalping at SPX scale

Take the long-gamma dealer of 6E's mirror walkthrough: 5,000 long SPX 6,000 calls at IV 18%, 30 DTE. Daily theta cost ≈ $1.0M (= per-contract theta × 5,000). Aggregate dollar gamma per 1% move ≈ $230M.

For a day with realized vol 20% annualized (about 1.26% daily, slightly above the 18% IV), expected gamma scalping income from *continuous* hedging is approximately:

```
E[gamma capture] = ½ × Γ_$ × σ_d² × scale  ≈  ½ × $230M × (0.0126)² × 100  ≈  $1.83M
```

Net of theta, the frictionless P&L lands near **+$830k/day**. That's the upper bound.

Now layer in friction. SPX bid-ask is ~$0.10 on a $6,000 spot — about 1.7 bps each way crossed. Each rebalance trades roughly $1M × (threshold in bps) of underlying notional per percentage point of dealer gamma (a 50 bp move on $230M dollar gamma per 1% rebalances ≈ $115M notional). The spread paid per rebalance scales with notional × half-spread.

| Threshold | Variance captured | Gamma gross | Rebalances/day | Spread cost/day | Net P&L |
|---:|---:|---:|---:|---:|---:|
| Continuous (frictionless) | ~100% | +$1.83M | — | $0 | **+$830k** |
| 5 bps | ~95% | +$1.74M | ~40 | −$80k | **+$660k** |
| 15 bps | ~85% | +$1.56M | ~15 | −$36k | **+$520k** |
| 25 bps | ~70% | +$1.28M | ~6 | −$22k | **+$258k** |
| 50 bps | ~45% | +$820k | ~3 | −$15k | **−$195k** |
| 200 bps | ~12% | +$220k | ~0.5 | −$3k | **−$783k** |

The U-shape is in the *net* column: 5-15 bps is near optimal; below 5 bps the spread eats every wiggle; above 25 bps the dealer leaves so much variance uncollected that theta exceeds gamma capture. The 50 bps and 200 bps rows show the strategy flipping from positive to negative as the threshold widens — same option position, same realized vol, same dealer.

The captured-variance column reflects the path's mean-reverting jaggedness: across 1.26% of daily net motion, the cumulative *path length* (sum of |ΔS|) is typically 2.5–4× the net move, and the sum of squared moves scales with how finely you slice that path. Fine thresholds catch nearly all of it; coarse thresholds catch only the large swings.

### Why the spread matters

Spread cost on each rebalance ≈ (notional rebalanced) × (half-spread). For SPX at $6,000 with $0.10 spread, that's about 0.83 bps per crossing. A 5 bp rebalance pays about 17% of the move width in spread; a 50 bp rebalance pays about 1.7%. **For tight thresholds, friction is a multi-percent-of-the-trade tax — which is exactly why high-frequency market makers, who provide the liquidity the dealer's rebalances consume, earn a steady fraction of the spread.** The dealer's discrete hedging *creates the order flow* that the HFT layer is selling into.

For single-stock options where spreads are 5-15 bps rather than 1.7 bps, the optimum threshold widens to 30-60 bps; the dealer simply cannot afford fine-grained rebalancing. This is also why illiquid-product dealer realized-vol estimates tend to *exceed* the underlying's true vol — there's a spread-cost overhead embedded in every hedge that doesn't appear in the unhedged price path.

### Forward connection — 8A's idealization

Section 8A treats GEX as if every contract's gamma is instantaneously hedged on every spot move. **It isn't.** There is a frequency-dependent friction layer between open interest and observed dealer flow. The idealization is *approximately* correct at daily-and-longer frequencies — the path catches up over a day — but loosens visibly at intraday horizons, where rebalance discreteness shows up as latency in the hedge response and as residual delta drift between rebalances. When you read "GEX is +$5B today, expect mean-reverting intraday character," the right mental supplement is "expect mean-reverting intraday character *averaged over a few-hours rebalance cycle*, with bursts of inverse character at the moments a large dealer is sitting on undelivered hedge."
