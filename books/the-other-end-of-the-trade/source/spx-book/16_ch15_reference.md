# Chapter 15 — Reference
## Glossary, reading list, math summary card

> **Purpose.** This chapter is for looking up specifics later. It's not designed to be read end-to-end. The glossary defines terms used throughout the book; the reading list points to primary sources; the math card summarizes the equations on one page.

---

## 15.1 Glossary

### A
- **Alpha:** return in excess of a benchmark, after controlling for known risk factors. In practice, what most people call "alpha" is actually compensation for negative skew (Jurek-Stafford 2015).
- **Annualized:** scaled to a one-year basis. Multiply daily by ~252, weekly by ~52, monthly by 12. Vol scales by square root of these.
- **Asymmetry:** see *skew*.

### B
- **BAB (Betting-Against-Beta):** factor strategy that buys low-beta stocks levered up and shorts high-beta stocks. Frazzini-Pedersen 2014 reported Sharpe 0.78 (US); Novy-Marx-Velikov 2022 show value-weighted version ~0.49.
- **Backwardation:** when the front month of a futures curve trades above the back month. For VIX, ratio > 1 indicates stress.
- **Behavioral edge:** return predictability arising from systematic mispricing by investors. Decays post-publication (~47% per Jensen-Kelly-Pedersen 2023).
- **Beta:** sensitivity to a benchmark. Equity beta of 1.0 = moves with SPX; 0.5 = half as much; -0.3 = inversely.

### C
- **Calmar ratio:** return / max drawdown. Better than Sharpe for path-dependent strategies.
- **Carry:** the return assuming no price change. High-yield assets earn more carry than low-yield. Cross-asset carry has documented Sharpe ~0.6-0.9 (Koijen et al. 2018).
- **Category (in this book):** one of five — foundation, factor, overlay, filter, rejected. Determines sizing and operational rules.
- **CDaR (Conditional Drawdown at Risk):** average drawdown beyond the α percentile.
- **CNDR (Cboe Iron Condor Index):** systematic iron condor on SPX. ~690% return 1986-2024 vs ~5500% for SPX TR — empirically underperforms.
- **Conditional drawdown:** see *CDaR*.
- **Conviction score:** $C = E \times M \times R \times X \times S$ from Chapter 4. Multiplicative across evidence, mechanism, regime, execution, sizing.
- **Contango:** front month below back month. For VIX, ratio < 1 indicates calm.
- **Correlation, tail:** correlation conditional on extreme events. Often dramatically different from unconditional correlation.

### D
- **Decay (factor):** the post-publication reduction in factor returns. Median ~47% (Jensen-Kelly-Pedersen 2023).
- **Defined-risk spread:** option spread with capped max loss. Doesn't eliminate path risk or margin expansion.
- **Delta:** sensitivity of option price to underlying. 30-delta put has ~30% chance of finishing ITM (rough heuristic).
- **DBMF, KMLM, RSST:** trend-following ETFs. DBMF is replication-style, KMLM is fixed asset universe, RSST is return-stacked.
- **Drawdown:** peak-to-trough loss. MaxDD = largest historical.

### E
- **EOQ (End-of-Quarter):** rebalancing flow from 60/40 mandates. NBER 2024 documents predictable equity-return effects.
- **ERP (Equity Risk Premium):** expected return of equities over bonds. Long-run realized US ~5-7%; forward implied (Damodaran 2025) ~4.3%.
- **ES (Expected Shortfall):** average loss conditional on being in the worst α tail. ES_95 = average loss in worst 5%.
- **ETP (Exchange-Traded Product):** broader term than ETF; includes notes (ETN). VIX ETPs (VXX, UVXY) are ETNs with structural decay.
- **Evidence tier:** T1 (peer-reviewed, replicated), T2 (strong empirical), T3 (thin or decayed).

### F
- **Factor:** systematic source of equity returns. Quality, momentum, value, low-vol, size.
- **Filter:** regime indicator used to size other strategies. NOT a trade.
- **Fed put:** market belief that the Fed will cut rates / provide liquidity in stress, reducing tail risk on equity.
- **FOMC cycle:** Cieslak et al. 2019 finding that equity premium is concentrated in even weeks of the FOMC cycle.
- **Foundation premium:** durable risk premium that anchors the portfolio. ERP, VRP, trend, carry.

### G
- **Gamma:** sensitivity of delta to underlying price. Long gamma = profit from movement; short gamma = loss from movement.
- **GEX (Gamma Exposure):** estimated dealer net gamma. Public models depend on assumptions about dealer positioning that are not robustly validated post-2022. Cboe 2025 estimated 0DTE MM hedging is ~0.2% of liquidity.

