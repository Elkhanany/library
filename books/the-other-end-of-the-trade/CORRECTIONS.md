# What the rewrite corrected

195 corrections to the two sources, collected by `tools/spx.py` from the "Changed" section of `notes/*.md`: the items that open with "Fixed" (found while rewriting) or "Checked:" (found by the second check of the maths). Each names the source it corrects (dl: the Dealer Mechanics Lab, spx: the Edge Book). Edit them in the notes, not here.

## 1A · What a return is

- Fixed: "The geometric mean ... is √(1.5 × 0.5) − 1 = −13.4% per pair." The expression is the geometric mean per period; per pair the loss is 1 − 0.75 = 25%. The text now gives both.
- Fixed: "+50%, −50%, ... ends in ruin." Wealth after k pairs is 0.75^k, which falls toward zero but never reaches it. The text says the sequence "grinds toward zero" and gives $100 → $5.63 after 10 pairs.
- Fixed: "With simple returns, the sum of percentage returns is not even well-defined as a distribution under most reasonable models." A sum of simple returns is well defined; it is just not the total return. The text now says what is true and matters: a normal simple return puts probability on prices below zero, and a product of normal growth factors is not normal, so the clean rule for adding periods is lost.

## 1B · The shape of returns

- Fixed: the sigma table (dl:1A). "3-sigma event: roughly 1 in 740 (twice per decade)": 1 in 740 trading days is once every 2.9 years, about three times a decade; the text gives 2.9 years. The 6-sigma row is made one-sided (above).
- Fixed: spx:0.1's worked example. "Strategy B: wins 95% of months by 1%, loses 5% of months by 14% on average. Same mean, same standard deviation, same Sharpe" as a strategy with a 5% mean and 10% standard deviation. Those numbers give a 3.0% annual mean and 11.3% volatility, a Sharpe ratio of 0.27, not 0.5. The text uses 1.08% and 12.17%, which give exactly 5% and 10%. Strategy A's "worst month −8%" is kept (2.9 standard deviations).
- Fixed: spx:2.3's misconception box, "A $1-credit / $9-max-loss put spread has −9× skew at a single-trade level". Skewness is not a multiple; the loss is nine times the gain. The worked example computes the spread's moments at a 90% win rate (mean 0, skewness −2.67, kurtosis 8.11), and the text shows that a two-outcome bet's skewness depends only on its win rate.
- Fixed: spx:0.2's misconception box, "A coin flip with −$1/+$0.10 payoff has 0% edge". A bet paying +$0.10 or −$1 has zero edge only at a 90.9% win rate; at the 80% of the misconception it loses $0.12 a trade. The text says so.
- Checked: strategy B's loss month, 4.36 standard deviations below its mean, has a normal probability of 1 in 153,800, so the text's "about 1 in 153,000, once in roughly 12,700 years" is now "about 1 in 154,000, once in roughly 12,800 years".
- Checked: after the reader drags the skew-simulator to −4 (standard deviation 0.63), the text said slider +3 has "the same standard deviation, 0.65" without saying the same as what. It is the same as at −3, the mirror-image shape (the figure draws the shapes for a and −a as mirror images), and the text now says "the same standard deviation as at −3".

## 1C · Expected value and edge

- Fixed: spx:2.2, "Sell a 90-delta short put for $0.50 of premium ... You win the $0.50 about 90% of the time." A put that expires worthless about 90% of the time is roughly a 10-delta put; a 90-delta put is deep in the money. The text describes the put by its win rate and calls it roughly 10-delta.
- Fixed: dl:1C's log-utility example. "A trade that has +$10,000 expected value on a $100,000 portfolio but a 5% chance of losing $80,000 has ... expected log return that is negative." With those numbers the winning branch gains $14,737 and the expected log return is +0.0501, positive, worth a sure $5,140. The text keeps the $80,000 case with the right arithmetic (log utility halves its value) and adds a $95,000 case, same dollar expectation, whose expected log return is −0.0127: the sign change the source meant to show.
- Fixed: dl:1C, "The payoff diagram of a short iron condor is identical to the payoff diagram of a long lottery ticket — limited risk, limited reward, in opposing geometries". "Identical" and "opposing" contradict each other. The text compares the short iron condor with its mirror image, the long iron condor.

## 1D · Risk-adjusted return

- Fixed: the ruin formula (dl:1D), "P(ruin to fraction f) ≈ f^(2μ/σ²)", with μ and σ "the drift and volatility of the levered strategy". For geometric Brownian motion with arithmetic drift μ the exact probability is f^(2μ/σ² − 1); the source's form holds only if μ is the drift of log wealth, μ − σ²/2. The text gives the exact form with a derivation and keeps "the ratio 2μ/σ² gets divided by k", which is true. The difference matters at high leverage: at four times, a Sharpe-0.5 strategy with 20% volatility halves with probability 84% (exact) against 42% (source form).
- Fixed: "Sortino is higher than Sharpe for any strategy with positive skew and lower than Sharpe for negative-skew strategies" (dl:1D). With the downside deviation measured below zero or the risk-free rate, the Sortino ratio exceeds the Sharpe ratio even for a symmetric strategy (1.09 against 0.5 for a normal with a 5% mean and 10% volatility). The text states the relation that holds, which also fits the source's PUT and SPX facts: the more of a strategy's volatility is on the upside, the more its Sortino exceeds its Sharpe.
- Fixed: spx:2.5's worked example. "Strategy B ... 95% of years return between $4-7, but in 5% of years the strategy loses $50-100 in a single bad month. Same mean ($5), same standard deviation ($10)". A 5% chance of losing $50 or more already gives a standard deviation above $12, and those ranges give a mean near $1.50. The text keeps what the example is for (mean $5, standard deviation $10, a Sharpe ratio of 0.5, a worst year about four times A's, a recovery that may be impossible) with numbers that satisfy it: about $6.00 in 99 years of 100 and a loss of about $94.50 in the hundredth. So "5% of years" became "1 year in 100". Strategy A's "Worst year historically: −$25" is kept (a three-sigma year); its "Recovery time after worst year: ~3 years" became "about five years" at its $5 average, which is what the example's own numbers give.
- Checked: "It answers the question of how many units of risk a strategy asks you to take for each unit of expected return" (dl:1D) described the reciprocal of the Sharpe ratio, risk per unit of return. The text now reads "how many units of expected return a strategy pays you for each unit of risk it asks you to take", which matches the formula (eq:sr) and the chapter's "excess return per unit of volatility".
- Checked: the put-writing sleeve's Step 5 wrote 0.65 × 0.5 = 0.32 and 0.65 × 0.7 = 0.45 (spx:2.8's "0.32-0.45", cut short rather than rounded). The products are 0.325 and 0.455, and the text now gives them.
- Checked: the Figures entry on deflated-sharpe-calculator below describes the app's widget before the correction listed in README ("Where the import departs from the app"). The text quotes the corrected figure, and its numbers match the figure's code: 2.54 and 23.9% at the starting settings; 95.9% at 1 trial; 1.19 and 72.0% at 5; 1.58 and 58.5% at 10; 1.90 and 46.0% at 20; 1.13 and 92.6% at 1,260 returns; 99.9% at 2,520. The bracket at K = 100 is 2.53, as the grind box says, and the box's expression agrees with the expected-maximum formula of Bailey and López de Prado (2014) as it is usually stated.

## 1F · Correlation, diversification and liquidity

- Checked: the six equations' expected shortfall, E[L | L > VaR_α], counts a loss as a positive number, while Chapter 1B (and the glossary) define VaR₉₅ and ES₉₅ on returns, as negative numbers, and the conviction threshold of equation 6 needs the positive sign. The symbol L was also left undefined there (equation 1's L is the loss on a losing binary bet). The text now says that L is the return with its sign reversed, which makes ES_α Chapter 1B's expected shortfall written as a positive number.

## 2B · Where your order goes

- Fixed: the NBBO was "the highest bid and the lowest offer across all registered exchanges and dark pools". Dark pools display no quotes, as the source's next section says, and fill "at the prevailing NBBO mid", so they cannot set the NBBO. The text takes the NBBO across the exchanges' displayed quotes and says that dark pools trade at or inside it.
- Fixed: "When Citadel sells you a SPY put, the SPY shares they buy as the hedge ...". A dealer short a put is long delta and hedges by selling shares, the same sign the brief's known errors correct in 9A. The text says "the SPY shares it sells as the hedge may go to another piece of internal Citadel flow".

## 2C · The order book

- Fixed: "the average fill price might be 5 cents worse than the top-of-book ask — about 0.5 bps of slippage on a $580 stock". Five cents on $580 is 0.86 bps. The text says "about 0.9 basis points" and shows the division.

## 2D · What execution costs

- Fixed: SPX's "largest contract size ($5,000 notional per point at SPX 5,000)". An SPX option carries $100 per index point (dl:3A), so its notional at SPX 5,000 is $500,000. The text says "$100 per index point, or $500,000 of notional at SPX 5,000".
- Fixed: for swing setups, "XSP is the default choice. The marginal spread cost vs SPX is paid back many times over in tax efficiency". SPX and XSP share the same 1256 treatment, so there is no tax gain against SPX. The text puts the tax point against SPY and keeps the sizing point against SPX.

## 2E · Accounts, margin and taxes

