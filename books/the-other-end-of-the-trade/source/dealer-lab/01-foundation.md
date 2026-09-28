# Section 1 · Foundation
*Math primitives the rest of the book builds on.*

Before we can talk about dealers, hedging, gamma, or any of the structural machinery of options markets, we need a common foundation in four things: what a return distribution actually looks like, why we use logarithmic returns instead of percentage returns, what "edge" really means in expected-value terms, and how to think about risk-adjusted performance without lying to ourselves. These four ideas are not optional preliminaries. They are the load-bearing assumptions under every claim that follows. If you skip them, every later chapter will mislead you in subtle and expensive ways.

This section is organized as four sub-chapters, each building on the previous. **1A** establishes that returns are not Gaussian and that the Sharpe ratio — the most-cited number in finance — is structurally blind to the deviation from Gaussianity that matters most: skew. **1B** justifies the use of log returns, which are additive over time and symmetric in a way that simple percentage returns are not. **1C** defines expected value precisely and shows the most important consequence: win rate is not edge. **1D** revisits the Sharpe ratio with full machinery — what it measures, what it misses, and why low-Sharpe strategies cannot safely use leverage no matter how positive their drift.

---

## 1A · Distributions, skew, and why Sharpe lies

The single most consequential thing to internalize before evaluating any short-volatility strategy is this: **the Sharpe ratio cannot see skew**. A strategy can win ninety-five percent of the time and still lose money. A strategy can show a Sharpe ratio of 0.8 in a backtest and a Sharpe ratio of 0.2 in a live retail account. The gap between these numbers is, mostly, the shape of the return distribution — specifically the third and fourth moments that Sharpe ignores by mathematical construction. If you only remember one thing from this entire section, remember that.

### The four moments, in order of operational importance

Any return distribution is described, to first approximation, by four numbers — the **moments** of the distribution. They have technical names but each one answers an intuitive question.

The **first moment** is the mean, μ = E[R]. It answers: *what is the average return?* This is the thing every backtest tab brags about. By itself it tells you almost nothing because the same mean can be produced by wildly different distributions.

The **second moment** about the mean is the variance, σ² = E[(R − μ)²]. Its square root, σ, is the standard deviation. It answers: *how spread out are the returns around the mean?* Variance is the engine of the Sharpe ratio: high mean and low variance produce high Sharpe; high mean and high variance produce mediocre Sharpe.

The **third moment**, normalized by σ³, is the skewness:

```
Skew = E[((R − μ) / σ)³]
```

It answers: *is the distribution symmetric, or is one tail longer than the other?* For a true Gaussian distribution, skew is zero. For SPX daily returns over multi-decade samples, skew is approximately **−0.7** (left-skewed — the left tail, the loss tail, is longer than the right). For the CBOE PUT Index — a benchmark for systematic monthly at-the-money put-writing on SPX, which Cboe has tracked since June 1986 — skew is roughly **−2.1** on monthly returns. The PUT Index has skew approximately three times worse than the underlying it sells protection on. Selling premium does not eliminate skew; it *concentrates* it.

The **fourth moment**, normalized by σ⁴, is the kurtosis:

```
Kurtosis = E[((R − μ) / σ)⁴]
```

It answers: *how fat are the tails relative to a Gaussian?* For a true Gaussian, kurtosis is exactly 3. (Some texts use "excess kurtosis," kurtosis minus 3, so that zero means Gaussian.) For SPX daily returns since 1928, kurtosis is roughly **15 to 20** depending on the sample — five to seven times the Gaussian value. Returns are massively fatter-tailed than a normal distribution. The tail events we care most about — Black Monday 1987, October 2008, Volmageddon 2018, March 2020 — are not rare flukes against a Gaussian baseline. They are routine against an empirically calibrated baseline that recognizes how fat the tails actually are.

To put this in operational terms: under a Gaussian model calibrated to pre-1987 SPX daily volatility, the −22.6% one-day move on October 19, 1987 had a probability of roughly **10⁻¹³⁷**. That number is so absurd it should have ended faith in Gaussian models permanently. The probability under the Gaussian model that this event would have occurred *once in the lifetime of the universe* (about 4×10¹⁷ seconds × maybe 10⁵ markets) is still essentially zero. The event happened anyway. Anyone who told you in 1986 that the Gaussian model was an acceptable approximation owed you an apology by October 20th.

### Mean and variance produce Sharpe; skew and kurtosis produce the gap between Sharpe and reality

The Sharpe ratio is defined as:

```
SR = (E[R] − r_f) / σ_R
```

Notice what's in the formula: mean (first moment), standard deviation (square root of second moment), and a risk-free rate. Notice what's *not* in the formula: skew, kurtosis, the entire shape of the left tail, autocorrelation, drawdown depth, recovery time, regime conditioning. The Sharpe ratio is a two-parameter summary of a distribution that requires four parameters to characterize even roughly, and many more to characterize honestly.

This would not matter if real return distributions were approximately Gaussian. They aren't. For most strategies retail traders care about — short premium, trend-following, factor tilts, volatility-targeted equity, momentum — the higher moments are big enough that ignoring them constitutes financial malpractice.

[INTERACTIVE: skew-simulator]

What you're seeing: at skew = 0 the distribution is symmetric — Sharpe matches the intuition. At skew = −3 the mean and standard deviation are essentially unchanged, but the left tail has grown much fatter and ES₉₅ has roughly doubled in magnitude. Sharpe drifts slightly because the asymmetry shifts the mean a hair, but it doesn't come close to reflecting the change in tail risk. **The same Sharpe describes two very different P&L distributions.** This is the canonical "Sharpe lies" demonstration.

