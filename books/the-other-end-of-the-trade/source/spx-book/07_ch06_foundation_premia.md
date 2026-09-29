# Chapter 6 — Foundation premia
## ERP, VRP, Trend, Carry

> **Core intuition.** These four edges anchor the portfolio. They share three properties: they're risk premia (so they don't decay when capital exploits them), they have multi-decade evidence across multiple markets, and they have measurable mechanisms tied to identifiable risks. Each chapter section follows the standard teaching template.

---

## 6.1 Equity Risk Premium (ERP)

### Core intuition
Equities pay a premium over bonds and cash because their cash flows are riskier in the states of the world that matter most to investors (recessions, when consumption is already low). The premium compensates for non-diversifiable consumption risk plus behavioral overlays (myopic loss aversion).

### Toy example
US: $1 invested in equities in 1900 grew to ~$107,409 nominal by 2024. $1 in long bonds grew to ~$268. The ratio (~400×) is enormous over 125 years even though both were "positive." That ratio is the equity risk premium compounding.

### Formal object
$$E[R_\text{eq} - R_f] = \beta_\text{eq} \cdot \pi_\text{cons-risk} + \text{behavioral premia}$$

Long-run realized US ERP: ~5-7% over bills, ~3-5% over long bonds. Forward-looking implied ERP (Damodaran 2025): ~4.3%, suggesting some compression vs 20th-century averages.

### Evidence
- Mehra-Prescott (1985, *JME*) — named the "equity premium puzzle" because observed ERP was too large to fit standard utility models
- Dimson-Marsh-Staunton 2025 UBS Yearbook — 35 markets, 23 with full 1900-2024 history; world equity real return ~5.2% vs bonds ~1.7%
- Damodaran updates implied ERP regularly using DDM-style models

### Why it exists
Compensated risk premium (Source 1). Equities have systematic exposure to consumption risk (they pay less in bad times). Behavioral additions: investors evaluate equity returns annually, so they overweight short-term losses (Benartzi-Thaler 1995 myopic loss aversion).

### Retail implementation
- **Vehicle:** SPY/VOO for US, VXUS/IXUS for ex-US, VT for global all-country
- **Haircut:** small. Academic 0.4-0.5 → ETF live 0.4-0.5 → user account 0.35-0.50.
- **Tax:** in taxable accounts, prefer tax-efficient ETFs; ES futures for leveraged exposure (1256 60/40)
- **Diversification:** Dimson et al. argue strongly for global diversification; US-only is simpler but risks overweighting one market's lucky century

### Failure mode
Multi-decade negative real returns are real (Japan 1989-2010+, Germany 1900-1955, US 1929-1949). Forward returns depend on starting valuations — high CAPE periods historically produce lower 10-year returns.

### Decision rule (today)
Allocate. ERP is the foundation. Tactical sizing reductions when:
- 1/CAPE - 10Y Treasury yield < -1% sustained
- VIX backwardated AND 12m earnings growth turns negative

But don't try to time exits. The cost of missing a few good years vastly exceeds the benefit of avoiding a few bad ones.

### Misconception box
> **Misconception:** "US ERP has been ~7% real, so I should expect ~7% real going forward."
>
> **Correction:** Forward expected ERP is meaningfully lower than 1900-2000 realized ERP because starting valuations are higher and the "lucky" path of US 20th-century returns isn't guaranteed to repeat. Use 4-5% real as a planning assumption, not 7%.

### Self-check (ERP)
1. Why does ERP exist?
2. What's the gap between historical realized and forward expected ERP?
3. Why do Dimson-Marsh-Staunton argue for global diversification?
4. State a tactical sizing rule based on valuation.

---

## 6.2 Index Variance Risk Premium (VRP)

### Core intuition
Option-implied volatility consistently exceeds subsequently realized volatility because option buyers (asset managers hedging portfolios, structured-product issuers, retail call buyers) pay a premium for insurance. Option sellers earn the premium for accepting crash risk.

### Toy example
From 1990-2018, VIX implied volatility averaged 19.3% versus realized SPX volatility of 15.1% — a 4.2 vol-point gap that compounded through systematic put-writing. Bondarenko's PUT index over the same period: 9.54% CAGR, vol 9.95%, Sharpe ~0.65, max DD -33% in GFC vs SPX 9.80%, vol 14.93%, Sharpe ~0.49, DD -51%.

### Formal object
$$\text{VRP}_t = \text{IV}_t^2 - E_t[\text{RV}_{t,T}^2]$$

