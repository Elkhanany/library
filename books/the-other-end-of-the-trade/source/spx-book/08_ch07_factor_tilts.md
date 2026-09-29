# Chapter 7 — Equity factor tilts
## Quality, momentum, value, low-vol, size

> **Core intuition.** Factor tilts modulate the equity sleeve to capture documented systematic excess returns. Each factor has a different mechanism, different decay risk, and different drawdown profile. Most factors had their best decade in academic papers; live retail experience is humbler. They're worth allocating to in moderate amounts as tilts (not concentrations), but require multi-decade patience to harvest.

---

## 7.1 Quality / Profitability (RMW, QMJ)

### Core intuition
Profitable, stable, growing companies with conservative investment have outperformed unprofitable, volatile, declining ones. The mechanism is partly behavioral (investors over-extrapolate growth in junky names) and partly risk-premium-related (quality companies have lower distress risk).

### Toy example
Two stocks: Stock A has 25% return on equity, stable margins, conservative balance sheet. Stock B has volatile earnings, growth-story narrative, leveraged balance sheet. Stock B trades at 10× P/E, Stock A at 18×. Empirically, Stock A outperforms over 5+ year periods because B's "growth story" tends to disappoint while A keeps compounding.

### Formal object
Quality is multi-dimensional. Asness-Frazzini-Pedersen (2019, *RAS*) define QMJ around four pillars:
- **Profitability:** gross profits / assets, ROA, ROE
- **Growth:** stability and rate of profit growth
- **Safety:** low beta, low leverage, low earnings volatility
- **Payout:** stable dividends and buybacks

Long high-quality, short junky stocks → QMJ factor.

### Evidence
- **Novy-Marx (2013, *JFE*)** "The Other Side of Value: The Gross Profitability Premium" — won 2013 Fama-DFA Prize
- **Asness-Frazzini-Pedersen (2019)** QMJ — alpha 0.66%/month US, 0.45% global; ~24 countries
- **Quality was the single factor that did not crash through the 2017-2022 value drawdown** — a key real-world test

### Why it exists
Mixed mechanism:
- **Risk premium component:** quality firms have lower distress risk; investors might rationally pay a premium for safety
- **Behavioral component:** investors over-pay for narrative growth, under-pay for boring profitability

The mixed source explains why quality has held up better than pure-behavioral factors. Some of the premium is risk-based and won't decay; some is behavioral and might.

### Retail implementation
- **QUAL** (iShares MSCI USA Quality, 0.15% expense): tracks MSCI Quality Index
- **COWZ** (Pacer US Cash Cows 100, 0.49%): high free cash flow yield, more concentrated
- **DGRO** (iShares Core Dividend Growth): proxy via dividend stability
- **Haircut:** academic 0.4-0.6 → ETF live 0.35-0.50 → user account 0.30-0.45

### Tracking error reality
QUAL is a *partial* implementation of academic quality. It uses MSCI's index methodology, which captures perhaps 60-70% of the academic factor premium. That's still meaningful — it's close to the live factor portfolio after fees and execution.

### Failure mode
Quality has had a much smaller drawdown than other factors recently, but no factor is permanently safe. A regime that rewards risky-junky names (e.g., 2020-2021 meme stock rally) can produce 1-2 year quality underperformance.

### Decision rule (today)
Allocate 5-15% of equity sleeve to quality (QUAL or COWZ). Don't over-concentrate; tilt rather than replace SPX.

### Misconception box
> **Misconception:** "Quality is just a fancy way to buy expensive stocks."
>
> **Correction:** Quality and value are *distinct* factors with different mechanisms. Asness et al.'s QMJ controls for valuation; the quality premium exists *after* you control for value. Quality is not "growth dressed up." It's a separate dimension related to fundamentals (profitability, stability) rather than price (P/E, P/B).

### Self-check
1. What are the four pillars of QMJ?
2. Why has quality held up better than other factors recently?
3. What's the difference between QUAL and COWZ implementation?

---

## 7.2 Cross-Sectional Momentum

### Core intuition
Stocks that have outperformed over the past 6-12 months tend to keep outperforming over the next 1-3 months. The mechanism is behavioral under-reaction to news, then over-reaction at trend extremes (creating crash risk during reversals).

### Toy example
Sort all S&P 500 stocks by 12-month total return as of last month. Top decile vs bottom decile (excluding the most recent month, which has reversal effects). Long top, short bottom. This is the canonical "winners minus losers" momentum factor.

### Formal object
$$\text{UMD}_t = R_t^{\text{Winners}} - R_t^{\text{Losers}}$$

where Winners are top decile by past 12-month return (skipping most recent month) and Losers are bottom decile.