### H
- **Haircut (retail):** the cumulative reduction from academic Sharpe to user-account Sharpe. Typically 30-60%.
- **HML (High-Minus-Low):** Fama-French value factor. Long high B/M, short low B/M.

### I
- **IBS (Internal Bar Strength):** technical indicator = (close-low)/(high-low). Used in mean-reversion archetypes.
- **Implied volatility (IV):** market-implied future vol from option prices.
- **Institutional friction:** mandate-driven flow that creates predictable patterns. Source 3 in Chapter 1.

### J
- **Jurek-Stafford (2015):** key paper showing hedge fund returns are indistinguishable from put-write after pricing skew. Required reading.

### K
- **Kill criterion:** pre-committed rule that halts a strategy or sleeve when triggered. Three levels: per-strategy, sleeve, portfolio.
- **Kurtosis:** fourth moment of distribution, measuring tail fatness. Normal = 3; SPX daily ~18.

### L
- **LEAP (Long-term Equity AnticiPation Securities):** options with expirations >1 year out.
- **Leverage:** ratio of total exposure to capital. Cheapest via box spread financing or futures; most expensive via options.

### M
- **MAE (Maximum Adverse Excursion):** worst MTM loss during a trade's life. Often larger than terminal loss.
- **Margin (Reg-T vs Portfolio Margin):** Reg-T is fixed-percentage; PM is stress-tested theoretical loss. PM expands non-linearly in stress.
- **MFE (Maximum Favorable Excursion):** best MTM gain during a trade's life.
- **Microstructure:** edges at the order-book level. Typically institutional-only for retail.
- **Momentum:** trend-following at single-stock level. Cross-sectional or time-series.
- **MOVE:** ICE BofA Treasury MOVE Index. >130 = bond stress.
- **MTM (Mark-to-Market):** current value of a position vs entry.

### N
- **Negative skew:** distribution leans left. Frequent small gains, rare large losses. Characterizes all premium-selling.

### O
- **OPEX:** options expiration. Monthly (3rd Friday) is the largest.

### P
- **Path dependency:** when MTM trajectory matters as much as terminal payoff. Most options strategies are path-dependent.
- **PEAD (Post-Earnings Announcement Drift):** behavioral edge from under-reaction to earnings news.
- **PUT (Cboe PUT Index):** systematic ATM monthly put-write benchmark. 1986-2024 Sharpe ~0.65.
- **PUTW:** ETF tracking the PUT index. Changed strategy in 2023 (moved to weekly options).

### Q
- **QMJ (Quality Minus Junk):** Asness-Frazzini-Pedersen quality factor.
- **Quality:** factor based on profitability, stability, safety, payout.

### R
- **Realized volatility:** ex-post measured vol over a window. 21-day commonly referenced.
- **Regime filter:** see *filter*.
- **Risk premium:** compensation for bearing non-diversifiable risk. Source 1 in Chapter 1.

### S
- **Selectivity:** the principle that high-quality trades come from explicitly choosing not to trade most of the time. Beats activity in retail data.
- **Setup card:** one-page operational summary of a strategy (Chapter 12).
- **Sharpe ratio:** $\frac{E[R-r_f]}{\sigma}$. Misleading for non-Gaussian (especially short-vol) strategies.
- **Skew:** third moment of distribution, measuring asymmetry. SPX daily ~-0.7; PUT index ~-2.09.
- **Sortino ratio:** Sharpe with downside-only volatility in denominator.
- **Source (in this book):** one of four — risk premium, behavioral, institutional, microstructure (Chapter 1).
- **SPX, XSP:** S&P 500 index options (full-size and mini, respectively). Both have 1256 60/40 tax treatment.

### T
- **TED spread:** 3M LIBOR (now SOFR proxy) – 3M T-bills. Funding stress indicator.
- **Theta:** option time decay.
- **Trend-following:** systematic trend strategy across asset classes. Hurst-Ooi-Pedersen 2017 documents 140-year evidence.
- **TSMOM (Time-Series Momentum):** trend-following formalism. Moskowitz-Ooi-Pedersen 2012.

### V
- **Value:** factor based on price-to-fundamental ratios. 2010-2020 was the worst documented value drawdown in modern history.
- **VaR (Value at Risk):** percentile loss threshold. 95% VaR = loss exceeded 5% of the time.
- **Vega:** sensitivity to implied volatility.
- **VIX, VIX3M:** 30-day and 3-month implied vol indices. Ratio is the key term-structure filter.
- **VRP (Variance Risk Premium):** difference between implied and realized variance. Long-run positive, often ~80% of months.