variance risk premium = implied variance minus expected realized variance.

For SPX index, this is positive ~80% of months. Across the full distribution it has mean ~+4 vol points but with negative skew (-2.09 for PUT index).

### Evidence
- **Carr-Wu (2009, *RFS*)** — canonical academic decomposition of VRP across asset classes
- **Bollerslev-Tauchen-Zhou (2009, *RFS*)** — VRP as predictor of future returns
- **Drechsler-Yaron (2011, *RFS*)** — VRP as exposure to time-varying disaster risk
- **Bondarenko (2014, 2019)** — PUT index empirical analysis
- **Jurek-Stafford (2015, *JOF*)** — *required reading*: hedge fund returns indistinguishable from put-write after pricing skew
- **Bakshi-Crosby-Gao (2024, *Math Finance*)** — formal ambiguity-averse framework; naive VRP harvest unattractive after risk pricing

### Why it exists
Risk premium (Source 1). Option buyers want insurance against bad outcomes; option sellers demand a premium to take the other side. The premium is compensation for crash risk — and Jurek-Stafford shows that the apparent "alpha" of premium-selling is largely just compensation for accepting negative skew.

### Retail implementation
- **Vehicle (preferred):** XSP cash-secured monthly ATM put-write (mini-SPX, 1256 tax)
- **Vehicle (passive):** PUTW ETF, but be aware it changed strategy in 2023 to weekly options
- **Haircut:** academic 0.65 → live PUTW 0.30-0.45 → self-managed XSP user-account 0.20-0.40