### The win-rate trap

Consider two coin-flip scenarios with identical 95% win rates but opposite expected values.

**Scenario A — the insurance buyer.** With probability 95% you pay $1; with probability 5% you receive $25. The win rate is 5% (you "win" when the rare event hits). The expected value is:

```
E[X] = 0.95 × (−1) + 0.05 × (+25) = −0.95 + 1.25 = +$0.30
```

The bet pays $0.30 per round in expectation. This is the structural shape of a tail-hedge buyer: pay small premiums most of the time, collect a large payoff when the rare event hits. Positive EV, low win rate, positive skew.

**Scenario B — the premium seller.** Flip Scenario A around: with probability 95% you receive $1; with probability 5% you pay $25. Win rate is now 95%. Expected value is:

```
E[X] = 0.95 × (+1) + 0.05 × (−25) = +0.95 − 1.25 = −$0.30
```

You win 19 times out of 20 and lose money in expectation. **This is the trap.** The same shape — 95% wins, 5% catastrophic losses — describes every undisciplined premium-selling strategy in existence. Sell a deep-out-of-the-money put: 95% of the time the premium expires worthless and you keep it; 5% of the time the underlying blows through your strike and erases a year of accumulated premium. The structural shape is identical to the coin flip; only the magnitudes change. **Win rate is not edge. Expected value is.**

The trap is *Scenario B*, not premium-selling in general. The CBOE PUT Index — mechanical at-the-money cash-secured monthly put writing on SPX from 1986 forward — has produced *positive* long-run risk-adjusted returns over four decades. Premium selling can be Scenario A or Scenario B depending on strike selection, sizing, roll discipline, and whether the premium collected actually compensates for the tail risk taken. The point is not that selling premium is bad; the point is that a 95% win rate tells you nothing about which scenario you're in.

This is also why the brokerage statements of new premium-sellers look magnificent for their first six to twelve months. The first batch of options expires worthless. The next batch expires worthless. The trader concludes they have discovered a free money machine. The 5% catastrophe hasn't happened yet because 5% events happen about once every twenty trials, and a monthly cadence means roughly twenty months between hits. The trader is sampling from a distribution they have not yet seen the left tail of, and concluding that the left tail doesn't exist.

Anyone who tells you their options-selling strategy has "an 85% win rate" or "a 92% probability of profit" is *telling you about the shape*, not the *edge*. Always ask: what does the average losing trade lose, in dollars, relative to what the average winning trade wins? That ratio, times the win rate, is what determines whether you're in Scenario A or Scenario B.

**The structural bridge to index premium-selling.** When you sell a deep-OTM index put, you've placed a structural bet that the equity skew and the variance risk premium together compensate you sufficiently for the rare tail outcome — and that you'll size and roll the position so the tail outcome doesn't end the game. Notice which assumptions are doing the work: *the premium has to be enough* (an empirical claim about the market — sometimes true, sometimes not), *and your sizing has to survive the tail* (a discipline claim about you, almost always the binding constraint). The Scenario A→B transition is rarely about a sudden change in market behavior; it's about a sudden change in *the trader's behavior* — a doubled position size after a winning streak, a strike moved one band closer to ATM "because vol is high right now," a stop level that wasn't pre-committed in writing. Section 12 (Discipline) returns to this in detail because it is the central practical issue, not Section 5 (Options) which is the technical preamble.

### Jurek and Stafford: most "alpha" is short skew

In a Journal of Finance paper that should be required reading for anyone evaluating a managed-futures or hedge fund pitch, Jakub Jurek (Princeton, NBER) and Erik Stafford (Harvard Business School) examined broad hedge fund index returns from 1996 to 2012 and asked a deceptively simple question: how much of the apparent alpha is real, and how much is just compensation for accepting negative skew that traditional factor models don't see? ([Jurek and Stafford, 2015, *Journal of Finance* 70(5), 2185–2226](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12269))

Their finding, restated in the cleanest possible form: the hedge fund return series is **not reliably distinguishable** from the returns of mechanical S&P 500 put-writing strategies. Once you correctly price the skewed payoffs — using a stochastic discount factor that recognizes downside risk in a way traditional linear models cannot — the apparent 6% to 10% pre-fee annual alpha of hedge fund indices over the 1996–2012 period largely disappears.

> *"Traditional risk factor models indicate that hedge funds capture pre-fee alphas of 6% to 10% per annum over the period from 1996 to 2012. At the same time, the hedge fund return series is not reliably distinguishable from the returns of mechanical S&P 500 put-writing strategies."*
> — Jurek & Stafford (2015), abstract

The implication is uncomfortable. If institutional sophistication — global research teams, prime brokerage relationships, custom risk systems, decades of pedigree, $20 billion AUM — cannot produce a skew-adjusted Sharpe meaningfully above what comes out of mechanical at-the-money put writing on SPX, then the retail trader's prior on "I can do better than put writing through clever entry timing, smart strike selection, or proprietary indicators" should be very, very low. The honest framing is: a retail trader running cash-secured ATM XSP puts with mechanical monthly rolls is operating at roughly the same after-tax expected risk-adjusted return as a sophisticated multi-billion-dollar hedge fund — if both are sized appropriately. Most of what separates the institutional return from the retail one is fees, not skill.

