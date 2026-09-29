# Questions for the author

339 questions the rewrite raised, collected by `tools/spx.py` from the "Questions for the author" in `notes/*.md`. Answer them there, or in the chapter, not here.

## 1A · What a return is

- Symbol clash across chapters: 1E (another writer) uses G for the gain needed to recover a drawdown, D/(1 − D). Here G is the compound growth rate μ − σ²/2, as in the variance-drag figure's readouts. Symbols are defined per chapter, but one book-wide choice would be cleaner.
- The source says "a stock with 10% expected simple return per year". In discrete annual terms, E[ln(1 + R)] with a 10% mean and 20% standard deviation is about 7.9%, not 8%; the 8% is exact for the continuous-time drift. The text frames μ as the continuous-time arithmetic drift, which keeps the source's numbers exact. Say if you want the discrete caveat spelled out.

## 1B · The shape of returns

- Which sigma count for 1987 do you want as primary, 22 or 25? The quoted probability, 10^-137, matches 25.
- The −0.81 for SPX (spx:2.3, also used in 1D's skew tax): on what frequency of returns is it measured?
- The 30-delta put's outcome table (spx:0.1) is kept as given. Its mid-points imply a negative mean; the text does not compute it, because the ranges are rough. Is that the intended reading?

## 1C · Expected value and edge

- "These two examples are foundational in quant trading curricula and worth committing to memory" (dl:1C) is kept as the source's claim. Keep?
- The ev-bet-builder's verdict for a positive expected value reads "Strong edge. Play this game as often as possible." It ignores size, which this chapter's last section shows can turn a bet with edge into a losing one. The text says the verdict judges expected value only. You may want the verdict to say so too.

## 1D · Risk-adjusted return

- "Most published 'anomaly' Sharpe ratios in the academic literature shrink to indistinguishable-from-zero after deflation" is attributed by dl:1A to Bailey and López de Prado. Worth checking: the usual citation for the multiple-testing critique of published factors is Harvey, Liu and Zhu (2016).
- "A strategy with Sharpe of 4.0 (typical of intraday market-making)": kept as stated. Is there a source?
- spx:2.8 attributes "ES₉₅ for monthly returns of ATM PUT is roughly −8%" to Bondarenko's 2019 data; the headline numbers the sources quote from that paper do not include it. Keep the attribution?
- The worked long-equity/short-put example now uses a 1-in-100-year loss rather than a 5%-of-years one (above). If you prefer 5% of years, the loss that keeps the mean at $5 and the standard deviation at $10 is about $38.60, with gains of about $7.30, and B's worst year is then only 1.5 times A's.

## 1E · Drawdown, leverage and margin

- The put-spread dollar amounts ($30, $5, $25, −$22, −$10, −$5 "per contract") read as index points. An SPX option contract carries a multiplier, so the dollar loss per contract is larger. Should the example say "per unit of the index", or multiply out?
- "Box spread financing (no MTM risk)": a box's expiry value is fixed, but its market value moves with interest rates before expiry. Is the claim meant as "no margin-driven path risk"? The chapter keeps the source's words.
- "Cash-secured short put held to expiry" as not path-dependent: this holds for European-style index options such as SPX and XSP. An American-style put can be assigned early. Should the text limit the claim to index options?
- "Naive Gaussian math says max drawdown over 10 years should be around 25%": which statistic is meant (the median maximum drawdown, the expected one, a percentile)? A figure built on this needs the definition.
- Is the SPX "~10%" return over 1990 to 2024 an arithmetic or a compound annual figure? The PUT index figure elsewhere in the book (dl:1A) is a compound 9.54% to 2018.
- "Sizing 30-50% smaller than what the terminal payoff would suggest": smaller in contracts, or in the risk budget allotted? The chapter keeps the source's wording.

## 1F · Correlation, diversification and liquidity

- Tail correlations (spx:0.6): over what window and threshold were the 2008, 2022 and "left tail" figures computed (worst 5% of months, a crisis window)? A figure that reproduces them needs the definition.
- "8 of 10 largest 60/40 drawdowns positive" (trend following): which trend index and which 60/40 series?
- "SPX/XSP normal-condition spreads are tight (a few cents on liquid strikes)" and "widen 10-50×": is there a source or a date range for these, as there is for Govindaraj-Li-Zhao (2020)?
- The source calls the gap between paper and live results "mostly" liquidity (spx:0.8), while Chapter 13A's haircut layers also include fees, taxes and behavior. Should the two statements be reconciled?

## 1G · Where an edge comes from

- McLean and Pontiff (2016): the source reads "a 26-58% decline in factor returns post-publication, depending on the factor". As I recall the paper, 26% and 58% are two different comparisons (the decline out of sample but before publication, and the decline after publication), not a range across factors. Please check the reading. The chapter keeps the source's wording.
- Jensen, Kelly and Pedersen (2023), "~47% post-publication decline across hundreds of factors": please confirm the figure and the paper.
- "This single classification step eliminates 80% of the noise in retail trading content": is 80% a measured figure or a manner of speaking? As it stands it is an unverifiable claim.
- "ERP is paid for in 30-50% drawdowns", "Momentum lost -73% from March-May 2009" and "Value's 2010-2020 drawdown was the worst in modern history": which series (index, long-short factor) and which sources?
- The ~7% S&P 500 inclusion effect "in the 1990s": is it from Greenwood and Sammon (2024) too, or from another study?
- The Cboe 2025 study has no title or link in the sources. The reading list (R3) will need one.

## 2A · What the S&P 500 is

- The tick column gives "$0.05 / $0.10" for SPX and XSP and "$0.01 / $0.05" for SPY. Which increment applies when (by premium level, or by product class)? The text gives both values without the rule.
- Which year is the divisor "in the eight-billion range"?
- Are any XSP series AM-settled? The table says PM; the SOQ paragraph lists XSP with SPX and VIX.

## 2B · Where your order goes

- "US equities and single-name options have been required to execute at or better than the NBBO" since Regulation NMS. Regulation NMS's trade-through rule covers NMS stocks; listed options have their own linkage rules. The text keeps the source's claim. Should it be narrowed?
- Apart from the Citadel quotations, the wholesaler shares ("as of late 2025/early 2026 data") and the FLEX volumes carry no named source. Can they be attributed?
- Rule 605's realized spread is measured against the mid "a short interval later". Should the text give the interval the 2024 amendments use?
- The two block quotations run to 39 and 46 words, over the brief's sentence limit. They are verbatim and kept whole.

## 2C · The order book

- Inverted markets. The source's rationale, "traders who want immediate execution badly enough are willing to pay for it explicitly, while liquidity is harder to attract", does not say which side pays for what: on an inverted venue the resting order pays and the taker is paid. The text keeps the source's sentence. Should the mechanism be spelled out?
- "When your resting order fills, the trade was almost certainly initiated by someone with marginally more information": kept at its strength, though the break-even model the text adds lets any fraction of traders be informed.

## 2D · What execution costs

- The square-root law is "the Almgren-Chriss square-root law" in dl:2D. Almgren and Chriss (2000), cited in Chapter 2C for optimal execution, model impact as linear in the trading rate; the square-root form is usually credited to later empirical work. Keep the attribution, or reword it?
- "A VRP-harvest strategy that collects 80 bps of annual edge over realized variance gets erased by a single 30% round-trip spread": the 80 bps is a yearly return on capital and the 30% a share of one option's premium, so the sentence mixes scales. The $0.30 against $0.40 example that follows is the one that computes, and the text leans on it. Restate the 80 bps sentence in dollars?
- Rule 4's windows (10:30 to 11:30 AM and 1:30 to 2:30 PM ET) and "the first 15 minutes ... widest spreads of the day as overnight charm and vanna unwinds clear": is there a source to cite?
- The journal's "Most retail traders ... guess 10-20% of spread. The journaled data routinely shows 40-60%": whose data? The text keeps the claim at its strength.

## 2E · Accounts, margin and taxes

- The corrected tax gap (10.2 points like for like, not 12 to 14) also changes Chapter 2A's summary, which now quotes both. Is the author content with presenting the quoted figures beside the corrected ones, or should the quoted ones go?
- The iron-condor comparison under portfolio margin: "both wings 5% out-of-the-money ... portfolio margin might require only the loss that would occur in a ±15% scenario — perhaps 1/3 the Reg-T number". If the short strikes sit 5% out of the money, a 15% move passes through them and the scenario loss is close to the spread's full width, the Reg-T number. The one-third holds only for wide wings. Which structure is meant? The text keeps the sentence with its hedges ("might", "perhaps").
- "Most retail accounts with $2,000+ equity qualify for Reg-T margin" and "The first PM account every trader opens is operated incorrectly": kept at the source's strength. Is there a source for either?
- Do the Pattern Day Trader thresholds need a date, given the rule's history of proposed changes?

## 3A · What a trading model is

- Purged k-fold cross-validation as López de Prado (2018) describes it also trains on data after the test fold, with purging and an embargo, rather than strictly before it. Should the chapter describe that procedure, or is the walk-forward description the intended one?
- "Lookahead bias is the most common backtest error in retail strategy development" and "the central empirical finding of three decades of academic finance" carry no citation in the source. They are kept at the source's strength. Is there a source to name?

## 3B · Mean reversion and momentum

- The Hurst paragraph says H < 0.5 for mean-reverting and H > 0.5 for persistent series. For any AR(1) with |w| < 1 the variance ratio settles at (1 + w)/(1 − w) at long lags, so over very long horizons the variance grows linearly again. The H the figure reads is a short-horizon one (lag 8). The text says the readout uses lag 8 but does not open this subtlety. Should it?
- "Typical first-order autocorrelations on daily SPX returns are between −0.05 and +0.05": which period and which data? A figure of the estimate over time would need them.

## 3C · Fitting a model

- "Saddle points ... are vastly more common than local minima in high-dimensional spaces" and "Adam ... the default choice in most modern ML codebases" carry no citation in the source and are kept at its strength.

## 3D · Position size and trading frequency

- The corrected worked example reverses a stated conclusion of the source. Please confirm the reading: \(G\) and \(L\) per dollar staked, Kelly far above the loss budget for this edge. If the example was meant to show Kelly as the more conservative rule, it needs a weaker edge (for instance 52% at even payoffs, where quarter-Kelly and the 1% budget coincide, as the chapter's third check question shows).
- The source says Thorp's research was "extended by Kelly (1956)". Kelly's paper came first, and Thorp's work applied it to gambling and markets. Should the text give the order, and with what dates for Thorp?
- "In any realistic behavioral model" (quarter-Kelly with a 30% discipline beating full Kelly) and "the dominant retail cost is slippage" carry no citation in the source. They are kept at its strength.
- "Most production quant strategies use either piecewise-linear or smooth-tanh sizing, calibrated so that the cap corresponds to half-Kelly": kept at the source's strength. Is there a source?

## 4A · What a derivative is

- The BIS figures (roughly $700 trillion of OTC notional, roughly $50 trillion exchange-traded): which survey, and which year? The book avoids "recent", so the year should be in the text, and R3 needs the citation.
- "Interest rate swaps with no fixed termination" as perpetual instruments: a standard interest rate swap has a fixed term (Chapter 4B's example runs 5 years). Which swaps are meant? The cryptocurrency perpetual future is enough to make the point if the swap example is doubtful.
- "For 95% of trading needs this is fine; for 5% ... it's not": a manner of speaking or a measured split? As written it reads as a statistic. The chapter keeps it.
- FLEX volumes (12 million contracts in 2012, 200+ million in 2024, 1.3 to 1.4 million a day in 2025, open interest from 2 million in 2019 to 35 million in 2025) and defined-outcome ETF assets (near zero in 2018, over $50 billion by 2024, over $100 billion in 2025): what are the sources? Chapter 2B's source (dl:3B) quotes Cboe for some of these; R3 needs them.
- Assignment: is the two-stage reading right (the OCC assigns at random to a clearing member's account, and the broker allocates among its customers by FIFO or at random)? The source's parenthesis can be read that way; the text says it plainly.

## 4B · Futures, swaps and options

- ES initial margin "~$15,000-$22,000 depending on volatility regime": is this the exchange's requirement or a typical broker's, and for which year? Margin schedules change, and the figure should be dated.
- "Most institutional FX hedging uses forwards rather than futures": is there a source for "most"?
- Please confirm the two fixes above (the direction of the swap conversion and the collar's decomposition).

## 4C · Why derivatives exist

- The VRP units: is "3-5 percentage points of annualized variance" meant as volatility points? If it is variance, which sample gives 0.03 to 0.05?
- The BIS figures (foreign-exchange derivatives notional of roughly $100 trillion; interest rate swaps over $500 trillion; commodities in the trillions): which survey and which year?
- "Eurodollar futures encode the market's expectation of central bank policy": as I understand it, Eurodollar futures were retired with LIBOR and replaced by SOFR futures. Should the text name SOFR futures, or date the statement? The chapter keeps the source's words.
- "Many retail accounts have been destroyed by over-leveraged option positions": is there a source, or is this a manner of speaking?
- The history ("traceable back to ancient grain markets and formalized in modern form in the 19th-century Chicago Board of Trade") and "plausibly comparable in importance" are kept as written; R3 may want a citation for the first.

## 5A · The option contract

- "US-listed broad-based index options (SPX, XSP, NDX, RUT, VIX) are European-style: this is a structural consequence of the cash settlement." The chapter keeps the claim. Cash-settled index options can be American-style, though (the S&P 100's OEX options are one example), so European exercise may be better described as a design choice that goes with cash settlement than as a consequence of it. Should the sentence say "goes with"?
- The XSP example's "potential assignment liability equal to 10 × $100 × strike ... $580,000 of cash-secured collateral obligation". For a cash-settled put, assignment pays the in-the-money amount in cash; $580,000 is the obligation only if XSP went to zero ($575,500 net of the premium). The text calls it the potential assignment liability and the collateral a cash-secured version must hold, which is accurate. Is that the intended reading?

## 5B · What an option's price is made of

- The rebuilt chain (above) is the largest change in this chapter. If you prefer the original numbers, the text around the chain would need to say that they are stylized and do not satisfy put-call parity.
- "A sudden 50,000-contract OI increase at a specific strike, when daily volume was also 50,000 contracts, tells you a single large player took a new position at that strike." The arithmetic shows that every contract traded opened a position on both sides; that one player was behind it is an inference. The text keeps the source's wording and adds the arithmetic. Should it be hedged ("most likely")?
- "Two trades at this spread to enter and exit can wipe out three months of theta collection" assumes a rate of theta that the source does not give. Kept as the source's hedged "can".
- "The further out of the money, the higher the extrinsic value relative to the intrinsic" (kept from dl:5B). An out-of-the-money option has no intrinsic value, so the ratio is undefined there, and read literally the sentence runs against the chapter's point that extrinsic value peaks at the money. Is it meant for in-the-money options moving toward the money, where the extrinsic share of the premium grows? (Raised by the second check of the maths.)

## 5C · The Greeks

- The vega correction above: is $680 a contract (6.8 points) the figure you want, or did the source mean a different expiry or unit?
- "The 2022-2023 Fed hiking cycle moved option valuations measurably through the rho channel for the first time in over a decade" and "the variance risk premium is, in aggregate, the empirical observation that this trade has paid for the dealer historically" are kept as the source states them. Neither names a study or data; Chapter 10C may be the place for the evidence.
- The probability map uses a 1.5% dividend yield, while the simulator and the Greek surface use none. The text says so where it quotes each, but the three figures would be easier to compare with one convention.

## 5D · Higher-order Greeks

- "The well-documented 'Monday gap-up' anomaly" and "the empirical regularity of Monday gaps and the 'charm bid' into OPEX Fridays": the source cites no study. Is there one to name?
- "Charm ... operates on calendar time": this is true of the Black-Scholes clock, which counts calendar days. Should the text say that desks that price on a trading-day clock see the weekend drift at Monday's open instead? The chapter keeps the source's statement and offers this as a figure idea only.
- "Roughly 95% of the higher-order dynamics": the author's own estimate, kept as such. Confirm it should stand without a source.
- Volmageddon: "the dealers short the VIX call wing had massively negative volga". Who were these dealers, and is there a source for the loss dynamics? Kept as written.
- "By the final hour of trading on OPEX Friday, virtually all the dealer gamma is concentrated within $5-10 of spot": for which index level? At an SPX near 6,000 that is 0.1% to 0.2% of spot. The chapter keeps the dollar band as written.

## 5E · Volatility

- "If the market is quoting a 30-day ATM SPX call at $35": no index level is given. By the ATM shortcut, $35 for 30 days implies an IV near 5% at an index of 6,000, so the number reads as an illustration of the definition only. The chapter keeps it and does not compute its IV; the worked inversion uses a hypothetical $100 underlying instead.
- Which Bondarenko analysis gives the +4.2 vol points for 1990 to 2018? The Edge Book cites Bondarenko (2014, 2019).
- The efficiency figures (about five and seven to eight times close-to-close) hold for a driftless continuous price without gaps. Should the text say so? The "When it fails" callout says the range estimators assume continuous prices within the day.
- "SKEW above 145 historically has preceded mean-reverting vol spikes": over what sample, and how often did readings above 145 come with no spike? The chapter keeps the claim and adds, as teaching, that a signal's hit rate depends on the base rate of spikes.
- "Retail traders systematically overpay for upside speculation (lottery-ticket calls on meme stocks, OTM SPY calls on event days)": is there a study behind this, or is it the author's observation?

## 5F · Put-call parity and the risks at expiry

- "Each of these risks has destroyed more retail accounts than missed delta calls": kept as the author's judgment. Is there evidence behind it, or should it be softened?
- "The OCC has never failed to deliver in its history": kept. Is there a date or source to cite?
- "Gap risk is ... modest for SPY (typical Monday gap of 0.2-0.5%, occasionally 2-5% on stress weekends)": over what period were these measured?
- "The 2020 March drawdown saw bid-ask spreads on liquid index options expand to 10× their typical width": which options and which data? The worked roll uses a hypothetical $0.20 spread.
- "GameStop in early 2021 had borrow rates exceeding 100% annualized at peak": source?
- The rule of thumb for early put exercise ("time value under $0.50 and a strike that would generate more than 2% annual interest") and Chapter 12H's test (strike × rate × time against time value) can disagree: a $0.40 time value on a $50 strike at 3% with a month left fails 12H's test ($0.125 of interest) but passes the rule of thumb. Should one of them be preferred?

## 5G · The volatility surface

- Skew timing: are the 5E pattern (flattening before vol spikes) and the 5G pattern (steepening 1 to 3 days before sell-offs) meant as two horizons of one cycle? Is there a source for either?
- "In typical equity environments, IV percentile is roughly 2× IV rank": over what sample of stocks and years?
- "Typical value: 4-8 vol points in normal conditions, expanding to 12-15 vol points during stress": at which tenor? The chapter's toy and check use 30 days.
- Stock B (front-month IV 60%, 90-day IV 28%, earnings in 5 days) is consistent only if the front month has fewer than about 19.6 days left, since 0.28² × 90 / 0.60² = 19.6. Should the example give the front month's days to expiry? The chapter's worked example assumes 10.
- "Sell premium via put credit spreads at high-delta strikes": does "high-delta" mean short strikes nearer the money? Kept as written.
- "Late 2020, mid-2024 NVDA-led periods" as examples of skew flattening: kept; is there a data source to cite?
- The strategy table's contango row, "Back IV high, front IV low: long forward vol" (kept from dl:5G). In contango the forward volatility between the two expiries sits above the back month's IV, and the chapter's own rule is to sell the rich part of the curve and buy the cheap part, which would point to short forward vol. Is long forward vol meant as a bet that the contango steepens? (Raised by the second check of the maths.)

## 6A · Who is on the other side

- The lifecycle's "$3.05" SPY $600 call with delta 0.58: if it is the 30-day call of the opening scene, Black-Scholes at 18% IV prices it near $13 to $15. $3.05 fits an option a few days from expiry. The chapter keeps the numbers and does not tie the lifecycle to 30 days. Which expiry is meant?
- "$0.02 better than their internal sub-mid mark": what is "sub-mid"? A $3.03 mark is above the midpoint of any quote whose bid is above $3.01. The chapter calls $3.03 the wholesaler's internal mark.
- "With per-contract edges in the $0.50-$2.00 range ... and hundreds of millions of contracts annually, the franchise produces multi-billion-dollar revenues": hundreds of millions of contracts at $0.50 to $2.00 give about $50 million to $2 billion. Multi-billion revenues need billions of contracts, as the paragraph before says. Kept as written; the toy example uses 1 to 2 billion contracts.
- Sources for "Citadel Securities lost $3 billion in March 2020", the $50 billion of monthly retail flow, and institutional spreads "10-30 bps wider than the SIP NBBO"?

## 6B · What the dealer inherits

- The source explains ½σ² in d₁ as accounting for "the lognormal distribution's mean [being] shifted upward relative to the median in log space". The chapter keeps that reading and illustrates it. Strictly, d₂ carries r − q − ½σ² (the risk-neutral median of the log price), and d₁ adds σ√T to it. Is a sentence on that wanted, or is the heuristic enough at this level?

## 6C · Delta hedging

- "Sharpe ratios in the 0.5-1.0 range ... strong by intraday standards, though insufficient to support strategy deployment after transaction costs": is the second half the authors' finding or the Lab's judgment? The chapter keeps it unattributed.
- Sources for the practitioner thresholds (a residual delta of 5% to 10% of the position; a spot move of 0.25% to 0.50%; hourly or slower for structured-product desks) and for "moves into 4 pm ET frequently extend rather than reverse"?

## 6D · Gamma

- A source for "Aggregate dealer dollar gamma across the listed SPX book typically ranges from $20B to $100B per 1% move on a normal day"?
- "Modern SPX intraday character has compressed measurably since 0DTE growth": which measure, and which study?
- Should the long-gamma example use the figure library's settings (delta 0.536, trades of about 7,700), so that a reader who checks with the units lab gets the same numbers?
- One clock for the book? Chapter 5C's breakeven move uses a calendar day (0.25/√365 = 1.31%), while 6D's rule cites 5C for "IV ÷ √252" and 7A also uses √252; for the same option 6D uses about $240 a contract a day of theta (the full theta) and 6E about $200 (its gamma part). Each is right on its own clock. Should the book pick one, or name the clock each time? (Raised by the second check of the maths.)

## 6E · How often to hedge

- Which spread is meant for the SPX hedge: $0.10 (0.17 bp) or 1.7 bps? With a tenth of the friction, the spread column shrinks and the optimum moves finer.
- Should theta be restated per trading day (about $1.48 million) or the capture per calendar day, so that the net column is on one clock?
- The spread column does not follow one rule. At notional × 0.83 bp: 5 bps × 40 rebalances of $11.5 million is about $38,000 (the table's $80,000 matches paying the full 1.7 bps each time); 15 bps × 15 is about $43,000 (table $36,000); 25 bps × 6 about $29,000 ($22,000); 50 bps × 3 about $29,000 ($15,000); 200 bps × 0.5 about $19,000 ($3,000). Is the column meant as stylized?
- The rebalance counts: a random walk with a 1.26% daily move crosses a 5 bp threshold about (126/5)² ≈ 635 times a day and a 25 bp threshold about 25 times, against the table's 40 and 6. Are the counts for a particular path?
- Sources for "the cumulative path length ... is typically 2.5–4× the net move", for single-stock spreads of 5 to 15 bps with an optimum of 30 to 60 bps, and for dealers' realized-volatility estimates in illiquid products exceeding true volatility?

## 7A · Why hedging works

- "It falls out of the PDE": the PDE is derived for one price-taking hedger, whose trades do not move the price. The feedback loop needs aggregate short gamma and hedging large enough to move the price, which is Chapter 8B's model. Should the sentence say it falls out of the hedging P&L once dealers' trades move the price? Kept as written.
- "The unique correct strategy": unique under the model's assumptions (continuous trading, no costs, no jumps). Kept as written; the "When it fails" callout lists the assumptions.
- "For most retail-scale ... delta-hedged positions, the first-order framing captures the bulk of P&L variability": is there a study behind this, or is it the author's judgement? Kept without attribution.
- The VIX is "fundamentally, the cost of replicating variance": the VIX is quoted as a volatility, the square root of that variance's fair strike. Should the text say so here, or leave it to Chapter 9A?

## 7B · Second-order Greeks in context

- The aggregate vanna flow: is "several hundred million to over a billion dollars" for a 500,000-contract book meant to be consistent with the example's 17,500 share-equivalents per 5,000 contracts ($79 million at SPX 4,500, so about $7.9 billion one for one)? If the range assumes a different mix of strikes and expiries, or SPY-share units, the text should say which.
- The Monday gap-up anomaly "documented in SPX since the 1990s": which study? notes/5d.md asks the same.
- "Empirically, the Monday-gap-up anomaly is more consistent with calendar-time charm decay", and "most dealer risk systems use calendar-time conventions for short-dated positions": is there a source for either?
- "The most you'll typically see this contribute to the SPX move post-FOMC is 0.3-0.5%, but it operates with high reliability across years": is there a study behind the range and the reliability?
- The charm example states no IV. Should it give one (about 16% with zero rates), so a reader can reproduce 0.004 a day?
- "100,000 SPX OTM put contracts (a typical institutional book)" sits oddly beside the FOMC example's "500,000-contract aggregate put book" for the whole dealer community. Is 100,000 meant per institution and 500,000 for one strike's aggregate?
- "Roughly 95%" (both versions) is unsourced; confirm it should stand as the author's estimate.

## 8A · Gamma exposure

- "Hundreds of trillions of dollars of open interest" (the part's opening). For listed SPX this seems far too large; is it meant as the notional of all derivatives worldwide? Kept as written.
- "Scaling the aggregate by a factor of 3-15× — which a real strip-vs-toy ratio supports": is there a source for the ratio? Kept as the source's claim.
- "Barbon and Buraschi (2021) find gamma imbalance effects of around 16 bps per standard deviation": 16 bps of what (an intraday return?) per standard deviation of what (the gamma imbalance measure?). Kept as written.
- "Real-world put-wing gammas under steep skew can be several times the BS-implied number ... consistently understates put-side gamma": is there a source? Kept with its hedge ("can be").
- "Volmageddon's VIX call wing was in FLEX" and "The March 2020 vanna cascade ran through structured-product hedges as much as through listed puts": sources? Kept as written.
- The stylized gamma profile (0.0013, 0.0010, 0.0006 at 0, 100 and 200 points) is narrower than Black-Scholes gives at 18% and 30 days (about 0.00129, 0.00121 and 0.00102). The text calls it stylized, as the source does. Should the toy use the Black-Scholes values? The total would rise to about +$8.1B with the same open interest.

## 8B · Two regimes

- Ni, Pearson, Poteshman and White (2021): "alters the probability of large daily moves (over 300 bps) by 5-14% historically, rising to 13-40%": relative changes in the probability, or percentage points? Kept as "by 5% to 14%".
- The illustrative κ = 0.0010 with G in the hundreds: what units does the Dealer Mechanics Lab have in mind for G (billions of dollars per 1%)? The text says only the product κG matters.
- Barbon and Buraschi: the source's "intraday momentum (reversal) is explained by the interaction of negative (positive) ex-ante gamma imbalance and illiquidity" is written out as two clauses. Please confirm the pairing (momentum with negative imbalance, reversal with positive).

## 8C · When the framework breaks

- "VIX had risen from 14 in late January to 53 by Friday March 13 — the largest two-week VIX increase in history at that point": is the two-week claim about the final two weeks of that rise? Which dates and levels?
- The inversion date: late February, seven trading days before March 16 (which would be March 5), or March 9?
- "Dealers were short gamma in the wings (the put protection that institutions had bought as COVID escalated)" and "SPX dealer gamma was short going into the event" (August 2024): what source shows the dealer positioning in each case?
- "Volmageddon's VIX call wing was in FLEX" (8A) and "Dealers sitting on the other side of VIX call wings were short gamma in vol-of-vol" (here): is there a source that names the dealers or the size of the wing?
- Robinhood's deposits "from ~$700M to >$3B": the source does not name the testimony. Which hearing and witness? The text says only "later congressional testimony".

## 8D · Gamma squeezes

- D, the dark ratio: the source says that D rising while P rises is "hidden accumulation". The text explains why short volume can mean buying (market makers selling short to fill purchases). Please confirm that this is the reading intended, or give the one you want.
- "mad − MA(mad)": is mad the mean absolute daily move, and over what window? The text says "a recent window" and does not give a length. What window does the moving average of mad use?
- tanh normalization "on a rolling window": is each indicator standardized (for example as a z-score over the window) before tanh? The text says only that tanh is applied over a rolling window.
- "Critical — typically > 20% of float, often > 50%" (single-name short interest): is there a source for these thresholds?
- Rule 2 assumes an exit at 50% of the intraday peak. For a position bought far below the peak, that exit may still be a profit; for one bought near the peak, it is a loss of about half. Should the text say which case the rule is aimed at? The worked example (entry $120, peak $200) and the check question (entry $80, peak $150) both show entries above half the peak, where the exit is a loss.

## 9A · The VIX

- The put-wing asymmetry at the index level. With the figure's default smile held fixed to its strikes, a 1% shock moves the computed VIX by +0.12 on a fall and −0.11 on a rise, nearly symmetric; the gap only opens at larger moves (+0.72 against −0.44 at 5%). The at-the-money IV does move 4.5 times more on the fall. So in this toy the −0.80 correlation cannot come mainly from the strike weighting of a fixed smile; it needs the level of implied volatility to rise in falls. Should the text say so?
- The vanna figure's steps are stylized well beyond Black-Scholes for a put 2% below spot: its vanna step of 0.07 for a 1.8-point IV rise is about 16 times what a 30-day put gives (0.004). Should the figure state an expiry and a strike further out, or should its caption say the vanna step is exaggerated for visibility?
- Step 5 of the figure reads a delta shift of +20,000 but a hedge flow of 19,500. Is the gap meant to be a lagging hedge? The text reports both readouts as they are.
- "weighted continuously per the CBOE methodology": what was meant? The chapter drops the phrase.
- VIX futures settlement: the source says Friday morning; Chapter 2A and the Wednesday expiry say Wednesday. The chapter follows Chapter 2A. Please confirm.
- UVXY is given as 2× leveraged long VIX futures. Please confirm the multiple against the issuer's current documents.
- VXX's "approximately −10% annualized" drag sits uneasily with the Edge Book's "VXX has lost 99.84% from 2009 inception through 2024" (Chapter 10I), which compounds to a loss of about 35% a year. Both are kept in their own chapters; which should this chapter's figure be?
- At K₀ the toy uses a single quote ($52). If Cboe's rule differs (an average of the put and the call there), should the toy say so? The chapter adds nothing about it.
- The −0.80 correlation, "reliable stress indicator" and "preceded major SPX drawdowns in nearly every multi-year cycle" have no cited study. Is there one to name?
- VIX options: do they reference the VIX index (dl:9A) or VIX futures (dl:4A, Chapter 4A)? The two chapters now read differently.

## 9B · Same-day options

- How is the upper end of "0.04% to 0.17%" derived? The median of $173 million per point against $400 billion gives 0.043% for a 1% move; 0.17% would need a move of about 4%, or another gamma figure.
- "Dealer gamma in 0DTE was likely net short" on the April 2025 and October 10, 2025 days: is there a source for the estimate? Kept with "likely".
- The 110 million contract record: is that all US listed options? The chapter says "the single-day options volume record", as the source does.
- The source cites Brogaard, Han and Won (2024) as a University of Utah working paper; is there a title to give?

## 9C · Reading the tape

- The classifier's GEX scale runs from −$10 billion to +$10 billion per 1% move, with every reading above +$4 billion scoring the same. Chapter 6D (dl:6E) puts aggregate dealer dollar gamma across the listed SPX book at $20 billion to $100 billion per 1% move on a normal day, while Cboe's 0DTE figures (−$1.1 billion to +$2.4 billion) fit the slider. Is the classifier meant for 0DTE GEX, or for whole-book GEX from a vendor? The chapter describes the slider as "net dealer GEX", as the figure labels it.
- "Ni, Pearson, and Poteshman document 16.5 bps return alteration on equity expiration days": which measure is this (an average absolute return shift for stocks near high-open-interest strikes)? The reading list dates the paper 2005, as Chapter 8A does.
- "Tens of basis points per standard deviation": the standard deviation of what? The worked example reads it as the standard deviation of dealer gamma imbalance, following Chapter 8A's Barbon and Buraschi figure.
- The claim that a regime-aware backtest "persists out-of-sample more reliably than most other technical signals" has no cited study. Is there one?

## 10A · Five kinds of edge

- "Most overlays add 10-30 bps of Sharpe": is this 0.10 to 0.30 of Sharpe ratio (the scale of spx:8.7), 0.001 to 0.003 (a literal basis point of Sharpe), or 10 to 30 bps of return? The chapter quotes the phrase and gives both readings.
- "VRP has been positive in roughly 80% of months for 30+ years": which series and which measure (the VIX against the following month's realized volatility, or the PUT Index's excess return)?
- "Trend has been positive in every decade since 1880": Hurst, Ooi and Pedersen (2017) run to 2016. Does the claim cover the 2010s in full, and anything after?
- "ERP has been positive in 35 of 35 markets in the Dimson-Marsh-Staunton database": over each market's full history, real or nominal, and over bills or over bonds? Chapter 10B's source says 23 of the 35 markets have the full 1900 to 2024 history.
- "Tracking error to academic factor > 4% annualized → switch vehicle": is the benchmark the academic long-short factor or a long-only factor index? A long-only ETF's tracking error to a long-short factor is usually large, which would trip the rule at once.
- "The Cieslak FOMC even-week cycle": the chapter glosses it as the equity premium concentrated "in the even weeks of the cycle between meetings of the Federal Open Market Committee". Please confirm the gloss; Chapter 10G gives the detail.
- The Cboe 2025 figure ("~0.2% of liquidity"): of SPX daily liquidity (spx:1.5, Chapter 1G) or of futures liquidity (dl:12E)? Chapter 1G's notes raise the same question.

## 10B · The equity risk premium

- Damodaran's implied ERP of about 4.3% for 2025: is it measured against the 10-year Treasury rate or against bills? The comparison with the realized premium ("over bills" or "over long bonds") depends on it.
- The valuation rule compares \(1/\text{CAPE}\), a real earnings yield, with the nominal 10-year Treasury yield. Is that intended, or should the comparison use a real (inflation-protected) yield? The chapter keeps the rule as written.
- "$1 invested in equities in 1900 grew to ~$107,409 nominal by 2024" and "$1 in long bonds grew to ~$268": from which edition of the Dimson-Marsh-Staunton data, and with dividends and coupons reinvested?
- The misconception says "US ERP has been ~7% real" and advises "4-5% real as a planning assumption". Is the 4% to 5% a real return on equities or a real premium over a safe asset? The chapter keeps the wording.
- "Germany 1900-1955" and "US 1929-1949" as multi-decade negative real returns: on which series (price or total return)?

## 10C · The variance risk premium

- The Sharpe ratios of about 0.65 (PUT) and 0.49 (SPX) sit beside compound growth rates and volatilities that would imply different risk-free rates (about 3.1% and 2.5%) if computed from them. Are the Sharpe ratios based on arithmetic means, or on another period?
- "Positive ~80% of months" and "mean ~+4 vol points": which series and which window (the toy example's 1990 to 2018, or longer)?
- "PUTW ... changed strategy in 2023 to weekly options": please confirm the year and the change, since the chapter tells readers the passive vehicle is now a different variant.
- "-28% in March 2020" for the PUT index: a peak-to-trough drawdown within the month, or the monthly return?
- Bondarenko (2014, 2019): the reading list (R3) will need titles.
- The Edge Book dates the same PUT Index figures (9.54%, 9.95%, 0.65, −33%) to 1990 to 2018 here (spx:6.2) and to 1986 to 2018 in its Chapter 3 (Chapter 13A). Which period is right? (Raised by the second check of the maths.)

## 10D · Trend following

- "Positive in 8 of 10 largest 60/40 drawdowns — including 2008 and 2022": Hurst, Ooi and Pedersen (2017) run to 2016, so which study or data set covers 2022?
- "Positive in every decade since 1880": does the 2010s decade, which contains the 2011 to 2018 drought, count as positive in the study's decades (which may run 2007 to 2016)?
- Live indices "realized Sharpes 0.3-0.5 over 20 years": which years? Edge Book 3.5 gives 2003 to 2024 for the SG Trend Index and the BTOP50.
- DBMF's "1-2 month lag": is it a lag in replicating positions, or in reporting? The chapter says the fund infers positions from recent returns and lags by 1 to 2 months.

## 10E · Carry

- Please confirm the fix to the carry formula's sign (see Changed).
- The VRP column of the stress table: −$110,000 in S3 on a $150,000 sleeve is 73% of the sleeve for a 35% fall in SPX, and −$25,000 in S1 is 17% for a 10% fall. A cash-secured at-the-money put sleeve would lose roughly the index's fall, less the premium, plus some mark-to-market; Chapter 1D puts the S3 loss of a $250,000 sleeve at $100,000 to $150,000 (40% to 60%). Is the table's sleeve levered, or marked at stressed prices?
- "Without trend, the same scenarios would lose another 5-10%": is that 5% to 10% more than the loss (the chapter's reading, which matches the table), or 5 to 10 points of the portfolio?
- The TED spread: Chapter 10H's source reads it as SOFR less the Treasury bill rate, since LIBOR is gone. Does the 200 bps threshold of this chapter's kill rule carry over unchanged to the SOFR-based measure? The chapter keeps "TED spread > 200 bps".
- "QSPRX/QSPIX-style mutual funds have closed/restricted": as of which year? A date would keep the page timeless.
- "MOVE > 150": in the index's own units; the chapter does not convert them.

## 10F · Equity factors

- Momentum's tax drag (spx:7.2): an ETF such as MTUM usually passes little of its turnover to holders as taxable gains, because it can shed low-basis shares through in-kind redemptions. Is "best held in tax-advantaged accounts" about a self-run momentum portfolio, or about the ETF? The chapter keeps the source's claim.
- "Add 0.2-0.4 of Sharpe to the equity sleeve": is this the information ratio of the tilts, or a rise in the sleeve's own Sharpe ratio? Read literally, the second needs 3% to 6% a year of extra return, above the 0.5% to 1.5% the same chapter expects.
- Quality "did not crash through the 2017-2022 value drawdown", while value's drawdown is dated 2010 to 2020 in spx:7.3. Which window is meant for quality's test?
- AQR Equity Market Neutral and AQR Absolute Return are multi-factor funds rather than pure value portfolios. Are their results (−38% by December 2020; +43.5% in 2022, +18.5% in 2023) meant as evidence about value specifically?
- "QUAL captures perhaps 60-70% of the academic factor premium", "Long-only captures roughly half the long-short Sharpe", and "Bali et al. (2017)": what are the sources? The reading list (R3) will need them.
- Jegadeesh and Titman (1993): over which sample are the "UMD ~1%/month, t≈3, Sharpe ~0.5" figures?

## 10G · Calendar and flow effects

- "NBER WP 33554 (2024) 'The Unintended Consequences of Rebalancing'": the authors are not named. The reading list (R3) will need them.
- "~17 bps" next-day effect: per quarter-end, per day, or per unit of divergence?
- "Aggregated across $5T in 60/40 mandates": which source gives the $5 trillion?
- "FOMC even-week tilt: +0.10-0.30 Sharpe" against spx:5.4's "most overlays add 10-30 bps of Sharpe": Chapter 10A (written in parallel) raises the same question of scale. The toy in this chapter, with equal daily volatility, gives a relative rise of 13% for a 25% odd-week cut, about 0.05 on an equity Sharpe ratio of 0.4, below the quoted range unless the odd weeks are cut much further.
- "Transaction cost discipline: if costs exceed 100 bps annualized, simplify": against an overlay worth 10 to 40 bps a year, a cost of up to 100 bps would already make it lose money. Is 100 bps meant as a hard ceiling, or should the trigger be a fraction of the expected gain?
- The Cieslak sample: "1994-~2014 in their analysis". Please confirm the end year.
- Stivers and Sun (2013): "~30 bps/week excess return" is for option-active large caps; the toy then holds SPY. Is SPY's own OPEX-week return in the paper?
- 180 bps per FOMC cycle over about eight meetings a year is about 14% a year from the even weeks alone, roughly twice the equity premium of Chapter 10B, so the odd weeks cannot have returned "about 0" over the same years unless the full-year total is far above the index's. Which figure should give way? (Raised by the second check of the maths.)

## 10H · Regime filters

- "ProShares 'Term Structure' research notes" and "Bloomberg/CBOE practitioner literature" (9.2): titles and dates for the reading list (R3)?
- "A disciplined filter stack can prevent the GFC-style -33% PUT drawdown" and "Empirically this opportunity cost is much smaller than the avoided drawdown benefit" (9.7): which backtest or study supports these?
- "March 2020 stayed >40% for 6+ weeks" (9.3): which estimator and window (21-day close-to-close)?
- "preserve only deep-OTM tails for assignment risk" (9.2): does it mean keeping the deep out-of-the-money shorts, whose assignment risk is small, or keeping long deep out-of-the-money options as protection?
- "(3-month LIBOR - 3-month T-bill, now SOFR-T-bill)" (9.4): LIBOR has been replaced; is SOFR minus the bill rate a published series, and are the 20-30, 100 and 250-400 bps levels (set in the LIBOR era) still the right scale for it?
- "long-vol funds cost 5-15% annual decay" (9.1) and "VXX has lost 99.84% ... since 2009 inception" (through 2024, per spx:10.8): sources?

## 10I · What not to trade

- Kurov, Halova, Wolfe and Gilbert (2021, *JFEcon*): which journal is "JFEcon", and is "the 2014 introduction of 'dot plot' projections" right? The Fed's dot plot is usually dated to 2012. The chapter keeps the source's wording.
- "-2 to -3 vol points realized after costs" against "+1-3 vol points net" for the short put spread's VRP (10.7): which is meant, and what does the minus sign mean?
- Greenwood and Sammon (2024): is the "<1%" figure for additions after 2010, as spx:5.6 says, or for "recent decades"? And is the 1990s 7% from Shleifer (1986) and Harris-Gurel (1986), whose samples end before the 1990s, or from later work?
- "With 40%+ of SPX volume now in 0DTE": as of which year?
- "VXX has lost 99.84% from 2009 inception through 2024": VXX was relaunched as a new note in 2019; is the figure for the combined series?
- SSO's "expense ratio 0.85%" and SVXY "now de-leveraged": as of which date?

## 11A · The market dashboard

- What does exactly one failed condition in the quick trend read mean: a wait, a smaller size, or still Stage 2?
- Is the undecided band of the volatility read (VIX percentile from the 60th to the 80th, in contango) meant to go to the composite of 11G?
- The translation table's thresholds (VIX under 16, VIX/VIX3M under 0.95, HY OAS under 400) differ from the marker tables' (VIX 14 to 18 normal, ratio under 1.0, HY OAS over 450 elevated). Is the gap deliberate, a buffer for the "quiet bull" state?
- "Delta-adjusted premium" is not defined in the source. The text defines it generically, as premium scaled by delta; vendors' definitions may differ.
- The source says a 0DTE share above 55% "supports Adams et al. (2025) framework" without saying how. The text points to Chapter 8A for the paper's finding.
- "Steep ATM curve up = event premium nearby" is read as a steep rise in at-the-money IV into the tenor that holds the event.

## 11B · Conditional mean reversion

- Tier A includes "official exchange or regulatory data", yet "0DTE composition data from Cboe" sits in Tier B. Is that because the composition, who is trading, is an estimate rather than a count? The chapter keeps the source's placement without comment.
- What should "sized larger than the trades that fail any of them" mean in practice: a fixed size step for three-gate trades, or only that failed trades get nothing?
- The thesis would be easier to trust with a number: the conditional next-day or next-week return after down stretches in the "on" regime, net of costs. Does the Dealer Mechanics Lab have one?

## 11C · Indicators

- ADX above 25 "corresponds empirically to negative-GEX regimes": is there a study or a dataset behind this? The text says the source cites none.
- "Donchian breakouts often coincide with mechanical institutional rebalancing flow at quarter ends": the Edge Book treats quarter-end rebalancing as a small effect (10G, 10I). Is there evidence for the coincidence?
- `s.ewm(span=n).mean()` defaults to `adjust=True`, which weights the first values differently from the recursive EMA until the history is long. The text keeps the source's call for the standard EMA, now written as a method of a series, and gives `adjust=False` only for Wilder. Should it say `adjust=False` for both?
- "The 23-indicator menagerie": the source names 16 plus "several others". The text keeps "some 23".

## 11D · Chart patterns

- Which period should Mansfield relative strength use? The source leaves it open.
- Is the "recent daily range" of the flag rule the ATR, and is the minimum 2 or 3 of them?
- The handle is "typically 3-12 weeks" and "shorter" than a cup "lasting weeks to months". A 12-week handle can outlast a short cup. Should the handle's length be tied to the cup's?
- "Final pivot should have a range less than 5% of price": which price, the pivot high, its low or the close? The text divides by the pivot high.

## 11E · Stage analysis

- Does "Stage 1 ... (otherwise)" mean that every bar the first three rules miss is Stage 1? If so, the ADX gate would matter, and the figure, ported rule for rule from the app, disagrees with the text. Which is intended? If the gate should bite, the figure needs a different fallback.
- The source says "30-bar". Should the chapter say which bar length the classifier is meant for, daily or weekly?
- Is the figure's readout "DON'T BUY DIPS" to be kept as the app prints it, beside the book's "DO NOT BUY DIPS"?

## 11F · Multiple timeframes

- What slope counts as a flat higher timeframe? Is Chapter 11E's ATR-normalized band the intended definition?
- Which RSI period does the 40-65 band assume, and how close to the 21-EMA counts as a pullback to it?
- Is there any published test of the triple screen's returns to cite, or is it offered as discipline only?

## 11G · The composite scorecard

- How are raw inputs scaled to the −1 to +1 range, and are the signals within a dimension weighted equally? The source says only that each dimension "averages multiple signals".
- Sentiment is "contrarian on short horizons ... aligned on longer horizons": which horizon does its score take?
- Should the composite carry an event-proximity input, as dl:10I says it does?

## 11H · Four swing setups

- Is "20-100× the dollar risk" meant for equity swing trades in general, or for the Trend Pullback, whose stated stops imply 100 to 200 times?
- The Compression Breakout requires positive GEX, while its mechanism has dealers short the upside. Is the intended picture short call gamma just above the range inside positive aggregate GEX?
- IBS and RSI: is the stop at the signal day's low, known at entry, or at the entry day's low named in the invalidation? dl:12D's Example 6 uses the signal day's low with a buffer.
- "A breakout on volume below 100% of average is statistically more often a fakeout than a continuation": is there a study or dataset behind it?
- Which grade should Connors' RSI(2) carry, Tier B or Tier 1?

## 11I · Pre-earnings momentum

- Condition 5, "Forward IV not cheap": as written it says that if forward IV is below 70% of ambient, the exit before earnings is mandatory, but the exit is mandatory in every case. Is it meant as a filter that excludes such candidates, or as a reminder?
- Is there evidence that the priced size of the event rises into reports, beyond the mechanical rise of the quote? Without it, the "structural IV bid" is available to long options only when the event is repriced.
- "A single bad earnings outcome can wipe out 10-20 successful pre-earnings momentum trades": at what average win and loss? With the example's 1.2R win and a 15% gap against a 3.5% stop (4.3R), one loss erases about 3.6 wins.
- The NVDA timeline: which day count was intended?
- The ORATS composite of the at-the-money straddle and the first two OTM strangles: with what weights?
- The figure's verdict says that "across many trials, the negative skew of single-name earnings moves makes exit-T-1 dominant in expectation". The figure computes one path, and neither source gives evidence on the skew of earnings moves. The text reports it as the verdict's claim and proposes a many-path figure.
- How should 13D's Example 8 (defined risk, not shares, in event weeks) be read beside this chapter's shares-by-default with an exit before the report?

## 11J · Post-earnings drift

- Should the NVDA example's Real Value make it a skip, with the trade shown only to illustrate management, or were different factor scores intended?
- Which pivot was meant for the entry, since $762 is above both the pullback low and the entry?
- Was the trim meant at +0.75R ($765.50), as the profit-taking rule says, or at $795?
- "Opening hour volume >2× the 20-day average": the 20-day average of daily volume, or of opening-hour volume?
- "Rising relative volume + accumulation signatures": which measures are meant?

## 11K · Catalyst trades

- "accepting the 0.15R cost to reduce gap exposure": half of a position at +0.3R carries 0.15R of open profit, and trimming banks it rather than losing it. Is the 0.15R the forgone upside of the trimmed half, an execution cost, or something else?
- "Close all positions ... original full position unchanged": was the untrimmed Trend Pullback position closed at 3:45 PM, and if so at what R, or was it kept open under its own 5-day time stop?
- "Vanna unwind signature confirmed (VIX down 3 points in 30 min)": from which level? From 19 before the release it is 2 points, from the spike to 22 it is 5, and from Tuesday's 20 it is 3. And is the entry signal's "VIX drops > 2 points within 15 minutes of the announcement" measured from the pre-announcement level or from the spike?
- "implied move on SPX for Wednesday is ±1.2%": the chapter treats it as the straddle's expected move, about 0.8 of a standard deviation (Chapter 11A). Please confirm.
- The chapter reads "enter ... when IV is elevating into the announcement but the event hasn't been fully priced" as a bet that the event is repriced, since the quote on a fixed expiry rises by arithmetic alone while the option decays. Please confirm the reading; Chapter 11I (pre-earnings IV ramp) should agree with it.
- Should the chapter warn an oncologist reader that trading options around a readout of a trial they work on, or have confidential knowledge of, would be trading on material nonpublic information? The source is silent, and the warning would be a new fact, so it is not in the text.

## 11L · Single stocks and the index

- "60% of weight in top 10 holdings" for QQQ: as of when? Holdings drift, and the chapter gives the figure without a date because the source gives none.
- "Mag-7 stocks have pairwise correlations of 0.5-0.8 during normal conditions and 0.8-0.95 during stress": over which period, and daily or weekly returns? The figure's matrices are illustrative and run lower at calm (0.35 to 0.70).

## 11M · Choosing an expiry

- "Trend Pullback | 14-30 DTE if using options; immediate exit if using equity": what does "immediate exit" mean for shares? The chapter reads it as "shares carry no expiry, so nothing constrains the exit". If it means something else (exit at the first target, say), the row should say so.
- "A 7 DTE call costs 30-50% less than a 30 DTE call at the same strike" and "paying 30% more for an option that has 3× the time to develop": at the money the square-root rule gives about 52% less and 73% more. The chapter shows both figures hold for a call about $10 in the money on a $600 stock at 16% implied volatility. Should the text name the moneyness it has in mind?
- "Retail traders consistently choose shorter DTEs than is optimal for their stated thesis": is there a study behind this, or is it the author's observation? The chapter attributes it to the source.

## 11N · How swing trades fail

- "Time stops exist because empirical work shows that swing setups that don't pay within their typical horizon have low forward expected value": which work? The chapter keeps it as the source's account and adds a Bayes illustration with hypothetical numbers.
- "Most retail traders believe this about themselves. The data systematically refutes it.": which data? The chapter points to Chapter 13A, whose evidence (Morningstar's "Mind the Gap", dl:12A) concerns fund investors' timing rather than traders' behavior under stress.
- "The act of writing slows the decision by 20-30 seconds": measured, or illustrative?

## 12A · Choosing a strategy by purpose

- "Iron condor (with extreme selectivity per 11A)": which section was meant? The text points to the iron condor entry (Chapter 12C).
- "shares + LEAP (PMCC)": is this two alternatives (shares, or a LEAPS-based poor man's covered call), as the text reads it, or shares held together with a LEAPS call?
- Principle 1 says to spread a long call on a single name through an event. Is the reason the IV crush on the premium, as Example 4 suggests, or something else?
- The IV bands overlap at their edges: 30 and 70 each belong to two bands as written ("< 30", "30-70", "> 70" leave 30 and 70 in "normal", but Example 4 reads 70 as rich). Which band owns each edge?
- The four-question filter asks for the horizon but neither the matrix nor the figure uses it. Should the matrix say that the horizon chooses the expiry, as the text now does?

## 12B · Novice strategies

- The example premiums are far below model values at the implied volatilities they state: the 6,050 call is about $101 at 18% and the 5,950 put about $127 at 22%, against $35 each. The text keeps the numbers and says they are illustrative. Should the examples be re-priced, which would move every breakeven and profit?
- The subtitle mismatch above: should the subtitle drop "simple spreads", or should a spread join this tier?
- "Negative drift baked into option premium structures": is this the variance risk premium (Chapter 10C), the put skew, or both? The text points to 10C.

## 12C · Intermediate strategies

- The CNDR figure's stand-in series put CNDR at 3.61% a year and the total-return index at 14.16 times CNDR by 2024. The Edge Book's own numbers give about 5.5% and about 7.1 times. Should the figure's stand-in series be rescaled to match the published figures, or replaced by the real index history?
- The premiums in the examples are illustrative and differ across entries for the same strike (the 6,000 call is $35, $40, $50 or $25 in different examples). Is that intended, one self-contained example per entry?
- The iron butterfly entry has no worked example in the source; the text works its formulas once with a hypothetical credit. Should a full example be added?
- Collar: "The 'JPM Hedged Equity Fund' collar is this on SPX." The text keeps the name as given. Is the comparison meant loosely? If the text is to describe the fund, its actual option structure should be checked against a source, since it may differ from a plain collar.

## 12D · Advanced strategies

- The naked put's Reg-T rule is "approximately 20% of strike value − OTM amount" here and "20% of underlying minus OTM amount + premium, same formula, floored at 10%" in dl:11.6. Should the atlas use one form? Cboe's rules may set a lower percentage for broad-based index options such as SPX than for equity options; if so, the 20% in both places overstates the SPX requirement. This needs checking against a current margin source.
- Ladders: should the reversed ladders (bear call ladder, bull put ladder, as some sources name them) get their own entries?
- "When used systematically with cash-secured collateral (XSP strangles), can be operationally viable": a strangle's short call cannot be secured by cash in the way a put can. Is the intended meaning a strangle held with enough cash to cover the put's assignment and a stress loss on the call?
- The short strangle's "probability of profit about 70%" (dl:11.3) does not follow from the example's own premiums, which imply about 8% volatility and give about 64%; at 15% to 18% volatility it would be about 33% to 39%. Which premiums or which probability should the example use? (Raised by the second check of the maths.)

## 12E · Expert strategies

- "Within 5–25 bps of broker margin call rates for borrowing": is the broker call rate meant, as the text reads it? If the margin rates retail brokers charge were meant, the sentence contradicts the next one.
- Box friction: is "1–4 cents per share of width" meant per dollar of width, as the $100 to $400 implies? At those costs a 90-day box's $60 of interest is lost to friction, which may understate how cheaply boxes trade. Worth checking against current quotes.
- The Robinhood box-spread story of 2019: was it SPX or SPY, and was the loss from margin calls or from early assignment? The text avoids naming the instrument until this is checked.
- The box example's 2.45% against 4.2% T-bills: should the example be re-priced to a credit near the T-bill rate (about $9,898), so that it does not show an arbitrage the source says does not exist?

## 12F · From a market view to a structure

- "Cards 1-7": which cards were meant? If the first seven rows of the cross-index, the rule reads naturally as "for the directional and mean-reversion views, prefer SPX or XSP"; the text states it for index views generally.
- The modest bullish drift row prefers a call debit spread at 45 DTE for a view of 2 to 4 weeks; the worked example uses 30 days for simplicity. Should the example use 45?

## 12G · Options margin

- Cboe's margin rules may set a lower percentage for broad-based index options such as SPX than the 20% the source uses for every underlying. If so, every SPX figure here overstates the requirement. This needs checking against a current margin source before publication.
- The iron condor rule: is the "vertical-spread margin" of each side its width less the condor's whole credit (the text's reading, which makes the requirement equal the maximum loss), or less that side's own credit?
- The short put's floor: the source says "floored at 10%" without a base. The text keeps the floor at 10% of the underlying for both calls and puts, as the call's rule states. Is a different base intended for puts?

## 12H · Exercise and assignment

- "SPX/XSP weekly options settle to the 4:15 PM PM-settled close" and "Weekly SPX (PM-settled to the Friday 4:15 PM close)": PM-settled SPX options are generally described as trading until 4:15 PM ET but settling to the index's official closing value, computed from the 4:00 PM closes of its stocks. The text keeps the source's wording; please check it.
- "any long option that closes more than $0.01 in-the-money": the OCC's exercise-by-exception threshold is usually described as $0.01 or more in the money. Which is right? The text keeps "more than".
- "Pin risk peaks for short options near strikes" is placed at Thursday's close (T − 1). For equity options and PM-settled index options the risk is usually described as peaking at Friday's close. Is Thursday meant for the AM-settled SPX monthlies, whose last trading day is Thursday? The text keeps the source's placement.
- The timeline is headed "monthly equity options, third Friday" but also covers SPX weeklies and monthlies. Should it be split by product?

## 13A · The retail haircut

- The swing example's tax step takes the Sharpe ratio from 0.65 to 0.45 at an effective 40% rate. A proportional tax with full loss offsets scales the mean and the volatility alike and leaves the ratio unchanged; the example implies that tax cuts the mean but not the swings. Please confirm the intended model, or give the example's \(h_3\) another basis.
- Please confirm the corrected haircut of 68% to 73% (source 65-70%) and the recomputed cumulative haircuts of the PUT table.
- Morningstar's Mind the Gap figures (100 to 200 bps a year for two decades) carry no edition year in either source. Which editions?
- "A single force-liquidation event during a 30 VIX environment can wipe out 12-18 months of accumulated edge" has no source; kept at its strength.
- The figure's buy-and-hold baseline, SPX at a user Sharpe ratio of about 0.40, comes from the app with no source in the prose. The text attributes it to the figure.

## 13B · The conviction score

- "the discipline that prevents 80% of bad trades" (spx:4.6) and "Cboe 2025 study found 0DTE MM hedging is ~0.2% of liquidity" (spx:4.4) carry no citation beyond the text. Kept at their strength.
- Should the Real Value threshold be 0.4 (as stated) with the table's 0.3 to 0.5 band reading "half size from 0.4", or is a half-size trade from 0.3 intended?
- The regime bands leave a composite of 0 to +10 unscored. Is a band intended there?
- Scenario C: were the 50% puts meant to be on margin? If they are cash-secured, the forced-liquidation reason for S = 0.20 needs restating (for example, as a behavioral capitulation risk).
- The sizing factor asks for "aggregate vega/delta within portfolio limits (per 12F)" (dl:12B), but dl:12F, Chapter 13H, sets limits on vega only. Should the book give a limit on the book's total delta, and where?

## 13C · From signal to trade

- "Behavioral economics (Thaler, Sunstein) shows that ex-ante decisions made in calm states are more rational than ex-post decisions made under stress" cites no specific work. Which?
- The selectivity figures (60% to 70% of days, 1 to 3 a week, 6 to 12 a month) are stated "empirically" in dl:12C with no source. Kept at the source's strength.
- Which kill rules should the book adopt for the Compression Breakout and IBS + RSI setups, those of dl:12C or those of dl:10G and dl:12E?
- "Margin cushion" is not defined in the sources; the chapter defines it as equity above the requirement, as a share of equity. Please confirm that is the intended measure.

## 13D · Worked examples: swing trades

- Example 1: $850 per contract for an 85-point move is $10 a point, which matches one XSP contract moving one for one with the index. Is XSP the intended instrument? The text leaves it unnamed.
- Example 2: where was the planned stop? A loss of $3,500 at 140% of plan implies the exit (5,920) came below the planned level, presumably Friday's low.
- Example 8: "NVDA gaps 7% on earnings" does not give the direction. The lesson ("the trades you skip are sometimes the trades that would have hurt you most") implies a gap against the long; the text leaves the direction open.
- Example 7: "vol crush gives 0.5R" gives no mechanism for a gain on a long index trade; kept as stated.

## 13E · Worked examples: the portfolio

- Example 2: is the "realistic 2-4%/year net contribution" a return on the collateral or on the whole portfolio? The text reads it as on the collateral, because a whole-portfolio reading needs 11% to 22% a year on $180,000.
- Example 2 and Card 02 put the S1 loss of an ATM put at about $3,000 and $3,500 a contract, below the intrinsic-value floor ($4,200 to $4,800 at a 600 strike). Were these delta-only estimates? The text now gives the floor and explains the lower figure.
- Example 7: are the rebuilt prices ($15 sold, $30 to close) acceptable, or did you intend a smaller fall than 4%?
- Example 8: at 75% implied volatility, a 3-day ATM straddle on $850 is worth about $46 (0.8 × 0.75 × √(3/365) × 850), close to the "~$45" expected move; the quoted $35 + $32 = $67 implies about 109%. The text keeps both as given without deriving one from the other. Should the prices or the IV change?
- Example 9: at an interest rate near 4.5% (the source's SOFR plus 10-20 bps ≈ 4.6-4.7%), a 2-year at-the-money call is bounded below by about S − K·e^(−rT) ≈ $431 before dividends, and its delta would be well above 0.50. The setup is labeled illustrative and kept; do you want realistic prices?
- Example 10: was the strike meant to be 600 (Steps 1 to 3) or 580 (Step 4 and Card 02)? The text uses 600 throughout.

## 13F · Setup cards

- Card 02's S1 loss of −$3,500: was it a first-order estimate? It is below what the put's intrinsic value allows.
- Card 04 names RSST as the carry vehicle; Chapter 10D (from spx:6.3) describes RSST as US stocks plus managed futures. Is there a carry fund you meant, or is RSST's futures book the intended exposure?
- The FOMC overlay's skip rule: is "stop distance × 1.5 exceeds 2× normal portfolio risk" meant as the dollar loss at the widened stop at the size you would hold? Under the overlay's own half size, that loss is 0.75 of normal, so the rule bites only for unusually wide stops or unhalvable positions.
- Card 02's net 3% to 5%: a return on the collateral? The text reads it so, as it reads 13E's Example 2.

## 13G · The portfolio

- B_exp: "expected loss budget" (spx:14) or "explicit loss budget" (spx:11, spx:13)? The text follows the latter.
- The stress table's VRP, trend and carry rows repeat the dollar figures of the Chapter 6 foundation table on smaller sleeves. Should they be rescaled to $125,000, $125,000 and $50,000, or computed from the cards? The text keeps them and shows the card-based check.
- The pragmatic risk target sums to 90%: where does the remaining tenth go?
- Who is Ahmed, for a reader of this book, and what is the BTF-style bot? The text keeps both names as the source gives them.

## 13H · Managing total vega

- The two vega limits: were the NAV percentages meant per 10 volatility points? At 0.1% of NAV per point, a $1 million account's threshold would be $1,000 a point, inside the $500 to $1,500 band, and "0.5% of NAV" would become $500 a point, the band's floor.
- "Several hundred SPX vega units": is the unit dollars per volatility point, as the text assumes?

## R2 · The maths on one page

- Which thresholds should the VIX term-structure filter use: the summary card's (halt new short volatility above 1.05, cut 50% above 1.10) or Chapter 9's (halt above 1.00, cut 50% above 1.05, close all but deep tails above 1.15)?

## R3 · Reading list

- Which author list is right for the 2021 paper on the disappearing pre-FOMC drift: Kurov, Sancetta, Strasser and Wolfe, or Kurov, Halova, Wolfe and Gilbert?
- "Bondarenko (2014), Cboe PUT Index empirical analysis" has no title or journal, and the chapters also cite Bondarenko (2019). Should the list give both, with titles?