### Evidence
- **Jegadeesh-Titman (1993, *JF*)** — canonical: UMD ~1%/month, t≈3, Sharpe ~0.5 unlevered
- **Asness-Moskowitz-Pedersen (2013, *JF*)** "Value and Momentum Everywhere" — pervasive across 8 asset classes globally
- **Daniel-Moskowitz (2016, *JFE*)** — *critical caveat*: momentum lost **-73% from March-May 2009** during bear-market V-bottom
- **Jensen-Kelly-Pedersen (2023, *JF*)** — ~47% post-publication decline across hundreds of factors

### Why it exists
Mostly behavioral (Source 2):
- Under-reaction to news (investors anchor on old information)
- Over-reaction at trend extremes (chase behavior)
- Possibly compensation for crash risk in V-shaped reversals

### Retail implementation
- **MTUM** (iShares MSCI USA Momentum, 0.15%)
- **PDP** (Invesco DWA Momentum)
- **Haircut:** academic 0.5 → ETF live 0.25-0.40 → user account 0.20-0.35

### Tax inefficiency
Momentum has high turnover (~80% annually). In taxable accounts, this generates short-term capital gains that significantly drag after-tax returns. Best held in tax-advantaged accounts.

### Failure mode
**Momentum crashes.** When the market reverses sharply (bear market bottoming), the "losers" you were short rally violently and the "winners" you were long collapse. Daniel-Moskowitz documented -73% loss in 3 months in 2009.

Vol-scaled / dynamic momentum (Daniel-Moskowitz construction) reduces exposure when crash conditions are flagged. This roughly doubles unconditional Sharpe but is harder to implement retail.

### Decision rule (today)
Allocate 5-10% of equity sleeve to MTUM. Smaller than quality because higher decay risk and worse tax behavior.

Kill criteria:
- After 6+ month sustained equity drawdown, momentum crash risk is elevated → reduce exposure 50% until 3-month equity return turns positive
- MTUM tracking error to academic UMD > 4% annualized → switch vehicle

### Misconception box
> **Misconception:** "Momentum has worked for 30 years, so it'll keep working."
>
> **Correction:** Momentum has decayed materially post-publication (Jensen-Kelly-Pedersen 2023 documents ~47% decline). And it can produce -70% drawdowns in 3 months. The strategy still has positive expected return, but smaller and with worse path properties than 1990s data suggests.

### Self-check
1. Define momentum (winners-minus-losers).
2. What's the canonical Daniel-Moskowitz finding about momentum crashes?
3. Why is momentum tax-inefficient in taxable accounts?

---

## 7.3 Value (HML)

### Core intuition
Cheap stocks (low price relative to fundamentals like book value, earnings, cash flow) outperform expensive stocks over long horizons. Mechanism is debated — risk premium for distress, behavioral over-extrapolation of growth, or measurement issues with intangibles in modern accounting.

### Toy example
Sort S&P 500 by book-to-market ratio. Long top decile (cheap), short bottom decile (expensive). This is the canonical Fama-French HML factor. It produced reliable excess returns from 1927-2010, then went into the worst drawdown in modern history.

### Formal object
$$\text{HML}_t = R_t^{\text{High B/M}} - R_t^{\text{Low B/M}}$$

Modern variations use composite valuation (E/P, B/M, FCF/P, EV/EBITDA) and may control for sector exposure.

### Evidence
- **Fama-French (1993, *JFE*)** — canonical: HML 0.40-0.50%/month, t≈3, Sharpe ~0.4 long-run
- **2010-2020: worst documented value drawdown in modern history.** AQR Equity Market Neutral lost ~38% peak-to-trough by Dec 2020
- **Arnott-Harvey-Kalesnik-Linnainmaa (2021, *JPM*)** "Reports of Value's Death May Be Greatly Exaggerated" — attributes drawdown to valuation-spread widening (cyclical), not fundamentals
- **Realized rebound:** AQR Absolute Return +43.5% in 2022, +18.5% in 2023; Russell 1000 Value +24.9% in 2024

### Why it exists
Disputed:
- **Risk premium view (Fama-French):** value stocks bear distress risk
- **Behavioral view (Lakonishok-Shleifer-Vishny):** investors over-extrapolate growth, under-pay for boring value
- **Intangibles view (Lev-Srivastava):** B/M is mismeasured as intangibles grew; intangible-adjusted HML works better post-1993

Probably all three. Mixed source mostly behavioral and partly risk-based.

### Retail implementation
- **RAFI / Schwab fundamental funds** (FNDX, FNDA): use cash flow, sales, book value, dividends as fundamentals
- **IVE** (iShares S&P 500 Value): traditional value
- **AVUV** (Avantis US Small-Cap Value): captures size-conditional-on-quality value
- **Haircut:** academic HML 0.4 → live 0.15-0.30 → user account 0.10-0.30