### What to use instead of Sharpe

No single number captures distribution shape. The honest move is to look at multiple metrics together, and to look at the actual historical path the strategy took to produce its returns.

**Sortino ratio.** Like Sharpe, but penalizes only downside volatility:

```
Sortino = (E[R] − r_f) / σ_downside
```

where σ_downside is the standard deviation of returns below some threshold (often zero or the risk-free rate). Sortino fixes one Sharpe defect — it stops penalizing upside surprises as "risk" — but doesn't capture kurtosis or the depth of the left tail.

**Calmar ratio.** Mean annual return divided by maximum drawdown:

```
Calmar = E[R_annual] / |MaxDD|
```

Calmar directly penalizes path-dependent risk. It asks: per unit of pain you had to absorb to participate in this strategy, how much did you get paid? Calmar rankings of strategies often differ sharply from Sharpe rankings. SPX over 1990–2024 has Sharpe around 0.50, Calmar around 0.18. The PUT Index over the same period has Sharpe around 0.65 but Calmar around 0.29. By Sharpe, PUT looks 30% better than SPX. By Calmar, PUT looks 60% better. Both are correct; they're answering different questions, and Calmar is the more honest one for capital-preservation decisions.

**Expected Shortfall (ES) at the 95% or 99% level.** Also called Conditional Value-at-Risk (CVaR):

```
ES_95 = E[R | R ≤ VaR_95]
```

The average loss *conditional on* being in the worst 5% of periods. Where VaR asks "how bad is the 5th percentile loss," ES asks "given that we hit the 5th percentile or worse, how bad is it on average?" ES is the metric Basel III adopted for bank capital after the 2008 crisis precisely because VaR is silent about the magnitude of losses beyond the threshold. For short-vol sizing, ES is the single most useful number you can compute.

**Maximum drawdown.** The largest peak-to-trough loss in the historical record:

```
MaxDD = max_t [ (Peak_t − Trough_t≥t) / Peak_t ]
```

Asymmetric (one-sided), real, and binding for portfolio survival. A 40% drawdown requires a 67% recovery to break even. A 60% drawdown requires a 150% recovery. A 90% drawdown requires 900%. Recovery cost is non-linear in loss size, which is why max-drawdown discipline is binding for portfolio survival: survive small losses and you can compound; survive a single large one and you may never compound back to your prior peak within your lifetime.

**Tail beta.** The strategy's beta to the underlying market *conditional on* the underlying being in its worst 5% of months:

```
β_tail = Cov(R_strategy, R_market | R_market ≤ VaR_market_95) / Var(R_market | R_market ≤ VaR_market_95)
```

For most premium-selling strategies, tail beta is approximately 1.0 — meaning your "diversifier" or "income overlay" fully correlates with everything else in your portfolio precisely when you needed diversification most. The CBOE PUT Index has tail beta near 1.0 to SPX in the worst months. So does most of the "alternatives" allocation in a typical endowment portfolio. This is the empirical content of "all correlations go to one in a crisis."

**Bondarenko's PUT Index analysis: real numbers.** In a Cboe-commissioned white paper, Professor Oleg Bondarenko (University of Illinois Chicago) analyzed the CBOE PUT Index over the 32-year period from June 30, 1986 to December 31, 2018 ([Bondarenko, 2019](https://cdn.cboe.com/resources/education/research_publications/PutWriteCBOE19_v14_by_Prof_Oleg_Bondarenko_as_of_June_14.pdf)). Headline numbers: PUT delivered annualized compound returns of **9.54%** with **9.95%** annualized volatility, producing a Sharpe ratio of **0.65**. Maximum drawdown was **−32.7%**, lasting 40 months. Skew on monthly returns was approximately **−2.09**, several multiples worse than the SPX itself. The PUT Index also delivered a Sortino ratio higher than SPX, MSCI World, Russell 2000, or 30-year Treasury bonds over the same window.

Through 2024, the PUT Index continued to deliver — 2024 calendar year return was 17.8% versus SPX Total Return at 25.0%. Over the 10-year window through September 2025, PUT delivered 8.0% annualized at lower volatility than the index. The strategy works. But understanding *why* it works — that it is paid for accepting negative skew, not for any clever timing — is the prerequisite for sizing it correctly.

### Kurtosis: rare events are not as rare as Gaussian implies

We touched on Black Monday above; it bears returning to in detail because the lesson is structural. On October 19, 1987, the S&P 500 closed down 22.6%. Under a Gaussian model with volatility calibrated to the trailing decade, that event was approximately a 22-sigma move. Sigma counts get unintuitive past about four; here are some benchmarks for orientation:

- 3-sigma event: roughly 1 in 740 (twice per decade)
- 4-sigma event: roughly 1 in 31,500 (once per 125 years)
- 5-sigma event: roughly 1 in 3.5 million (once per 14,000 years)
- 6-sigma event: roughly 1 in 506 million (once per 2 million years)
- 22-sigma event: roughly 1 in 10¹³⁷ (more rare than picking a specific atom in the observable universe at random — twice)

The 22-sigma event happened. So did the 18-sigma move during the 2008 financial crisis, the 14-sigma move on COVID Monday in March 2020, and the 19-sigma single-day VIX move during Volmageddon. These are not flukes against the correct baseline; they are routine against an empirically-calibrated baseline that admits fat tails.

