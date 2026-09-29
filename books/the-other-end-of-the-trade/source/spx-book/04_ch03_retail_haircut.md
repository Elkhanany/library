# Chapter 3 — The retail-realism haircut
## From academic Sharpe to user-account after-tax

> **Core intuition.** A strategy with 0.8 paper Sharpe routinely shows 0.2-0.4 in a retail account. The gap isn't because academics are wrong; it's because real implementation introduces friction at four distinct layers. Skipping the haircut analysis is the single biggest cause of disappointment when traders try to replicate published strategies.

---

## 3.1 The four layers

Every strategy degrades through these four layers:

| Layer | What's measured | Typical Sharpe haircut | Source of friction |
|---|---|---|---|
| **Academic** | Long-short factor portfolio, daily rebalance, mid-quote fills, no taxes | Baseline | Idealized |
| **Investable index** | CBOE PUT, BTOP50, MSCI Quality | -15 to -30% | Index construction rules, monthly rebalance, real bid-ask |
| **ETF / fund live** | PUTW, DBMF, KMLM, MTUM | Additional -10 to -25% | Expense ratio, tracking error, manager dispersion |
| **User after-tax** | Your account | Additional -10 to -30% | Slippage, taxes, behavior, sub-optimal sizing |

### The compounding haircut

Each layer multiplies the previous one. A strategy with academic Sharpe of 0.8 and 25% haircut at each layer becomes:

$$\text{SR}_\text{user} = 0.8 \times 0.75 \times 0.75 \times 0.75 = 0.34$$

A 58% cumulative haircut. This isn't pessimistic — it's typical.

### Worked example

**Strategy: monthly ATM put-writing on SPX/XSP.**