### Failure mode
Multi-year drawdowns. 2010-2020 was the worst in modern history, with AQR funds losing ~40% over 5 years and breaking many investors' commitment. If you'd panic-exited in 2020 you'd have missed the +43.5% 2022 rebound.

### Decision rule (today)
Small tilt (3-8% of equity sleeve) only if you're committed to multi-decade patience. **If you'd panic-exit during a 5-year drawdown, don't allocate to value.** The 2010-2020 episode showed how punishing the path can be.

### Misconception box
> **Misconception:** "Value has come back, so we're in a new value-friendly regime."
>
> **Correction:** Value has rebounded from a deep drawdown but is still cyclical. The 2022-2024 outperformance might be a regime shift or might be a bear-market mean reversion that reverses in the next bull. Don't extrapolate. Allocate to value only with multi-decade tolerance.

### Self-check
1. What was the 2010-2020 value experience?
2. Why does Arnott et al. (2021) attribute the drawdown to valuation spread widening?
3. Why does Lev-Srivastava's intangibles framework matter for modern value?

---

## 7.4 Low-Volatility / BAB

### Core intuition
Low-volatility stocks have outperformed high-volatility stocks on a risk-adjusted basis. This contradicts CAPM (which says higher beta = higher expected return) and is one of the most counterintuitive results in factor literature. Mechanism: leverage-constrained investors bid up high-beta stocks to get equity exposure, depressing low-beta returns relative to CAPM.

### Toy example
Stock A: beta 0.6, expected return 6%. Stock B: beta 1.5, expected return 15% (per CAPM). Empirically, Stock A returns more like 8% and Stock B returns more like 11% — both diverge from CAPM in the same direction. The "betting against beta" strategy goes long Stock A levered up, short Stock B levered down.

### Formal object
$$\text{BAB}_t = \beta_\text{H}^{-1} R_\text{Low} - \beta_\text{L}^{-1} R_\text{High}$$

(simplified) — vol-scaled long-short portfolio that's market-beta-neutral.

### Evidence
- **Frazzini-Pedersen (2014, *JFE*)** — "Betting Against Beta" — US BAB Sharpe 0.78 (1926-2012)
- **CRITICAL caveat — Novy-Marx & Velikov (2022, *JFE*) "Betting Against Betting Against Beta":** the FP Sharpe is largely an artifact of (a) FP's non-standard rank-weighting that overweights micro/nano-caps and (b) FP's specific beta-shrinkage. Value-weighted BAB Sharpe falls to ~0.49 (still positive, t=3.5, 76 bps/month, but materially smaller).
- **Bali et al. (2017):** lottery demand for high-beta lottery-like stocks creates the same effect

### Why it exists
Institutional friction (Source 3) primarily:
- Leverage-constrained investors (mutual funds, pensions) can't lever; instead they buy high-beta stocks to get exposure → high-beta becomes overpriced
- Behavioral overlay: lottery demand for high-beta names

### Retail implementation
- **USMV** (iShares MSCI USA Min Vol, 0.15%): long-only low-vol
- **SPLV** (Invesco S&P 500 Low Volatility, 0.25%)
- **Long-only captures roughly half the long-short Sharpe** but is fully scalable
- **Don't try to replicate the leveraged long-short** — the leverage is what causes BAB to break in stress

### Failure mode
- Liquidity stress (TED > 200 bps, MOVE > 150) historically punishes BAB
- Long-only low-vol still has equity beta and loses in crashes (~0.6 of SPX losses)

### Decision rule (today)
Allocate 3-8% of equity sleeve to USMV. Keep small because the academic Sharpe is overstated and the live haircut is large.

Kill criteria:
- During liquidity-stress regimes, reduce allocation 25%

### Misconception box
> **Misconception:** "BAB has Sharpe 0.78, so it's a great factor."
>
> **Correction:** Novy-Marx & Velikov (2022) show that the 0.78 figure is methodology-specific. Value-weighted version is 0.49 — still positive but materially smaller. Don't over-allocate based on the Frazzini-Pedersen number.

### Self-check
1. Why does BAB exist? What's the institutional mechanism?
2. What does Novy-Marx & Velikov (2022) show about the Sharpe number?
3. Why is long-only low-vol preferable to leveraged long-short for retail?

---

## 7.5 Size (conditional on quality)

### Core intuition
Banz (1981) reported a ~5%/year size premium — small-caps outperform large-caps. Standalone, the effect has been roughly flat post-1981. But conditional on quality (excluding junky small-caps), the size premium re-emerges substantially.