The lesson is not that markets are mysterious or that quants are dumb. The lesson is that **the Gaussian assumption is wrong**. Returns have fat tails. Kurtosis is high. Once-per-century events happen multiple times per career. Any sizing model that assumes Gaussian tails will under-size stress reserves by orders of magnitude. The right starting point is to assume kurtosis between 10 and 20 in your tail model, treat any "30-sigma" event as roughly a "1-in-30-years" event, and size your largest single position so that a 4-standard-deviation move (against the empirical distribution, not the Gaussian one) does not threaten the survival of the account.

This is also why every quantitative risk manager you will ever meet talks about *stress scenarios* rather than *VaR percentiles*. A stress scenario asks "what happens if SPX falls 20% in three days and VIX goes from 15 to 60?" — a concrete, scenario-based question that you can answer with explicit Greek calculations. A VaR percentile asks "what's the 99th percentile loss?" — a question whose answer depends entirely on your assumed tail thickness. The first question survives bad assumptions; the second one is hostage to them.

### The drawdown asymmetry

Let me belabor the recovery math because it is the single most underweighted fact in retail trading. If you lose 40% of your capital, you need a 67% gain on the remaining 60% to get back to even. If you lose 60%, you need 150%. If you lose 90%, you need 900%. The recovery cost is non-linear in loss size, governed by:

```
Recovery_needed = 1 / (1 − DD) − 1

DD = 0.40 → recovery = 0.67 (67%)
DD = 0.50 → recovery = 1.00 (100%)
DD = 0.60 → recovery = 1.50 (150%)
DD = 0.70 → recovery = 2.33 (233%)
DD = 0.80 → recovery = 4.00 (400%)
DD = 0.90 → recovery = 9.00 (900%)
```

This is why max-drawdown discipline is binding for portfolio survival. A strategy with positive expected return but a 60% drawdown that *would have happened anyway in your backtest* requires you to make 150% from the trough to get back to even. At the strategy's normal compound rate, that recovery may take a decade or more. Meanwhile, the opportunity cost of capital sitting in a deep drawdown is the return you could have earned in a simpler, lower-drawdown strategy over those same years. **Survive small losses and you can compound; survive a single large one and you may never compound back to your prior peak within a useful career window.**

This is also why the academic literature distinguishes "drawdown-adjusted" performance metrics from volatility-adjusted ones. A strategy that produces its volatility through small, frequent moves around a rising mean (high Sharpe) is fundamentally different from a strategy that produces the same volatility through occasional catastrophic losses with smooth gains in between (the short-vol shape). The Sharpe ratio reads them the same; Calmar, Sortino, ES, and max drawdown all read them very differently.

### The deflated Sharpe ratio (Bailey and López de Prado)

A more recent contribution to this literature: David Bailey and Marcos López de Prado introduced the **deflated Sharpe ratio** ([Bailey and López de Prado, 2014](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551)) to address a separate Sharpe defect: backtested Sharpe ratios are biased upward, and the bias grows with the number of strategies tested. If you backtest 1,000 strategies, the best one will have a phenomenal Sharpe — purely from selection. The deflated Sharpe corrects for this by computing the probability that the observed Sharpe is statistically distinguishable from zero given (a) the number of trials run, (b) the non-Gaussianity of the returns, and (c) the length of the backtest.

Their empirical finding is sobering: most published "anomaly" Sharpe ratios in the academic literature shrink to indistinguishable-from-zero after deflation. The retail equivalent is even worse: a trader who has spent six months testing parameter combinations on TradingView and finally finds one with a Sharpe of 1.2 over their three-year backtest has run thousands of implicit trials; the deflated Sharpe is almost certainly not significant. Most "discovered" trading systems are statistical artifacts.

### The operational rule

Before sizing any short-vol position, compute its ES₉₅ and its expected behavior in stress scenarios calibrated to SPX −10% / −20% / −35% combined with VIX +10 / +25 / +50 vol-point spikes. The Sharpe is, at best, a third-tier input. The binding questions are:

1. **What is the average loss in the worst 5% of months?** (ES₉₅)
2. **What is the maximum drawdown likely under stress?** (path-dependent risk)
3. **Is the portfolio recoverable from that drawdown without behavioral capitulation?** (survival)

If you cannot answer those three questions in dollar terms for your current portfolio, the position is too big or you don't understand it. Probably both.

### The equity risk premium — the structural reward you're competing with

Everything we've said about Sharpe, tail risk, and the haircut chain sits inside a particular numerical reality: equities have, over the longest data sets available, paid a real risk premium of roughly 4–6% over the risk-free rate, with extreme variation across countries and centuries.

The canonical citations:

- **Mehra and Prescott (1985), "The Equity Premium: A Puzzle," *Journal of Monetary Economics*.** Using US data from 1889 to 1978, Mehra and Prescott documented an average real return on equities of about 7% versus about 1% on short-term debt — a 6 percentage-point premium that traditional consumption-based asset pricing models could not rationalize without implausibly high risk aversion. The "puzzle" framing is decades old; the empirical magnitude has held up remarkably well in subsequent data.

- **Dimson, Marsh, and Staunton, *Triumph of the Optimists* (2002) and ongoing Credit Suisse / UBS Global Investment Returns Yearbook.** DMS extended the dataset to 16+ countries over 100+ years. Their headline number for the global ex-US equity risk premium relative to bills is approximately 4.4% (geometric mean, 1900–present), with substantial cross-country dispersion. Some markets (US, Australia, South Africa) ran higher; others (Italy, Japan, Belgium) were materially lower. There are countries where 50-year equity returns were negative in real terms.