### "Put-writing" is not one thing
The variants behave very differently:
- ATM monthly cash-secured (closest to academic VRP)
- OTM 30-delta short put (better risk-adjusted, smaller premium)
- Far-OTM 5-delta tail put (structurally dangerous, small premium with catastrophic tails)
- Weekly / 0DTE premium selling (different vega/gamma profile, much higher operational risk)
- Put-spread / iron condor (defined-risk but inferior expected return; CNDR underperforms massively)
- Short variance swap (cleanest theoretical exposure, retail can't access)

When this book refers to "VRP harvest" it specifically means **ATM monthly cash-secured XSP puts**. Other variants are different strategies.

### Failure mode
- Crashes: PUT lost -33% in GFC (vs SPX -51%); -28% in March 2020
- Specifically dangerous in negatively-skewed events: 1987-style gaps can produce force-liquidation under PM
- Path dependency: even cash-secured puts MTM badly in stress and can require holding through 3-month underwater periods

### Decision rule (today)
Allocate 10-15% of portfolio to ATM monthly cash-secured XSP put-write, with kill criteria:
- VIX/VIX3M > 1.05 for 3 days → halt new sales
- 21-day realized vol > 30 → reduce sizing 50%
- Sleeve drawdown > 20% PTP → stop and reassess

### Misconception box
> **Misconception:** "VRP is +4 vol points, so I'm guaranteed money over time."
>
> **Correction:** VRP is a long-run *average* premium with heavy negative skew. In any 12-month window, you can lose 30%+ of the position even with the average premium being positive. The "guarantee" is over very long horizons (5+ years) AND only if you size correctly to survive the path.

### Self-check (VRP)
1. State the VRP. Why is it positive?
2. What does Jurek-Stafford 2015 show about VRP "alpha"?
3. Why do variants of put-writing produce very different P&L profiles?
4. State the kill criteria for an XSP put-write sleeve.

---

## 6.3 Trend-following / Time-Series Momentum

### Core intuition
Across asset classes and across centuries, recent winners tend to keep winning over horizons of 1-12 months. The effect is most visible in trending periods (2008 commodity crash, 2022 inflation move, 2014-2015 oil collapse) and frustratingly absent in chop. The mechanism is multifactorial: behavioral under-reaction, hedger compensation, and liquidity provision in stressed markets.

### Toy example
Hurst-Ooi-Pedersen (2017): 1880-2016, 67 markets. Average net Sharpe ~0.4 after 2/20 fees. **Positive in every decade since 1880.** Best decade: 1973-1982 (rising rates, refuting the "secular bond bull" critique). **Positive in 8 of 10 largest 60/40 drawdowns** — including 2008 and 2022.

### Formal object
For each asset, position size proportional to recent trend signal:
$$w_{i,t} = \text{sign}(R_{i,t-12,t}) \cdot \frac{1}{\sigma_{i,t}}$$

Long winners, short losers, vol-scaled. Diversified across many asset classes — equities, bonds, FX, commodities. The aggregate strategy has positive expectation and unique crash payoff property.

### Evidence
- **Moskowitz-Ooi-Pedersen (2012, *JFE*)** — canonical TSMOM paper across 58 markets
- **Hurst-Ooi-Pedersen (2017, *JPM*)** — 140-year evidence
- **Asness-Moskowitz-Pedersen (2013, *JF*)** — Value and Momentum Everywhere
- Live indices: SG Trend, BTOP50 — realized Sharpes 0.3-0.5 over 20 years

### Why it exists
Combination of all four sources:
- Risk premium (compensation for whipsaw risk)
- Behavioral (under-reaction to slowly-incorporated information)
- Institutional (commodity producer hedging needs)
- Microstructure-related liquidity provision

The breadth of mechanisms is itself evidence — multiple independent reasons for the effect, all of which would have to fail simultaneously for trend to disappear.

### Retail implementation
- **Vehicles (NOT interchangeable):**
  - **DBMF** (iMGP DBi Managed Futures): replication-style, lower fees, 1-2 month lag
  - **KMLM** (KFA Mount Lucas): fixed asset universe, transparent, less diversified
  - **RSST** (Return Stacked US Stocks & Managed Futures): 100% equity + 100% trend in one wrapper, capital-efficient but levered
  - **Self-managed**: feasible but operationally heavy
- **Haircut:** academic 0.8-1.2 (paper) → live CTA index 0.3-0.5 → ETF live 0.25-0.45 → user-account 0.20-0.40
- **Tax:** futures-based vehicles get 1256 (favorable)

### Failure mode
- Long whipsaw periods (2011-2018 was the worst trend drought in modern history)
- Rapid V-shaped reversals where trend is forming the wrong direction (March 2020 example)
- Manager dispersion is real — picking the wrong vehicle can underperform the SG Trend Index by 200-400 bps annually

### Decision rule (today)
Allocate 10-15% of portfolio to a single transparent trend vehicle (DBMF or KMLM, not multiple stacked). Don't time entries — buy and hold across cycles. Kill criteria:
- Vehicle drawdown > 25% PTP
- Tracking error to BTOP50 > 4% annualized
- 3 consecutive years of negative absolute returns → reassess (don't auto-exit)

### Misconception box
> **Misconception:** "Trend has lower Sharpe than VRP, so it's worse."
>
> **Correction:** Trend's value is not its standalone Sharpe — it's its crash complementarity. Trend was positive in 8 of 10 largest 60/40 drawdowns. VRP was negative in essentially all of them. In a portfolio context, a 0.3 Sharpe trend sleeve adds *more* to portfolio Sharpe than a 0.5 Sharpe sleeve that's correlated with everything else premium-selling. Allocate by portfolio contribution, not standalone Sharpe.

### Self-check (Trend)
1. What's the canonical evidence for trend-following?
2. Why is trend's portfolio contribution larger than its standalone Sharpe suggests?
3. What's the difference between DBMF and KMLM?
4. What's the typical trend "drought" duration, and what's the operational implication?

---

## 6.4 Cross-Asset Carry

### Core intuition
"Carry" is the expected return assuming prices don't change. Currencies with high yields, bonds with steep curves, commodities in backwardation, and equities with high dividend yield all pay positive carry. Across asset classes, high-carry assets earn higher returns on average than low-carry assets, with concentrated underperformance in liquidity events.

### Toy example
Buy AUD (high yield) and short JPY (low yield). The interest rate differential is ~3-4% annually. If exchange rates are random walks, you earn the differential. Empirically, AUDJPY tends to drift up in calm periods and crash in stress (2008, 2020). The compensation for the crash risk is the "carry premium."

### Formal object
$$\text{Carry}_{i,t} = \frac{F_{i,t} - S_{i,t}}{S_{i,t}}$$

(futures-spot ratio, simplified). Positions: long high-carry assets, short low-carry; vol-scaled and diversified across asset classes.

### Evidence
- **Koijen-Moskowitz-Pedersen-Vrugt (2018, *JFE*)** "Carry" — Sharpes 0.37-1.80 across asset classes, average ~0.74 standalone, combined 0.6-0.9 diversified
- Common bad periods cluster in global recessions

### Why it exists
Risk premium (Source 1) with institutional component. High-carry assets bear "bad-times" risk: FX crashes during liquidity events, commodity backwardation reverses during demand collapses, high-yielding bonds underperform when defaults rise. The carry premium compensates for this.

### Retail implementation
- **Vehicle:** limited retail access. QSPRX/QSPIX-style mutual funds have closed/restricted. Some return-stacked products. Self-managed FX carry via futures (small effect post-2008).
- **Haircut:** academic combined Sharpe 0.6-0.9 → realistic retail 0.15-0.30
- **Operational:** complex; multiple asset classes; futures execution

### Failure mode
Liquidity events. Carry trades unwind violently — 2008 saw AUDJPY drop 40% in 4 months as carry trades reversed. Stop-losses don't help because the gap moves are larger than typical stops.

### Decision rule (today)
Small allocation (5-10%) if accessible. Honest position: cross-asset carry is institutional-quality but the retail implementation gap is wide. **Don't treat as foundation; treat as supplementary diversifier.**

Kill criteria:
- TED spread > 200 bps OR MOVE > 150 → halt new positions
- Carry-spread-to-vol ratio < 0.3 → reduce sizing

### Misconception box
> **Misconception:** "FX carry is easy retail money."
>
> **Correction:** Post-2008, rate dispersion across major currencies has been compressed (most G10 banks moved toward zero rates, then synchronously back up). Carry premiums in FX have shrunk substantially. Diversified cross-asset carry (FX + bonds + commodities + equities) still has documented Sharpe, but FX-only is much weaker than its 1990s-2000s reputation suggests.

### Self-check (Carry)
1. State the carry formula.
2. Why is carry a risk premium?
3. Why is FX-only carry weaker post-2008?
4. What's the binding retail constraint on cross-asset carry?

---

## 6.5 Putting the foundation premia together

### Aggregate allocation
- Long equity (ERP): 50-60% of portfolio risk
- VRP harvest (XSP put-write): 10-15% of risk
- Trend-following: 10-15% of risk
- Cross-asset carry: 5-10% (if accessible)

Total foundation: ~70-80% of portfolio risk. The remaining 20-30% is for factor tilts, structural overlays, and tactical positions.

### Correlation structure
Foundation premia correlate to varying degrees in stress:
- ERP and VRP: highly correlated in left tail (~1.0) — both lose in crashes
- ERP and Carry: moderate-high correlation in liquidity events
- ERP and Trend: **negatively correlated in slow drawdowns** — this is the key reason trend is in the foundation
- VRP and Trend: mostly uncorrelated; trend can be positive while VRP is negative

The trend allocation is the single most important diversifier. Without it, foundation = "different ways to be long equity beta and short skew." With it, foundation has a genuine crash hedge.

### Stress P&L on the full foundation
Hypothetical $1M portfolio, 60/15/15/10 weighting:

| Scenario | ERP P&L | VRP P&L | Trend P&L | Carry P&L | Total |
|---|---|---|---|---|---|
| **S1: SPX -10/VIX +10** | -60k | -25k | flat | -3k | **-88k** |
| **S2: SPX -20/VIX +25** | -120k | -50k | +10k | -8k | **-168k** |
| **S3: SPX -35/VIX +50** | -210k | -110k | +30k | -15k | **-305k** |
| **S4: 1987 gap** | -132k overnight | -80k | +5k | -10k | **-217k** |

Trend partially offsets the equity-correlated sleeves in S2/S3. Without trend, the same scenarios would lose another 5-10%. This is why the allocation matters.

---

## 6.6 Self-check (Chapter-level)

1. Name the four foundation premia. Why is each a foundation rather than an overlay?
2. Which foundation premium has the worst standalone Sharpe but the best portfolio contribution? Why?
3. Apply the conviction score (Chapter 4) to a hypothetical 12% allocation to XSP put-write in a calm regime (VIX 14, contango). What's C?
4. Why does cross-asset carry have a wider retail haircut than ERP?
5. What's the operational difference between buying SPY and writing ATM puts on XSP? When would you prefer each?

---

## Where this fits

Chapter 6 is the heart of the framework — the foundation that anchors the portfolio. Chapter 7 will cover factor tilts that modulate the equity sleeve. Chapter 8 covers structural overlays. Chapter 9 covers regime filters. Chapter 10 covers the rejected category (what NOT to trade and why).

Chapter 11 will provide worked examples that walk through the conviction analysis for each of these strategies in different market conditions. That's where concept becomes judgment.

[← Previous: Chapter 5 — Taxonomy](06_ch05_taxonomy.md) | [Next: Chapter 7 — Factor tilts →](08_ch07_factor_tilts.md)