### W
- **Whipsaw:** rapid reversals that produce losses in trend-following strategies.

### X
- **XSP:** mini-SPX options. 1/10th the size of SPX. 1256 tax. Preferred retail vehicle for systematic put-write.

---

## 15.2 Reading list (primary sources)

### Foundational papers (read these)
- **Mehra & Prescott (1985)** "The Equity Premium: A Puzzle." *JME* 15:145-161.
- **Jegadeesh & Titman (1993)** "Returns to Buying Winners and Selling Losers." *JF* 48:65-91.
- **Fama & French (1993)** "Common Risk Factors in the Returns on Stocks and Bonds." *JFE* 33:3-56.
- **Carr & Wu (2009)** "Variance Risk Premiums." *RFS* 22:1311-1341.
- **Asness, Moskowitz & Pedersen (2013)** "Value and Momentum Everywhere." *JF* 68:929-985.
- **Frazzini & Pedersen (2014)** "Betting Against Beta." *JFE* 111:1-25.
- **Jurek & Stafford (2015)** "The Cost of Capital for Alternative Investments." *JF* 70:2185-2226. **Required reading for VRP.**
- **Daniel & Moskowitz (2016)** "Momentum Crashes." *JFE* 122:221-247.
- **Hurst, Ooi & Pedersen (2017)** "A Century of Evidence on Trend-Following Investing." *JPM* 44:15-29.

### Critical updates and corrections
- **Asness, Frazzini, Israel, Moskowitz & Pedersen (2018)** "Size Matters, If You Control Your Junk." *JFE* 129:479-509.
- **Cieslak, Morse & Vissing-Jorgensen (2019)** "Stock Returns Over the FOMC Cycle." *JF* 74:2201-2248.
- **Bondarenko (2014)** Cboe PUT Index empirical analysis.
- **Asness, Frazzini & Pedersen (2019)** "Quality Minus Junk." *RAS* 24:34-112.
- **McLean & Pontiff (2016)** "Does Academic Research Destroy Stock Return Predictability?" *JF* 71:5-32.
- **Arnott, Harvey, Kalesnik & Linnainmaa (2021)** "Reports of Value's Death May Be Greatly Exaggerated." *JPM*.
- **Kurov, Sancetta, Strasser & Wolfe (2021)** documents pre-FOMC drift decay post-2015.
- **Novy-Marx & Velikov (2022)** "Betting Against Betting Against Beta." *JFE*.
- **Jensen, Kelly & Pedersen (2023)** "Is There a Replication Crisis in Finance?" *JF*. ~47% post-publication decline.
- **Greenwood & Sammon (2024)** S&P 500 inclusion premium decay.
- **Bakshi, Crosby & Gao (2024)** "Disaster-Sensitive Portfolios." *Math Finance*.

### Practitioner / data sources
- **Damodaran**, NYU Stern, ERP updates: pages.stern.nyu.edu/~adamodar
- **Dimson-Marsh-Staunton**, UBS Yearbook (annually)
- **Cboe research**: cboe.com/insights — VRP, 0DTE studies
- **AQR Insights**: aqr.com — practitioner-quality factor research

### Books worth owning
- **Pedersen, *Efficiently Inefficient*** — practitioner framework
- **Asness et al., AQR Insights collected** — readable factor essays
- **Bouchaud & Potters, *Theory of Financial Risk*** — quantitative
- **Sinclair, *Volatility Trading* (2nd ed)** — practitioner options vol
- **Kelly et al. (eds), *Recent Advances in Financial Engineering*** — research compilation

---

## 15.3 Math summary card

The recurring equations from the book, on one page:

### Distribution moments
$$\mu = E[R], \quad \sigma^2 = E[(R-\mu)^2]$$
$$\text{Skew} = E\left[\left(\frac{R-\mu}{\sigma}\right)^3\right], \quad \text{Kurt} = E\left[\left(\frac{R-\mu}{\sigma}\right)^4\right]$$

### Expected value
$$E[R] = pG - (1-p)L - c$$

### Sharpe ratio
$$\text{SR} = \frac{E[R - r_f]}{\sigma_R}$$

### Sortino ratio
$$\text{Sortino} = \frac{E[R - r_f]}{\sigma_\text{downside}}$$

### Calmar ratio
$$\text{Calmar} = \frac{E[R]}{\text{MaxDD}}$$

### Tail loss (Expected Shortfall)
$$\text{ES}_\alpha = E[L \mid L > \text{VaR}_\alpha]$$

