# Section 12 · Discipline
*From paper Sharpe to compound returns — swing-trade discipline.*

Everything in Sections 1-11 was about understanding the mechanism. This section is about the operational discipline that turns understanding into compound returns. The framework is specifically oriented around **swing trading SPX/SPY/QQQ/Mag-7 setups on horizons of 2 to 20 trading days**, which is where most of the framework lives and where the dealer-mechanics framework has its sharpest practical application.

The retail trader's problem isn't usually edge — most have access to genuinely tradeable setups. The problem is the gap between paper performance and live performance, which is dominated by behavioral and operational factors. **A strategy with paper Sharpe of 0.80 routinely shows 0.20-0.40 in a retail account.** This section is about closing that gap.

Five sub-chapters:

- **12A** — The retail haircut. Why paper Sharpe degrades to user-account Sharpe, with concrete numbers.
- **12B** — The conviction score. E × M × R × X × S as a pre-trade discipline.
- **12C** — Pipeline and kill rules. Observation → interpretation → trade implication → sizing → invalidation, plus three levels of kill rules.
- **12D** — Ten worked examples. Real swing-trade reasoning chains, applied.
- **12E** — Setup cards. Operational one-pagers for the four core swing archetypes plus do-not-trade reference cards.

---

## 12A · The retail haircut for swing strategies

