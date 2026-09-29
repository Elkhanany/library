# Chapter 4 — High-conviction moves
## A formal definition and the conviction score

> **Core intuition.** "High conviction" is not "I believe in this trade strongly." It's a trade where independent evidence layers converge: positive expected value after costs, survivable tail loss, low margin-breach probability, and acceptable correlation to existing exposures. If any of these layers fail, the conviction collapses regardless of how strong the signal feels.

---

## 4.1 The reviewer's challenge

The reviewer of v2 raised a problem: the document didn't define "high conviction" formally. Without a definition, the framework is just a collection of edges with no clear threshold for action. This chapter solves that.

The proposed test:
$$\text{Trade if: } \hat{\mu}_\text{net} > 0, \quad \text{ES}_{95} < L_\text{max}, \quad P(\text{margin breach}) < \epsilon, \quad \rho_\text{tail} \text{ acceptable}$$

In plain English:
- Expected value must be positive after costs
- Tail loss must be survivable
- Margin failure probability must be low
- Correlation to existing positions in stress must be acceptable

These four conditions are *necessary* but not jointly sufficient — strong evidence and good mechanism design also matter. So we extend to a five-domain score.

---

## 4.2 The conviction score

For any candidate move $i$ at time $t$:

$$C_i(t) = E_i \times M_i \times R_i(t) \times X_i(t) \times S_i$$

Where each factor scores 0-1:

| Factor | Domain | What it measures |
|---|---|---|
| $E_i$ | **Evidence quality** | Tier-based: T1 (peer-reviewed, replicated) ≈ 0.8-1.0; T2 (strong empirical) ≈ 0.5-0.8; T3 (thin/decayed) ≈ 0.0-0.4 |
| $M_i$ | **Mechanism clarity** | Why does this edge exist? Is the source identified? Risk premium / behavioral / institutional / microstructure ≈ 0.7-1.0; "I don't know why this works" ≈ 0.0-0.3 |
| $R_i(t)$ | **Regime alignment** | Is the current regime supportive? VIX backwardated for short-vol ≈ low; trend in middle of drought ≈ low; FOMC even-week for equity ≈ high |
| $X_i(t)$ | **Execution feasibility** | Can I actually trade this? Liquidity, spread, fill quality, operational complexity. Liquid ETF ≈ 0.9-1.0; multi-leg index option ≈ 0.5-0.7; thin single-name option ≈ 0.2-0.4 |
| $S_i$ | **Sizing survivability** | Can I size this so S2 is operational and S3 is recoverable? With explicit kill criteria? |

**Multiplicative form is the key feature.** Any factor at 0 makes the entire product 0. A trade with strong evidence (E=0.9) but poor regime (R=0.2) has C=0.18, not high conviction. A trade with great mechanism (M=0.9) but unsurvivable sizing (S=0.1) has C=0.09. Each domain is a *necessary* condition; you can't compensate for a 0 in one domain with a 1 in another.

### Threshold for action

Define:
- **C ≥ 0.5:** high conviction, allocate
- **0.3 ≤ C < 0.5:** medium conviction, small allocation or test sizing
- **C < 0.3:** insufficient conviction, do not trade

These thresholds are heuristic but disciplined. The point isn't the exact number — it's the multiplicative structure that forces every domain to clear the bar.

---

## 4.3 Worked example: VRP harvest in different regimes

Consider XSP cash-secured ATM monthly put-write at 15% of portfolio.

### Scenario A: VIX 14, contango, normal regime
- $E$ = evidence quality. T1 (Bondarenko, Carr-Wu, Jurek-Stafford). Score: **0.85**
- $M$ = mechanism. Risk premium with clear theoretical foundation. Score: **0.90**
- $R(t)$ = regime. VIX low-normal, contango, no impending event. Score: **0.85**
- $X(t)$ = execution. XSP is liquid, spreads tight, easy to roll. Score: **0.90**
- $S$ = sizing. 15% of portfolio is well within survivability bounds; cash-secured eliminates margin risk. Score: **0.90**