- **Fama and French (2002), "The Equity Premium," *Journal of Finance*.** Argued that the *expected* equity premium, derived from dividend and earnings yields, is closer to 3–4% — meaningfully below the *realized* historical premium, because much of the realized premium came from unexpected valuation expansion (multiple expansion, declining discount rates) that cannot be repeated indefinitely.

**Three operational takeaways:**

1. **The risk premium is real but smaller than retail intuition assumes.** "Stocks return 10% per year" is a rounded nominal pre-tax figure, not the real after-tax post-fee expected return you'll actually compound. The honest expected real after-tax retail figure for a US equity buy-and-hold is roughly 4–5% — meaningfully positive, not a windfall.

2. **The country selection in the data set matters enormously.** The most-cited US-only ERP figures embed a survivorship bias: the US happened to be the *winning* market of the 20th century. The DMS global panel — which includes markets that lost world wars, suffered hyperinflation, were closed by political revolution, or had decades of stagnation — gives a more honest baseline for the *ex-ante* premium an investor in 1900 could have expected.

3. **The competitor for your active strategy is not zero — it's the equity risk premium.** Any active strategy you run has to beat buy-and-hold of a broad equity index *after taxes and fees*, not beat zero. The four-layer retail haircut framework (Section 12A) and the Jurek-Stafford finding above are both pointing at the same operational conclusion: most retail active strategies fail to beat the structural reward already available from passive equity exposure once frictions are honestly accounted for.

The equity risk premium is the baseline against which everything in this book competes. When a strategy claims "edge," the right comparison is not "is this better than nothing?" — it's "is this better than the variance risk premium / equity risk premium combination that I could harvest passively?" That comparison is the operational frame for the rest of the curriculum.

[INTERACTIVE: deflated-sharpe-calculator]

---

## 1B · Log returns and why they're additive

Before we can talk about volatility, expected value, or compounding coherently, we need a return definition that behaves mathematically. The standard simple percentage return — (P_t − P_{t−1}) / P_{t−1} — has a quiet but fatal flaw: it is *asymmetric*. A stock that goes up 20% and then comes back to its starting price has, by simple-return arithmetic, gone up 20% and then down 16.67% — two different magnitudes for what is obviously the same-sized round trip. Professionals use logarithmic returns instead, and the reasons run deeper than mere convenience.

### Two return definitions

```
Simple return:   r_t = (P_t − P_{t−1}) / P_{t−1}

Log return:      r_t = ln(P_t / P_{t−1})  =  ln(P_t) − ln(P_{t−1})
```