A swing strategy with paper Sharpe of 1.0 in a clean backtest routinely shows Sharpe of 0.3-0.5 in a retail account. The gap is not because backtests are wrong (well, sometimes they are — but assume yours isn't). The gap is because real implementation introduces friction at multiple layers, each one compounding on the previous.

> **Defining "mechanical sleeve."** Throughout Section 12 (and in the kill rules of 12C, the conviction discussion of 12B, and the discipline pipeline), the term *mechanical sleeve* refers to a rules-only sub-portfolio that executes predefined entries and exits without discretionary override. Examples: a systematic SPX cash-secured-put writing program; a 200-day-moving-average crossover allocation; a Connors RSI(2) mean-reversion bot on QQQ; a fixed monthly Iron Condor sale at 30 DTE. The defining property is that *no human judgment intervenes between signal and execution*.
>
> Why the distinction matters: mechanical sleeves provide **baseline market exposure** that continues to compound during periods when discretionary judgment must be suspended — drawdown timeouts (per 12C kill rules), personal/health events, regime confusion, or simple loss-of-conviction phases. The mechanical sleeve is the portfolio's heartbeat; the discretionary sleeve is its thinking layer. A trader running only discretionary positions has no baseline; if discretion fails (and it sometimes will), the entire portfolio sits in cash earning Treasury yields.
>
> **Sleeve sizing.** A reasonable structure for a swing-trading retail account is **60-80% mechanical, 20-40% discretionary**, with the mechanical sleeve weighted toward systematic equity exposure (factor or buy-and-hold) plus modest systematic premium selling. The discretionary sleeve takes the swing trades described in Section 10 and is where this entire curriculum's tactical layer operates.
>
> When this curriculum talks about "stopping all trading after a 25% drawdown" (12C) or "the conviction score governing entries" (12B), those rules apply to the **discretionary** sleeve only. Mechanical sleeves run regardless.

### The four layers of friction for swing strategies

**1. Paper backtest.** Baseline performance on historical data. Mid-quote fills (entry at midpoint of bid-ask). No transaction costs beyond a token commission. No taxes. Idealized entries. This is what the backtest engine produces.

**2. Out-of-sample.** Same strategy, same parameters, but on unseen data. This is where overfitting bias appears. A strategy with paper Sharpe 1.0 from in-sample optimization typically delivers Sharpe 0.5-0.7 out-of-sample on truly fresh data. The gap is the **deflation factor** from López de Prado's work (Section 1A).

**3. Live execution.** Real bid-ask spreads on entry and exit (not mid-quote). Real slippage when sizing exceeds top-of-book depth. Real timing — you don't always see the setup form in real time as cleanly as you see it in the backtest. Real-world execution typically introduces another 20-30% Sharpe degradation.

**4. After-tax, after-behavior.** Tax friction (ordinary income on short-term gains for SPY/QQQ; 1256 60/40 for SPX/XSP, ES). Behavioral interventions — early exits, missed setups, position-size inconsistencies, the urge to revenge-trade after a loss. Behavioral friction is the largest single source of loss in the chain, and the one most retail traders deny exists.

### The compounding haircut equation

```
SR_user = SR_paper × h_1 × h_2 × h_3 × h_4

typical product: 0.30-0.60 — i.e., 30-60% of the paper Sharpe survives
```

Typical haircut values for a competent retail swing trader operating with discipline:

- **h₁ = 0.70-0.85** (out-of-sample degradation)
- **h₂ = 0.80-0.90** (execution slippage and timing)
- **h₃ = 0.85-0.95** (tax friction; depends heavily on instrument choice — XSP vs SPY)
- **h₄ = 0.70-0.90** (behavioral; depends on discipline)

Product: 0.35-0.58. A paper-Sharpe-1.0 strategy typically delivers user-Sharpe 0.4-0.6 in practice. **This is the median outcome, not a pessimistic projection.**

[INTERACTIVE: retail-haircut-decomposition]

If you find yourself thinking "I'll be better than the median because I'm more disciplined," you may be right — but the burden of proof is on you. Most traders who think they'll be better than the median are wrong.

### The behavioral component is the biggest single factor

Of the four haircut layers, the user-account layer (h₄) is consistently the largest single source of loss. **Morningstar's annual *Mind the Gap* study has measured this for two decades**: the difference between time-weighted fund returns and dollar-weighted investor returns runs consistently 100-200 basis points annually, with the gap widest in volatile, complex, and non-intuitive strategies.

For swing trading specifically, the behavioral failure modes are:

1. **Position-size inconsistency.** Sizing larger after wins, smaller after losses. The reverse of what disciplined trading requires.
2. **Stop migration.** Moving stops further away as price approaches them, "to give the trade more room." This converts small losses into large ones.
3. **Premature exits on winners.** Closing winners early to "lock in profit" while letting losers run. The classic disposition effect.
4. **Revenge trading.** Taking marginal setups after a loss to "make it back," with predictable consequences.
5. **Setup creep.** Lowering the bar for what counts as a valid setup during slow weeks.
6. **News chasing.** Entering positions based on news after the move has already happened, rather than based on setup geometry.

The fix is not "I'll behave better than the average investor." Most people who think this are wrong. **The fix is structural**: written rules, pre-committed entry criteria, mechanical position sizing, pre-committed kill criteria. Discipline only exists when it is binding under stress, and it is only binding when it was written down in calm conditions before the trade.

### Worked example: a swing setup, paper to user

Consider a trend-pullback swing setup on SPY: enter on RSI(2) < 10 during Stage 2, exit at 21-EMA reclaim or 3-day time stop, fixed dollar-risk position sizing.

- **Paper backtest** (2015-2024, in-sample optimization): Sharpe 1.1, average trade duration 4 days, win rate 67%, average win/loss ratio 1.4:1.
- **Out-of-sample** (2025 forward-walk, parameters frozen): Sharpe 0.8. Win rate drops to 60%.
- **Live execution** (slippage on entry/exit at limit orders that don't always fill at mid): Sharpe 0.65.
- **After-tax**: For a top-bracket US retail trader, all gains are short-term. Effective tax rate ~40%. After-tax Sharpe 0.45.
- **After-behavior**: Sharpe 0.30-0.35.

The paper 1.1 became user 0.30-0.35. **A 65-70% Sharpe haircut.** This is normal. Plan for it.

### Plan for the haircut, not against it

When you read a strategy description claiming Sharpe 0.85, your default expectation should be user-account 0.30-0.40. Use the haircut equation to **filter strategies before committing capital**: if the user-after-tax Sharpe doesn't beat just holding SPX outright, the strategy isn't worth the operational complexity.

The honest framing: spending 100 hours implementing a paper-Sharpe-1.0 swing strategy and realizing 0.35 user-Sharpe is the median outcome. The win condition is to:

1. **Pick strategies whose value doesn't depend on perfect execution.**
2. **Pick instruments with favorable tax treatment.** XSP/SPX/ES over SPY for the 1256 60/40 advantage.
3. **Pick setups with simple, mechanical entry/exit rules.**
4. **Pre-commit to position sizing.**

---

## 12B · The conviction score — when to take a swing setup

"High conviction" should not mean "I believe in this strongly." It should mean **every independent evidence layer converges**: the evidence is robust, the mechanism is articulable, the regime is supportive, execution is feasible, and sizing is survivable. If any single layer fails, conviction collapses regardless of how strong the signal feels.

### The formal definition

```
Conviction score: C_i(t) = E_i × M_i × R_i(t) × X_i(t) × S_i

Each factor ∈ [0, 1]. Threshold for high conviction: C ≥ 0.5.
```

The form is **multiplicative**. A single factor at 0 zeros the whole product. A strategy with stellar evidence (E=0.95) but unsurvivable sizing (S=0.10) produces C = 0.095 — insufficient conviction, regardless of how good the paper looks. **Multiplicative form is the load-bearing assumption**: in operational reality, you really cannot compensate for one broken dimension with extra strength in another.

### The five factors, applied to swing trades

**E — Evidence.** How well-supported is the setup in academic and practitioner literature? Has it been replicated across multiple datasets and time periods?

- Tier 1 (peer-reviewed, multi-decade, replicated): 0.8-1.0 (Jegadeesh-Titman momentum; Connors RSI(2) mean reversion in trending markets; Ni-Pearson-Poteshman pinning near OPEX)
- Tier 2 (strong empirical but sample-sensitive): 0.5-0.8
- Tier 3 (thin, recent, or decayed): 0.0-0.4

**M — Mechanism.** Can you articulate *why* this setup has positive expected value?

- Clear mechanism with academic support: 0.7-1.0
- Partial mechanism story: 0.4-0.7
- "I don't know why this works": 0.0-0.3

**R(t) — Regime.** Is the current regime supportive of this specific setup? **Time-dependent.**

- Composite signal (Section 10F) ≥ +40, Stage 2 confirmed, positive GEX, contango: 0.8-1.0 for long swing trades
- Composite +10 to +40, Stage 2-3 transition, neutral GEX: 0.5-0.7
- Composite < 0, Stage 4, negative GEX, backwardation: 0.0-0.3 for long trades

**X(t) — eXecution.** Can you actually trade this at retail? Liquid, low spread, operationally clean?

- SPX/SPY/QQQ/Mag-7 with standard order types: 0.85-1.0
- Multi-leg index option with manageable spreads: 0.6-0.8
- Thin single-name option with wide spreads: 0.2-0.4
- Strategies requiring infrastructure you don't have: 0.0-0.2

**S — Sizing.** Can you size such that S2 (SPX −20% / VIX +25) is operational and S3 (SPX −35% / VIX +50) is recoverable, with explicit kill criteria?

- Sized for survivability, kill rules pre-committed in writing, drawdown plan documented: 0.85-1.0
- Sized "comfortably" without explicit stress testing: 0.5-0.7
- Sized aggressively without kill criteria: 0.1-0.3

### Live: score a swing setup

[INTERACTIVE: conviction-score-builder]

### Worked example: Trend Pullback on SPX in two regimes

Consider the canonical RSI(2)-on-Stage-2-pullback swing setup. **Same setup, evidence and mechanism unchanged. Only the regime changes.**

**Scenario A — Calm regime.** SPX above rising 200-SMA, VIX 14, composite signal +50, positive GEX above flip, contango term structure.

- E = 0.85, M = 0.90, R = 0.85, X = 0.90, S = 0.90

**C = 0.85 × 0.90 × 0.85 × 0.90 × 0.90 = 0.527 — HIGH CONVICTION. Take the trade at full intended size.**

**Scenario B — Stress regime.** SPX in Stage 3-4 transition, VIX 28, term structure backwardated, composite signal −30, negative GEX, recent CPI shock.

- E = 0.85, M = 0.90, R = 0.20, X = 0.65, S = 0.40

**C = 0.85 × 0.90 × 0.20 × 0.65 × 0.40 = 0.040 — INSUFFICIENT CONVICTION. Do not enter; reduce existing positions.**

Same setup, identical evidence and mechanism, regime collapse from +50 to −30 → conviction collapse from 0.527 (high) to 0.040 (don't trade). **This is what operational discipline looks like — selectivity is mostly not trading.**

### The five swing-trade failure modes

**1. Strong evidence, hostile regime.** Trend pullback in a Stage 4 market. E and M high, R low. Operational rule: **respect the regime filter even when the underlying setup is well-supported**.

**2. Right idea, oversized.** 25% of portfolio in a single swing trade. All else high, S low. Operational rule: **edge cannot compensate for unsurvivable size**.

**3. Beautiful backtest, no mechanism.** Optimized parameters that produce great paper Sharpe with no articulable reason it should work forward. Operational rule: **backtest performance without mechanism is data-mining**.

**4. Real edge, wrong infrastructure.** Cross-sectional dispersion edge that requires daily multi-leg delta-hedged positions on 50 names. Operational rule: **edges requiring infrastructure you lack aren't edges for you**.

**5. Vivid narrative, thin evidence.** "GEX scalping" with compelling dealer-positioning story but no actual backtest evidence. Operational rule: **narrative compellingness is not evidence quality**.

> *High-conviction swing trading is mostly not trading. Most observations don't pass interpretation. Most interpretations don't pass conviction. The trades that exist have all five gates clear — which is why they should be larger and more durable than the trades you'd otherwise make.*

### Companion framework: the Real Value score for single-name positions

The C-score above (E × M × R × X × S) is calibrated for **index** or **broad-market** swing positions where regime, execution, evidence, and sizing dominate. For **single-name** positions — individual stocks, particularly with options overlays — there are additional layers that the C-score doesn't capture cleanly. The Real Value score is the single-name companion.

```
RV = F × T × O × G × V × X × S

where each factor ∈ [0, 1]
```

Threshold for taking the trade: **RV ≥ 0.4** (slightly lower than the C-score's 0.5 because there are more factors, all bounded ≤ 1, so a uniformly "decent" position multiplies down faster).

**F — Fundamentals (0-1)**. Revenue/EPS revisions trending in the right direction; margin trend constructive; analyst estimate dispersion narrowing (consensus forming); guidance revisions positive (or, for shorts, negative); sector/industry tailwind. *F = 0.9-1.0*: rising estimates, narrowing dispersion, positive guidance, large institutional buying. *F = 0.5-0.7*: stable estimates, mixed analyst views, sector neutral. *F = 0.2-0.4*: declining estimates, widening dispersion, mixed/negative guidance. *F = 0*: clear negative fundamental break.

**T — Technical structure (0-1)**. Stage 2 confirmed; base quality (proper consolidation, not noise); relative strength versus benchmark; volume dry-up on the pullback; clean pivot or reclaim. *T = 0.9-1.0*: textbook Stage 2 pullback with tight consolidation, strong RS, clean pivot. *T = 0.5-0.7*: Stage 2 but with imperfect base or mediocre RS. *T = 0.2-0.4*: choppy structure, weak RS, ambiguous pivot. *T = 0*: Stage 4 or Stage 3 distribution.

**O — Option flow signature (0-1)**. Net premium bought at ask in supporting direction; opening transactions (next-day OI confirms new positioning, not closing); aggressor side aligned with thesis; repeated flow across sessions, not one-off; skew/IV change consistent. *O = 0.9-1.0*: large net premium bought at ask in supporting direction, opening transactions confirmed, repeated over 3+ sessions. *O = 0.5-0.7*: modest aligned flow, single session, opening status unclear. *O = 0.2-0.4*: mixed flow, possibly closing transactions, hard to interpret. *O = 0*: flow opposite to thesis. **Note**: flow alone is never a signal — O is a *confirmation* factor; F or T must already be ≥ 0.6 before O matters.

**G — GEX path support (0-1)**. Does dealer positioning support the move? Is spot below a call wall that becomes a magnet on the upside? Or below a put wall that creates a floor? Is the gamma flip near, creating regime instability? *G = 0.9-1.0*: clear path support (e.g., long thesis with positive GEX above flip, call wall well above target, put wall well below entry). *G = 0.5-0.7*: neutral path (flat GEX, no immediate walls). *G = 0.2-0.4*: path obstruction (gamma flip in the way, call wall immediately overhead on a long thesis). *G = 0*: GEX actively opposes the move (negative GEX in a mean-reversion long thesis).

**V — Vol-value (0-1)**. Is the option priced reasonably relative to realized vol, event risk, and IV history? Is the IV percentile attractive for the direction? Is the expected move plausible relative to ATR and announced catalysts? *V = 0.9-1.0*: option priced cheap relative to realized and history (favorable for buyers); or rich relative to realized (favorable for sellers). *V = 0.5-0.7*: option fairly priced; neither buyer nor seller advantage. *V = 0.2-0.4*: option mispriced against the direction (rich for buyers, cheap for sellers). *V = 0*: structural arbitrage against the trade (e.g., buying a long call into IV percentile >90).

**X — Execution quality (0-1)**. Bid-ask spread tight; liquidity sufficient at intended size; time of day favorable; not a known fragility window (last 30 minutes; first 5 minutes post-open; lunch hours for less liquid names). Same as the C-score X factor.

**S — Sizing survivability (0-1)**. Position survives a 3× stop blow-through; correlation with existing book accounted for; aggregate vega/delta within portfolio limits (per 12F). Same as the C-score S factor.

#### Real Value interpretation buckets

After computing RV, classify:

| RV range | Interpretation | Action |
|---|---|---|
| 0.5+ | Real signal: fundamentals + technical + flow + surface all agree | Take, at full size per 12C |
| 0.3-0.5 | Borderline: most factors aligned, one or two weak | Take at half size, or skip in favor of next setup |
| 0.15-0.3 | Mixed signal: enough green to be tempting but enough red to be dangerous | Skip; common loss-maker for retail |
| <0.15 | Avoid | Mostly noise; don't trade |

#### Four common single-name pathologies (low RV at a glance)

**1. Flow-only noise.** Massive call buying at ask, but F < 0.4 (no fundamental story) and T < 0.4 (no technical setup). Drives chasing trades that immediately fade. RV typically <0.1.

**2. Good thesis, bad vehicle.** F and T both >0.7, but V < 0.3 (option priced unreasonably). The thesis is real but you're paying too much for the expression. Often resolves to: trade the shares instead of the options.

**3. Good setup, bad path.** F, T, O all >0.6, but G < 0.3 (call wall directly overhead, or gamma flip in the way). The directional thesis is solid but the path is blocked by dealer mechanics. Wait for the obstacle to clear or pick a different strike/vehicle.

**4. Stretched stretching further.** All factors look OK in isolation, but the stock has already moved 30% in the prior month. The fundamental story is in the price. This is where RV correctly downgrades: F should account for "is this already reflected in price?" not just "is this story positive?"

The C-score and Real Value are not redundant. **Use C-score for index swings; use Real Value for single-name swings.** They share execution (X) and sizing (S) factors but differ in the layers that matter for index vs single-name decision-making.

---

## 12C · The signal-to-trade pipeline and the kill rules

Every action in your portfolio should pass through the same five-step grammar: **observation → interpretation → trade implication → sizing → invalidation**.

### The five steps

**01 — Observation.** What did I see? A measurable, specific market state. "SPX RSI(2) closed at 5 today, with Stage 2 confirmed by 30-SMA slope > 0.05 and ADX 22." NOT "the market feels oversold."

**02 — Interpretation.** What does it mean? Map the observation to a known mechanism. "RSI(2) < 10 during Stage 2 with positive GEX = dealer hedging will fade the pullback, providing mechanical buying support at the EMA."

**03 — Trade implication.** What action follows? Specific entry, direction, instrument, and timing.

**04 — Sizing.** How big? From explicit loss budget, not intuition.

**05 — Invalidation.** What kills the trade? **Pre-committed** in writing. Not "I'll see how it goes."

### Critical distinction: risk vs position size

"Risk 1% of portfolio per trade" means: **if the stop is hit, the realized dollar loss equals 1% of total portfolio value**. It does NOT mean "deploy 1% of capital."

Position size = Dollar risk budget / Stop distance.

For $500k risking 1% ($5,000) with $6 stop on $600 underlying:
- Position size = $5,000 / $6 = 833 shares
- Notional deployed = 833 × $600 = $500k = **100% of portfolio**

Correct sizing: 1% **risk**, 100% **notional**. Acceptability depends on:
- **Liquidity** — can you exit cleanly under stress?
- **Margin** — do you have buying power?
- **Correlation** — what's the aggregate risk with existing positions?
- **Gap risk** — can the stop blow through?

For options, notional is bounded by premium (long) or collateral (short). The risk-to-notional ratio is structurally different from equity.

**Common mistake A:** interpreting "1% sizing" as "1% notional deployed" → under-sizes by 50-100× and the framework's edge never realizes.

**Common mistake B:** interpreting "1% risk" as "1% notional" → over-sizes by buying $500k of underlying without thinking about the stop → 5% adverse move = $25k loss, not the planned $5k.

[INTERACTIVE: position-size-clarifier]

### Position sizing from explicit loss budget

```
n ≤ ⌊ B_exp / L_max ⌋

where:
- B_exp is the explicit dollar loss budget you're willing to absorb on this trade
- L_max is the per-unit (per-contract or per-share) loss at your stop
```

**Worked example:** $500,000 portfolio. Maximum risk per trade is 1% = $5,000. Trend Pullback trade on XSP with a clear technical stop $20 below entry.

```
B_exp = $5,000
L_max = $20 × 100 (multiplier) = $2,000 per contract
n ≤ ⌊5,000 / 2,000⌋ = 2 contracts
```

[INTERACTIVE: position-size-calculator]

### Kelly and loss-budget — same framework, different unit

Section 2E derives the Kelly criterion as the bet fraction that maximizes expected log compound growth. This section's loss-budget rule (n ≤ ⌊B_exp / L_max⌋) sizes from a per-trade dollar cap. A reader emerging from 2E thinks Kelly is the answer; one emerging from here thinks loss-budget is. They are not in conflict; they answer different questions and converge for honest retail-scale edges.

**Both frameworks size positions; the question each answers differs.**

- **Kelly maximizes expected log growth.** Output: a *capital fraction* under an assumed bet-outcome geometry (binary win G / lose L per unit bet). The criterion assumes you have estimated edge correctly and that you are willing to commit the full Kelly bet to a single opportunity.
- **Loss-budget bounds dollar loss per trade.** Output: a *position size* under a stop-distance geometry. The criterion makes no claim about long-run growth optimality — it caps drawdown contribution from any single trade.

**Where they converge.** For a typical retail edge — say 52-55% win rate with near-symmetric payoffs — Kelly recommends a fraction in the 4-10% range. Half-Kelly halves that; quarter-Kelly quarters it. For modest edges, the quarter-Kelly dollar bet sits near the dollar loss the loss-budget rule produces at 1% risk per trade with a typical stop distance. The two frameworks land in roughly the same dollar position because the underlying anchor — "size in proportion to honest edge, not to confidence" — is the same.

**Where they diverge — case 1: diversification.** Kelly is per-strategy. If you run five uncorrelated strategies each at quarter-Kelly, aggregate exposure is the sum (potentially ~12.5% of capital at risk simultaneously). Loss-budget is per-trade and caps each trade at 1% independently; aggregate is bounded only by the number of simultaneously open trades. For a portfolio running 10 concurrent trades at 1% each, loss-budget tolerates 10% aggregate at-risk capital. Kelly-aggregated comparable portfolios at quarter-Kelly tolerate roughly the same. **The two frameworks agree on aggregate exposure ceilings when you do the arithmetic, which is exactly where retail traders fail to do the arithmetic.**

**Where they diverge — case 2: edge uncertainty.** Kelly assumes edge is known. Over-estimating edge produces over-betting, and the Kelly utility function is concave — the penalty for over-betting exceeds the gain from under-betting. If your edge estimate has 30% standard error (typical for backtest-derived estimates), point-estimate Kelly betting is meaningfully too aggressive. Loss-budget is robust to this: it caps loss regardless of edge correctness. For traders who don't trust their edge estimate (which is most traders, including this book's intended reader), **loss-budget is the safer first-line tool**; Kelly is a sanity check on whether the aggregate of those loss-budgeted positions is plausible.

**Operational rule for this book's framework.** Size individual trades by the loss-budget rule (1% risk per trade, stop-distance-scaled). Use Kelly as a sanity check on the aggregate: if your loss-budget-derived positions across the open book imply ≥30% capital at simultaneous risk, you are effectively past half-Kelly even if no single trade exceeds 1% risk. Either reduce concurrent positions, tighten the per-trade budget, or recheck the edge estimates that justified taking that many trades at once. Section 2E's worked example shows the per-trade chain end-to-end; this section's job is to keep the *aggregate* honest.

### The 25% drawdown / 30-day cool-off

**When portfolio drawdown crosses 25% peak-to-trough, all discretionary tactical activity halts for 30 days.** Mechanical sleeves (if any) continue running; new entries are suspended.

Four reasons: drawdowns produce sub-optimal decision-making; forced halt prevents revenge trading; mechanical systems continue running; knowing the cool-off exists makes the drawdown less catastrophic psychologically.

The 25%/30-day rule is binding regardless of how good the next setup looks. **The rule exists precisely to override your judgment during the period when your judgment is most compromised.**

### Kill rules at three levels

**Strategy-level kill rules (per setup):**
- Trend Pullback: close below the entry-day low OR time stop at 5 days
- Compression Breakout: close back inside the consolidation range OR time stop at 7 days
- Undercut and Reclaim: close below the undercut low OR time stop at 3 days
- IBS + RSI Mean Reversion: 21-EMA reclaim achieved OR time stop at 3 days

**Sleeve-level kill rules (per strategy bucket):**
- If 3 of last 5 swing trades are losers: pause new entries for 1 week, review the framework
- If sleeve drawdown > 15% peak-to-trough: reduce sizing 50% for next month
- If sleeve drawdown > 25% peak-to-trough: pause for 30 days

**Portfolio-level kill rules:**
- Portfolio drawdown > 25% PTP: halt all discretionary tactical for 30 days
- Personal behavioral state degraded: halt new entries for 1 week minimum
- Account margin cushion < 30%: force-deleverage by closing smallest tactical positions first

[INTERACTIVE: behavioral-state-checklist]

### The selectivity principle

Retail traders bias toward action because action feels productive. Doing nothing feels lazy. **The data systematically rewards the opposite: doing nothing is the highest-EV move on most days.**

Empirically, a competent swing trader running this framework should expect:

- **Most days: no new positions.** 60-70% of days produce no qualifying setups.
- **Most weeks: 1-3 new positions** across the entire watchlist.
- **Most months: 6-12 positions** with explicit conviction scores ≥ 0.5.

The pipeline imposes selectivity by structure: most observations don't pass interpretation; most interpretations don't pass conviction; the trades that exist have all four gates clear. **This is the system working, not failing.**

---

## 12D · Ten worked swing-trade examples

Each example follows the same five-step structure: **Question → Setup → Walkthrough → Conclusion → What this teaches**. The cumulative effect of working through ten of these is to internalize the pattern of disciplined swing-trade reasoning.

### Example 1: Trend Pullback that worked

**Question:** SPX in clear Stage 2, Friday close shows RSI(2) at 8 after a 1.2% pullback to the 21-EMA. Composite +45. Take the trade?

Conviction: E=0.85, M=0.90, R=0.85, X=0.90, S=0.90 → **C = 0.527 (high)**. Take at full size. Monday opens slightly higher; entry at 5,955; exit on Wednesday at 6,040 for $850 profit per contract.

**Lesson:** When all factors align, take the trade at the conviction-implied size.

### Example 2: Trend Pullback that failed

**Question:** Same setup geometry as Example 1, but composite signal is only +15.

Conviction: R=0.55 → **C = 0.343 (medium)**. Take at reduced size. SPX rallies briefly then sells through Friday's low. Stop hit at 5,920, loss = $3,500 (140% of planned loss).

**Lesson:** Lower R = lower size. Same setup geometry produces different outcomes in different regimes.

### Example 3: Compression Breakout — taking it correctly

**Question:** SPY consolidating in a 2.5% range for 9 sessions. ADX falling to 15. VIX 13. Composite +60. Breakout above the range high on 145% volume.

Conviction: E=0.75, M=0.85, R=0.90, X=0.95, S=0.90 → **C = 0.491**. Take. SPY rallies to target at 608 over 8 sessions. $4,350 profit. ~1.7R.

**Lesson:** Range expansions in positive-GEX regimes carry dealer-hedging tailwinds.

### Example 4: Compression Breakout — fakeout

**Question:** Same SPY setup as Example 3, but VIX 19 and composite +5.

Conviction: R=0.35 → **C = 0.191 (insufficient)**. Pass. SPY rallies briefly to 595 then fails back into the range on day 2. By day 7 SPY is at 572 — a 3.5% loss from the failed-breakout high.

**Lesson:** **The trades you don't take are as important as the trades you do.**

### Example 5: Undercut and Reclaim

**Question:** AAPL undercut-and-reclaim of the 200-day MA on a clean intraday reversal.

Conviction: E=0.65, M=0.80, R=0.75, X=0.85, S=0.85 → **C = 0.282 (medium-low)**. Take at reduced size. AAPL hits time stop at 172 for $1,000 profit. 1R.

**Lesson:** Undercut-and-Reclaim has lower E than Trend Pullback. Treat the framework's outputs literally — smaller conviction = smaller size.

### Example 6: IBS + RSI Mean Reversion

**Question:** QQQ closes near the day's low (IBS = 0.14). RSI(2) = 9. Stage 2. Composite +35.

Conviction: → **C = 0.413**. Take.

**Trade plan with explicit R math.** Entry $513.50 (today's close). Stop $511.50 (below today's low at $513.00 with a $1.50 noise buffer; the buffer matters because IBS mean reversion fails most often on a gap that takes out the low intraday before turning). **Initial risk = $2.00 per share.** Planned risk budget: $10,000 → position size = 5,000 shares.

QQQ gaps up the next morning and rallies to a high of $518.50. Exit on the close at $518.00 (above today's high at $517.00 by a buffer; the rule is "close above prior high"). **Realized P&L = ($518.00 − $513.50) × 5,000 = $22,500.** R-multiple = $4.50 / $2.00 = **2.25R**.

**Lesson:** Combining indicators that measure *different features* (IBS = intraday; RSI(2) = multi-day) is genuine confluence. The narrow-but-realistic stop (wide enough to survive the morning noise on a volatile index ETF) is what makes the strategy survive over a sample of trades; setting the stop $0.20 below the low produces a much higher R *on the winners* but stops the strategy out of half the trades that would have worked, destroying the expectancy. Beware the "narrow stop = high R" fantasy: in practice, narrow stops below natural noise levels just turn winners into losers.

### Example 7: FOMC overlay — sizing reduction

**Question:** Two days before FOMC. SPX in clean Trend Pullback setup. Composite +40.

Conviction: R=0.70 (event uncertainty), S=0.75 → **C = 0.342**. Take at 50% of full size. FOMC unchanged; vol crush gives 0.5R × half size = 0.25R.

**Lesson:** Reducing size during event-risk windows protects against path-dependent downside while preserving optionality on the favorable outcome.

### Example 8: Pre-earnings momentum screen — when to skip

**Question:** NVDA momentum signal firing 5 days before earnings. Implied move ±9%.

Conviction: E=0.55, M=0.65, R=0.80, X=0.85, S=0.40 → **C = 0.097 (insufficient)**. Pass. NVDA gaps 7% on earnings.

**Lesson:** Event-week single-name positions need defined-risk structures, not naked equity. **The trades you skip are sometimes the trades that would have hurt you most.**

### Example 9: Stop discipline — the migrating stop

**Question:** Long SPY at 580. Stop at 575. Position now at 576.50. Move the stop to 572?

**Conclusion:** Keep stop at 575. Triggers at 574.20 = $580 loss. Alternative (migrated): stops at 570.50 = $950 loss. **64% more loss than original plan.**

**Lesson:** **Stops exist to terminate failed theses, not to be argued with.** Once committed, the only allowable change is closing the trade *early*, never moving the stop further.

### Example 10: Sizing from the loss budget — multi-position interactions

**Question:** Two correlated setups firing: SPY Trend Pullback and AAPL Undercut-and-Reclaim. Both pass conviction. How to size?

**Use portfolio-level loss budget**, not per-trade. Max simultaneous risk: 2% portfolio = $8,000. Allocate $5,000 to SPY, $3,000 to AAPL.

**Lesson:** **Correlated positions share risk.** Per-trade sizing as if each trade were independent overstates total exposure. Use portfolio-level budgets when multiple correlated trades are active.

### Patterns that recur across the examples

1. **The same setup geometry in different regimes produces different outcomes.**
2. **The trades you skip are as informative as the trades you take.**
3. **Kill rules exist to override behavioral intuition.**
4. **Position sizing comes from explicit loss budgets**, not from intuition.
5. **Single-name event risk requires defined-risk structures**, not naked equity exposure.
6. **Correlation between positions matters** even when the setups are nominally different.
7. **The simpler setup often wins**: Trend Pullback is high-evidence, mechanism-clear, regime-sensitive — the simplest archetype is often the most profitable.

---

## 12E · Setup cards for swing-trade archetypes

Setup cards compress each strategy into the form needed for live execution: **edge source, regime requirement, sizing, invalidation, common failure modes**. The cards are designed to be printed, taped next to your monitor, copied into a trading journal. Their value is in being **binding** when you are tempted to override them.

### Trend Pullback / Reclaim

| Field | Specification |
|---|---|
| **Edge source** | Mean reversion within Stage 2 trend; dealer-hedging support at moving averages |
| **Evidence tier** | Tier A (Connors RSI(2), Jegadeesh-Titman, dealer-mechanics framework) |
| **Regime** | Composite ≥ +30; Stage 2 confirmed (30-SMA rising, ADX 20-30); positive GEX |
| **Vehicle** | XSP (preferred for tax) or SPY/QQQ options; equity for liquid single names |
| **Entry trigger** | RSI(2) < 10 OR IBS < 0.20 on pullback to 10/21-EMA; reclaim of EMA on intraday confirmation |
| **Sizing rule** | Risk 1-1.5% portfolio per trade; n ≤ ⌊B_exp / L_max⌋ |
| **Profit target** | 1.5-2R OR close above prior 5-day high, whichever first |
| **Time stop** | 5 trading days |
| **Invalidation** | Close below entry-day low OR 30-SMA slope turns negative |
| **Common failure** | Setup fires during composite < +20 (regime weakening); rolls over instead of bouncing |
| **Skip when** | VIX > 25; backwardated term structure; ADX > 30; composite < +20 |

### Compression Breakout

| Field | Specification |
|---|---|
| **Edge source** | Range expansion after vol contraction; dealer hedging tailwind in positive-GEX regime |
| **Evidence tier** | Tier B/C (VCP / Minervini practitioner support) |
| **Regime** | Composite ≥ +30; ADX falling toward 15; volume contracting; positive GEX |
| **Vehicle** | Equity directly OR bull call spread for defined risk |
| **Entry trigger** | Price breaks above range high OR VCP pivot on volume ≥ 130% of 20-day average |
| **Sizing rule** | Risk 1% portfolio per trade; entry slightly above breakout level |
| **Profit target** | Range width above breakout level OR 2R, whichever first |
| **Time stop** | 8 trading days |
| **Invalidation** | Close back inside the prior range within 2 sessions |
| **Common failure** | Fakeouts on weak volume |
| **Skip when** | Volume on breakout < 100% of 20-day average; composite weakening; VIX > 22 |

### Undercut and Reclaim

| Field | Specification |
|---|---|
| **Edge source** | Stop-run dynamics at well-known technical levels (200-day MA, prior swing lows) |
| **Evidence tier** | Tier B (Minervini, short-covering literature) |
| **Regime** | Composite ≥ +10 (less regime-sensitive than Trend Pullback) |
| **Vehicle** | Equity directly OR bull call spread |
| **Entry trigger** | Intraday low penetrates major technical level; close back above by EOD |
| **Sizing rule** | Risk 0.5-1% portfolio per trade |
| **Profit target** | Next overhead resistance level OR 1.5R |
| **Time stop** | 3 trading days |
| **Invalidation** | Close below the undercut low (rejection of the reclaim) |
| **Skip when** | VIX > 22 (stop-runs become bear flag continuations); composite < 0 |

### IBS + RSI Mean Reversion

| Field | Specification |
|---|---|
| **Edge source** | Combining intraday positioning (IBS) with multi-day oscillator (RSI(2)) |
| **Evidence tier** | Tier A (Connors documented IBS + RSI strategies have multi-decade replication) |
| **Regime** | Stage 2 confirmed; composite ≥ +20; positive GEX above flip |
| **Vehicle** | QQQ or SPY equity for cleanest execution |
| **Entry trigger** | IBS < 0.20 AND RSI(2) < 15 on close |
| **Sizing rule** | Tight stops permit larger size: risk 1% portfolio; stop at intraday low |
| **Profit target** | First close above entry-day high OR 1R |
| **Time stop** | 2 trading days |
| **Invalidation** | Close below intraday low of entry day |
| **Skip when** | Composite < +15; ADX > 30; VIX rising 5+ points in last 3 days |

### Risk overlay cards

**FOMC week overlay:** Active T-2 to T+1. Reduce all new entries to 50% of normal size. Widen stops by 50%. Skip any new entry where stop distance × 1.5 exceeds 2× normal portfolio risk. Look for vanna-unwind opportunities in the 60-90 minutes after the announcement.

**Earnings overlay:** Active T-2 to T+2 for any position in the affected name. Single-stock positions: close before earnings or convert to defined-risk options structure. Permitted: Long call spread, long put spread; never naked equity or naked options through earnings. Verify position size such that the implied move would not produce > 2% portfolio loss.

### Do-not-trade reference cards

These cards exist to inoculate against narrative-driven retail bait.

**🚫 Buying the Friday rip into Monday.** Charm-driven Monday-morning flow is roughly 10-20 bps on average — insufficient to justify a swing trade. **Mechanical effects exist but are usually too small to be tradeable as standalone signals.**

**🚫 Pre-FOMC drift.** Lucca-Moench (2015) documented 49 bps pre-FOMC return 1994-2011. Kurov et al. (2021) found the effect disappeared post-2015. **Mechanism-clear edges can decay suddenly when the underlying institutional context changes.**

**🚫 Earnings short-vol on single names.** Adams-Neururer (2020): NEGATIVE mean despite positive median at retail. The structural negative skew on single-stock earnings exceeds the premium collected. **Win rate ≠ EV.**

**🚫 GEX level scalping.** Models are vendor-dependent; post-2022 0DTE has changed structure; Cboe 2025 data shows 0DTE MM hedging is ~0.2% of futures liquidity. **Narrative compellingness ≠ evidence quality.** Use GEX sign as a regime indicator, not as a level-by-level scalping signal.

**🚫 Systematic iron condors.** CBOE CNDR index 1986-2024: ~690% total return vs SPX total return ~5,500%. **38 years of empirical underperformance is decisive.** Wing breaks during stress dominate the long-run distribution.

**🚫 Holding through events on full size.** Event-day implied moves are typically 1.5-3× normal daily range. Standard swing stops can gap through entirely. Either close before the event or convert to defined-risk structure.

**🚫 Revenge trading after a loss.** Post-loss trades show systematically worse outcomes. The 25%/30-day cool-off rule is the structural defense; day-level discipline is to **simply not trade for the rest of the session** after taking a planned loss.

### How to use these cards

Print or copy the cards relevant to your portfolio. Reference *before* trading — verify every condition is met. Update on regime change. Review quarterly — confirm kill rules haven't triggered. Annual recalibration.

**The cards are deliberately rigid.** Discretion lives at the observation step (12C); the cards constrain the execution step. **Discretion at observation, mechanism at execution.**

### The book in one paragraph

Classify any new "edge" by source (risk premium / behavioral / institutional / microstructure). Score conviction (E × M × R × X × S). Apply the four-layer retail haircut. Stress-test S1-S4. Specify the kill criterion at all three levels. Then size for survivability using n ≤ ⌊B/L⌋. **If you do this consistently, you'll filter ~80% of retail trading content as low-conviction or rejected, and the remaining 20% will be sized appropriately to anchor a multi-decade portfolio.**

The framework's success depends not on finding rare edges but on **operating consistently with the edges that are available**. Most retail traders have access to the same setups, the same indicators, the same information. The differences in outcomes come from differences in execution discipline.

Everything else in this book was the context that justifies the discipline.

---

## 12F · Aggregate vega management — the portfolio-level vega framework

Sections 5-9 cover vega thoroughly at the single-position level: what it measures, how it scales with DTE and IV, how vanna and volga refine it. What they don't address is what happens when you have **five short-premium positions running simultaneously**. The aggregate vega exposure of a swing portfolio is rarely discussed in retail education, and it is the single largest source of catastrophic loss in real premium-selling portfolios. This section closes that gap.

### Why position-level vega is insufficient

Consider a swing trader running, simultaneously:
- One SPX iron condor (short vega)
- Two short put credit spreads on SPY (short vega)
- One short strangle on QQQ (short vega)
- A covered call program on individual stocks (short vega)
- A LEAP collar on a core equity holding (mixed)

Each position, viewed alone, looks reasonable. The trader has assigned each position 1-2% of portfolio risk. But the **aggregate vega exposure** — the total dollar P&L impact per vol point of VIX movement — is typically the equivalent of being short several hundred SPX vega units. When VIX moves from 15 to 25 over three days (a routine stress episode, not a tail event), the mark-to-market loss across the portfolio can exceed the sum of individual position stop-loss budgets — because vega losses compound across positions before any single stop is triggered.

This is the **vega correlation problem**: short-vega positions across SPX, SPY, QQQ, and individual stocks are *not* diversified. They all lose simultaneously in a VIX-spike regime. The "1% per trade" sizing rule that works perfectly well for delta exposure produces concentrated portfolio risk on the vega axis.

### The aggregate vega framework

For each position, compute:

```
position_vega_$ = vega_per_contract × number_of_contracts × multiplier × position_sign
                  × 0.01    (to convert to dollar P&L per 1 vol point IV change)
```

Where `position_sign = +1 for long, -1 for short`.

**Adjust for VIX beta of the underlying** (single-name vega doesn't move 1:1 with VIX):

```
adjusted_vega_$ = position_vega_$ × β_underlying_to_VIX
```

Typical VIX betas:
- SPX, SPY: 1.00 (definitional — VIX is SPX's vol)
- QQQ: 0.85-0.95 (high-beta, slightly lower IV vol than SPX)
- IWM: 0.80-0.90
- Large-cap individual stocks (NVDA, MSFT, AAPL): 0.60-0.85 (varies by company)
- Mid/small caps: 0.40-0.65 (idiosyncratic IV less correlated with VIX)

**Aggregate portfolio vega** = sum across positions:

```
Portfolio_Vega_$ = Σ_i adjusted_vega_$ᵢ
```

For a swing-oriented retail account ($250k-$1M), a reasonable upper bound on aggregate short vega is **$500-$1,500 per vol point** (meaning a 10-point VIX spike costs $5-15k mark-to-market). Beyond that, the portfolio becomes a directional bet on VIX rather than a diversified swing book.

### Monitoring cadence

- **Daily** (end of day): compute aggregate vega using current marks. Compare to last week's number; large changes warrant investigation.
- **Weekly** (Friday close): full report — aggregate vega, per-position contribution, % of portfolio NAV that a 10-vol-point spike would cost.
- **Pre-event**: before FOMC, CPI, NFP, or major single-name earnings the portfolio is exposed to, recompute aggregate vega. Consider trimming if elevated.
- **Stress threshold**: when aggregate short vega exceeds 1% of NAV per vol point, the portfolio is over-concentrated; trim or hedge before adding new short-premium positions.

### Hedging short vega — the macro vega overlay

Three practical hedges for an over-concentrated short-vega book:

**1. Long-dated VIX calls (90-180 DTE)**. The cleanest macro vega hedge. Strike selection: VIX 25-30 (well above VIX9D-3M mean of ~17). Sized to cover **half** of aggregate short vega — a full hedge is too expensive in carry and defeats the VRP harvesting purpose. Roll quarterly.

**2. Long SPX puts (90-180 DTE) at 90-92% strikes**. Carries direction along with vega. Cheaper than VIX calls in absolute dollar terms but more correlated with the delta book (so less pure as a vega-only hedge). Useful when the swing portfolio is already net long delta.

**3. Long-dated SPX call spread or put spread purchases (60-90 DTE)**. Defined risk; small positive vega exposure. Less powerful than the above but cheaper. Useful as a partial offset when the short vega is modest (<0.5% of NAV per vol point).

**Anti-pattern: don't try to hedge short vega with more options sales.** Selling deeper-OTM puts to "fund" the hedge increases aggregate short vega rather than reducing it. The hedge must consume premium, not generate it.

### Common failure modes

**Failure mode 1 — Stealth vega accumulation.** A trader adds one Iron Condor per month for six months. Each one looks like 1% risk. The aggregate vega has grown to 6× single-position size, but no single decision triggered review. Mitigation: track aggregate vega as a portfolio-level metric, not just per-position risk.

**Failure mode 2 — Pre-event hedge sizing too small.** Before an FOMC meeting, the trader buys $500 of VIX calls "for protection" against a portfolio with $1,200/vol-point short vega exposure. The hedge is too small to matter. Mitigation: size hedges as a fraction of the gross exposure they're hedging (e.g., 30-50%), not as a fraction of free cash.

**Failure mode 3 — Hedging with same-month VIX calls.** Short-dated VIX calls have catastrophic theta decay (VIX vol-of-vol is high; charm collapses the value quickly). Long-dated calls cost more in absolute dollars but decay slower, providing real protection across multi-week stress windows.

**Failure mode 4 — Forgetting the LEAP collar isn't short vega.** A covered call on stock + protective put (the classic LEAP collar) is approximately vega-neutral. Don't double-count it as short vega in the aggregate.

[INTERACTIVE: vega-portfolio-monitor]

The `vega-portfolio-monitor` widget lets you input up to six positions, each with instrument, DTE, delta, vega per contract, and number of contracts. It computes aggregate vega, applies VIX-beta adjustment per instrument, and shows the estimated P&L impact of +5, +10, and +15 vol-point VIX spikes. A secondary panel sizes the macro vega overlay needed to offset the short-vega exposure to a user-chosen target (flat vega, half-vega, or full hedge).

---

### Appendix: Trade Journal Template

For systematic framework application, every trade should be logged with the following fields. Implement in any tool (Notion, Obsidian, Sheets, plain markdown) — keep the field set consistent across trades.

```
Trade ID: YYYY-MM-DD-N

═══ PRE-TRADE ═══
Date / Time of decision:
Symbol / Instrument:
Setup type: [Trend Pullback | Compression Breakout | Undercut and Reclaim | IBS+RSI | Pre-earnings momentum | Other]
Macro regime (composite signal):
Stage classification:
Required conditions (check all):
  [ ] Composite signal conditions met
  [ ] Setup-specific entry trigger fired
  [ ] No event-day overlay restrictions
  [ ] Position size within portfolio limits
  [ ] Conviction score:
        E (evidence):
        M (mechanism):
        R (regime):
        X (execution):
        S (sizing):
        C (product):

═══ EXECUTION ═══
Mid price at decision:
Limit order submitted:
Fill price:
Fill time:
Bid-ask spread at fill:
Slippage vs mid (bps):
Time of day:

═══ POSITION ═══
Risk budget (dollar):
Risk budget (% portfolio):
Entry price:
Stop level:
Position size:
Notional deployed:
Notional as % of portfolio:
Time stop:
Profit target:

═══ MANAGEMENT ═══
[Adjustments during trade — additions, partials, stop moves]
[Allowed: stop trailed UP on winners, or full exit. NO stop migration toward profit.]

═══ OUTCOME ═══
Exit reason: [profit target | stop | time stop | discretionary | event-driven]
Exit price:
Exit time:
Days held:
P&L (dollars):
P&L (% of portfolio):
R-multiple (P&L / risk budget):

═══ POST-TRADE REVIEW ═══
What went as planned:
What surprised me:
Errors made:
Framework lessons:
Should I have skipped this trade in hindsight? Why?
Did the regime change during the hold?
```

Three principles:

1. **Write everything before the trade**: pre-trade fields are filled before you click buy. This catches lazy setups.
2. **Don't editorialize outcomes**: record what happened, not what should have.
3. **Review monthly**: scan the prior 4-6 weeks of trades, look for patterns — which setups produced positive R-multiples, which regimes worked.

The journal is the framework's external memory. Without it, the framework cannot improve over time.