- **Academic** (Bondarenko 2019, 1986-2018, idealized): Sharpe ~0.65
- **Investable index** (CBOE PUT, mechanically tracked): Sharpe ~0.55-0.60. Haircut: ~10-15% from monthly rebalance and real fill prices on ATM SPX puts.
- **Live ETF** (PUTW, 2016-2024 actual returns): Sharpe ~0.30-0.45. Haircut from index: another 25-35% from expense ratio (~50 bps), tracking error, and PUTW's specific implementation choices (which differ slightly from the PUT index).
- **User account** (running it manually with realistic slippage and taxes): Sharpe ~0.20-0.40. Haircut from PUTW: another 10-25% from your slippage on entries (which won't perfectly match index timing), tax friction (most monthly rolls trigger short-term capital gains treatment in taxable accounts; XSP gets 1256 60/40 which is much better), and behavioral interventions (closing early in stress, sizing inconsistently).

**Net:** academic 0.65 → user account ~0.20-0.40. **The haircut is real. Plan for it.**

---

## 3.2 Why each layer takes a haircut

### Academic → Investable index

**What's lost:** the idealizations of academic backtests. Academic factor portfolios use:
- Daily rebalancing (impractical at scale)
- Mid-quote pricing (no bid-ask)
- No transaction costs (or unrealistically low)
- No shorting borrow costs (or implausible borrow availability)
- Infinite capacity (no market impact)

**What replaces them:** Real-world index construction. Monthly or quarterly rebalance, real execution prices, capacity limits, defined methodologies that may not optimally implement the theoretical signal.

**Typical haircut:** 15-30%. Larger for strategies that depend on micro-cap exposure, daily rebalancing, or dispersed positions. Smaller for liquid index strategies.

**Example:** academic BAB Sharpe 0.78 (Frazzini-Pedersen 2014) becomes 0.49 in a value-weighted version (Novy-Marx & Velikov 2022) — a 37% haircut from one methodology choice.

### Investable index → ETF/fund

**What's lost:** wrapping the index in a tradable product introduces:
- Expense ratio (40-100 bps typical for factor ETFs, 60-100 bps for managed futures)
- Tracking error from cash drag, dividend reinvestment timing, sampling
- Manager discretion (active funds) or methodology drift (passive funds)
- Tax inefficiency (depending on wrapper structure)

**Typical haircut:** 10-25%. Larger for active funds or complex strategies; smaller for vanilla index-tracking ETFs.

**Example:** PUT index Sharpe ~0.55-0.60 becomes PUTW Sharpe ~0.30-0.45 over 2016-2024. The PUTW wrapper changed strategy slightly in 2023 (moved to weekly options); pre-2023 was closer to PUT index. The wrapper drift introduces another haircut beyond pure expense ratio.

### ETF/fund → User account

**What's lost:** the gap between "buying an ETF and holding" and "running the strategy yourself." For pure ETF allocations, this layer is small. For self-managed strategies, it's large.

For self-managed strategies the friction includes:
- **Slippage:** your entries and exits won't perfectly match the index. Even small slippage compounds over hundreds of trades.
- **Taxes:** XSP options get 1256 treatment (60/40 LTCG/STCG); SPY ETFs get standard treatment. ETFs in a taxable account create ordinary-income tax events on monthly distributions; rebalancing creates capital gains. The tax drag for active strategies in taxable accounts can be 100-200 bps annually.
- **Behavioral:** Morningstar's "Mind the Gap" study has documented investor returns lagging fund returns by 100-200 bps annually for two decades. The gap is largest in volatile, complex, non-intuitive strategies.
- **Sizing:** real users under-size on entry ("I'll test it small first") and over-size after wins ("I should have allocated more").
- **Missed rebalances, trading errors, timing mistakes.**

**Typical haircut:** 10-30%. Smaller for ETF-only allocations; larger for self-managed options strategies.

---

## 3.3 The behavioral component is the biggest

Here's an uncomfortable truth: the *behavioral* component of the user-account haircut is often larger than all the other components combined.

### The Mind the Gap data

Morningstar publishes annual "Mind the Gap" studies measuring the difference between *time-weighted* fund returns (what the fund did) and *dollar-weighted* investor returns (what investors actually got). Across 20+ years, the gap is consistently 100-200 bps annually, with the largest gaps in:

- **Sector funds:** investors chase performance, buy after rallies, sell after drops
- **Complex strategies:** investors don't understand them, panic at drawdowns
- **High-volatility strategies:** investors enter at peaks, exit at troughs

Premium-selling strategies and trend-following both qualify as "complex and high-volatility" by retail standards. The behavioral gap on these can easily be 200+ bps annually.

### The forced-liquidation cost

Beyond simple panic selling, the behavioral cost includes *forced liquidation* events: portfolio margin requirements expand in stress, and undisciplined sizing means you're forced to close positions at the worst time. This isn't strictly behavioral (it's structural), but it's often caused by behavioral failure to size for stress in advance.

A single force-liquidation event during a 30 VIX environment can wipe out 12-18 months of accumulated edge.

### Misconception box

> **Misconception:** "I'll behave better than the average investor; the behavioral haircut doesn't apply to me."
>
> **Correction:** Most people who think this are wrong. The behavioral haircut is consistent across decades of data, including among sophisticated investors. The minority who genuinely outperform their funds do so through specific structural choices (automation, written rules, kill criteria, behavioral safeguards) — not through "self-discipline" alone. If you don't have written rules and kill criteria, you'll experience the average behavioral gap regardless of your perceived discipline.

### Building behavioral resistance

The fix isn't willpower. It's structure:

1. **Written rules** for entry, exit, sizing
2. **Kill criteria** specified in advance (Chapter 14)
3. **Behavioral kill criterion** at portfolio level: 25% DD halts all discretionary tactical sleeves for 30 days
4. **Mechanical execution** where possible (automated rebalances, scheduled rolls)
5. **Strategy diary** documenting what you actually did vs what the rules said
6. **Periodic review** (quarterly) comparing your account performance to the underlying ETF/index it's supposed to track

If your account is consistently 200+ bps behind the relevant benchmark, the gap is behavioral and only structural changes will fix it.

---

## 3.4 Worked example: applying the haircut to PUT index

Let's walk through the full haircut for a "VRP harvest via XSP cash-secured monthly puts" strategy.

### Layer 1: Academic
Bondarenko 2019 PUT index analysis, 1986-2018:
- Annual return: 9.54%
- Annual vol: 9.95%
- Sharpe: ~0.65
- Max DD: -33% in GFC
- Skew: -2.09 (negatively skewed)

### Layer 2: Investable index → already at PUT level
PUT is already an investable mechanical index, so this layer is small. The "academic" version would idealize fills further; the PUT methodology is honest.
- Effective haircut: ~5-10%
- Adjusted Sharpe: ~0.55-0.60

### Layer 3: Live ETF (PUTW or self-managed approximation)
PUTW expense ratio: 0.44%
PUTW also changed strategy in 2023; pre-2023 tracked PUT closely, post-2023 moved to weekly options.
- For 2016-2022 PUTW data: Sharpe ~0.40-0.50
- Live realized: 0.30-0.45

If you self-manage XSP puts (rather than buying PUTW), you skip the wrapper expense but pick up:
- Slightly worse fills (mid-quote vs index pricing assumption)
- Better tax treatment (1256 60/40 vs PUTW's distribution treatment)
- Operational risk (missed rolls, errors)

Net: self-managed XSP put-write should track close to PUT index, perhaps slightly worse on Sharpe but better on after-tax. Realistic Sharpe before behavioral: 0.45-0.55.

### Layer 4: User account
Behavioral and execution friction:
- Slippage: 1-3 vol points per round-trip
- Tax drag: ~30-40 bps annually after 1256 treatment (in taxable account)
- Behavioral: 50-150 bps from sub-optimal entries/exits, sizing inconsistency
- Force-liquidation risk: low if cash-secured; significant if leveraged

Net haircut from layer 3: 15-30%. Final Sharpe: 0.20-0.40.

### Summary table

| Layer | Sharpe | Cumulative haircut |
|---|---|---|
| Academic PUT (Bondarenko) | 0.65 | 0% |
| Investable PUT methodology | 0.55-0.60 | -8 to -15% |
| Self-managed XSP equivalent | 0.45-0.55 | -15 to -30% |
| User after-tax with realistic execution | 0.20-0.40 | -40 to -65% |

**Plan for a Sharpe of 0.25-0.35 if you allocate to this. Anything higher is a pleasant surprise.**

---

## 3.5 Worked example: applying the haircut to trend-following

### Layer 1: Academic
Hurst-Ooi-Pedersen (2017) "Century of Evidence":
- 1880-2016, 67 markets
- Average net Sharpe ~0.4 *after 2/20 fees*
- Sharpe ~0.8-1.2 in idealized models without manager fees

### Layer 2: Investable index
SG Trend Index, BTOP50 (live CTA composite):
- 2003-2024 realized Sharpe: ~0.3-0.5
- Already close to academic net Sharpe (Hurst-Ooi-Pedersen included fees)
- Live experience matches paper roughly

### Layer 3: Live ETF
DBMF (replication, 0.85% expense), KMLM (Mount Lucas, 0.92%), RSST (return-stacked, 1.04%):
- Live realized Sharpe 2018-2024: 0.25-0.45 depending on vehicle
- Tracking error to SG Trend can be 200-400 bps annually
- Vehicle-specific quirks (replication lag for DBMF, fixed signal for KMLM)

### Layer 4: User account
- Behavioral: trend has long droughts (2011-2018) which test patience; many investors capitulate
- Tax: futures-based vehicles get 1256 (favorable)
- Sizing: many users under-allocate during droughts and over-allocate after winners

Net Sharpe: 0.20-0.40.

### Why trend's haircut is similar to VRP's

You might expect trend (lower-leverage, less complex) to have a smaller haircut than VRP. In some ways it does:
- No margin expansion risk
- Cleaner tax treatment
- Lower path dependency

But trend's *behavioral* haircut is large because of the long whipsaw periods. Investors who ride trend through 4-7 year droughts before eventually capturing a 2008 or 2022 are rare. Most exit during droughts and miss the payoff.

The *value* of trend, however, isn't in its standalone Sharpe — it's in its crash complementarity. Even a trend Sharpe of 0.20 contributes more to portfolio Sharpe than its standalone math suggests, because of the negative crash beta.

---

## 3.6 The haircut for "complex" strategies

Some strategies have larger haircuts than others. The general rule:

| Strategy type | Typical haircut |
|---|---|
| Long-only equity ETF | -5 to -15% |
| Factor ETF (QUAL, MTUM) | -15 to -30% |
| Index put-write (ETF-form) | -25 to -40% |
| Self-managed put-write | -30 to -50% |
| Self-managed multi-leg options | -40 to -60% |
| Discretionary timing strategies | -50 to -80% |

The haircut grows with:
- Complexity (more legs = more friction)
- Discretion (more decision points = more behavioral risk)
- Self-management (more operational risk)
- Active timing (more missed-trade risk)

**Operational implication:** prefer simple implementations. Every additional leg in an options structure must add enough premium or risk-management value to overcome the additional haircut. Often it doesn't.

---

## 3.7 The retail-haircut equation

To formalize:
$$\text{SR}_\text{user} = \text{SR}_\text{paper} \times h_1 \times h_2 \times h_3 \times h_4$$

Where:
- $h_1$ = academic to investable index haircut (typically 0.70-0.95)
- $h_2$ = investable to ETF haircut (typically 0.75-0.90)
- $h_3$ = ETF to self-managed haircut (typically 0.80-0.95)
- $h_4$ = self-managed to user-after-tax haircut (typically 0.65-0.90)

For most strategies, the cumulative haircut $\prod h_i$ falls in the 0.30-0.60 range.

**Use this equation explicitly:** when you read a paper claiming Sharpe 0.8, multiply by 0.40 as your default expectation. If the strategy is unusually clean (low complexity, ETF-implementable, tax-efficient), you can use a higher multiplier (0.55-0.70). If it's unusually friction-heavy (active timing, multi-leg, complex), use lower (0.25-0.35).

---

## 3.8 Misconception box: "but my edge is real"

> **Misconception:** "I'll outperform the haircut because my specific implementation is better than the typical retail approach."
>
> **Correction:** Maybe. But the prior probability of any given retail trader beating the haircut is low. The data on investor performance vs fund performance (Mind the Gap) is consistent across decades. Plan for the typical haircut; treat outperformance as a positive surprise.
>
> If you've operated a strategy for 3+ years with documented kill criteria, written rules, and a strategy diary, and your realized Sharpe matches or beats the paper expectation, you have *some* evidence of better-than-haircut execution. Until then, plan conservatively.

---

## 3.9 The "should I trade this?" gate

Combining the haircut framework with the conviction work in Chapter 4:

**Before allocating, ask:**
1. What's the academic Sharpe?
2. What's my expected user-after-tax Sharpe (apply the haircut)?
3. Is the user-after-tax Sharpe still positive after fees and effort?
4. Does the strategy add to the portfolio (positive contribution to portfolio Sharpe), or duplicate existing exposures?
5. Can I commit to written rules and kill criteria that prevent the behavioral haircut from compounding?

If any of these answers are "no" or "I don't know," the strategy isn't ready to allocate to.

### A pessimistic but honest framing

Many sophisticated retail traders will spend 100+ hours implementing a strategy with paper Sharpe 0.6, expect to realize 0.5, and actually realize 0.15 after a year. The gap is the haircut.

The fix isn't to find better strategies. It's to:
1. Plan for the haircut explicitly
2. Pick strategies whose value depends less on perfect execution
3. Use ETF implementations where possible
4. Build behavioral safeguards (kill criteria, written rules)
5. Let go of complex strategies that won't survive the haircut

---

## 3.10 Self-check

1. State the four layers of the retail haircut. Why does each one introduce friction?
2. Apply the haircut equation: a paper strategy has Sharpe 0.8, with haircuts 0.85, 0.80, 0.85, 0.75. What's the user-account Sharpe?
3. Why is the behavioral component often the largest part of the haircut?
4. What structural choices reduce the behavioral haircut?
5. For a strategy you're considering, walk through the four-layer haircut and produce a realistic user-after-tax Sharpe expectation.
6. Why do complex multi-leg options strategies typically have larger haircuts than simple ETF allocations?

---

## Where this fits

Chapter 0 gave us distributions. Chapter 1 gave us why edges exist. Chapter 2 gave us why Sharpe lies for short-vol. Chapter 3 gives us realistic retail expectations. Chapter 4 will use all of these to formalize the conviction framework — the trade-admission test that any strategy must pass before it gets capital.

Without the haircut framework, you'd over-allocate to academically-attractive strategies that don't survive implementation. The haircut is the gravity that pulls paper Sharpes back to reality.

[← Previous: Chapter 2 — Sharpe trap](03_ch02_sharpe_trap.md) | [Next: Chapter 4 — Conviction framework →](05_ch04_conviction.md)