$C = 0.85 \times 0.90 \times 0.85 \times 0.90 \times 0.90 = 0.53$

**High conviction. Allocate.**

### Scenario B: VIX 28, backwardated 5 days, post-CPI shock
- $E$ = same evidence. **0.85**
- $M$ = same mechanism. **0.90**
- $R(t)$ = regime. VIX backwardated → strategy kill criterion would trigger. Score: **0.20**
- $X(t)$ = execution. Spreads wider in volatility but still tradeable. Score: **0.65**
- $S$ = sizing. Scaling down is mandatory in this regime; full 15% allocation is unsafe. Score: **0.40**

$C = 0.85 \times 0.90 \times 0.20 \times 0.65 \times 0.40 = 0.040$

**Insufficient conviction. Do not enter new positions; reduce existing.**

The same strategy, same evidence, same mechanism — but regime alignment and sizing survivability collapse. C drops by an order of magnitude. **This is what discipline looks like.**

### Scenario C: VIX 18, normal, but allocating 50% of portfolio
- $E$ = **0.85**
- $M$ = **0.90**
- $R(t)$ = **0.85**
- $X(t)$ = **0.90**
- $S$ = sizing. 50% notional in short puts means a 30 VIX/-20% gap likely force-liquidates. Score: **0.20**

$C = 0.85 \times 0.90 \times 0.85 \times 0.90 \times 0.20 = 0.117$

**Insufficient conviction.** Same exact strategy, but oversized. The evidence and regime don't matter when sizing is wrong. The conviction framework correctly catches this.

---

## 4.4 Worked example: GEX-level scalping

Consider "buy SPX at the put wall, sell at the call wall" using SqueezeMetrics or SpotGamma data.

- $E$ = evidence. Academic literature on dealer gamma (Garleanu-Pedersen-Poteshman) supports *directional* effects; specific level-trading rules don't validate post-2022. Cboe 2025 study found 0DTE MM hedging is ~0.2% of liquidity. Score: **0.25**
- $M$ = mechanism. The general gamma-hedging story is plausible; the specific level-trading mechanism (dealers must hedge at exactly these strikes) is not robustly supported and depends on assumptions about who's long/short which strikes. Score: **0.30**
- $R(t)$ = regime. Sometimes dealers are net long gamma, sometimes short. Public GEX models don't reliably distinguish. Score: **0.40**
- $X(t)$ = execution. Liquid SPX, but the strategy requires specific intraday entries near the wall — high execution complexity. Score: **0.50**
- $S$ = sizing. Stop placement is unclear (where do you stop if the wall doesn't hold?), and crash risk is asymmetric (wall fails, you're caught long puts). Score: **0.35**

$C = 0.25 \times 0.30 \times 0.40 \times 0.50 \times 0.35 = 0.005$

**Effectively zero conviction.** This isn't a knock on the user — it's the framework correctly identifying that a popular strategy doesn't pass even basic conviction screening. Most of its appeal is narrative; the multiplicative structure exposes that.

---

## 4.5 Worked example: Trend-following allocation via DBMF

15% allocation to DBMF as a portfolio diversifier.