### Toy example
Compare Russell 2000 to S&P 500 since 1980: roughly equal long-run returns. But split Russell 2000 into "high quality" (profitable, low leverage) and "junk" (unprofitable, high leverage). High-quality small-caps significantly outperform; junk small-caps significantly underperform. The aggregate index is dragged down by the junk component.

### Formal object
Size premium conditional on quality:
$$\text{SMB}^{\text{adj}}_t = R_\text{Small, HighQuality} - R_\text{Large}$$

### Evidence
- **Banz (1981)** — original ~5%/year size premium
- **Asness-Frazzini-Israel-Moskowitz-Pedersen (2018, *JFE*) "Size Matters, If You Control Your Junk"** — premium nearly doubles after controlling for quality

### Why it exists
Mixed:
- Risk premium for small-cap illiquidity and distress
- Behavioral underpricing of obscure small companies
- Conditional on quality, the "junk" drag is removed

### Retail implementation
- **AVUV** (Avantis US Small-Cap Value, 0.25%)
- **DFSV** (Dimensional US Small Cap Value, 0.30%)
- **ZIG** (Acquirers Fund deep value)
- These ETFs filter for quality within small-caps

### Decision rule
Modest tilt (3-7% of equity sleeve) via AVUV or similar. Standalone size (e.g., IWM) is much weaker than size + quality combination.

### Self-check
1. Why is standalone size a weak factor post-1981?
2. What does Asness et al. (2018) show about size conditional on quality?

---

## 7.6 Aggregate factor allocation

### Combined within equity sleeve
A reasonable factor tilt within the equity allocation:

| Factor | Weight in equity sleeve | Vehicle |
|---|---|---|
| Quality | 8-12% | QUAL or COWZ |
| Momentum | 5-10% | MTUM |
| Value | 3-8% | RAFI fund or AVUV |
| Low-vol | 3-8% | USMV |
| Size + Quality | 3-7% | AVUV |
| Pure cap-weight | Remainder (50-70%) | SPY/VTI |

Total factor tilts: 25-40% of equity sleeve. Don't go higher — tracking error to broad equity becomes large and the diversification benefit between factors saturates.

### Why diversify across factors
Factors don't all underperform at the same time:
- 2020-2021: momentum strong, value weak, quality OK
- 2022: value strong, momentum mixed, quality OK
- 2008: low-vol best, momentum and value badly hit
- 1990s: value strong, momentum strong, low-vol weaker

Diversifying across 4-5 factors smooths the path materially. Single-factor concentration produces multi-year drawdowns that test patience.

### Total factor expected contribution
- **Academic combined factor portfolio:** ~2-3% annual excess return over cap-weight, Sharpe ~0.6
- **Realistic retail implementation:** ~0.5-1.5% annual excess, Sharpe ~0.2-0.4 above cap-weight

The retail haircut is large because (a) ETF implementations are partial, (b) tax friction matters, (c) behavioral exits during multi-year drawdowns are common.

---

## 7.7 Misconception box (chapter level)

> **Misconception:** "I can time factor rotation by buying whichever factor is hot."
>
> **Correction:** Factor performance is highly cyclical and difficult to predict. Most academic literature finds that *factor timing adds no value* relative to a static diversified factor allocation. The exception is valuation-based timing of value (when value spreads are extreme) — but even that is contentious. **Default to static diversified tilts**, not factor rotation.

---

## 7.8 Self-check (chapter)

1. Name the five major equity factors. Which has held up best post-2010?
2. State the conviction score for a hypothetical "go all-in on momentum" allocation in a calm regime. Identify the binding constraint.
3. Why is value harder to allocate to than quality despite similar academic Sharpes?
4. What's the academic Sharpe vs realistic retail Sharpe for combined factor portfolios?
5. Take a factor ETF you're considering. Decompose: which factor source dominates? What's its specific implementation drift from the academic factor?
6. Why does diversifying across factors reduce path risk?

---

## Where this fits

Chapter 6 covered the foundation premia. Chapter 7 covers factor tilts that modulate the equity sleeve. Chapter 8 will cover structural overlays (FOMC cycle, EOQ rebalancing, OPEX). Chapter 9 covers regime filters. Chapter 10 covers the rejected category.

Factor tilts are smaller than foundation premia but cumulative — combining quality + momentum + value + low-vol can add 0.2-0.4 of Sharpe to the equity sleeve. Worth doing, but only with multi-decade commitment and explicit understanding of the path.

[← Previous: Chapter 6 — Foundation premia](07_ch06_foundation_premia.md) | [Next: Chapter 8 — Structural overlays →](09_ch08_overlays.md)