### Retail-realism haircut
$$\text{SR}_\text{user} = \text{SR}_\text{paper} \times h_1 \times h_2 \times h_3 \times h_4$$
typical product 0.30-0.60.

### Portfolio variance
$$\sigma_p^2 = \mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}$$

### Risk contribution of sleeve i
$$RC_i = w_i \cdot \frac{(\Sigma w)_i}{\sigma_p}$$

### Conviction score
$$C_i(t) = E_i \times M_i \times R_i(t) \times X_i(t) \times S_i$$
threshold: C ≥ 0.5 = high conviction.

### Conviction threshold (long form)
$$\text{Trade only if } \hat{\mu}_\text{net} - \lambda \cdot \text{ES}_{95} - \kappa \cdot C_\text{exec} > 0$$

### Position sizing from loss budget
$$n \leq \left\lfloor \frac{B_\text{exp}}{L_\text{max}} \right\rfloor$$

### VRP
$$\text{VRP}_t = \text{IV}_t^2 - E_t[\text{RV}_{t,T}^2]$$

### VIX term structure filter
$$\text{Term ratio}_t = \frac{\text{VIX}_t}{\text{VIX3M}_t}$$
- > 1.05 for 3 days → halt new short-vol entries
- > 1.10 for 3 days → reduce short-vol 50%
- < 1.00 for 5 days → phased re-entry

### Carry
$$\text{Carry}_{i,t} = \frac{F_{i,t} - S_{i,t}}{S_{i,t}}$$

---

## 15.4 The four-source / five-category mapping (one-page)

| Source ↓ / Category → | Foundation | Factor | Overlay | Filter | Rejected |
|---|---|---|---|---|---|
| **Risk premium** | ERP, VRP, Trend, Carry | (some quality) | — | — | — |
| **Behavioral** | — | Momentum, Value, (some quality) | (some) | — | naive earnings, GEX scalping |
| **Institutional** | — | BAB | EOQ rebalance, FOMC cycle | — | S&P inclusion |
| **Microstructure** | — | — | (OPEX partial) | Dealer gamma sign | GEX-level scalping |

---

## 15.5 The five-question stress test (one-page)

Before allocating to any strategy:

1. **What's my tail loss?** Specifically, ES₉₅ — average loss in the worst 5% of months.
2. **What's the margin expansion under stress?** Run through SPX -20 / VIX +25.
3. **Can I hold to expiry?** If the position MTMs to -X% in 30 days, would I be force-closed?
4. **Is the premium adequate compensation for the skew?** Apply the 30-50% Sharpe haircut.
5. **What's the kill criterion?** Specific, measurable, pre-committed.

If you can't answer all five, the position is too big or you don't understand it well enough.

---

## 15.6 The 13-item trade admission checklist (one-page)

- [ ] Source identified (one of four)
- [ ] Category assigned (one of five)
- [ ] Evidence tier (T1 / T2 / T3) with primary source cited
- [ ] Mechanism stated (why does this work?)
- [ ] Academic Sharpe documented
- [ ] Retail haircut applied → realistic user-account Sharpe
- [ ] Regime check (current state supportive?)
- [ ] Tail loss calculated (ES_95, S2, S3 P&L)
- [ ] Margin behavior under stress
- [ ] Position size survivable in S2 and recoverable in S3
- [ ] Kill criteria specified, measurable, pre-committed
- [ ] Correlation to existing book in stress
- [ ] Conviction score $C \geq 0.5$

---

## 15.7 The four scenarios (one-page)

For every portfolio and every sleeve, test:

- **S1:** SPX -10%, VIX +10
- **S2:** SPX -20%, VIX +25
- **S3:** SPX -35%, VIX +50
- **S4:** 1987-style overnight gap

Sleeve must be operational in S2 and recoverable in S3. If not, resize.

---

## 15.8 Closing thought

This book is a *thinking framework*, not a prediction. The literature will update; some edges in here will decay; some currently-rejected ideas will be re-validated. The framework — sources, categories, conviction score, haircut equation, kill criteria, monitoring cadence — is more durable than any specific edge.

The two-line operational summary:

> **Before allocating to any new "edge," classify its source (1 of 4) and its category (1 of 5). Score conviction (E × M × R × X × S). Apply the haircut. Stress-test S1-S4. Specify the kill criterion. Then size for survivability.**

If you do this consistently, you'll filter 80% of retail trading content as low-conviction or rejected, and the remaining 20% will be sized appropriately to anchor a multi-decade portfolio.

That is the book in one paragraph.

[← Previous: Chapter 14 — Portfolio framework](15_ch14_portfolio_kill.md) | [Back to Home →](index.md)