These two definitions agree for small moves (they're equal to first order in the Taylor expansion of ln(1+x) ≈ x), but they diverge for large moves and they have fundamentally different mathematical properties.

### Property 1: log returns are symmetric

A stock at $100 goes up to $120, then comes back down to $100. Simple returns describe this as:

```
Up:    (120 − 100) / 100 = +20.0%
Down:  (100 − 120) / 120 = −16.67%
```

Same round trip, two different magnitudes. The asymmetry is real: a 20% gain followed by a 16.67% loss does indeed return to the starting price, because multiplicative returns require a smaller down-percentage to undo a bigger up-percentage. But this asymmetry makes simple returns awkward to reason about.

Log returns describe the same round trip as:

```
Up:    ln(120/100) = +0.1823
Down:  ln(100/120) = −0.1823
```

The same magnitude in opposite directions. Symmetric. Negation. This matters when you're trying to build intuition about volatility — which is, after all, a measure of magnitude irrespective of direction.

[INTERACTIVE: log-return-symmetry]

### Property 2: log returns are additive over time

The multi-period simple return requires chaining multiplications:

```
Total simple return over T periods:
R_total = ∏_{t=1}^{T} (1 + r_t) − 1
```

That's a product, not a sum. Annoying to work with, hard to differentiate, hard to bound, and a nightmare in any time-series statistical analysis.

The multi-period log return is just the sum:

```
Total log return over T periods:
r_total = ln(P_T / P_0) = ∑_{t=1}^{T} ln(P_t / P_{t−1}) = ∑_{t=1}^{T} r_t
```

This is the **additivity property**: total log return is the sum of period-by-period log returns. The proof is one line — a telescoping product of price ratios collapses to a single ratio, and the log of a single ratio is one log. It is the single most useful property in quantitative finance.

Why does additivity matter operationally?

**Volatility scaling becomes clean.** If you assume returns are independent over time, the variance of a sum is the sum of variances, so:

```
σ²_total = ∑_{t=1}^{T} σ²_t
```

If daily log returns have constant variance σ²_daily, then T-day variance is T·σ²_daily, and T-day standard deviation is σ_daily·√T. This is the famous **square-root-of-time rule**. It only works cleanly for log returns under independence.

**Annualization becomes trivial.** Daily log returns annualize as:

```
σ_annual = σ_daily × √252
```

(252 trading days per year). Weekly: ×√52. Monthly: ×√12. These are exact under the independence assumption, not approximations.

**Multi-day stress tests become a clean sum.** If you want to ask "what's the cumulative drawdown over a 5-day stress event?" you sum five log returns. With simple returns you'd be compounding (1+r) terms, which produces convexity errors when the moves are large — exactly when you most want the answer to be accurate.

**Distributional assumptions become natural.** The classical Black-Scholes model assumes asset prices follow geometric Brownian motion, which in continuous time means log returns are normally distributed. Under that assumption, the sum of independent normals is normal — so the T-period log return is also normal, with mean Tμ and variance Tσ². No correction. With simple returns, the sum of percentage returns is not even well-defined as a distribution under most reasonable models.

### The Itô correction (a preview)

There's a subtle point that becomes important in Section 7. If a stock's instantaneous return is normally distributed with mean μ_dt and variance σ²·dt, the *instantaneous log return* is NOT normal with mean μ·dt — it's normal with mean (μ − ½σ²)·dt. The −½σ² term is called the **Itô drift correction** or **variance drag**. It arises because the log function is concave: when you log-transform a random variable, you don't just transform the mean by ln(mean) — you also pick up a negative term proportional to variance.

The practical implication: a stock with 10% expected simple return per year and 20% volatility has expected log return of only:

```
E[ln(1+r)] ≈ μ − ½σ² = 0.10 − 0.5 × 0.04 = 0.08 = 8%
```

The 2% gap between expected simple return and expected log return is variance drag. It's the reason that, all else equal, lower-volatility strategies compound to higher terminal wealth than higher-volatility strategies *with the same arithmetic mean return*. This is also the mathematical engine behind the Kelly criterion, which we'll cover in 1C and 2E.

> *Variance drag is why a sequence of returns +50%, −50%, +50%, −50%, … ends in ruin even though the arithmetic mean is zero. The geometric mean — which is what compounding actually delivers — is √(1.5 × 0.5) − 1 = −13.4% per pair.*

[INTERACTIVE: variance-drag-explorer]

### The convention

For the rest of this book, "return" means log return unless otherwise stated. Volatility, Sharpe ratio, variance, drift — all of them assume log returns under the hood. When you see σ_daily × √252 to annualize, that's a log-return convention. When you see a derivation of Black-Scholes invoking dS/S = μ·dt + σ·dW, recognize that as a statement about log returns. Almost every formula in derivatives pricing is more natural in log space.

The one place where simple returns persist is in reporting to non-quant audiences: clients want to hear "the strategy returned 12% this year," not "log return of 0.1133." That's fine. Translate at the boundary, not in the middle of your math.

---

## 1C · Expected value and the definition of edge

Edge is not a feeling. It is not a story. It is not "I really think this stock is going up." Edge is a number — the expected value of a trade or strategy, net of all costs, after appropriate discounting for risk. The most important consequence of taking expected value seriously is the one we previewed in 1A: **a strategy that wins the majority of the time can still lose money, and a strategy that wins less than half the time can make money**. Win rate is correlated with edge but not identical to it. The retail bias toward strategies with high "probability of profit" is a bias toward shapes that *feel* like edge but may not contain any.

### The definition

For a single bet or trade with discrete outcomes:

```
E[X] = ∑_i p_i × x_i
```

For a binary bet — wins amount G with probability p, loses amount L with probability 1−p, costs c upfront:

```
E[X] = p × G − (1 − p) × L − c
```

The trade has edge if and only if E[X] > 0. If E[X] = 0 the trade is "fair." If E[X] < 0 you are paying for the privilege of playing.

### Two famous coin flips

These two examples are foundational in quant trading curricula and worth committing to memory.

**Coin flip 1.** Probability 0.55 of winning $1, probability 0.45 of losing $1.25.

```
E[X] = 0.55 × 1 − 0.45 × 1.25 = 0.55 − 0.5625 = −$0.0125 per round
```

Win rate is 55% — better than even! Expected value is *negative* — about a penny and a quarter lost per round. Play this game enough times and you go broke for sure. The high win rate masks the asymmetric payoff structure that makes the bet unprofitable.

**Coin flip 2.** Probability 0.25 of winning $35, probability 0.75 of losing $1.

```
E[X] = 0.25 × 35 − 0.75 × 1 = 8.75 − 0.75 = +$8.00 per round
```

Win rate is 25% — three losses out of every four bets! Expected value is *massively positive*. This is the shape of a long out-of-the-money option, of a venture capital portfolio, of a discretionary trader who takes many small losses chasing rare large wins. It looks awful on a day-to-day basis. It is fantastic.

[INTERACTIVE: ev-bet-builder]

### Why edge is the foundation of everything

Risk management, position sizing, and discipline (Section 12) keep you in the game. They cannot manufacture edge. **If your underlying expected value is negative, perfect discipline just means losing money more methodically.** This is the single most important sentence in this entire document, and I will repeat it in different forms throughout. The framework that follows in later chapters — dealer mechanics, regime classification, conviction scoring, kill rules — assumes you have an EV-positive process. The framework exists to keep an edge from being destroyed by behavior, fees, taxes, and bad sizing. It does not create edge where none exists.

### The expected utility correction

The plain expected value calculation above implicitly assumes you have linear utility of wealth — that gaining $1,000 and losing $1,000 are equal in impact. This is approximately true for small bets relative to your wealth and approximately false for large bets. Real people have *concave* utility: a $1,000 gain when you have $50,000 in the bank is more impactful than a $1,000 gain when you have $5 million. Equivalently, a $1,000 loss hurts more than a $1,000 gain feels good — that's just concavity of utility expressed in symmetric form.

The mathematical formalization is **expected utility theory** (von Neumann and Morgenstern, 1944), which says rational decision-makers should maximize:

```
E[U(W)] = ∑_i p_i × U(W_i)
```

where U is some concave utility function and W is wealth. The most-used utility function in finance is logarithmic:

```
U(W) = ln(W)
```

Log utility has a special property: the bet size that maximizes expected log utility is **the Kelly criterion bet size**, which we'll meet in 2E. Log utility is also the natural utility function for compound-growth investors, because maximizing expected log return is equivalent to maximizing expected compound growth rate. For an investor with a multi-decade horizon and no consumption needs in the near term, log utility is approximately the right utility function.

The practical implication: when computing expected value for sizing purposes, you should be computing expected *log* return on the portfolio, not expected dollar return. A trade that has +$10,000 expected value on a $100,000 portfolio is great. A trade that has +$10,000 expected value on a $100,000 portfolio but a 5% chance of losing $80,000 has expected dollar value of about $10,000 but expected log return that is *negative* — because losing 80% of the portfolio crushes the log of remaining wealth far more than the +$10,000 gains help it. Log utility automatically penalizes catastrophic outcomes; dollar expected value does not.

### Where this connects to options

Every options strategy can be — must be — evaluated by its expected value, decomposed by component. A short ATM put has positive expected gross premium minus the expected payout under exercise minus transaction costs minus the expected cost of margin financing. A long calendar spread has positive expected gain from forward-vol re-pricing minus the cost of the calendar setup minus the expected loss from the underlying moving against the position. Every line in a brokerage statement is a sample drawn from a distribution, and the question is always: is the mean of that distribution positive after costs?

This is also why most options education content fails: it teaches you the *shape* of a strategy (the payoff diagram) without teaching you how to evaluate whether the strategy has positive EV in the current market. A payoff diagram tells you nothing about edge. The payoff diagram of a short iron condor is identical to the payoff diagram of a long lottery ticket — limited risk, limited reward, in opposing geometries — and one has negative expected value while the other has positive expected value, depending on whether implied vol is over- or under-pricing realized vol. Edge is what determines outcome. Geometry tells you about path, not about edge.

---

## 1D · Sharpe ratio — return per unit of risk

Now that we have expected value as the foundation, the next question is: how *stable* is that expected value? A strategy that earns 10% per year with 5% annual volatility is different from a strategy that earns 10% per year with 30% volatility. The Sharpe ratio formalizes this question: it is the ratio of expected excess return to the standard deviation of returns, and it answers "how many units of risk does this strategy ask me to take for each unit of expected return?"

### The definition

```
SR = (E[R] − r_f) / σ_R
```

The numerator is excess return — what you earned above the risk-free rate. The denominator is the standard deviation of those returns. By construction, Sharpe is dimensionless and scale-invariant: doubling your position size doubles both the numerator (return) and the denominator (volatility), leaving Sharpe unchanged. This is what makes Sharpe useful as a *comparison* metric across strategies of different sizes.

For short-horizon intraday strategies — the regime most quant trading chapters in Sections 2 and below will assume — the risk-free rate is negligible per-bar, so the practical form drops it:

```
SR_intraday ≈ E[R] / σ_R
```

The annualization follows the square-root-of-time rule from 1B. A strategy with Sharpe = X computed on daily returns has annualized Sharpe of approximately X × √252:

```
SR_annual = SR_daily × √252 ≈ SR_daily × 15.87
```

This is the famous "Sharpe scales with square root of frequency" relationship, and it's the structural reason high-frequency strategies report eye-popping Sharpes (we'll see this in 2E).