- Fixed: the top-bracket tax comparison. The source gives "37% ordinary income, 23.8% long-term capital gains including the 3.8% Net Investment Income Tax" and then a 1256 blend of "approximately 27-28%" against "approximately 40-41%" for short-term gains, "roughly 12-14 percentage points". On its own inputs the blend is 0.6 × 23.8% + 0.4 × 40.8% = 30.6%; the 27% to 28% is the blend without the surtax (0.6 × 20% + 0.4 × 37% = 26.8%), while the 40% to 41% includes it (37% + 3.8%). Like for like, the saving is 10.2 points either way, 60% of the gap between the short-term and long-term rates. The text keeps the quoted figures as quoted, labels them, and works the like-for-like arithmetic in a table.
- Checked: the scenario grid said "Widening the range by 5 and 10 points", in an example that measures the loss in XSP index points (60, 48, 78 and 108 points). The widening is of the scenario, from ±15% to ±20% and ±25%, so the text now says "5 and 10 percentage points". Every other number in the chapter and its figure's quoted readouts recomputed and agree.

## 3B · Mean reversion and momentum

- Fixed (known error): "As |w| approaches 1, the process becomes non-stationary; variance grows unbounded with horizon ... Watch the simulated paths fan out as you push the weight toward ±1." The return series is stationary only for |w| < 1, and its variance σ²/(1 − w²) does blow up at both ends. But the price paths the figure draws are sums of returns, whose spread over n steps is about σ√n/(1 − w): they fan out toward +1 and draw in toward −1. The text derives both formulas (eq:var, and eq:spread in a grind box) and says so, and it agrees with the ar1-regime-explorer figure, which reads the negative end as mean reversion.
- Checked: the standard deviation of the final log prices at φ = 0.9 was given as 1.56. The figure's code at seed 42, 50 paths of 250 steps, gives 1.5657 with the sample formula that gives the other two values (0.1582 and 0.0854), so the text now says 1.57.
- Checked: "the true k-period standard deviation is σ√k times √VR(k)". In this chapter σ is the innovation's standard deviation, not a single return's, and by eq:vr the k-period variance is k·V·VR(k). With σ the text disagrees with eq:spread at long lags (at w = 0.5 it gives σ√k·√3 against σ√k/0.5). The text now says √(kV) times √VR(k), with V the variance of each return from eq:var.

## 3C · Fitting a model

- Checked: AdaGrad was said to divide the learning rate "by the running sum of squared past gradients" (dl:2C's wording). The AdaGrad update (Duchi et al., 2011) divides by the square root of that sum; the text now says "the square root of the running sum".
- Checked: "That halving is no accident, and the figure below shows why" led into eq:contract, whose factor \(1 - 2\eta\) is zero at \(\eta = 0.5\): on the figure's loss that rate lands on the minimum in one step, while on the five returns it halves the distance. Both are right, because the toy's slope \(w + 0.5\) is once its distance from the minimum and the figure's \(2(w - 0.5)\) twice it. Two sentences after the list of five cases now say so: on the five returns the factor is \(1 - \eta\), one half at \(\eta = 0.5\). Every other number in the chapter, and the figure readouts it quotes, recomputed and agree.

## 3D · Position size and trading frequency

- Fixed: the retail-scale worked example put dollars per share into \(f^* = p/L - (1-p)/G\): \(0.60/3 - 0.40/4 = 0.100\), read as 10% of $250,000 = $25,000 = 500 shares. The formula needs \(G\) and \(L\) per dollar staked, as the source's own explanation says ("the entire position rises or falls by G or L per unit"). Per $50 share, \(G = 0.08\) and \(L = 0.06\), so \(f^* = 5.0\): full Kelly is $1,250,000 or 25,000 shares, and quarter-Kelly 6,250 shares. A direct check agrees: maximizing \(0.6\ln(1 + 4n/W) + 0.4\ln(1 - 3n/W)\) over the share count \(n\) gives \(n = W/10 = 25{,}000\). The source's conclusion is therefore reversed: for this edge Kelly is far *more* aggressive than the 1% loss budget (1,250 shares), by a factor of 5 against quarter-Kelly and 20 against full Kelly. The text now gives the correct chain, keeps every number of the source's version inside a "Common mistake" callout that explains the unit error, and rewrites "is the loss-budget rule sufficient on its own? ... only if you don't actually have 10% Kelly worth of edge" to what the corrected arithmetic supports: the budget is sufficient for an edge this strong, and stops being so only if the true edge is much weaker than estimated (below about 52% at even payoffs it exceeds quarter-Kelly, below 50.5% full Kelly). "Most retail strategies don't [have such an edge]" is kept. This needs the author's eye; see Questions.
- Fixed: "Quarter-Kelly gives up about 44% of expected compound growth." Growth at a multiple \(c\) of Kelly is \(2c - c^2\) of the maximum, so quarter-Kelly keeps 43.75% and gives up about 56%. Half-Kelly's "gives up about 25%" is right (it keeps 75%). The text derives \(2c - c^2\) and checks both against the exact binary growth at 55% even odds (0.0038 and 0.0022 against 0.0050).

## 4A · What a derivative is

- Fixed: "perpetual bonds in fixed income" appears in the source among derivatives that are perpetual. A perpetual bond is a bond, not a derivative. The text keeps the example and says so.
- Fixed: "you actually receive delivery of barrels of oil ... if you hold to expiration" is "hold a long one": only the long side receives delivery; the short side makes it.

## 4B · Futures, swaps and options

- Fixed: "Party A has converted their fixed-rate funding into floating-rate exposure; Party B has done the reverse." Party A pays fixed and receives floating, which turns floating-rate funding into a fixed rate, not the other way round. The text now says so: A, with floating-rate funding, ends up paying a fixed 4.5%; B, with fixed-rate funding, does the reverse.
- Fixed: "A collar is long stock + long put + short call → equivalent to a long call spread + a put exposure." At expiry, long stock with a long put at K1 and a short call at K2 is worth exactly cash of K1 plus a K1 to K2 call spread; no put exposure remains. The worked example checks it at three prices (80, 100, 130 with strikes 95 and 110), and Chapter 5F's put-call parity gives the same result.

## 4C · Why derivatives exist

- Checked: the risk-parity example scaled by "\(10/5.4 = 1.86\)", with "$0.86" of extra exposure. As written, 10/5.4 is 1.85 (the unrounded 10/5.39 is 1.86), and the example's own $0.44 of equities and $1.41 of bonds add up to $1.85. The text now says 1.85 and $0.85, so every step follows from the numbers shown. The "1.86 times leverage" in the teaching list above is the unrounded value.

## 5A · The option contract

- Checked: the decision rule gave a short put's maximum loss as "the strike less the premium times the multiplier and the number of contracts", which reads as K − (P × m × n). A comma after "premium" now makes it (K − P) × m × n, the $9,700 a contract of the worked example.

## 5B · What an option's price is made of

- Fixed: the synthetic chain broke put-call parity, which the source invokes in the next paragraph. With no interest, a call and a put at the same strike differ by S − K, but the source's 148-strike call and put (4.34 and 0.34 at the mid) differ by 4.00 against S − K = 2, and its 140 pair by 11.65 against 10. Its 150 and 152 calls (2.50 and 0.34 at the mid) differ by 2.16, more than the 2 points between their strikes, so a 150/152 call spread would cost more than it could ever pay; the 148 and 150 puts have the same fault. The 140 call's $1.70 of extrinsic value was also hardly the "tiny extrinsic component" the text describes. The chain is rebuilt with the Black-Scholes model, no interest or dividend, and one implied volatility of 14.1%, chosen so that the at-the-money mid stays at the source's $2.50. Each quote is the model price ± $0.05, the source's spread width. Every sentence the source says about the chain still holds, and more exactly: the 140 call is almost all intrinsic ($10.13, with 13 cents of extrinsic), the 140 put is near zero, the 150 call and put match at $2.45/$2.55, and the 160 call is near zero ($0.12/$0.22). The text says how the chain was made.

## 5C · The Greeks

- Fixed: "A long ATM 30-day SPX call has substantial positive vega: perhaps $10 of P&L per 1 vol-point rise in IV at SPX 6000." By the chapter's own formula, S e^(−qT) φ(d₁) √T / 100 at SPX 6,000, 30 days and 20% IV (the probability map's defaults) is about 6.8 index points per vol point, or about $680 a contract. Ten points would need about 63 days to expiry, and $10 a contract fits no unit. The text gives the computed figure.
- Fixed: "the actual ITM probability is N(d₂), lower by approximately σ√T". Two corrections. First, d₂ lies exactly σ√T below d₁, but the probabilities differ by about φ(d₁)σ√T, roughly 0.4σ√T near the money; for the reference call the gap is 0.029 against σ√T = 0.072. Second, "lower" holds for a call only. A put's probability of finishing in the money is 1 − N(d₂), which is higher than its |Δ|, so the source's own example, "30-delta puts have a 30% chance of being assigned", errs the other way: about 32% at 30 days and 20% IV, 38% at a year. The probability map figure already reports this, saying that |Δ| "falls short of" P(ITM) for a put. The text and the source's table now say "a call" where they give N(d₂), and the put's side is stated.
- Checked: the reference call's price step multiplied four-decimal values, 100 × 0.5326 − 100 × 0.99672 × 0.5040, which comes to 3.025, not the 3.02 it states (the true price is 3.021). Step 3 and Step 4 now give N(0.0817) = 0.53256 and N(0.0100) = 0.50399, which give 3.022.
- Checked: "the gap is 0.5326 − 0.5040 = 0.029, close to 0.3976 × 0.0717 = 0.028": the product is 0.0285, so at three places both are 0.029. Both are now given to four places, 0.0286 against 0.0285.
- Checked: the +$5 what-if wrote "0.533 × 5 = +2.663", which is 2.665; the figure's 2.663 uses the unrounded delta. It is now 0.5326 × 5. The first self-check had the same slip (0.533 × 2 written as 1.065) and now uses delta 0.5326. Its "within a fifth of a cent" is now "about a fifth of a cent above", since the estimate, 4.1972, is 0.22 cents above the reprice of 4.1950.
- Checked: "a delta-hedged long option earns gamma times the difference between the realized squared return and the implied variance" left out the factor ½S² that [eq:hedgedpnl] carries (277.4 for the reference call, not 0.0555). It now says ½ΓS² times the difference.