- $E$ = evidence. T1 (Hurst-Ooi-Pedersen, 140-year evidence; Moskowitz-Ooi-Pedersen). Score: **0.90**
- $M$ = mechanism. Multiple complementary mechanisms (under-reaction, hedger compensation, liquidity provision). Decomposition is well-understood. Score: **0.85**
- $R(t)$ = regime. Trend has been mixed in 2023-24, in a drought between strong years. Score: **0.55** (don't allocate at peak; current is mid-cycle)
- $X(t)$ = execution. DBMF is a single ETF, easy to buy. Score: **0.95**
- $S$ = sizing. 15% allocation is well within survivability; trend has positive crash skew (rare upside in stress). Score: **0.90**

$C = 0.90 \times 0.85 \times 0.55 \times 0.95 \times 0.90 = 0.36$

**Medium conviction.** The regime score is the binding constraint. This means: the *structural* allocation case is strong (high E, M, X, S), but timing the entry isn't great. Operational implication: build the position over time, don't lump-sum, and scale up if a drawdown creates a better entry point.

This kind of nuance is exactly what the conviction score is supposed to surface.

---

## 4.6 The trade-admission checklist

The conviction score is a number, but it should be backed by a written checklist. Every candidate move passes through this:

### Trade-admission checklist

- [ ] **Source identified.** Which of the four (risk premium, behavioral, institutional, microstructure)?
- [ ] **Category assigned.** Foundation premium, factor, overlay, filter, or rejected?
- [ ] **Evidence tier.** T1, T2, or T3? Cite the primary source.
- [ ] **Mechanism stated.** Why does this edge exist? What would make it disappear?
- [ ] **Academic Sharpe.** What does the literature suggest?
- [ ] **Retail haircut applied.** What's my realistic user-account Sharpe?
- [ ] **Regime check.** Is the current regime supportive? What would invalidate?
- [ ] **Tail loss calculated.** ES₉₅, S2 P&L, S3 P&L.
- [ ] **Margin behavior.** What's the margin expansion under stress?
- [ ] **Position size.** Survivable in S2 (operational), recoverable in S3 (no irrecoverable loss)?
- [ ] **Kill criteria.** Specific, measurable, pre-committed.
- [ ] **Correlation to existing book.** Does this duplicate exposures I already have?
- [ ] **Conviction score.** $C = E \times M \times R \times X \times S \geq 0.5$?

If you can't tick all 13 boxes, the trade isn't admission-ready. This isn't bureaucracy — it's the discipline that prevents 80% of bad trades.

### Why this beats intuition

Intuition correlates strategies with vivid narratives, not with edge quality. The checklist forces you to articulate each domain *separately* before committing capital. Stories die under separate analysis; real edges survive it.

---

## 4.7 The decision tree

When evaluating any candidate move, walk through this:

1. **What is this?**
   - Risk premium / behavioral / institutional / microstructure?
   - Foundation premium / factor / overlay / filter / rejected?

2. **Is the evidence robust?**
   - Peer-reviewed, multi-decade, replicated → T1
   - Strong empirical, sample-sensitive → T2
   - Thin or decayed → T3 (likely don't trade)

3. **What's the mechanism?**
   - Can I articulate why this works?
   - What would make it stop working?
   - Has anything changed that affects the mechanism?

4. **Does it survive the haircut?**
   - Apply academic → user-account haircut
   - Is realistic Sharpe still positive?
   - Is realistic Sharpe materially better than the simpler alternative (just hold SPX)?

5. **What's the worst-case path?**
   - SPX -10/-20/-35 stress P&L
   - Margin expansion
   - Force-liquidation risk

6. **What's the kill rule?**
   - Specific trigger
   - Pre-committed action
   - Revalidation criteria

7. **Compute the conviction score.**
   - C ≥ 0.5: allocate
   - 0.3-0.5: small or test
   - <0.3: don't trade

This isn't 7 separate analyses — it's one analysis structured to surface the issues that informal evaluation misses.

---

## 4.8 Common conviction failures

The framework identifies several recurring patterns that look like edge but score low:

### Pattern 1: Strong evidence, wrong regime
*Example: VRP harvest in backwardation.*
$E$ high, $M$ high, $R(t)$ low. Conviction collapses. Operational rule: respect the regime filter even when the underlying evidence is strong.

### Pattern 2: Right idea, oversized
*Example: 50% of portfolio in put-write.*
All other factors high, $S$ low. Conviction collapses. Operational rule: position sizing is multiplicative, not additive.

### Pattern 3: Beautiful theory, no mechanism
*Example: a backtested signal with strong historical performance but no clear reason it should work going forward.*
$E$ medium-high, $M$ low. Conviction collapses. Operational rule: backtest performance without mechanism is a warning sign; data mining produces high-Sharpe results in any sufficiently large sample.

### Pattern 4: Real edge, terrible execution
*Example: cross-sectional option mispricing requiring 200-name daily-rebalanced delta-hedged portfolio.*
$E$ high, $X$ low. Conviction collapses. Operational rule: edges that require infrastructure you don't have aren't edges for you.

### Pattern 5: Vivid narrative, weak evidence
*Example: GEX scalping based on dealer-positioning narrative.*
$M$ feels high (the story is compelling), $E$ is actually low. Conviction collapses. Operational rule: narrative compellingness is not evidence quality.

The conviction framework systematically catches all five patterns because the multiplicative structure forces every domain to score independently.

---

## 4.9 What the conviction score is NOT

A conviction score is not:

- **A guarantee.** High conviction trades still lose. The score measures expected risk-adjusted return after frictions, not certainty.
- **A reason to size big.** Even at C=0.7, sizing is determined by tail loss and portfolio context. Conviction tells you *whether* to trade; it doesn't tell you *how much*.
- **A backtest substitute.** The score is a thinking tool; backtests, stress tests, and live paper trading still have value.
- **A static number.** Regime ($R$) and execution ($X$) shift over time. The score updates as conditions change.

What the score *is*: a forcing function for honest, multi-domain evaluation before committing capital. It works because the multiplicative structure mirrors reality — you really can't compensate for unsurvivable sizing with great evidence, or for poor execution with strong mechanism.

---

## 4.10 Misconception box

> **Misconception:** "I have strong intuition about this trade, so I don't need to score it."
>
> **Correction:** Strong intuition is your unconscious applying patterns from your past experience. It's useful, but it's also exactly the channel through which behavioral biases enter. The conviction score forces conscious evaluation that surfaces issues your intuition skipped. If your intuition agrees with the score, you've cross-validated. If they disagree, one of them is wrong — and the score has a written audit trail you can review.

---

## 4.11 The signal-to-trade pipeline

Tying back to the reviewer's framing: every trade should pass through a pipeline:

$$\text{Observation} \rightarrow \text{Interpretation} \rightarrow \text{Trade implication} \rightarrow \text{Sizing} \rightarrow \text{Invalidation}$$

The conviction score is what gates the *trade implication* step. Observations and interpretations are constant; the conviction score determines whether they become positions. If conviction is insufficient, the observation is logged and watched but not traded.

This is what high-conviction trading looks like in practice: most observations don't generate trades. The trades that exist have all five domains checked, scored, and survived. This is the operational meaning of "selective."

---

## 4.12 Self-check

1. State the conviction score equation. Why is it multiplicative rather than additive?
2. Walk through the conviction score for a hypothetical trade you've considered. Identify the binding constraint (the lowest factor).
3. Why does "strong intuition" not satisfy any of the five domains?
4. What's the difference between $E_i$ (evidence quality) and $M_i$ (mechanism clarity)?
5. How does $R(t)$ change between scenario A and scenario B in §4.3? What's the operational implication?
6. Take a trade you'd consider "high conviction" right now. Score it. Is it actually high conviction?

---

## Where this fits

Chapter 0 gave us primitives. Chapter 1 gave us sources. Chapter 2 gave us why Sharpe lies. Chapter 3 gave us realistic retail expectations. Chapter 4 ties these together into a *decision rule*: the conviction score that determines whether a candidate move becomes a position.

Chapter 5 will introduce the five-category taxonomy, which determines how to *implement* a high-conviction move (foundation, factor, overlay, filter). Chapters 6-10 will populate the taxonomy with specific edges. Chapter 11 will provide worked examples that walk through the full conviction analysis for each major strategy.

The conviction framework is the spine. Every other chapter either defines the inputs to the score or applies it to specific strategies.

[← Previous: Chapter 3 — Retail haircut](04_ch03_retail_haircut.md) | [Next: Chapter 5 — Taxonomy →](06_ch05_taxonomy.md)