### What Sharpe gives you that EV alone doesn't

Two strategies can have identical expected return but very different Sharpes if their volatilities differ. The lower-volatility strategy is preferable for three concrete reasons:

**1. Compound growth is higher.** From the Itô correction in 1B, expected log return is approximately μ − ½σ². For two strategies with identical arithmetic mean μ, the one with lower σ² compounds to higher terminal wealth. Variance drag is real money over multi-year horizons.

**2. Leverage becomes safe.** A strategy with Sharpe of 0.5 cannot safely be leveraged 4×, because the 4× leveraged version still has Sharpe of 0.5 but has 4× volatility, meaning routine drawdowns become catastrophic. A strategy with Sharpe of 4.0 (typical of intraday market-making) can be safely leveraged 4× because the volatility was small to start with and the drift was overwhelming. The maximum sustainable leverage is, roughly, a function of how confident you are that the next move is positive — which is what Sharpe measures.

**3. Behavioral survivability improves.** A strategy that wins 51% of trades with tight bounds and high Sharpe feels safe to operate. A strategy that wins 51% of trades with wide bounds and low Sharpe feels terrifying — you have long losing streaks, you can't tell in real time whether the strategy is working or just lucky, and you'll likely abandon it during a drawdown. The path of a high-Sharpe strategy is psychologically easier to ride than the path of a low-Sharpe strategy with identical expected return.

[INTERACTIVE: sharpe-curves]

### The frequency-Sharpe relationship

Here is one of the most important and least-understood facts in quant trading: if you have a tiny edge per trade — say, a 51% win rate at fixed sizing — you don't want to trade it once. You want to trade it many times. The reason is that the Sharpe of a strategy scales as the square root of the number of independent bets:

```
SR_N ≈ SR_1 × √N
```

A strategy with per-trade Sharpe of 0.05 (a tiny edge) traded once a day produces daily Sharpe of 0.05. The same strategy executed 10 times a day with independent outcomes produces daily Sharpe of approximately 0.05 × √10 ≈ 0.16. Executed 100 times a day, daily Sharpe of 0.50. The annualization (×√252) then gives annual Sharpes of 0.8, 2.5, and 7.9 respectively. Trading frequency turns a tiny per-trade edge into a high Sharpe — which then permits leverage and compounding to do their work.