## 5D · Higher-order Greeks

- Fixed (CONVENTIONS, known error): "With K < S, d₁ and d₂ are typically negative." With the strike below spot both are positive. The text now says so, shows it on the example put (d₁ = 0.563, d₂ = 0.463), gives the reason (ln(S/K) outweighs σ²T/2 unless the strike sits within a hair of spot), and keeps the conclusion: vanna is negative because d₂ > 0.
- Fixed: the post-FOMC paragraph said the dealers "were holding extra long shares against the short puts; now they buy fewer shares." A dealer short puts is long delta and hedges with a short position, as the vanna paragraph before it says ("they buy back hedge stock"). The text now says the dealers were holding an extra short hedge, which they buy back. This is the same slip as the known 9A error.
- Checked: the vanna example's dealer step went from long 28,700 units (delta 0.287) to "long 29,400 and must sell about 750 more units" (delta 0.294), but those rounded figures differ by 700. The repriced change is 0.0075 of delta, 751 units. The step now says the rise makes each put's delta 0.0075 more negative, so the dealer is long about 750 more units.
- Checked: volga's closed form was explained as "the product of two slopes", the slope of φ(d₁), −d₁φ(d₁), times the slope of d₁ in σ, −d₂/σ. That product is φ(d₁)d₁d₂/σ, not the factor d₁d₂/σ. The text now says that differentiating vega by σ replaces φ(d₁) with its slope times the slope of d₁, which gives ν d₁d₂/σ.
- Checked: the color example a week out wrote φ(1.83) = 0.0751. φ(1.83) is 0.0748; 0.0751 is φ at the unrounded d₁ = 1.8276, which is what gives the stated gamma (0.0265) and color (−1.52). It now reads φ(d₁).
- Checked: the straddle example said "one day's passing moves the straddle's delta by 0.105" two days out. 0.105 a day is charm's instantaneous rate; repricing from 2 days to 1 day at spot 101 moves the delta by 0.158, since the rate climbs as expiry nears. The text now gives 0.105 as a rate and adds the repriced 0.158. At 30 days the rate and the day's move agree (0.0019).

## 5E · Volatility

- Checked: the Garman-Klass paragraph and the three-day example called ln(C_i/O_i) the "close-to-open" move, three times. It runs from a day's open to that day's close, while the chapter's own Yang-Zhang paragraph gives the overnight move as running "from each close to the next open", the gap Garman-Klass ignores. All three now say "open-to-close". The numbers (0.0050, −0.0150, 0.0101; 24.0% a year) were already those of ln(C_i/O_i).

## 5G · The volatility surface

- Fixed: "IV rank exaggerates the apparent 'richness' of vol because the rare upward spikes pull the range maximum far above the typical level." Spikes that raise the maximum pull the rank *down*, so in the typical, bottom-heavy equity history the rank understates how elevated vol is. That is what the source's own rule says (percentile about twice the rank) and what the figure says (README, "Where the import departs from the app": the reading had top-heavy and bottom-heavy the wrong way round). The text now says the rank understates for the typical history, and exaggerates only for a top-heavy one, where rare lows pull the minimum down.
- Fixed: the table's first row read "Front IV high, back IV low (steep contango — i.e., backwardation since front > back)". Front above back is backwardation, as Chapter 5E defines it, so the row now reads "(backwardation: front above back)".

## 6A · Who is on the other side

- Fixed: the lifecycle step at 3 to 5 ms said the fill at the NBBO offer ($3.05) was "'price improvement' of $0.00 from the NBBO offer" and then "Their reported execution beats the SIP NBBO". A fill at the NBBO offer does not beat the NBBO. The chapter says the fill is at the NBBO with no price improvement, and that the $0.02 over the wholesaler's internal mark ($3.03) is its edge. "Sub-mid" is dropped (see Questions).

## 6B · What the dealer inherits