This is the structural reason a Renaissance Technologies-style high-frequency strategy can produce double-digit annual Sharpes on a 51-52% win rate. It is not that each bet is highly profitable. It is that each bet is *slightly* profitable and there are tens of thousands of bets per day. The same edge, traded once a year, would be statistically indistinguishable from luck and certainly unsafe to leverage.

The retail implication is sobering: most retail strategies operate at frequencies of one to ten trades per month. Even if each trade has a real edge (which most don't), the resulting Sharpe is going to be modest, leverage is going to be constrained, and the compound growth is going to be slow. There is a fundamental advantage to high frequency that retail traders cannot match — and trying to overcome it by adding leverage to a low-frequency strategy is exactly the path to ruin that Sections 12A and 12C will repeatedly warn against.

### Why low Sharpe caps leverage

Let me make the leverage point quantitative. Suppose your strategy has annualized Sharpe SR and you lever it by factor k. The levered strategy has:

- Expected return: k × E[R]
- Volatility: k × σ
- Sharpe: still SR (leverage doesn't change Sharpe)

But the *probability of ruin* — the probability that the levered equity curve hits zero or some pre-defined floor before reaching its long-run drift — scales with both leverage and Sharpe. For a continuous Geometric Brownian Motion model, the probability that the equity curve ever falls to fraction f of its starting value before going to infinity is approximately:

```
P(ruin to fraction f) ≈ f^(2μ/σ²)
```

where μ and σ are the drift and volatility *of the levered strategy*. Levering up multiplies both μ and σ by k, but σ² is multiplied by k², so the ratio 2μ/σ² gets *divided* by k. Higher leverage = lower exponent = ruin probability gets closer to 1.

The practical consequence: a Sharpe-0.5 strategy levered 4× has effective μ/σ² that produces ruin probabilities approaching unity over long horizons. A Sharpe-4.0 strategy levered 4× still has comfortable survival probabilities because the underlying drift-to-variance ratio was so high. **Sharpe sets the leverage ceiling.** No amount of clever risk management overrides this.

### Sortino, Information Ratio, and the Sharpe family

The basic Sharpe ratio has several variants worth knowing:

**Sortino ratio.** Same formula but uses downside-only standard deviation:

```
Sortino = (E[R] − r_f) / σ_downside
```

where σ_downside is computed only from returns below some threshold (often zero or r_f). Sortino correctly recognizes that upside volatility is not "risk" — nobody complains about big gains. Sortino is higher than Sharpe for any strategy with positive skew and lower than Sharpe for negative-skew strategies. The CBOE PUT Index has Sortino approximately equal to Sharpe (because most PUT volatility is downside volatility — there's not much upside surprise in collecting fixed premium). SPX has Sortino noticeably higher than Sharpe (because some of SPX's volatility comes from upside surges).

**Information Ratio.** Same idea but excess return is measured against a benchmark instead of the risk-free rate:

```
IR = (E[R_strategy] − E[R_benchmark]) / σ(R_strategy − R_benchmark)
```

The denominator is the volatility of the *tracking error* — the variation of strategy returns relative to benchmark. IR is the right metric for active portfolio managers who are evaluated against a benchmark and care about how much active risk they take to produce active return.

**Treynor ratio.** Excess return divided by beta instead of standard deviation:

```
Treynor = (E[R] − r_f) / β
```

Used when you assume idiosyncratic risk can be diversified away and only systematic (market) risk matters. Less common in modern practice because the CAPM-style assumptions it relies on don't hold well empirically.

**Calmar ratio.** Already covered in 1A — annual return divided by maximum drawdown. The most honest single-number metric for capital-preservation-focused strategies.

### The probabilistic Sharpe ratio

A subtle and important variant: how confident are you that the *true* Sharpe of your strategy exceeds some threshold, given the finite sample you've observed? The **probabilistic Sharpe ratio (PSR)**, also from Bailey and López de Prado, answers this:

```
PSR(SR*) = Φ( (SR_observed − SR*) × √(T − 1) / √(1 − γ_3·SR_observed + (γ_4 − 1)/4 × SR_observed²) )
```

where T is the number of observations, γ_3 is sample skewness, γ_4 is sample kurtosis, and Φ is the standard normal CDF. The PSR explicitly corrects the standard error of the observed Sharpe for skewness and kurtosis — which, as we established in 1A, are the moments Sharpe ignores. Strategies with negative skew (premium selling) have *wider* PSR confidence intervals than strategies with the same observed Sharpe but symmetric returns. The same observed Sharpe is less reliable when the underlying distribution is skewed against you.

This connects everything in Section 1 to a single statistical reality: not only does Sharpe under-report tail risk, but the *estimate* of Sharpe is less reliable when there is more tail risk. Both errors push in the same direction. Both flatter premium-selling strategies. Both inflate retail trader confidence. Be humble about Sharpe estimates from short backtests of skewed strategies.

### What this enables next

Section 2 (Quant Trading) is where the foundations laid in Section 1 become operational. Building a model with a tiny positive edge per prediction is step one. The edge only becomes meaningful when executed many times so the Sharpe rises and leverage becomes usable. That's the unit of analysis from here on. Section 3 then establishes *what* you can trade — the specific products that exist in the SPX/SPY/options complex, and why product choice (especially the tax treatment of XSP vs SPY) is the most consequential operational decision a US retail trader makes.