- Fixed: "For 30-day 30-delta options at 20% IV, the gap is about 3 percentage points." With N(d₁) = 0.30 and σ√T = 0.0573, N(d₂) = 0.280, a gap of 2 points (the 30-delta put's chance is 0.320, also 2 points). This agrees with Chapter 5C's table (28% for the call, 32% for the put). The chapter says "about 2 percentage points" and shows the arithmetic. "At 60% IV and 90 days, the gap can exceed 10" is kept, with the worked numbers: 9.5 points for the call and 11 for the put.
- Checked: the practice callout said "Use N(d₂) for the odds of assignment" and then gave a short put as its example. For a put, N(d₂) is the risk-neutral chance of finishing out of the money; its chance of finishing in the money is 1 − N(d₂), which the worked example's Step 3 uses. The bullet now adds "and 1 − N(d₂) for a put". Every other number was recomputed (the S = 105 example, the 30-delta gaps of 2, 9.5 and 11 points, the at-the-money drift 0.534, 0.551 and 0.624 with its 0.111 and 0.013 split, the ±0.2 lognormal, the check answers) and the figure's readouts re-run under Node; all agree.

## 6C · Delta hedging

- Checked: two products did not equal their own factors. "0.0128 × 6 × 100 × 100 = 770" is 768 (770 came from the unrounded gamma, 0.012833); the text now says 768, still close to the exact 755. In "Daily against hourly hedging", "$0.065 a share" and "√6.5 × 0.065 = 0.165" gave 0.166 as written; the hourly error is 0.42/6.5 = $0.0646 a share, and √6.5 × 0.0646 = 0.165, about $1,650 for 100 contracts (unrounded, 0.164 and $1,643). The text now says $0.0646. The rest was rechecked and agrees: the figure's values, the derivation of eq:hedgevar (Var(Z² − 1) = 2), the 5% threshold (268 share-equivalents, $2.09, 0.35%), the leveraged-fund rule k(k − 1)RA for k = 2, −1 and 3, and the check answers.

## 6D · Gamma

- Fixed: "For SPY at $600 spot: approximately $460 per contract per 1% (same Γ, 100× smaller notional)." An at-the-money SPY option does not have the same gamma per dollar as the SPX option: gamma scales as 1/S, so SPY's is ten times larger (0.0128 against 0.00128). Dollar gamma, ΓS² × 0.01, therefore scales with S, and one SPY contract carries 0.0128 × 600² × 0.01 × 100 = $4,620 per 1%, a tenth of the SPX contract, not a hundredth. The dollar-gamma figure agrees: at SPX 6,000 with the multiplier set to 10 it gives $4.62k. The chapter says "about $4,600", explains the scaling, and makes it the "Common mistake" callout.
- Fixed (README, "Where the import departs from the app", 6E): the gamma hedge simulator's heading gave a long option's P&L, ½Γ·S²·[(dS/S)² − σ²·dt], for a dealer who is short. The chapter gives the short dealer's sign, eq:shortpnl, as the figure's caption does, with the theta income and the rebalancing cost named as the caption names them.
- Checked: "½ × 0.0693 × 1² × 100,000 = $3,466 a move" is $3,465 ($3,466 came from the unrounded gamma, 0.06932), and only $3,465 makes "two moves make $6,930" add up. The text now says $3,465.
- Checked: the dollar-gamma worked example used Γ = 0.00129 to reach the source's $464 a unit and $46,400 a contract. At the chapter's 4% rate the gamma is 0.00128, as its own gamma example finds, or 0.001283 to more places; 0.00129 is the gamma at a zero rate. So "with gamma carried to more places, 0.001283" did not follow from 0.00129. The text now gives 0.00128 × 6,000² × 0.01 = $461 and $46,100 a contract, still "about $46,000". This replaces the earlier decision above to keep "$464/share × 100 = $46,400".
- Checked: "The path's daily noise is 1.1%, about 17.5% a year" described the simulator's setting, not the path it drew. Re-running the figure's path (seed 13), the daily moves over bars 1 to 30, while the calls were alive, have a root-mean-square of 0.70%, about 11% a year; the P&L says the same, 20% × √(60,766/189,826) = 11.3%. The text now says the path is drawn with 1.1% daily noise, moved about 0.7% a day, or 11% a year, while the calls were alive, and that both are below the 20% sold. The other quoted figure values, the worked examples and the check answers were recomputed and agree.

## 7B · Second-order Greeks in context

- Fixed (CONVENTIONS and README, known error): after the higher-order Greeks figure the source said "Gamma peaks sharply at-the-money. Crank the days-to-expiry slider down and watch the peak grow". The figure draws vanna, charm, volga, speed and color, not gamma. The text now reads gamma's growth into the strike from color (positive at the strike, about 0.34 a year at 30 days and 5.0 at 5 days, negative beyond spots of about 93 and 107) and from speed's change of sign just below the strike.
- Fixed, same passage: "Charm is largest near the money". On the figure, and by README's 5D entry, charm is largest a short way either side of the strike and small at it (about −1.7 a year near 93 and +1.2 near 107 at the starting settings, −0.2 at the strike). The text says so and keeps "it is the mathematics of pinning".
- Fixed: the vanna recap said "For an OTM put (negative delta), it [higher IV] pulls delta toward zero in magnitude." That contradicts the next paragraph ("When VIX spikes, OTM put deltas become more negative in magnitude") and Black-Scholes: for a put struck below spot, \(d_2 > 0\), vanna is negative, and higher IV makes the delta more negative. The text now says the delta becomes more negative, further from zero.
- Fixed: "They were holding extra long shares against the short puts; now they have too many shares and must sell some back." A dealer short puts is long delta through them and hedges with a short position, and after a vol crush it buys, as the source's own worked example says ("they buy 17,500"). The text says the dealer holds an extra short hedge and buys some back. This is the slip that notes/5d.md fixed in dl:5D and the known 9A error. A "Common mistake" callout warns against it.
- Fixed, a sign: the charm example writes "Charm is approximately −0.004 per calendar day ... ΔΔ_put = Charm × ΔT = (−0.004) × 2.73 = −0.011. Toward zero. So ... −0.25 + 0.011 = −0.239." The product is −0.011 but is added as +0.011. With charm measured with time running forward, Chapter 5D's convention, the put's charm is +0.004 a day and its delta rises by 0.011. Every number and the conclusion are unchanged.
- Checked, the vanna example: at the stated inputs (SPX 4,500, strike 4,400, 30 days, IV 25%, r = 4%, q = 1.5%) Black-Scholes gives a put delta of −0.352 (the source's "approximately −0.36") and a vanna of −0.0045 per volatility point (its "approximately −0.005"). At 18% the delta is −0.308 and vanna −0.0088. Repricing gives a change in delta of 0.044 and a trade of about 22,200 share-equivalents, against the linear 0.035 and 17,500. The source invites the check ("verify with your own calculator"); the text keeps its numbers and adds the result.
- Checked, the charm example: the source gives no IV. With r = q = 0, a put struck at 0.97S with 30 days has a delta of −0.25 at an IV of 16.3%, and then a charm of 0.0033 a day, a Monday delta of −0.2403 and a trade of about 96,600. With the FOMC example's r = 4% and q = 1.5% the figures are IV 17.5%, 0.0029 a day and about 83,400. The text gives the zero-rate check and keeps the source's 0.004 and 110,000 as the example.

## 8A · Gamma exposure

- Fixed: "dealers net long puts (from buying retail puts), net short calls (from buying retail calls)". Buying calls makes a dealer long calls. The text now says dealers are net long puts, bought from customers who write them, and net short calls, sold to customers who buy them. It says that premium selling explains the puts, and that the calls rest on customers buying more calls than they sell, which is part of the assumption. It also says plainly, under the conventions table, that both rows are assumptions about who holds what, and that a customer who sells calls (call spreads, iron condors) pushes the call sign the other way.
- Fixed: same slip in the conventions table: the JPM-era row said dealers were short puts "sold by hedgers" and the 0DTE-era row long puts "bought by retail premium sellers". Hedgers buy puts and premium sellers write them. The table now reads "short puts, sold to hedgers who buy them" and "long puts, bought from retail premium sellers who write them". The source's own prose ("short puts (from selling them to hedgers)") already had it this way.
- Fixed: wording, conclusion unchanged: "dealers' short puts get more negative delta — they sell stock to stay flat". The puts' deltas grow more negative, which makes the dealers who are short them *longer* in delta; that is why they sell. The text says so.
- Fixed: units of the hedge-flow formula: "dH ≈ −G_$ × (dS/S)" is right only if dS/S is in percent, since G_$ is per 1% move. The text writes ΔH ≈ −GEX × (ΔS/S)/0.01 and says the fraction divided by 0.01 is the move in percent. The worked sum and a check question apply it.
- Fixed: "The treatment is empirically grounded throughout: where I cite numbers, they come from peer-reviewed work or directly from exchange data": the part cites working papers too (Dim, Eraker and Vilkov is described in dl:8A itself as a working paper; the SSRN papers are preprints). The text says "academic research, peer-reviewed papers and working papers, or directly from exchange data". The first person is recast.

## 8B · Two regimes

- Fixed: "κ is the feedback coefficient (proportional to market depth × dealer aggressiveness)". Feedback must grow as depth falls, not rise with it: Chapter 8C's third precondition is that "market depth had degraded", and the effect is stronger for the least liquid securities (Barbon and Buraschi). The text says κ is how far prices move per unit of hedging flow, larger when market depth is thin and when dealers hedge aggressively. "κ is regime-fit and varies with depth, dealer aggressiveness, and prevailing positioning concentration" is kept.
- Fixed: "Three regimes" listed four cases (stabilized, neutral, amplified, edge of explosion). They are a four-row table with a column for published GEX and one for the dealers' side.
- Fixed: "Several peer-reviewed papers have measured the effects": Barbon and Buraschi is an SSRN paper and Dim, Eraker and Vilkov a working paper (dl:8A). The text says "Several academic papers, some peer-reviewed and some working papers".
- Checked: the practice callout gave a day's standard deviation at 15% volatility as 15%/√252 = 0.95%. It is 0.945%, which rounds to 0.94%; the text now says 0.94%. The stop of about 1.9% (two standard deviations, 1.89%) is unchanged.
- Checked: the first figure idea had its readout give "the realized volatility of the simulated paths" and promised it would agree with σ/(1 − w). That holds for the volatility of the paths' cumulative moves, not for the standard deviation of single returns, which is σ/√(1 − w²), about 1.12σ at both w = +0.45 and w = −0.45 (Chapter 3B draws the same distinction). The idea now asks for the paths' volatility over many steps, from the spread of their endpoints.

## 8C · When the framework breaks

- Checked: the singular-limit paragraph said that, with G and κ both rising, "their product nears 1 from both sides". In the language of limits that means from above and from below, but κG can only rise toward 1 from below (above 1 the formula has no meaning). The sentence now says "so both push their product up toward 1".

## 8D · Gamma squeezes

- Fixed: the source's table writes "MA(returns) / MA(|returns|)", whose pipes the app's markdown read as cell breaks. The table writes \(\text{MA}(r)/\text{MA}(|r|)\), with the bars inside maths, which the build keeps as text. The text also gives P as a display, [eq:p].

## 9A · The VIX

- Fixed: the opening hedge (dl:9A, "Initial delta-hedge: long approximately 410 shares"). A dealer short puts is long delta and hedges by selling. The chapter works the hedge on an assumed 30-day expiry with a zero rate (the source gives no expiry): d₁ = 0.374, put delta −0.354, so the dealer is long 35,400 share-equivalents and sells 35,400. Step 4 of the figure then sells 11,000 more (0.11 of delta on 1,000 contracts of 100, the readout's number), taking the short hedge to 46,400. This agrees with the figure, whose README entry records the same correction.
- Fixed: "a 1% downside move in SPX re-prices the put wing far more than a 1% upside move re-prices the call wing." The claim is kept and attributed to the Dealer Mechanics Lab, with its mechanism: the 1/K² weights (a put at 4,400 counts 1.14 times a call at 4,700 of the same price), the steeper put wing of the skew, and implied volatility that stays attached to its strikes, so that a fall moves the money onto the steep put side. A toy on the figure's default smile shows the at-the-money IV rising 0.18 of a point on a 1% fall and falling 0.04 on a 1% rise. The text says the figure moves its whole smile with the forward and so cannot show this (18.507, 18.505, 18.503, as README gives). It adds a calculation the figure does not make: with the default smile held fixed to its strikes, a 5% fall lifts the computed VIX from 18.505 to about 19.22 (+0.72) and a 5% rise lowers it to about 18.07 (−0.44). These use the figure's own formula with the smile centered on 100 instead of on the forward.
- Fixed: "The strip's premium level scales VIX roughly linearly." The VIX scales with the square root of the premium level, which the source's own numbers show: doubled quotes give 16.3 (its "16-17") and tripled quotes 19.9. The source's "low 20s" for tripled quotes is written "near 20".
- Fixed: "Front-month sits below spot VIX" (contango). That contradicts the source's own definition of contango, "short < long", and the glossary's. The text says the front month sits above spot VIX, with the second month above the front.
- Fixed: VIX futures "Settle at the SOQ of VIX computed Friday morning" is written "settles to a special opening quotation (SOQ) of the VIX on its expiry morning (Chapter 2A)". The same source sentence has them expiring on a Wednesday, and Chapter 2A (dl:3A) says VIX contracts settle to an SOQ on Wednesday morning.
- Checked: "Holding ΔK/K² of each strike across all out-of-the-money strikes gives a position whose P&L is, exactly, total realized variance minus a fixed strike." A static strip pays a function of the final price alone and cannot pay a path's realized variance; DDKZ's replication needs the strip delta-hedged (the chapter's own derivation, its recap and Chapter 7A, "when it is dynamically delta-hedged"). The sentence now says "delta-hedged"; the source's "exactly" is kept.
- Checked: the derivation called −ln(S_T/S_0) itself "a log contract", while the glossary entry marked on that word defines the log contract as paying the logarithm of the final price, and Chapter 7A calls the strip's minus-log payoff "a short position in the log contract of Chapter 9A". Step 2 now says −ln(S_T/S_0) is a short position in a log contract, which pays the logarithm of the final price; Step 5 and the recap say the 1/K² is the curvature of the short log contract (the log itself curves the other way, −1/K²); Step 6 speaks of the short log contract's expected payoff. The algebra is unchanged.
- Checked: the opening-hedge display gave d₁ as (0.0225 + 0.0022)/0.0659 = 0.374, but those rounded figures give 0.3748, which reads 0.375. The unrounded d₁ is 0.3738, so 0.374 is right; the display now carries one more digit, (0.02247 + 0.00217)/0.06594 = 0.374. The delta, −0.354, is unchanged.

## 9B · Same-day options

- Fixed: "For OTM strikes the divergence is faster — gamma compresses into ATM as T shrinks; OTM gamma collapses." The first clause reads as if out-of-the-money gamma diverged faster, which the rest of the sentence contradicts. The text keeps the substance: away from the strike time works the other way, gamma compresses into the at-the-money strike and out-of-the-money gamma collapses (negative color, Chapter 5D).
- Checked: the source's table gave the 1-day row as √T = 0.0524 and a gamma ratio of 5.47×. √(1/365) = 0.05234, which rounds to 0.0523, and the ratio is √30 = 5.477, which rounds to 5.48× (5.47 came from dividing the rounded 0.2867 by the rounded 0.0524). The row now reads 0.0523 and 5.48×; the other rows are correct.
- Checked: after the gamma-profile-dte figure the text said that at about an hour "both ratios read 24.5 or so". With the figure's own code (r = 4%) at the slider's floor of 0.05 days, the ratio readout shows 24.6 (24.59, because φ(d₁) at 30 days sits a little below its peak) and the 1/√T expectation 24.5 (24.49), as at 4 hours (13.5 against 13.4). The sentence now says the ratio reads 24.6 against an expectation of 24.5.

## 9C · Reading the tape

- Checked: the seventh heuristic sent the reader to Chapter 8B for effect sizes of "tens of basis points per standard deviation", but 8B gives no effect in basis points; the per-standard-deviation figure (Barbon and Buraschi, about 16 bps) and pinning's 16.5 bps are in Chapter 8A. The reference now reads "Chapters 8A and 8B".

## 10A · Five kinds of edge

- Fixed: one classification of calendar effects (spx:5.4, spx:5.7), stated in the chapter under "How this book files OPEX and Halloween": both are overlays by category; by source OPEX is microstructure with an institutional part, and Halloween is filed with the behavioral seasonality effects, provisionally, as Chapter 1G files it. The matrix row "Behavioral / Overlay: (some)" now reads "(some, including Halloween)" to match. See Conflicts for the other filings.

## 10C · The variance risk premium

- Checked: the at-the-money price at 15.1% was given as 1.74% of the index, but \(0.4 \times 0.151 \times 0.289 = 1.7456\%\) rounds to 1.75%, which the text now gives. The seller's share is now computed directly, \(0.4 \times 0.042 \times 0.289 = 0.49\%\), so that the two rounded prices and their difference do not seem to disagree.
- Checked: the kill-criteria example ended at $128,000, a drawdown of exactly 20%, but the rule stops the sleeve only when the drawdown *exceeds* 20%. The sleeve now stands at $120,000, a drawdown of 25%, more than 20%.
- Checked: the last check question gave SPX's daily moves with no window, while its answer applies the rule on 21-day realized volatility. The question now says SPX has moved about 2% a day for 21 trading days.

## 10D · Trend following

- Fixed: the source's toy example (spx:6.3) puts "Positive in 8 of 10 largest 60/40 drawdowns — including 2008 and 2022" under Hurst, Ooi and Pedersen (2017), whose data end in 2016. The chapter keeps the claim but attributes it to the Edge Book ("a record that runs past the study's end"), not to the 2017 paper. See Questions.

## 10E · Carry

- Fixed: the sign of the carry formula (spx:6.4). The source gives \(\text{Carry}_{i,t} = (F_{i,t} - S_{i,t})/S_{i,t}\), "futures-spot ratio, simplified". Its own definition of carry is "the expected return assuming prices don't change", and its own example says commodities in backwardation pay positive carry. For a long futures position with spot unchanged, the return is \((S - F)/F\), which is positive in backwardation (\(F < S\)); the source's ratio has nearly the same size and the opposite sign, and is negative there. The chapter uses \((S - F)/F\) (eq:carry), states the source's form, and says it is the premium of the futures over spot, the carry of a short position. See Questions.
- Checked: the second check question (spx:6.6) asked which premium has "the worst standalone Sharpe ratio but the best portfolio contribution". Its answer calls trend's retail Sharpe ratio of 0.20 to 0.40 middling, and the book's own figures agree: carry's realistic retail 0.15 to 0.30 is lower, and the VRP's retail 0.20 to 0.40 is the same. The question now asks which premium has "only a middling standalone Sharpe ratio but the best portfolio contribution".

## 10F · Equity factors

- Fixed: the BAB formula. spx:7.4 gives \(\text{BAB}_t = \beta_H^{-1} R_{\text{Low}} - \beta_L^{-1} R_{\text{High}}\) "(simplified)" and calls it market-beta-neutral. With those weights the portfolio's beta is \(\beta_L/\beta_H - \beta_H/\beta_L\), which is negative whenever \(\beta_L < \beta_H\), so the subscripts are swapped. The chapter writes the beta-neutral form, \((1/\beta_L)(R_L - r) - (1/\beta_H)(R_H - r)\), checks that its beta is zero, and works it with the source's toy (8% and 11% at betas of 0.6 and 1.5: 13.3% less 7.3% is 6.0%).
- Fixed: the allocation table (spx:7.6) is kept as given, with a reading added. Its rows add to 22% to 45%; "Total factor tilts: 25-40%" leaves 60% to 75% for cap weight, not the table's "Remainder (50-70%)"; and AVUV appears in both the value and the size rows. The text says so and tells the reader to count AVUV once.
- Checked: the gloss of eq:spread said value's relative return is "the change in the spread times the difference in fundamental growth". The identity multiplies two ratios, \(V_0/V_1\) and \((1+g_c)/(1+g_e)\); read as a difference, equal growth would give zero, against the worked example's loss of a third. It now reads "times the ratio of their fundamental growth".
- Checked: the years an information ratio of 1/3 needs to reach a t-statistic of 2 were given as \((2/0.33)^2 \approx 37\), an artifact of rounding the ratio first. Exactly, \(2/(1/3) = 6\) and \(6^2 = 36\), so the text now gives \((2 \times 3)^2 = 36\) years.

## 10G · Calendar and flow effects

- Fixed: classification, as the brief asks. The Edge Book files OPEX and Halloween differently in its Chapters 1, 5 and 8 (see Conflicts). This chapter uses one filing, set out in a table: FOMC cycle and end-of-quarter rebalancing institutional (Source 3); OPEX microstructure with an institutional part (Sources 4 and 3), as spx:8.4 has it; Halloween behavioral seasonality (Source 2), provisionally, as spx:1 (Chapter 1G) has it; turn of the month institutional by its proposed mechanism (pension and 401(k) flows), which spx:8.6 states without classifying. The same filing is used in Chapter 10A (written in parallel) and matches Chapter 1G's final check answer, which says 10G files OPEX as part microstructure and part institutional.
- Checked: the text said Chapter 11K "turns it into a short trade" after the announcement. Chapter 11K's post-FOMC trade has a long bias (long ES, SPY or call spreads, as dealers buy back hedges) and is short only in duration, so "a short trade" read as the wrong direction. It now reads "a brief long trade".

## 10H · Regime filters

- Fixed: spx:9.1 says that above 1.05 "near-term realized vol is meaningfully higher than longer-dated". The VIX and the VIX3M are implied volatilities, so the chapter says near-term volatility is *priced* above longer-dated volatility.
- Checked: the closing rule said "Give GEX a tenth of a filter's weight at most", which contradicts the chapter's own "10% to 15% of one filter's weight" (spx:9.5: "Worth 10-15% of one filter's weight"), since 15% is more than a tenth. It now reads "Give GEX only 10% to 15% of one filter's weight". Chapter 13F, below its Card F4, paraphrases the old wording ("a tenth of one filter at most").

## 10I · What not to trade

- Checked: the LEAPS-against-ES example said the put spread must make up "that gap of up to $5,000 a year". On the example's own figures, a LEAPS drag of $2,000 to $6,000 against ES at $400 to $800 above the risk-free rate, the gap runs from $1,200 to $5,600, so it now reads "up to $5,600".
- Checked: "a later 50% fall in the index only restores half of the product's tiny remainder" could be read as recovering half the loss. A −1 times product gains 50% on what is left, so it now "only adds half to the product's tiny remainder, taking 4% of its old value to 6%".
- Checked: the first check answer set CNDR's 690% against "about 5,500% for SPX". The 5,500% is the SPX Total Return index's, as the rest of the chapter and Chapter 1D say, and SPX in this book is the price index; the answer now names the Total Return index.

## 11A · The market dashboard

- Fixed: the IV rank row described IV rank as "current IV's percentile in its own 1Y range", which is the IV percentile. The row now gives Chapter 5G's definition, where today's IV sits within its 52-week range.
- Checked: the VIX row read "30-day at-the-money SPX implied volatility", from the source's "30-day ATM SPX IV". The VIX is the model-free implied volatility of a strip of out-of-the-money options (Chapter 9A), not the at-the-money one; the row now reads "30-day SPX implied volatility", as Chapter 5E and the glossary put it.
- Checked: the forward-volatility example said the four days after tomorrow "carry" 0.0464. That is the annualized forward variance \(\sigma_f^2\); in Chapter 5G's usage the window carries \(0.0464 \times 4 = 0.1856\) in variance-days. It now says they carry "a forward variance of" 0.0464. All other arithmetic, the grind box and the six check answers recomputed in Python; the figure's numbers rerun with its own code in Node.

## 11B · Conditional mean reversion

- Fixed: the source lists the MOVE index among "credit spreads (HY OAS, IG OAS, MOVE index)". The MOVE is Treasury volatility, not a credit spread, so the text lists the three as "credit and rates stress".
- Checked: the gloss on \(D\) said a positive \(D\) means "up stretches are followed by gains" and a negative one "down stretches are followed by gains". The sign of \(D = m_{\text{up}} - m_{\text{down}}\) compares the two means and says nothing about either one's sign: with a positive drift both can be gains whatever \(D\) is. It now says up stretches are followed by higher returns than down stretches, and the reverse for a negative \(D\).
- Checked: "How often the gates open" multiplied the pass rates "if the layers pass independently". The rates are conditional (15% "of those days", 70% "of those"), so their product is the share of days passing all three by the multiplication rule, with no independence needed. It now says each rate is a share of the days that passed the gates before it. All other arithmetic, including both Bayes calculations and the signal-to-noise examples, recomputed in Python.

## 11C · Indicators

- Fixed: the source says "six indicators across three pedagogical functions" and then lists four (momentum extremes, trend regime, volatility regime, structural levels), as does its own "one indicator per pedagogical function" list. The text says four.
- Fixed: the source's `pandas.ewm(span=n).mean()` (dl:10B) is not a top-level pandas function; it is a method of a series. The text writes `s.ewm(...)` for a series `s` of closes, and says that `adjust=False` starts from the first value, not from Wilder's plain average of the first n bars.

## 11D · Chart patterns

- Checked: the prevalence \(\pi\) was defined as "the share of flagged-looking stretches that sit on genuine accumulation". Among flagged stretches that share is the PPV itself; the prevalence in the PPV formula is the share of all scanned stretches, as the worked example and the check question use it. It now reads "the share of scanned stretches".
- Checked: the worked example said genuine accumulation "sits under 5% of the stretches you scan", which reads as "less than 5%", while the PPV of 32% needs exactly 5%. It now says 5% of the stretches you scan sit on genuine accumulation.
- Checked: the recap said the bull flag "needs a pole of 2 to 3 daily ranges", which reads as a band and would fail the worked example's 4-ATR pole. It now says "at least 2 to 3", as the anchor does. All other arithmetic (depths, ranges, retracements, Mansfield ratios, the three PPVs and the five check answers) recomputed in Python.

## 11F · Multiple timeframes

- Checked: the text quoted the figure's verdict as "with explicit invalidation per Section 12C" and glossed the old number. The figure has since been renumbered (commit "new chapter numbers in figures") and now prints "per Chapter 13C", so the quotation is now "with explicit invalidation per Chapter 13C" and the gloss is gone. The first item above and the Figures section are updated to match. Every other number the text quotes from the figure (seed 7: +6.35, −1.13, 1.43%, 43.9; seed 9 the only agreement; seeds 18, 19 and 25; the counts 19, 20 and 5) reran with the figure's own code in Node, and all worked arithmetic recomputed in Python. Seed 25's slope is −3.19 as the figure prints it, not −3.20 as the Figures section had it; the chapter does not quote it.

## 11G · The composite scorecard

- Fixed: the source's bucket ranges overlap at their edges ("+10 to +40", "−10 to +10", "≤ −40"). The text uses the figure's rule (+40 or more strong bull, +10 or more bull tilt, above −10 neutral, above −40 bear tilt), stated as "each edge belongs to the more extreme bucket", and demonstrates both edges in the figure.
- Checked: Step 4 of "Scoring one day" said trend, "the dimension with the most room", can add only \(17 \times (1 - 0.6) = 6.8\) points. Room is \(w_k(1 - s_k)\), and at that day's scores trend has the least room of the eight. Rates has the most, \(12 \times (1 + 0.2) = 14.4\), with sentiment next at 14.0, so the step now names rates. The conclusion stands: 14.4 is short of the 22.6 points needed, so no single dimension can reach +40. All other arithmetic, the five figure scenarios and the four check answers recomputed in Python and with the figure's own code in Node.

## 11H · Four swing setups

- Fixed: "Resulting notional is typically 20-100× the dollar risk for equity trades" stands under the Trend Pullback, whose stop is "typically 0.5-1.0% below entry". Notional per dollar of risk is the price over the stop distance, one over the stop's fraction of the price, so stops of 0.5% to 1.0% give 100 to 200 times. The text keeps "20 to 100 times" as the source's general figure for equity swing trades, which corresponds to stops of 1% to 5%, and gives 100 to 200 times for the two tight-stop setups. Setup 4's own "$300k ... ~200% notional" agrees.
- Checked: the IBS and RSI worked example said a $3,000 budget buys 1,168 shares, worth $599,768. With the stop at $510.93, d is $2.57 and ⌊3,000/2.57⌋ = 1,167 (1,168 shares would risk $3,001.76, over the budget). It now says 1,167 shares, worth $599,255, still 200% of the portfolio.
- Checked: the grind box called the true range of 70 "the gap down from the previous close". The gap is 10 (the 5,960 close to the 5,950 high); 70 is the whole fall from the previous close to the low. It now reads "the fall from the previous close to the low".
- Checked: the grind box said the normalized slope "divides the 30-bar SMA's change over five bars by the ATR", which gives 20/60 = 0.33, while its own sum, (20/5)/60 = 0.067, and Chapter 11E's definition divide the rise per bar. It now reads "the 30-bar SMA's rise per bar over the last five bars".
- Checked: the practice callout said the mean-reversion setups' stops produce positions of 100% to 200% of the portfolio. That holds at 1% risk; the Trend Pullback's own row allows 1.5% risk with a 0.5% stop, which is 1.5/0.5 = 300%, beyond Reg-T's overnight 200%. It now says 100% to 300%.

## 11I · Pre-earnings momentum

- Fixed: "A trader who held would have lost approximately $7,000 instead of gaining $6,000. The $13,000 swing represents 2.6R of avoided loss." The holder, in at $702 and marked at $698, is down $800 on the trade. The $7,000 is the fall from the $733 close on T−1, and it already includes $6,200 of open profit. The exit beat holding by ($732 − $698) × 200 = $6,800, about 1.4R (1.36R) on the $5,000 risk. The text keeps $13,000 and 2.6R as the tempting tally and shows the double count.
- Fixed: the forward-IV intermediates. 0.32² × 90/365 is 0.02525, not 0.02527, and the difference is 0.01641, not 0.01643. The text works the same formula in days, as Chapter 5G does (9.216 − 3.226 = 5.990, so σ_f² = 0.0788 and σ_f = 28.1%), which reaches the source's answer.
- Checked: the IV-ramp example priced its call "by Black-Scholes" without a rate. Its $3.61 and $2.95 need r = 4% (at r = 0 they are $3.52 and $2.91, a fall of 17%). It now says "with a 4% interest rate and no dividend", as Chapter 5C states its reference call.
- Checked: condition 1 read "ADX above 20 (Chapter 11E)", but Chapter 11E's Stage 2 test is ADX above 18. The source's 20 is kept, and the text now says it is stricter than the 18 of Chapter 11E, as Chapter 11H does for its own ADX window.
- Checked: "(Chapter 5E)" followed the median absolute move of 0.67, which Chapter 5E does not give; 5E gives the 0.8. The citation now follows the 0.8. The 0.67 is right (the median of |Z| is 0.674).

## 11J · Post-earnings drift

- Fixed: the exit. The source trims 50% at $795 "(+0.75R per share × 100 = +$3,700)", adds "another $2,000 on the trailed half" at $815, and totals "+$5,700 on $1,000 risk = +5.7R". R is $10 a share (entry $758, stop $748), so $795 is +3.7R a share, not +0.75R, and the trim is 50 shares, not 100: 50 × $37 = $1,850. The trailed 50 shares make 50 × ($815 − $758) = $2,850. The total is $4,700, +4.7R; the source's $5,700 is what all 100 shares held to $815 would make, as if nothing had been trimmed. The text gives the corrected figures and adds what the chapter's own rule, half off at +0.75R ($765.50), would have made: $375 + $2,850 = $3,225, 3.2R.
- Fixed: the Real Value product. 0.85 × 0.80 × 0.70 × 0.75 × 0.70 × 0.85 × 0.85 = 0.181, not "≈ 0.20". The text computes 0.18 and says the Dealer Mechanics Lab puts it at about 0.20. With T = 0.9 and V = 0.8 the product is 0.232.

## 11K · Catalyst trades

- Checked: the binary-readout call spread was "worth about 0.45 × 10 = $4.55". As written, 0.45 × 10 is $4.50; the $4.55 comes from the unrounded p = 25/55. It now reads 10 × 25/55 = $4.55. The 10 spreads, $4,550 and 0.91% are unchanged.

## 11M · Choosing an expiry

- Checked: the shortcut was written 0.4 × 600 × 0.16 × 0.287 = $11.01, which is $11.02 as written, and √T = 0.138 gives $5.30, not the $5.32 stated. √T is now shown to four places, 0.2867 and 0.1385, which give $11.01 and $5.32.
- Checked: the text called the figure's gamma scalp row (5, 5, 4, 2, 1, 0) and PMCC row (0, 1, 2, 3, 4, 5) "mirror images"; reversed, the PMCC row is 5, 4, 3, 2, 1, 0, so they are not exact. It now says "near mirror images".

## 11N · How swing trades fail

- Fixed: failure 9's "Buying 90 DTE LEAPS for a 3-day pivot trade" reads "90 DTE options or LEAPS", since LEAPS start beyond 365 days in Chapter 11M's table (180 days in its figure).

## 12A · Choosing a strategy by purpose

- Fixed (dl:11.0): "(Section 8B CNDR empirical evidence)" points to the wrong place. Section 8B (new 8B, the two gamma regimes) has no CNDR evidence. The CNDR material is in the atlas's own iron condor entry (dl:11.2, now Chapter 12C, with the figure), the Dealer Mechanics Lab's do-not-trade card (old 12E, now Chapter 13F) and the Edge Book's 10.6 (now Chapter 10I). The text points to those three.

## 12B · Novice strategies

- Fixed (dl:11.1): the cash-secured put example gave a "net effective purchase price $569". Assigned at $570 with $4.00 of premium received, the effective price is 570 − 4 = $566 a share ($57,000 less the $400 premium is $56,600 for 100 shares). The text gives $566, and adds that at $565 the shares show a $100 loss. The facts checker reports 569.
- Checked: the Black-Scholes check of the example premiums did not say which interest rate it used, and its numbers hold only at zero ($100.6 and 8.2%); at Chapter 5C's 4% the call is about $109 and $35 is about 7%. The text now says "with interest ignored".

## 12C · Intermediate strategies

- Fixed (dl:11.2): the calendar call spread's gamma. The source gives "Γ mixed (short near gamma, long far gamma; net positive)". With both legs at the money, the near-dated short call has more gamma than the far-dated long call (at-the-money gamma grows as \(1/\sqrt{T}\), Chapter 5C), so the calendar is net short gamma at the strike. A Black-Scholes check at 15% implied volatility, 7 and 30 days, gives net gamma of −0.0017 per point at the strike, turning positive beyond about 3% either side. The card says "gamma − at the strike, turning + far from it", which keeps the source's "mixed".
- Fixed (dl:11.2): in the calendar example, the long call "has ~21 days remaining" at the 7-day expiry. A 30-day option has 23 days left after 7. The text says 23; the rest of the example is unchanged. The facts checker reports 21.
- Fixed (dl:11.2): the diagonal call spread example buys a 1-year LEAPS and says that "after 16 monthly rolls, premiums collected = $400 = full LEAP cost basis". A 1-year LEAPS lives about 12 months, so 16 monthly rolls do not fit; at $25 a month the rolls collect about $300 before it expires. The text keeps the 16 rolls and the $400 as the arithmetic of the source, says why they do not fit, and adds that the premiums need only cover the LEAPS's 100 points of time value (it is 300 points in the money at SPX 6,000) while SPX holds. A common-mistake callout repeats the point.
- Fixed (dl:11.2): the bull put spread's regime fit says the defined risk lets you size "without the unbounded loss exposure of naked puts". A naked put's loss is bounded, at the strike less the premium (Chapter 5A), though large. The text says "the open-ended exposure of a naked put, whose loss runs all the way to the strike less the premium".
- Checked: the bull call spread card (from dl:11.2, "Γ ±, Θ negative, ν + / −") gave theta as always negative while gamma and vega change sign with the price. With one volatility, theta has the opposite sign to gamma: at 18% and 30 days the 6,000/6,100 spread has gamma, vega and theta of +, + and − at 6,000 and −, − and + at 6,100. The card now reads "Delta +; gamma and vega + near \(K_1\) and − near \(K_2\); theta the opposite sign to gamma".

## 12D · Advanced strategies

- Fixed (dl:11.3): the jade lizard example said that below 5,950 "you're assigned long stock at 5,950 minus the $51 credit = effective basis 5,899". The example is on SPX, whose options settle in cash, so nothing is assigned as stock (Chapter 5A). The text says the put costs \((5{,}950 - S_T) \times \$100\) at settlement and the position breaks even at 5,899, the same number.
- Checked: "Every entry here has an unbounded or very large loss on at least one side" and the recap's "The advanced structures each leave one side open" were false for the long call and put condors, whose card gives a maximum loss of the debit \(D\) (the iron condor's payoff). They now read "Every entry here but the long condors has ..." and "Most advanced structures leave one side open".

## 12E · Expert strategies

- Fixed (dl:11.4): the box friction arithmetic. The source says "1–4 cents per share of width. On a $10,000 box, that's $100–$400". Per share of the multiplier, 1 to 4 cents would be $1 to $4 per box; only "per dollar of width" gives $100 to $400. The text says "1 to 4 cents for each dollar of width, or $100 to $400 on a $10,000 box". See the questions below.
- Fixed (dl:11.4): the early-assignment condition. "Even SPX boxes (European) are safe" is written "SPX boxes are European-style and safe from it". The source's condition for early exercise, "when the discounted strike exceeds time value", is written as Chapter 12H's test, the interest on the strike exceeding the remaining time value.

## 12F · From a market view to a structure

- Checked: the worked example's Black-Scholes prices (110, 52 and 58) hold only with a zero interest rate, which the text did not state (at 4% the 6,000 call is about 120, and the at-the-money shortcut of Chapter 5E assumes a zero rate). Step 1 now adds "with interest ignored".
- Checked: after the income and hedging table, "these rows prefer 90 days or more" contradicted the equity-book hedge row, which prefers 30 to 90 DTE; only the short-volatility book's hedge prefers 90 days or more and avoids short-dated options. The sentence now names that row: "the hedge for a short-volatility book prefers 90 days or more, and avoids short-dated options".

## 12G · Options margin

- Fixed (dl:11.6): the Reg-T list labels the uncovered put formula "Short cash-secured put". A cash-secured put posts the strike in cash (as the source's own cash-account section says); the formula applies to an uncovered put. The text labels it "Short uncovered put" and adds that a cash-secured put is the other way to hold a short put.
- Fixed (dl:11.6): the short call example, "0.20 × 6,000 − 100 = $1,100/share × 100 = $110,000", leaves out the premium that the formula itself adds. The text gives the $110,000 as the requirement "before the premium", then adds a 15-point premium (the 6,100 call's price in Chapter 12C's bear call spread) for $111,500, and checks the 10% floor. The formula is written as [eq:naked].
- Fixed (dl:11.6), a qualification: "Reg-T is fixed and formulaic. It doesn't move with realized volatility. In stress, your margin requirement on a $1,100 short call stays $1,100". The first two sentences are kept. The requirement does move as its inputs move (the index level, the out-of-the-money amount and the premium), so the text says it changes only through those inputs and never by a widened scenario. The danger the source names, position size relative to equity, is kept as written.
- Fixed (dl:11.6): SPAN's paragraph says futures are the cleanest leveraged exposure because, among other things, "the contract is European". A futures contract has no exercise; the point that survives is that nothing can be assigned early, and the text says that.
- Fixed (dl:11.6): the list "options on futures (also ES options, /VX VIX futures, /CL crude options)" names VIX futures, which are futures rather than options on futures. The text lists VIX futures with the futures and keeps all four names.
- Checked: the naked call against the call spread, "$111,500 to $4,200, by a factor of about 26": the ratio is 26.5, so the text now says "about 27".

## 12H · Exercise and assignment

- Fixed (dl:11.7): the SOQ example says "the short call is assigned at 6,005". SPX options settle in cash (Chapter 5A), so nothing is assigned in shares; the text says the call "settles 5 points in the money", which gives the same $500 per contract.
- Checked: the "after the bell" figure idea said a position turns into an assignment "in the two and a half hours after the close". From the 4:00 PM close to the 5:30 PM exercise cutoff is an hour and a half (2.5 hours is the figure's 3:00 PM start to the cutoff). It now says "in the hour and a half after the close".

## 13A · The retail haircut

- Fixed: dl:12A's worked example says the paper 1.1 becoming 0.30 to 0.35 is "a 65-70% Sharpe haircut". It is \(1 - 0.35/1.1 = 68\%\) to \(1 - 0.30/1.1 = 73\%\), so the text says 68% to 73% (it keeps 27% to 32%).
- Fixed: the cumulative-haircut column of spx:3.4's summary table is recomputed from the Sharpe ratios in the same table: 0.55 to 0.60 against 0.65 is −8% to −15% (as the source says), 0.45 to 0.55 is −15% to −31% (source "-15 to -30%"), and 0.20 to 0.40 is −38% to −69% (source "-40 to -65%").
- Checked: the PUT example's Step 4 said the account layer takes "a further 15% to 30%, leaving 0.20 to 0.40" (spx:3.4's own wording). From the self-managed 0.45 to 0.55, a cut of 15% to 30% leaves 0.315 to 0.47, so no reading of the range reaches 0.20. The step now gives both of the Edge Book's numbers as its estimates and says the end point assumes more than the stated cut, which would leave about 0.32 to 0.47.
- Checked: "an expense ratio of 0.44%, about 50 bps" read as a conversion, but 0.44% is 44 bps. It now says "0.44%, or 44 bps, which the Edge Book rounds to about 50 bps" (spx:3.1 gives ~50 bps, spx:3.4 gives 0.44%).
- Checked: the recap said 30% to 60% of the paper Sharpe ratio survives, "so a paper 0.8 routinely becomes 0.20 to 0.40". 30% to 60% of 0.8 is 0.24 to 0.48; the two source statements are now joined by "and" rather than "so".

## 13D · Worked examples: swing trades

- Fixed (known error): Example 2 gives "R=0.55 → C = 0.343". With Example 1's other factors the product is \(0.85 \times 0.90 \times 0.55 \times 0.90 \times 0.90 = 0.341\). The text says 0.341.
- Fixed (known error): the trade taken below 0.3. It is Example 5 in the source (AAPL, Undercut and Reclaim, "C = 0.282 (medium-low). Take at reduced size"), not Example 4 as CONVENTIONS.md and the README say; Example 4 is the Compression Breakout fakeout at 0.191, which the source passes. At 0.282 the trade is below Chapter 13B's floor of 0.3 (spx:4.2; the conviction figure says "pass or reduce"), so the chapter makes it a pass. It keeps the source's version and its outcome (a time stop at 172, $1,000, 1R) as what the trade did, and turns the lesson into one about outcome bias: a win does not validate a trade the rule excluded. The source's lesson, "smaller conviction = smaller size", is kept and extended: below 0.3 it means no position.
- Fixed: Example 7 gives "R=0.70 (event uncertainty), S=0.75 → C = 0.342" without the other factors. With Example 1's (the same "clean Trend Pullback setup"), the product is \(0.85 \times 0.90 \times 0.70 \times 0.90 \times 0.75 = 0.361\), and no combination of the chapter's usual values gives 0.342 (X = 0.85 gives 0.341). The text says 0.361; the conviction band (medium) and the decision (50% size) are unchanged.
- Fixed: Example 4 says SPY at 572 is "a 3.5% loss from the failed-breakout high" of 595. That is 23 points, 3.9%. A fall of 3.5% to 572 would start from about 593, near a breakout entry, but the source measures from the high. The text says 3.9%.
- Fixed: Example 6 gives "IBS = 0.14", but its own prices (high $517.00, low $513.00, close $513.50) give \((513.50 - 513.00)/4.00 = 0.125\). The text computes 0.125; both are below the setup's 0.20.
- Checked: Example 9 called the $580 loss at the original stop "the planned loss". It includes the fill's $0.80 of slippage: the loss planned at the 575 stop on 100 shares is $500, as the chapter's own definition of R and Example 2's use of "planned loss" require. The ratio 950/580 = 1.64 compares the two fills, as the source's "64% more loss than original plan" does, so the text now says "1.64 times the loss at the original stop".

## 13E · Worked examples: the portfolio

- Fixed: Example 2, gross premium. Twelve months at 0.36% to 0.54% a month is 4.32% to 6.48% a year, so "~4.5-6.5%/year gross" is now 4.3% to 6.5%.
- Fixed: Example 2, stress test. The source's per-contract marks were S1 ~$3,000 (3 contracts $9,000, 0.9%), S2 $8,000-12,000 ($24,000-36,000, 2.4-3.6%) and S3 $15,000-20,000 ($45,000-60,000, 4.5-6%). Their low ends fall below the floor set by intrinsic value less the $12-18 premium, the method the source itself uses in Example 10. The text gives S1 $4,200-4,800, S2 $10,200-12,000, S3 $19,200-20,000 a contract (keeping the source's upper ends as allowances for time value), and explains the $3,000 as a delta-only estimate that ignores gamma. The conclusion's "worst-case monthly MTM in S3: ~5% of portfolio" is now "about 6%".
- Fixed: Example 7's prices did not reconcile. A put struck at the money at 600 is $24 in the money after a 4% fall, so it cannot cost "$13 per contract for $1,300 to close"; and a $13 close with an "$8" loss implies a $5 sale, against Example 2's $12 to $18. The example now sells at a hypothetical $15 and buys back at $30 ($24 intrinsic plus $6 time value; Black-Scholes gives about $29.50 at 25% volatility and 22 days). The loss is $15 a contract, $4,500 in all (source: −$8 and −$2,400); closing one costs $3,000 and locks in $1,500 (source: $1,300 and −$800).
- Fixed: Example 7, "close 1 (rounded down conservatively) or 2 (rounded up aggressively). Conservative is closer to the rule": both miss the 50% target by half a contract. The text says so, keeps the Edge Book's choice of one, and notes that closing two is the more cautious reading of a risk limit.
- Fixed: Example 8, "stock drops 12%, you lose $80+ on the put side": 12% of $850 is $102, and a put sold for $32 loses $70; the text says $70, "and a deeper drop costs more". "You keep most premium (~+$30 per side)" on a $30 move is replaced by the straddle arithmetic: you keep $67 − $30 = $37. The per-side expected value (0.75 × 15 − 0.25 × 60 = −3.75) is kept as the Edge Book's rough model.
- Fixed: Example 9, Step 2 mixed scales: it set "$250k notional equivalent (1 ES contract)" beside "$9,000 margin" (0.6 of a contract) and an "$18,000 capital outlay" (which is the structure's cost for $150,000 of exposure), and compared that outlay with a yearly financing cost of $11,500. The text rebuilds the comparison on $150,000 of exposure: ES margin $9,000 (a deposit) against $17,900 of premium (spent); futures financing of 4.6% to 4.7%, $11,500 a year on a full contract and $6,900 to $7,050 on $150,000; the LEAP's extra drag of $750 to $2,250 against the futures' $150 to $300. The Edge Book's "50-100% more" is kept as its estimate, with the note that the capital comparison supports the upper end.
- Fixed: Example 9, Step 3. The stated distribution (60-70% at +$42, 25-30% at −$30 to −$80, 5-10% at −$158) has an expected value of +$0.33 at the midpoints and ranges from −$14.60 to +$14; the source's "+$15 to +$20 before friction" is above even the most favorable reading. The text computes it, then grants the Edge Book's +$10 (2.8% of $358) anyway. The source's net edge of "−50 bps to +180 bps" mixes drag assumptions at its two ends; with a yield of 0 to 2.8% and a drag of 0.5% to 1.5% the range is −1.5% to +2.3%. "Within noise" stands.
- Fixed: Example 9, Step 4. "LEAP loses ~80% of value (delta + vega both bad)": a long call has positive vega, so the rise in the VIX offsets part of the delta loss. The text attributes the loss to delta and keeps the 80% as the Edge Book's rough figure. "Short put spread loses near max ($150)" disagreed with the $116 in the source's own total ($320 + $116 = $436); the text uses $116 of the $158 maximum. The margin "~triples" is given as about $15,000 to about $45,000.
- Fixed: Example 10, Step 4 used "XSP 580 strike × 100" ($58k, 4 contracts $232k, 23%) after Steps 1 to 3 used a strike of 600. The text uses 600: $60,000 a contract, $240,000 for four (24%), or $58,800 of your own cash each after the $1,200 premium. The conclusion's "~$232k" is about $240,000, and "~$43k" is written $43,200.
- Fixed: Example 6, ZN sizing. "Similar sizing = 1 contract" does not follow from the same budget: a 1% move on one ZN contract is $1,100, so $5,000 allows up to 4. The text says so and keeps the Edge Book's 1 contract.
- Fixed: Example 6's score of 0.224 is below the 0.3 threshold of Chapter 13B ("do not trade"), while the source calls it "medium-conviction range" and trades a test size, the same issue as the known error in old 12D (its Example 4 in the source; 13D reads that trade, scored at 0.282, as a pass). The text states both readings for this trade: an exception (a pilot to generate personal evidence) or a pass, since the Edge Book's example deliberately takes it.
- Checked: Example 2's score, \(0.85 \times 0.90 \times 0.85 \times 0.90 \times 0.85\), was given as 0.50 and "high conviction, so allocate" (spx:11 says the same). The product is 0.497, below Chapter 13B's line of 0.5, the same rounding across a threshold as the known error of old 12D. The step now gives 0.497, calls it formally medium conviction and says the Edge Book rounds it to 0.50, reads it as high and allocates; the decision (2 to 3 contracts) is unchanged. The insight says the product "puts it at the line for high conviction", the summary table says 0.497 and the recap "about 0.50". Example 10, with sizing at 0.90, is the version that clears 0.5 (0.53).
- Checked: Example 1 said SPX's 12% a year at 16% volatility is "a Sharpe ratio of about 0.65", right after showing that the pitch's 0.85 is 11/13 with no risk-free rate taken out. On that basis SPX's figure is 12/16 = 0.75; 0.65 needs a risk-free rate of about 1.6% taken out. The text now says both, which widens the gap the example draws and leaves its conclusion as it was.

## 13F · Setup cards

- Checked: the text below Card F4 said Chapter 10H weights the sign of GEX "at a tenth of one filter at most", paraphrasing 10H's old rule. Chapter 10H now gives it "only 10% to 15% of one filter's weight", which is also the Edge Book's "10-15%" (spx:9). The text now says "only 10% to 15% of one filter's weight", and the Conflicts entry below says the same.

## 13G · The portfolio

- Checked: Level 1 attributed the factor-tilt rule ("a 24-month rolling Sharpe ratio below 0 cuts the tilt by 50%") to Chapter 10F, which does not state it (its kill rules are momentum's drawdown and tracking-error rules). Chapter 10A states it in its table, its worked example and its decision rule, and Card 05 of Chapter 13F repeats it, so the text now cites Chapter 10A. spx:14 names no chapter for it.
- Checked: the VRP row check said the row's 88% loss "would need about 2.5 times as much notional as the cash secures". By the step's own floor, two puts lose $38,400 to $40,000 in S3, 32% to 33% of their notional, so $110,000 needs \(110/40 = 2.75\) to \(110/38.4 = 2.9\) times as much. 2.5 is the ratio if the puts lost the index's full 35% with no premium kept. The text now says about 2.8 times.

## 13H · Managing total vega

- Fixed (known error, CONVENTIONS.md and README): the source said each widget position has "instrument, DTE, delta, vega per contract, and number of contracts", and that the overlay's targets are "flat vega, half-vega, or full hedge". The figure has no delta input and no days to expiry; its targets are the target vega: flat (a full hedge, zero vega), half of today's vega, or full (the vega left in place, so it buys nothing). The text says so and walks the three targets with numbers.
- Fixed: the template's management line read "[Allowed: stop trailed UP on winners, or full exit. NO stop migration toward profit.]", which contradicts itself, since trailing a stop up behind a winner moves it toward profit. The text reads it as forbidding stop migration in the sense of Chapter 11N (moving a stop away from the price as the price approaches it) and says so beside the template: "Allowed: a stop trailed up behind a winner, or a full exit. Not allowed: stop migration, moving the stop away from the price." (Raised by the writer of 11K to 11N.)
- Checked: the opening-state walkthrough wrote the strike as \(1.4 \times 17 = 24\). The product is 23.8, which the figure rounds to 24 ("strike ~24"), so the text now writes \(1.4 \times 17 \approx 24\).
