# Literature search: empirical evidence on dealer gamma and prices

Area: EMPIRICAL EVIDENCE. Feeds the rewrite of Part VIII of "The Other End of the Trade".
Compiled 2026-09-29. Every source below was confirmed by a search result (Consensus or WebSearch)
showing its title and authors; the confirming URLs are listed per entry. Details not seen in a
search result are marked [unverified].

Conventions used in this file:
- "Dealer" means the option market maker / liquidity provider side as the paper defines it.
- Effect sizes are quoted in the paper's own units, followed by a plain-language reading.
- bp = basis point = 0.01 percentage point. SD = standard deviation.

## Sources

### A. Pinning and expiration

### NiPearsonPoteshman2005
- Citation: Ni, S. X., N. D. Pearson and A. M. Poteshman (2005). "Stock price clustering on option expiration dates." Journal of Financial Economics 78(1): 49-87. DOI 10.1016/j.jfineco.2004.08.005. SSRN version: abstract_id=519044.
- Type: peer-reviewed article.
- Verified via: https://consensus.app/papers/details/00f6db59793954a6b7d502a06400bf9e/ (title, authors, journal, DOI, abstract); https://ideas.repec.org/a/eee/jfinec/v78y2005i1p49-87.html (volume 78, issue 1, pages 49-87); https://www.sciencedirect.com/science/article/abs/pii/S0304405X05000577 ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=519044 . Sample dates and data sources below come from search-result summaries of the paper's text.
- Question: Does option trading move the prices of the underlying stocks on expiration dates?
- Data and method: US individual stocks with listed options ("optionable") against stocks without listed options, 1996-2002. OptionMetrics Ivy DB (end-of-day quotes, open interest and volume on every US-listed single-stock option, January 4, 1996 to September 13, 2002), plus CBOE data that split open interest and volume by type of trader, used to measure the net option positions of market makers and of firm proprietary traders. Test: the distribution of closing prices relative to the nearest strike on expiration Fridays (and the preceding Thursday) against other days, and against non-optionable stocks.
- Findings: (1) On expiration dates the closing prices of optionable stocks cluster at strike prices; non-optionable stocks show no such change. (2) "On each expiration date, the returns of optionable stocks are altered by an average of at least 16.5 basis points, which translates into aggregate market capitalization shifts on the order of $9 billion" (abstract). Reading: 16.5 bp is a lower-bound estimate of the average size of the return distortion per stock per expiration date, for single stocks, in 1996-2002; it is not a directional return and not an index figure. (3) Mechanism: clustering is much more frequent when market makers who delta-hedge are net LONG options (long gamma: they sell above the strike and buy below it) than when they are net short. The authors also find evidence consistent with manipulation by firm proprietary traders, who can profit from moving the close relative to a strike where they hold options.
- Limits: Single stocks only; the paper does not measure an S&P 500 index pin. The effect is a pre-2003 estimate, before penny quoting of options, weeklies, and electronic market making at today's scale. Later work finds the clustering persists for monthly expirations but is much weaker for weekly single-stock options, and absent in many individual firms (ZhangEtAl2013/2017 below). The manipulation channel means not all clustering is hedging.
- Use in the book: The canonical pinning citation (Chapters 8A, 9C, 11B, 13B). CORRECTION: the book (8A limit 5; 9C) converts 16.5 bp into "about 10 points of SPX at 6,000". That transfers a single-stock, lower-bound, per-expiration distortion to the index, which the paper does not study. The index-level evidence is GolezJackwerth2012. The book's 9C statement that pinning needs dealers who are LONG gamma at the strike is consistent with this paper; that condition also means the 16.5 bp cannot be read as an effect of short-gamma dealers.

### KrishnanNelken2001
- Citation: Krishnan, H. and I. Nelken (2001). "The effect of stock pinning upon option prices." Risk (magazine), December 2001.
- Type: practitioner article (trade magazine), theoretical model.
- Verified via: search summaries of the references in Avellaneda, Kasyan and Lipkin (2012) and Jeannin, Iori and Samuel (2008): https://math.nyu.edu/inmemoriam/avellaneda/PowerLaw.pdf ; https://www.citystgeorges.ac.uk/__data/assets/pdf_file/0010/89974/0604_jeannin-et-al.pdf ; https://consensus.app/papers/details/445af86fa62452c98ce4d3e9662dcade/ . Unverified: the exact title wording ("upon" in one summary, "on" in another) and the page range (one summary gave S17-S20).
- Question: How should options be priced if the stock tends to finish at a strike?
- Data and method: No data. The log price follows a Brownian bridge that ends at the strike with probability p and ordinary Brownian motion with probability 1 - p; the model prices the effect on options of pinning, motivated by hedge funds selling large amounts of options to floor market makers.
- Findings: A pricing model, not an estimate. It assumes pinning rather than deriving it from hedging.
- Limits: Descriptive; no mechanism and no test.
- Use in the book: History of the pinning idea, and the contrast between assuming a pin (Krishnan-Nelken) and deriving it from long-gamma hedging (AvellanedaLipkin2003).

### GolezJackwerth2012
- Citation: Golez, B. and J. C. Jackwerth (2012). "Pinning in the S&P 500 futures." Journal of Financial Economics 106(3): 566-585. DOI 10.1016/j.jfineco.2012.06.010. SSRN abstract_id=1664261.
- Type: peer-reviewed article.
- Verified via: https://consensus.app/papers/details/79ed465239ea504e828a0b00e3462b1d/ (title, authors, journal, DOI, abstract); https://econpapers.repec.org/RePEc:eee:jfinec:v:106:y:2012:i:3:p:566-585 (volume 106, issue 3, pages 566-585); https://www.sciencedirect.com/science/article/abs/pii/S0304405X12001365 ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1664261 . Unverified: the exact sample years and the share of expiration days pinned (not seen in any search result).
- Question: Does pinning occur at the index level, in S&P 500 futures, around the expiration of options on those futures (CME serial options) and of SPX index options?
- Data and method: CME S&P 500 futures and the options on them, with SPX (Cboe) index options for the cross effect; daily and intraday behaviour of the futures price relative to the at-the-money strike on expiration days, sample years [unverified].
- Findings: (1) Pinning: S&P 500 futures "are pulled toward the at-the-money strike price on days when serial options on the S&P 500 futures expire". (2) Anti-cross-pinning: the futures "are pushed away from the cost-of-carry adjusted at-the-money strike price right before the expiration of options on the S&P 500 index". (3) Mechanism: market makers rebalance delta hedges both because of the time decay of those hedges (charm) and in response to individual investors reselling, and exercising early, in-the-money options. The time decay on its own produces anti-pinning; the reselling and early-exercise channels outweigh it, so the net effect at serial expirations is pinning. (4) Size: "The associated shift in notional futures value is at least $115 million per expiration day" (abstract). Reading: a lower bound on the notional value moved per expiration day, a small number beside the S&P 500 futures market.
- Limits: Pre-0DTE sample. The channel is specific to American-style futures options (early exercise) and to a pit/early-electronic era. It shows index pinning exists but is small in dollar terms; it gives no basis-point figure comparable to NPP's 16.5 bp. Anti-cross-pinning means the sign of the expiration effect depends on which option complex expires and on hedge decay, not simply on open interest at a strike.
- Use in the book: The correct citation for an index-level pin (Chapters 8A, 9C). It supports "pinning is real but small" and adds a complication the book lacks: charm on its own pushes AWAY from the strike (anti-pinning); the pull toward the strike came from investor behaviour (reselling, early exercise) that dealers absorb.

### AvellanedaLipkin2003
- Citation: Avellaneda, M. and M. D. Lipkin (2003). "A market-induced mechanism for stock pinning." Quantitative Finance 3(6): 417-425. DOI 10.1088/1469-7688/3/6/301. Follow-up: Avellaneda, M., G. Kasyan and M. D. Lipkin (2012). "Mathematical models for stock pinning near option expiration dates." Communications on Pure and Applied Mathematics (2012) [volume and pages unverified]. DOI 10.1002/cpa.21404.
- Type: peer-reviewed articles (theory).
- Verified via: https://consensus.app/papers/details/6436d72b30605e68bb8aeb621491db18/ (2003: title, authors, journal, DOI, abstract); search result showing "QUANTITATIVE FINANCE VOLUME 3 (2003) 417-425" (https://www.cis.upenn.edu/~mkearns/finread/PinningPaper.pdf); https://consensus.app/papers/details/445af86fa62452c98ce4d3e9662dcade/ (2012 paper: title, authors, journal, DOI).
- Question: Can aggregate delta hedging by market makers who are long a large open interest at one strike drive the stock to that strike?
- Data and method: A stochastic differential equation for the stock price with a singular drift that represents the price impact of delta hedging; the probability of pinning is computed from volatility, time to maturity, open interest and a "price elasticity" constant.
- Findings: The stock has a finite probability of finishing exactly at the strike when market makers are long the options at that strike; the probability rises with open interest and price impact and falls with volatility and time left. The 2012 paper cites NPP 2005 as the conclusive empirical evidence.
- Limits: Theory; the elasticity constant is not estimated from market data in the abstract seen.
- Use in the book: The formal model behind 9B's "magnet" and 9C's pinning; it makes explicit that pinning requires dealers LONG the options at the strike (long gamma), the opposite of a gamma squeeze.

### FilippouGarciaAresZapatero2023
- Citation: Filippou, I., P. A. Garcia-Ares and F. Zapatero (2022, revised 2023). "No Max Pain, No Max Gain: Stock Return Predictability at Options Expiration" (later retitled "No Max Pain, No Max Gain: A Case of Predictable Reversal"). SSRN abstract_id=4140487; Boston University Questrom School of Business Research Paper. DOI 10.2139/ssrn.4140487.
- Type: working paper (SSRN; first posted June 18, 2022; revised November 9, 2023, per search summary). Not found as a journal article.
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4140487 ; https://consensus.app/papers/details/68a591e6f5395f1d82f3ac84992f6d0c/ ; https://www.econbiz.de/Record/no-max-pain-no-max-gain-stock-return-predictability-at-options-expiration-filippou-ilias/10013405282 ; https://pedrogares.wordpress.com/2022/08/18/no-max-pain-no-max-gain-stock-price-predictability-at-options-expiration/ ; https://sites.google.com/view/iliasfilippou/working-papers .
- Question: Does "max pain", a retail folk level (the strike at which the total payoff owed to option holders at expiry is smallest), predict stock returns into expiration?
- Data and method: US stocks on NYSE, AMEX and NASDAQ with listed options, 1996-2021 (25 years). Each stock gets a "Max Pain gain/loss" measure (distance of price from its max-pain strike); stocks are sorted into portfolios; a long-short spread buys high-measure stocks and sells low-measure ones through expiration.
- Findings: The spread earns large, positive, statistically significant returns and alphas, about 0.4% per week on average (search summary), strongest in small-cap and illiquid stocks. The authors attribute most of the predictability to a REVERSAL in stocks that had fallen substantially, and they cannot rule out manipulation as the reason the reversal's timing coincides with expiration.
- Limits: Single stocks; working paper; a reversal story, not a dealer-hedging story. It does not test SPX. Weekly return before costs; strongest where costs are highest.
- Use in the book: The only academic test found of a retail option "level" (max pain). It gives the level some predictive content in single stocks while attributing it to reversal and possible manipulation rather than dealer hedging. Useful for Chapter 10I's skepticism about level-trading: even where a level "works", the mechanism may not be the one retail narratives claim.

### Chiang2014
- Citation: Chiang, C.-H. (2014). "Stock returns on option expiration dates: Price impact of liquidity trading." Journal of Empirical Finance [volume and pages unverified]. DOI 10.1016/j.jempfin.2014.03.003.
- Type: peer-reviewed article.
- Verified via: https://consensus.app/papers/details/dbf20fc71a1a50eebf3b0bf43db28158/ (title, author, journal, year, DOI, abstract).
- Question: Do exercise-related flows move stock prices on expiration dates?
- Data and method: US stocks with large amounts of deep in-the-money call options; returns on expiration dates and the days after [sample years unverified].
- Findings: Stocks with a sufficiently large amount of deep in-the-money calls "experience a significant return drop of 0.8 percentage point on option expiration dates", followed by a short-term reversal. The author attributes it to call buyers who exercise and immediately sell the delivered stock; the selling is offset neither by option writers' purchases nor by put rebalancing.
- Limits: Single stocks with physically settled options; not applicable to cash-settled SPX.
- Use in the book: A second expiration-day channel beside hedging (exercise and liquidation flow), relevant to SPY (physically settled) against SPX (cash-settled) in Chapter 2B/5F; shows expiration effects need not come from gamma.

### ZhangEtAl2013
- Citation: Zhang, G. et al. (2013/2014). "Stock clustering effect from weekly equity options." Journal of Economics, Business and Management 2 [issue and pages unverified]. DOI 10.7763/joebm.2014.v2.110. Companion working paper: Zhang, G. et al. (2017). "Weekly options on stock pinning." William Paterson University working paper.
- Type: peer-reviewed article (small journal) and working paper. Co-author names not seen in the search results [unverified].
- Verified via: https://consensus.app/papers/details/13515ee2430f544181e38b570269a563/ (2013 article: title, first author, journal, DOI, abstract); https://consensus.app/papers/details/623bf6cdc8f35384beff68ca458da276/ (2017 working paper); https://www.wpunj.edu/Weekly%20Options%20on%20Stock%20Pinning%20upto%20page%208.pdf .
- Question: Did pinning survive the introduction of weekly single-stock options?
- Data and method: 96 common stocks with weekly options, 2010-2012; clustering of closes at strikes on monthly and weekly expiration days, firm by firm.
- Findings: Clustering still exists on monthly expiration days but is much weaker for the newly listed weekly options; close to three quarters of firms show no clustering effect at all. The 2017 paper finds significant clustering only for weeklies with high volume and a wide strike grid, and evidence for both the delta-hedge time-decay and the manipulation hypotheses.
- Limits: Small sample, small journal.
- Use in the book: Pinning is not uniform and weakens as expirations multiply, a caution for 0DTE-era claims that every day now "pins".

### FigueiredoEtAl2023
- Citation: Figueiredo, A. et al. (2023). "The role of fleeting orders on option expiration days." Quantitative Finance [volume and pages unverified]. DOI 10.1080/14697688.2023.2229375. Earlier SSRN version (2021): "The role of fleeting orders on options expiration," DOI 10.2139/ssrn.3805050.
- Type: peer-reviewed article. Co-author names not seen [unverified].
- Verified via: https://consensus.app/papers/details/361b179fe61f5f4098af6864fe3a0cca/ ; https://consensus.app/papers/details/add96969b4ef531bb4ef1aa8a8583fae/ .
- Question: Who moves stocks toward or across strikes on expiration days?
- Data and method: NASDAQ order-level data; fleeting (quickly cancelled) orders in optionable stocks on expiration and non-expiration days.
- Findings: More fleeting orders in optionable stocks on expiration days; their direction relates to the distance of the quote from strike prices and to option open interest; they are placed outside the best quotes, which the authors read as spoofing and manipulation rather than a search for liquidity; they move subsequent quotes and increase the likelihood of stock prices crossing strikes on expiration days.
- Limits: Single stocks; order-book inference about intent.
- Use in the book: Supports NPP's second channel: part of expiration-day price behaviour is strategic, not mechanical hedging.

### StollWhaley1987
- Citation: Stoll, H. R. and R. E. Whaley (1987). "Program trading and expiration-day effects." Financial Analysts Journal 43(2) [pages unverified]. DOI 10.2469/faj.v43.n2.16.
- Type: peer-reviewed practitioner journal article.
- Verified via: https://consensus.app/papers/details/6b88508c9e98564398982e8d84573380/ (title, authors, journal, DOI, abstract).
- Question: Do index-futures and index-option expirations ("triple witching") move the stock market?
- Data and method: S&P 500 index and futures, quarterly expirations 1984-1985; last-hour volume and price changes, and next-morning reversals.
- Findings: Last-hour volume substantially higher and price-change volatility significantly higher on expiration days, with the market tending to fall; the average price effect, measured by next-morning reversal over the ten most recent quarterly expirations, was "about 0.4 per cent of the closing index value", about 0.15% of transaction value once the normal bid-ask impact is removed. S&P index option expirations on their own did not produce abnormal market movements.
- Limits: 1980s close-settled expirations; index options then settled on the close; SPX monthly options now settle on the opening SOQ, which moved the effect to the open.
- Use in the book: Historical baseline for index expiration effects (Chapter 2C, 9C): the classic index expiration effect came from futures-arbitrage unwinds, not option hedging, and was a fraction of a percent.

### StiversSun2013
- Citation: Stivers, C. T. and L. Sun (2013). "Returns and option activity over the option-expiration week for S&P 100 stocks." Journal of Banking and Finance 37(11): 4226-4240. DOI 10.1016/j.jbankfin.2013.07.030. SSRN abstract_id=1571786.
- Type: peer-reviewed article.
- Verified via: https://consensus.app/papers/details/ef9d378c9d985089bbb62e69ec34370e/ (title, authors, journal, abstract); https://ideas.repec.org/a/eee/jbfina/v37y2013i11p4226-4240.html (volume 37, issue 11, pages 4226-4240); https://www.sciencedirect.com/science/article/abs/pii/S0378426613003051 . Unverified: the size of the weekly return difference and the sample years (not seen in any search result).
- Question: Are returns in the option-expiration (OPEX) week different for option-active large caps?
- Data and method: S&P 100 stocks; weekly returns in the week ending on the month's third Friday (the OE week) against other weeks, other stocks with less option activity, and asset-pricing alphas.
- Findings: OE-week returns of S&P 100 stocks "tend to be high" relative to less option-active stocks' third-Friday weeks, to the same stock's other weeks, and to risk-based alphas; the following (fourth-Friday) week underperforms modestly. Proposed partial explanations: delta-hedge rebalancing by market makers, with a reduction in short-stock hedge positions over the OE week, and falling option-implied volatility over the OE week.
- Limits: Single stocks, not the index; effect size not seen; mechanism is suggested ("likely partial contributors"), not identified.
- Use in the book: The academic source for an "OPEX week" effect, which practitioners assert for SPX; the evidence is for option-active single stocks, and the hedging channel is proposed, not proven.

### EllahieEtAl2025
- Citation: Ellahie, A., Z. Kaplan, C. Potter and S. Saha (2025/2026). "Levering up! Short-horizon option availability and the gamification of the stock market." Working paper, SSRN abstract_id=6538358 (SSRN date March 27, 2026); earlier PDF posted by Yale SOM, May 2025.
- Type: working paper (SSRN 2026; Yale SOM conference PDF 2025).
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6538358 ; https://som.yale.edu/sites/default/files/2025-05/Levering%20up!%20Short-horizon%20option%20availability%20and%20the%20gamification%20of%20the%20stock%20market.pdf ; https://consensus.app/papers/details/a939113283bd52e79e5fe52f33828ca6/ . Unverified: sample period, number of firms, effect sizes.
- Question: Does listing weekly options on a stock change its trading and price formation?
- Data and method: Stacked difference-in-differences around the staggered introduction of weekly single-stock options (firm level).
- Findings: Weekly option introductions increase equity return volatility, equity trading volume and option volume; weekly option trades correlate positively with contemporaneous stock returns (speculation, not hedging). Two proposed channels: leverage attracts less-informed speculators, and the higher gamma of short-dated contracts raises market makers' hedging needs. Institutional holdings fall, retail volume rises.
- Limits: Single stocks; the gamma channel is posited, and whether dealers are long or short that gamma is not identified in the material seen.
- Use in the book: A counterweight to the "0DTE stabilizes" reading of Chapter 9B: at the single-stock level, adding short-dated expirations RAISED volatility. The contrast with AdamsDimEtAl2025 (SPX) suggests the sign depends on who is on the other side of the short-dated flow.

### JeanninIoriSamuel2008
- Citation: Jeannin, M., G. Iori and D. Samuel (2008). "Modeling stock pinning." Quantitative Finance 8(8): 823-831. DOI 10.1080/14697680701881763.
- Type: peer-reviewed article (theory and simulation).
- Verified via: https://consensus.app/papers/details/5bbcb245e26f5dcbad0d974b13c32e12/ (title, first author, journal, year, DOI, abstract); https://www.citystgeorges.ac.uk/__data/assets/pdf_file/0010/89974/0604_jeannin-et-al.pdf (working-paper version, City University Department of Economics). Full names, volume and pages confirmed at https://ideas.repec.org/a/taf/quantf/v8y2008i8p823-831.html .
- Question: What in delta hedging produces pinning?
- Data and method: Extends Avellaneda-Lipkin using the Frey-Stremme feedback model, plus a simulated double-auction market.
- Findings: Pinning comes from two effects: a hedging-dependent drift toward the strike and a hedging-dependent fall in volatility near the strike; pinning also emerges in the microstructure simulation when hedging is discrete and impact stochastic. The model assumes hedgers LONG the options.
- Limits: Theory.
- Use in the book: Explains why realized volatility is compressed near a heavily held strike when dealers are long gamma (Chapter 9C).

### B. Dealer gamma, returns and volatility

### BaltussenDaLammersMartens2021
- Citation: Baltussen, G., Z. Da, S. Lammers and M. Martens (2021). "Hedging demand and market intraday momentum." Journal of Financial Economics 142(1): 377-403. DOI 10.1016/j.jfineco.2021.04.029. SSRN abstract_id=3760365.
- Type: peer-reviewed article.
- Verified via: https://consensus.app/papers/details/daa1769f2ffb58d588e1b315f3eb9e62/ (title, authors, journal, DOI, abstract); https://www.sciencedirect.com/science/article/abs/pii/S0304405X21001598 ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3760365 ; a search result titled "Journal of Financial Economics 142 (2021) 377-403" for https://www3.nd.edu/~zda/intramom.pdf (volume and pages). The NGE construction, sample split and Sharpe ratios below come from search-result summaries of the paper's text, not from the abstract; exact regression coefficients were not seen [unverified].
- Question: Does hedging of short gamma (by option market makers, leveraged ETFs and others) create momentum into the close?
- Data and method: Intraday returns on over 60 futures (equity indexes, bonds, commodities, currencies), 1974-2020. Predictive regression of the last-30-minute return on the "rest-of-day" return (previous close to 30 minutes before the close). Gamma measure for the S&P 500: "net gamma exposure" (NGE) of option market makers computed from S&P 500 index option open interest, gamma, the index level and the multiplier, January 1996 to May 2020, ASSUMING market makers are long calls and short puts (the SqueezeMetrics / "JPM-era" convention). By that measure there were about 2,930 negative-NGE days and 3,158 positive-NGE days between 1996 and May 2020 (search summary). Leveraged-ETF hedging demand is measured directly from each LETF's assets and leverage.
- Findings: (1) "Market intraday momentum everywhere": the rest-of-day return positively predicts the last-30-minute return, economically and statistically highly significant, and the effect reverts over the following days (abstract). (2) For the S&P 500, intraday momentum is present when NGE is negative and stronger the more negative NGE is; it is weak or absent when NGE is positive (search summaries). (3) LETF hedging demand on an index drives the size of that index's intraday momentum, across indexes and over time. (4) A simple timing strategy earns annualized Sharpe ratios of about 0.87 to 1.73 at the asset-class level (search summary; before costs).
- Limits: The S&P 500 NGE sign rests on the long-calls/short-puts assumption, not on observed positions, so "negative NGE" days are days with more put than call gamma near spot. Momentum is also explained by other rule-based flows (LETFs, volatility targeting), which the paper treats as part of "hedging demand". Replications: similar patterns reported for China, India and VIX futures (see Section B extras). The effect reverses over the next days, so it is a price-pressure effect, not information.
- Use in the book: Chapters 2B, 2C, 6C, 6D, 9B, 11B. CORRECTIONS: (a) Chapter 2C's "first half-hour's return predicts the last half-hour's return, across more than 60 futures" merges two papers: the first-half-hour predictor for SPY 1993-2013 is GaoHanLiZhou2018; Baltussen et al. use the rest-of-day return across 60+ futures. (b) Chapter 6C's "Sharpe ratios in the 0.5 to 1.0 range" does not match the 0.87-1.73 (asset-class level) found in search summaries; treat the book's range as unverified. (c) Chapter 6C's "morning return's predictive power" should read "rest-of-day return". (d) Chapter 6C says dealers were "net short gamma in aggregate, which was typical historically"; in the paper that is an output of the assumed long-call/short-put convention, and by that measure NGE was negative on slightly under half of days (about 2,930 of 6,088).

### GaoHanLiZhou2018
- Citation: Gao, L., Y. Han, S. Z. Li and G. Zhou (2018). "Market intraday momentum." Journal of Financial Economics 129(2): 394-414. DOI [unverified]; ScienceDirect PII S0304405X18301351.
- Type: peer-reviewed article.
- Verified via: https://econpapers.repec.org/RePEc:eee:jfinec:v:129:y:2018:i:2:p:394-414 ; https://www.sciencedirect.com/science/article/abs/pii/S0304405X18301351 ; https://profiles.wustl.edu/en/publications/market-intraday-momentum/ .
- Question: Does the market's first half-hour predict its last half-hour?
- Data and method: High-frequency SPY (S&P 500 ETF) data, 1993-2013; the first half-hour return measured from the previous close.
- Findings: The first half-hour return significantly predicts the last half-hour return on the same day. (Coefficient and R-squared not seen [unverified].)
- Limits: No gamma measure; the mechanism proposed (late-informed trading, infrequent rebalancing) is not dealer hedging.
- Use in the book: Source of Chapter 2C's "first half-hour" description, which the book attributes to Baltussen et al.; cite both, each for its own predictor.

### AndereggUlmannSornette2022
- Citation: Anderegg, B., F. Ulmann and D. Sornette (2022). "The impact of option hedging on the spot market volatility." Journal of International Money and Finance 124 (June 2022): 102627. DOI 10.1016/j.jimonfin.2022.102627.
- Type: peer-reviewed article.
- Verified via: https://consensus.app/papers/details/26ae2470017f5d8c945bf61b115a874d/ (title, first author, journal, DOI, full abstract with numbers); https://www.sciencedirect.com/science/article/pii/S0261560622000304 ; search summary giving authors, volume 124 and article number 102627; https://www.researchgate.net/publication/358837574_The_Impact_of_Option_Hedging_on_the_Spot_Market_Volatility .
- Question: How much does option market makers' delta hedging change spot FX volatility?
- Data and method: A model with an aggregate option market maker (OMM) and an aggregate option market taker, linear permanent price impact of net hedge trades. Empirically, the OMM's gamma exposure is REconstructed from trade-repository data on FX options (not assumed), for EURUSD and USDJPY, October 21, 2017 to June 30, 2018, daily and intraday.
- Findings: (1) The reconstructed aggregate OMM gamma was NEGATIVE over the sample. (2) OMM gamma is highly significant for spot volatility: short gamma raises it, as the model predicts. (3) Size: "a negative gamma exposure of the OMM of approximately -1000 billion USD (which is around what we observe from our reconstructed OMM data) leads to an absolute increase in volatility of 0.7% in EURUSD and 0.9% in USDJPY" (abstract). Reading: at the observed level of dealer short gamma, annualized volatility was about 0.7 to 0.9 percentage points higher than it would have been with no dealer gamma, against typical FX volatility of several percent. [The unit of the -1000 billion USD gamma figure (per what move) was not seen; unverified.]
- Limits: Eight-month sample; two currency pairs; positions reconstructed from repository data with the dealer/client split inferred; FX is an OTC market with no public open interest.
- Use in the book: The rare study that measures dealer gamma from position data rather than a sign convention, outside equities. It supports the direction of Chapter 8B's regime table and gives a modest effect size: under a percentage point of annualized volatility.

### BuisEtAl2024
- Citation: Buis, B., M. Pieterse-Bloem, W. F. C. Verschoor and R. C. J. Zwinkels (2024). "Gamma positioning and market quality." Journal of Economic Dynamics and Control 164 (May 2024): 104880. DOI 10.1016/j.jedc.2024.104880.
- Type: peer-reviewed article (simulation study).
- Verified via: https://www.sciencedirect.com/science/article/pii/S0165188924000721 ; https://ideas.repec.org/a/eee/dyncon/v164y2024ics0165188924000721.html ; https://consensus.app/papers/details/b9581f4be60754e197a9cc2d4515038b/ (abstract); search summary giving the four authors.
- Question: How does the net gamma of dynamic hedgers affect liquidity, volatility, stability and price discovery?
- Data and method: A zero-intelligence agent-based market with dynamic (delta) hedgers whose net gamma is varied; normal and stressed scenarios.
- Findings: Dynamic hedgers improve liquidity in normal conditions; positive gamma sustains liquidity under stress while negative gamma depletes it; higher net gamma lowers volatility and raises stability, negative gamma raises volatility and makes the market more prone to failure; price discovery worsens as hedgers become more prevalent whatever their sign. The authors suggest steering hedgers' net gamma as a policy tool, especially for illiquid instruments.
- Limits: Simulation, not data.
- Use in the book: A formal model for Chapter 8B's regime table and 8C's "depth vanishes" precondition: negative gamma both amplifies moves and drains liquidity, which raises the feedback coefficient kappa in the same step.

### C. 0DTE options (2022 onward)

### VasquezAmayaPearsonGarciaAres2025
- Citation: Vasquez, A., D. Amaya, N. D. Pearson and P. A. Garcia-Ares (2025). "0DTE Index Options and Market Volatility: How Large is Their Impact?" Working paper, SSRN abstract_id=5113405 (January 2025); also published as a Cboe Options Institute research paper, https://cdn.cboe.com/resources/education/research_publications/gammasqueezes.pdf .
- Type: working paper (SSRN 2025), supported by and hosted at the Cboe Options Institute.
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5113405 (title, four authors, abstract, keywords); https://cdn.cboe.com/resources/education/research_publications/gammasqueezes.pdf (title); search summaries for the numbers. Unverified: the exact volatility models and the table behind each number.
- Question: How much can options market makers' (OMM) gamma in 0DTE S&P 500 options move index volatility, at most?
- Data and method: Proprietary trade records of all trades in SPX and SPXW options, January 2020 to June 2023, which identify the aggregate OMM position and hence its gamma (positions observed, not assumed). Models relate realized index volatility (daily and 30-minute) to OMM gamma; the models are then simulated under the counterfactual that OMM gamma has no effect, and the difference is the estimated impact, reported as an upper bound.
- Findings: (1) The MAXIMUM impact of OMM gamma is to raise daily volatility by 3.3 percentage points, and annualized volatility measured over 30-minute periods by 6.4 percentage points (search summary of the paper). Reading: even on the days and half-hours when dealer gamma is most destabilizing, the upper bound adds a few points of annualized volatility (for example, from 15% to about 18%), not a crash. (2) The paper notes that prior research finds the AVERAGE impact is to reduce volatility, because OMMs typically hold positive gamma. (3) Customer 0DTE flow is balanced: on the average day, January 2020 to June 2023, customers buying 0DTE options from market makers were 14.952% of all SPX and SPXW volume and customers selling to market makers 14.062% (search summary; the sample matches this paper, attribution to it not certain).
- Limits: An upper-bound, model-based counterfactual; SPX only (not SPY or single stocks); ends June 2023. Balanced buy and sell volume does not fix the gamma sign, which depends on strikes and timing.
- Use in the book: Chapters 8A, 8B, 9B, 10H, 10I. It is the strongest direct evidence on the size of 0DTE dealer-hedging effects. It supports "modest on typical days" and bounds the destabilizing case. CORRECTION: the balanced customer flow (buys 14.95% against sells 14.06% of volume) contradicts 8A and 9B's "retail and small institutional accounts overwhelmingly sell premium" in 0DTE.

### CboeXu2023
- Citation: Xu, M. (2023). "Much Ado About 0DTEs: Separating Fact From Fiction" / "Volatility Insights: Evaluating the Market Impact of SPX 0DTE Options." Cboe Global Markets, Volatility Insights, 2023 (published about September 2023; Cboe webinar of the same name announced November 1, 2023). Reprinted on IBKR Campus.
- Type: exchange research note (vendor/exchange material, not peer-reviewed).
- Verified via: https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options ; https://www.interactivebrokers.com/campus/traders-insight/securities/options/much-ado-about-0dtes-separating-fact-from-fiction/ ; https://www.nasdaq.com/press-release/cboe-partners-with-benzinga-for-much-ado-about-0dtes-webinar-2023-11-01 ; https://finance.yahoo.com/news/same-day-expiry-options-really-130000545.html . Numbers from search summaries of those pages. Unverified: the exact publication day, and the +$2.4 billion upper end of the "typical range" (the summary's text was cut off at that point).
- Question: Are market makers' 0DTE hedging flows large enough to move the S&P 500?
- Data and method: Market-maker net gamma in SPX 0DTE options (dollars of S&P exposure to trade per 1% move) in 30-minute increments through the day, shown as box plots (25th to 75th percentile, median) [data source, presumably Cboe's own trade data by participant type, not described in the summaries; unverified].
- Findings: (1) On average, market-maker net 0DTE gamma ranges from about $170 million to $670 million through the day. (2) Against about $400 billion of daily S&P 500 futures liquidity, hedging flows are 0.04% to 0.17% of futures liquidity. (3) The median net gamma AT 3:30 PM is +$173 million, with a "typical range" from -$1.1 billion to [about +$2.4 billion]. (4) Customer 0DTE activity is "very balanced" (hedging, yield harvesting, tactical leverage, systematic trading). (5) Conclusion: no discernible market impact from 0DTE trading; SPX intraday volatility and price patterns in line with historical averages. (6) 0DTE was 5% of SPX volume in 2016, over 40% after Tuesday/Thursday expiries were added, and about 50% in August 2023.
- Limits: Exchange material with a commercial interest in the product; methods not peer-reviewed; covers SPX only; data through mid-2023.
- Use in the book: CORRECTIONS for Chapter 9B: (a) the +$173 million median is the median at 3:30 PM, not an all-day median; (b) the "0.04% to 0.17%" range is Cboe's own figure, from the $170-$670 million intraday range divided by about $400 billion, which answers the notes' question on how the upper end was derived; (c) the note is from 2023. The Edge Book's "Cboe study of 2025 ... about 0.2% of SPX daily liquidity" (Chapters 1G, 6A, 10A, 10H, 10I, 11A, 11D, 11K, 13B, 13F) most likely rounds the 0.17% upper end of this 2023 note, and the base is S&P 500 FUTURES liquidity, not "SPX daily liquidity". No 2025 Cboe study giving 0.2% was found; the closest 2025 Cboe-hosted work is VasquezAmayaPearsonGarciaAres2025, which reports volatility impacts, not a liquidity share.

### DimErakerVilkov2023
- Citation: Dim, C., B. Eraker and G. Vilkov (2023/2024). "0DTEs: Trading, Gamma Risk and Volatility Propagation." Working paper, SSRN abstract_id=4692190, DOI 10.2139/ssrn.4692190 (SSRN date November 17, 2023; circulated in 2024, including the Western Finance Association program).
- Type: working paper (SSRN). No journal publication found as of this search.
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4692190 ; https://dx.doi.org/10.2139/ssrn.4692190 ; https://westernfinance-portal.org/viewpaper?n=950096 ; https://www.researchgate.net/publication/377984312_0DTEs_Trading_Gamma_Risk_and_Volatility_Propagation ; https://www.maths.ox.ac.uk/node/67396 (seminar listing). Data description from search summaries of the paper's text. Unverified: sample start year, regression coefficients and effect sizes in standard-deviation units (not seen).
- Question: Is the explosion of 0DTE trading in S&P 500 index options destabilizing for the index?
- Data and method: SPX options (including SPXW 0DTEs). Intraday 30-minute bars from Cboe DataShop (NBBO, OHLC, volume, open interest at the start of each day, implied volatilities and Greeks). Market-maker inventory is approximated from the Cboe Open-Close database, which reports daily buy and sell volume by end users (non-market-makers): the cumulative net end-user order flow since each option's listing is minus the market makers' position. Net market-maker gamma is then the gamma of that inferred inventory. Regressions of future intraday volatility, return reversal and momentum on this inventory gamma.
- Findings: (1) "Market Makers' inventory, as measured by the net gamma of their positions, is on average positive and negatively related to future intraday volatility" (abstract). (2) "Positive (negative) Market Makers' inventory gamma strengthens intraday price reversal (momentum)"; the evidence "is consistent with delta-hedging but inconsistent with information-based trading" (abstract). (3) Intraday variation in market makers' hedging needs predicts stronger order-flow reversals, lower momentum returns and lower volatility. (4) Average daily open-interest gamma did not grow after 2016, for 0DTEs or other maturities, so even if short-gamma holders delta-hedge, 0DTE growth is unlikely to have raised volatility (search summary).
- Limits: The inventory is inferred from Open-Close end-user flow, which starts at a data-availability date and misses flows not captured (other exchanges' SPX-equivalents, SPY, futures options, OTC). It is SPX-only. A working paper. The sign result is an average: the same paper's momentum finding for negative-gamma periods is the flip side.
- Use in the book: Chapters 6D, 8A, 8B, 9B, 9C. CORRECTIONS: (a) SSRN posting is November 17, 2023; "2024" in the book is the circulation year, acceptable if labelled "working paper, SSRN 2023". (b) The book (8A) calls it "a working paper from George Washington University"; it is an SSRN working paper by three authors at different institutions (affiliations beyond Dim not verified), so "a working paper" suffices. (c) The book's quotation marks around the finding match the abstract. (d) Chapter 9B's gloss that dealers are long gamma BECAUSE retail sells premium is the Dealer Mechanics Lab's interpretation, not the paper's finding; the paper infers positions from end-user order flow without attributing them to retail premium selling.

### AdamsFontaineOrnthanalai2024
- Citation: Adams, G., J.-S. Fontaine and C. Ornthanalai (2024, revised 2025). "The Market for 0DTE: The Role of Liquidity Providers in Volatility Attenuation." Working paper, SSRN abstract_id=4881008 (search summaries give first dates of May 3 or July 3, 2024, and a revision of June 20, 2025).
- Type: working paper (SSRN). Authors' affiliations per search summary: University of Pennsylvania (Adams), Bank of Canada (Fontaine), University of Toronto (Ornthanalai).
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4881008 ; https://discover.research.utoronto.ca/14511-chay-ornthanalai/publications ; https://www.researchgate.net/scientific-contributions/Jean-Sebastien-Fontaine-80985946 . Unverified: exact SSRN posting date (two summaries disagree), and whether a Bank of Canada Staff Working Paper version exists.
- Question: Do market makers' 0DTE positions amplify or damp S&P 500 volatility?
- Data and method: Intraday SPX option trading volume, 2019-2023; identification from "exogenous variation in contract expiration days" (days with and without an expiring contract) [how market-maker positions are built, and whether the 2022 Tuesday/Thursday additions supply the variation, unverified].
- Findings: (1) Market makers' intermediation of 0DTE options lowers index volatility on average. (2) "Index volatility decreases by 60-90 annualized basis points on days with 0DTE trading" (abstract, per search summary). Reading: on a day with an expiring SPX option, annualized realized volatility is about 0.6 to 0.9 percentage points lower than on a comparable day without one, for example 15.0% against 15.7%. (3) Market makers match (pass through) most same-day 0DTE order flow, but absorb end users' trades in longer-dated options that later become 0DTE positions; hedging those expiring positions creates futures order flow that damps volatility.
- Limits: Working paper; the effect is an average across days and does not rule out destabilizing days; positions inferred from flow data; SPX only.
- Use in the book: The precursor of AdamsDimEtAl2025 and the source of its key numbers. It gives Chapter 9B a quotable effect size (60-90 annualized bp) and the mechanism the book quotes (longer-dated positions becoming 0DTEs).

### AdamsDimEtAl2025
- Citation: Adams, G., C. Dim, B. Eraker, J.-S. Fontaine, C. Ornthanalai and G. Vilkov (2025). "Do S&P500 Options Increase Market Volatility? Evidence from 0DTEs." Working paper, SSRN abstract_id=5641974.
- Type: working paper (SSRN; the search summaries give an SSRN date of October 17, 2025).
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5641974 (title, six authors, abstract); https://www.researchgate.net/publication/396839836_Do_SP500_Options_Increase_Market_Volatility_Evidence_from_0DTEs ; https://quantpedia.com/do-sp500-0dtes-options-increase-market-volatility/ (numbers). Unverified: the book's "posted December 3, 2025" (search results show October 17, 2025; SSRN pages carry both a written and a posted date, so the December date could be a revision); the units of the "hedging needs" numbers.
- Question: Do 0DTE options destabilize the S&P 500 through market makers' hedging?
- Data and method: SPX options and market makers' net gamma and delta-hedging demands; identification from days with and without 0DTE trading ("0DTE trading days"). The book describes the design as a natural experiment from the staggered 2022 addition of Tuesday and Thursday SPXW expirations; the search summaries mention only 0DTE trading days [design details unverified].
- Findings: (1) "A robust negative relation between 0DTE trading days and realized S&P500 volatility", driven by changes in intermediaries' net gamma and delta-hedging demands (abstract). (2) Mechanism: positions in longer-dated options accumulate before expiry and "roll down the term structure", raising market makers' instantaneous hedging needs in a direction that makes them trade AGAINST contemporaneous index moves. The abstract's own words: "On the contrary, we show that the presence of 0DTEs dampens market volatility through a shift in market makers' hedging needs. Importantly, this shift occurs not due to trading 0DTEs on their expiration day but due to positions in longer-dated options accumulated earlier and becoming 0DTEs." (3) Size (Quantpedia summary): pre-existing market-maker positions raise hedging needs by 24 bp during the expiration day on average; hedging needs were about one percent before 2022, and the presence of 0DTEs on a day raises them by 0.15 percentage points on average [units of "hedging needs" not seen].
- Limits: Working paper; the natural experiment is two non-random steps in 2022, close in time to other market changes (Fed tightening, volatility regime); SPX only; an average effect.
- Use in the book: Chapters 8A, 8B, 9B, 9C, 11A. CORRECTIONS: (a) Tuesday SPXW options were LISTED from April 18, 2022 and Thursday SPXW from May 11, 2022; April 26 and May 19, 2022 were the first EXPIRATION days (Cboe press release and product notice). The book's "not available for trading until April 26 and May 19" should say "first expired on". (b) The date "posted December 3, 2025" conflicts with the October 17, 2025 date in search results. (c) "Establish causally" (8B) is the book's phrase; the paper's language is a "robust negative relation" identified from expiration-day variation, a natural experiment rather than a randomized design.

### BrogaardHanWon2023
- Citation: Brogaard, Jonathan, [first name unverified] Han and [first name unverified] Won (2023, revised 2024/2025). "Does 0DTE Options Trading Increase Volatility?" Earlier title: "How Does Zero-Day-To-Expiry Options Trading Affect the Volatility of Underlying Assets?" Working paper, SSRN abstract_id=4426358, DOI 10.2139/ssrn.4426358 (first posted April 22, 2023).
- Type: working paper (SSRN). No journal version confirmed. First names of Han and Won not seen in any search result.
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4426358 ; https://consensus.app/papers/details/f4bcd68477ac5ddcaaaac16884d86523/ (earlier title, Brogaard et al., 2023, DOI); https://www.researchgate.net/publication/370319866_How_Does_Zero-Day-To-Expiry_Options_Trading_Affect_the_Volatility_of_Underlying_Assets ; https://ouci.dntb.gov.ua/en/works/4kYGEGg9/ . Numbers from two independent search summaries of the abstract. Unverified: which indexes and ETFs are in the sample, sample end date, the volatility measure.
- Question: Does 0DTE trading raise the volatility of the underlying indexes?
- Data and method: 0DTE options on indexes (monthly index 0DTE volume rose from 0.08 million contracts in January 2011 to 34.4 million in August 2023, 48% of index option trading); instrumental-variables regressions using the staggered introduction of index weekly options as the instrument for 0DTE trading; controls for option market makers' gamma hedging.
- Findings: (1) "A one standard deviation increase in 0DTE options trading leads to 9.10% increase relative to the mean value of volatility, which is 15.91% of its standard deviation" (abstract, per search summaries). Reading: moving 0DTE activity up by one standard deviation raises volatility by about 9% of its average level, a moderate effect (about a sixth of volatility's own day-to-day spread). (2) The effect stays positive after controlling for market makers' gamma hedging and is "primarily driven by speculative retail investors".
- Limits: Working paper; the instrument (weekly-option introductions) may affect volatility through channels other than 0DTE volume; results concern volume, not dealer positions. It conflicts with DimErakerVilkov2023, AdamsFontaineOrnthanalai2024 and AdamsDimEtAl2025, which use position-based gamma measures and find damping.
- Use in the book: CORRECTION (Chapter 9B): the book says this paper "independently confirmed that the introduction of 0DTE did not increase market volatility" using "an event-study methodology around the staggered introduction of the Tuesday and Thursday SPXW expirations". Both statements are wrong on the evidence found: the paper reports that 0DTE trading INCREASES volatility, and its identification uses the staggered introduction of index weekly options as an instrument. The book's summary "the academic consensus ... is that 0DTE has stabilized rather than destabilized" must be softened: the literature is split, with position-based studies (DEV, Adams et al., Vasquez et al.) finding damping on average and a volume-based IV study (this one) finding amplification. Also, the note "a University of Utah working paper" should be "SSRN working paper" (affiliation not verified).

### BeckmeyerBrangerGayda2023
- Citation: Beckmeyer, H., N. Branger and L. Gayda (2023, revised 2024). "Retail Traders Love 0DTE Options... But Should They?" Working paper, SSRN abstract_id=4404704 (SSRN date March 30, 2023).
- Type: working paper (SSRN; presented at FoFI 2024, Lancaster).
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4404704 ; https://wp.lancs.ac.uk/fofi2024/files/2024/04/FoFI-2024-146-Leander-Gayda.pdf ; https://www.researchgate.net/publication/370012499_Retail_Traders_Love_0DTE_Options_But_Should_They ; https://sites.google.com/site/nicolebranger01/working_papers . Numbers from search summaries of the abstract and text.
- Question: Who trades 0DTE SPX options at retail, and do they make money?
- Data and method: SPX option trades identified as retail through Cboe's Automated Price Improvement Mechanism (retail orders routed to price-improvement auctions), February 2021 to September 2023; trade-level profit and loss by strategy type.
- Findings: (1) More than 75% of retail trades in S&P 500 options are in 0DTE contracts. (2) Retail's share of trading is about 6% in the 0DTE segment against 2% to 4% in longer maturities (by this identification). (3) Retail investors lost about $241,000 on an average day from February 2021 to September 2023, and about $350,000 per day after the daily expiration calendar began in May 2022. (4) Losses come from single-leg trades, trades that pay premium up front, and high-implied-volatility options; multi-leg trades that collect the volatility and jump premium are significantly more profitable. (5) Retail investors BOUGHT more 0DTE options than they sold, leaving market makers net short, and "the aggregate net-short position of market makers in 0DTE options has grown considerably in recent months" (search summary of the text).
- Limits: Retail identified only through auction-routed orders, which gives a far smaller retail share (about 6%) than Cboe's own estimates (about 50% to 60%; CboeRetailShare2025), so "retail" here is a narrower slice. Net short by count or premium is not the same as net short gamma at every strike and hour. Working paper.
- Use in the book: Chapters 8A and 9B claim that retail 0DTE flow is "mostly premium selling" and that this "keeps dealers net long gamma in 0DTE on most days". This paper's retail slice was a net BUYER of 0DTE options, and it reports a growing market-maker net-short 0DTE position; VasquezAmayaPearsonGarciaAres2025 find customer buys and sells roughly balanced. The dealers' average long gamma found by DEV and Adams et al. comes mainly from longer-dated positions rolling into expiry, not from same-day retail premium selling. The book should drop "overwhelmingly sell premium" and present retail direction as contested.

### CboeRetailShare2025
- Citation: Cboe Global Markets (Xu, M., Derivatives Market Intelligence) (2025). "SPX 0DTE Options Jump to Record 62% Share in August" and related 2025 Cboe insights posts; press coverage: FOW, "ANALYSIS: Cboe points to retail flow as zero-day options grow"; Seeking Alpha reprint "SPX 0DTE Options Jump To 61% Share On Retail Resurgence".
- Type: exchange research notes (vendor/exchange material).
- Verified via: https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august/ ; https://www.fow.com/insights/analysis-cboe-points-to-retail-flow-as-zero-day-options-grow ; https://seekingalpha.com/article/4791896-spx-0dte-options-jump-61-percent-share-retail-resurgence ; https://www.cboe.com/insights/posts/the-state-of-the-options-industry-2025/ . Numbers from search summaries.
- Question: How big is 0DTE in SPX, and how much of it is retail?
- Data and method: Cboe volume data with Cboe's own classification of retail flow [method not described in the summaries; unverified].
- Findings: 0DTE reached a record 62% of SPX volume in August 2025; retail made up an estimated 53% of SPX 0DTE volume in August 2025; the retail share fell to 47% during the early-April 2025 volatility spike and rose back to about 60% as volatility abated; Cboe estimates retail at about 50-60% of SPX 0DTE trading.
- Limits: Exchange estimates of "retail" are not comparable to BeckmeyerBrangerGayda2023's auction-based identification (about 6%). Volume shares say nothing about the direction (buying or selling premium) of that flow.
- Use in the book: Supports 9B's volume figures (62.4% in August 2025; retail roughly half). The fall in retail share during the April 2025 spike is the only data found about retail behaviour in that episode; it does not show retail "buying directional protection", which remains an unsupported claim in 9B.

### BandiFusariReno2023
- Citation: Bandi, F. M., N. Fusari and R. Renò (2023). "0DTE Option Pricing." Working paper, SSRN abstract_id=4503344, DOI 10.2139/ssrn.4503344 (dated July 7, 2023; posted July 16, 2023; a March 15, 2024 draft circulated at the Northern Finance Association). One search summary says "forthcoming in the Journal of Finance" [unverified].
- Type: working paper (SSRN), possibly forthcoming in a journal [unverified].
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4503344 ; https://doi.org/10.2139/ssrn.4503344 ; https://www.researchgate.net/publication/372407812_0DTE_Option_Pricing ; https://portal.northernfinanceassociation.org/viewp.php?n=2240145012 .
- Question: How should options that expire within hours be priced and hedged?
- Data and method: A local-in-time approach using Edgeworth-like expansions of the log-return characteristic function, giving closed-form skewness and kurtosis adjustments; tested on SPX 0DTE options.
- Findings: Significant improvements in pricing and hedging 0DTE options over state-of-the-art models; structurally estimated 0DTE return and variance risk premia give "suggestive evidence of nearly instantaneous predictability".
- Limits: The paper does not measure dealer gamma or its effect on index volatility (on the evidence of the abstract).
- Use in the book: For the 0DTE survey only: it answers neither "damps" nor "amplifies". Cite it for why Black-Scholes gamma misstates 0DTE risk (skewness and kurtosis matter over hours), which bears on 8A's limit 4.

### Vilkov2024
- Citation: Vilkov, G. (2023/2026). "0DTE Trading Rules" (later subtitle "Tail Risk, Implementation, and Tactical Timing"). Working paper, SSRN abstract_id=4641356, DOI 10.2139/ssrn.4641356. Replication package: https://github.com/vilkovgr/0dte-strategies .
- Type: working paper (SSRN; first version late 2023, sample extended to February 2, 2026 in the version seen).
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4641356 ; https://www.researchgate.net/publication/376157104_0DTE_Trading_Rules ; https://github.com/vilkovgr/0dte-strategies .
- Question: Do simple 0DTE option strategies (single options and multi-leg structures such as straddles and condors) earn money after costs?
- Data and method: Realized payoffs of SPX 0DTE options and standard multi-leg structures from September 2016 to February 2, 2026; conditional trading rules estimated at 10:00 ET with strict out-of-sample tests.
- Findings: A positive 0DTE variance risk premium exists but is small at same-day horizons and "difficult to monetize after realistic frictions"; P&L distributions are wide, state-dependent and dominated by tail risk, loading more on direction and skewness than on realized variance; selected conditional rules deliver economically meaningful net performance, "pointing to selective timing opportunities rather than to a broad unconditional edge".
- Limits: Practitioner replication (FirmTape, dev.to, practitioner material, not peer-reviewed) reports that a unit-scale bug in the replication package charged the half-spread at one hundredth of its size, and that after rescaling every unconditional structure has negative net mean (best gross edge +0.0251% of spot per day against a 0.0343% spread); the post says the author confirmed the bug: https://dev.to/firmtape/we-replicated-a-published-0dte-options-paper-to-four-decimals-one-unit-scale-bug-reverses-its-3ddj . The current abstract already describes the unconditional edge as small and hard to monetize. Not a paper about dealer gamma.
- Use in the book: 0DTE premium selling as a strategy (Chapters 9B, 10H, 10I): the edge is thin and tail-dominated. On damping versus amplifying, it is silent.

### TodorovVilkov2024BIS
- Citation: Todorov, K. and G. Vilkov (2024). "What could explain the recent drop in VIX?" Box in BIS Quarterly Review, March 2024. https://www.bis.org/publ/qtrpdf/r_qt2403x.htm
- Type: regulator report (central-bank research box).
- Verified via: https://www.bis.org/publ/qtrpdf/r_qt2403x.htm (title); search summary giving authors and content.
- Question: Did the rise of 0DTE options pull trading away from one-month SPX options and so depress the VIX?
- Data and method: SPX option volume by maturity; comparison of 0DTE and one-month (1MTE) activity [details unverified].
- Findings: 0DTE was more than 50% of SPX option volume in August 2023, up from 5% in 2016; but 0DTE growth "did not, on net, lure activity away from one-month options" and is unlikely to be the main reason for the low VIX. Alternative explanation: option dealers "effectively dampen volatility when they hedge structured products", which had become more popular (search summary; the position behind this, presumably dealers long volatility bought from structured-product issuance, is not described in the summary).
- Limits: A short box; the structured-product channel is proposed, not measured in the summary seen.
- Use in the book: Supports 8A's "invisible book": the largest dealer long-gamma position in 2023-2024 may sit in OTC structured-product hedges, not in listed open interest. Also rebuts the "0DTE killed the VIX" story.

### FedSCOOS2023
- Citation: Board of Governors of the Federal Reserve System (2023). "The September 2023 Senior Credit Officer Opinion Survey on Dealer Financing Terms," special questions on zero-days-to-expiry (0DTE) options. https://www.federalreserve.gov/data/scoos/files/scoos_202309.pdf
- Type: regulator report (survey of dealers).
- Verified via: https://www.federalreserve.gov/data/scoos/files/scoos_202309.pdf ; https://finadium.com/feds-scoos-shows-increased-equity-funding-demand-examines-0dte/ (press summary).
- Question: How do dealers manage the risk of institutional clients' 0DTE trading, and how much of it is there?
- Data and method: Survey of 21 dealers (conducted August 14-28, 2023); the 0DTE questions went to the 10 dealers whose clients regularly trade equity options and actively trade 0DTE.
- Findings: Clients who actively trade 0DTE are a small fraction of equity-option clients; for those clients, half of dealers said 0DTE is under 5% of their option trades by premium, one-fifth said 10-20%, the rest higher. The survey notes that the OCC's daily margining does not apply to positions opened and closed within the day.
- Limits: Institutional (not retail) clients; qualitative; says nothing about dealer gamma or index volatility.
- Use in the book: The only Federal Reserve publication on 0DTE found in this search. It shows 0DTE is concentrated in a subset of institutional clients and flags intraday margin as a risk-management gap. No Fed note testing whether 0DTE dealer hedging damps or amplifies volatility was found.

### ECBFSR2023Box
- Citation: European Central Bank (2023). Financial Stability Review, November 2023, box on risks from hidden leverage in short-term equity options (0DTE). https://www.ecb.europa.eu/press/financial-stability-publications/fsr/html/ecb.fsr202311~bfe9d7c565.en.html ; box page https://www.ecb.europa.eu/press/financial-stability-publications/fsr/focus/2023/html/ecb.fsrbox202311_02~0cf2c71d00.en.html [box title and authors unverified].
- Type: regulator report.
- Verified via: the two ECB URLs above (search results); content from a search summary.
- Question: Do same-day options create hidden leverage and stability risks, in the US and potentially the euro area?
- Data and method: Descriptive review of US SPX 0DTE growth; notes that Eurex expanded EURO STOXX 50 weekly options to every business day on August 28, 2023.
- Findings: 0DTE exceeded 50% of S&P 500 option volume after Cboe added daily expirations; the box treats 0DTE as a hidden-leverage risk to monitor [no quantitative test of dealer-gamma effects in the summary].
- Limits: Descriptive; no measurement of dealer positions.
- Use in the book: Regulator framing of 0DTE risk for Chapter 9B; shows central banks flagged the risk while the position-based evidence (DEV, Adams et al.) found damping on average.

### BankUnderground2024
- Citation: Xiao, B. (2024). "Zero-day options and financial market vulnerability." Bank Underground (Bank of England staff blog), December 4, 2024. https://bankunderground.co.uk/2024/12/04/zero-day-options-and-financial-market-vulnerability/
- Type: central-bank staff blog (views of the author, not the Bank of England).
- Verified via: https://bankunderground.co.uk/2024/12/04/zero-day-options-and-financial-market-vulnerability/ (search summary giving author and content).
- Question: Could 0DTE options produce a Volmageddon-type event?
- Data and method: Descriptive analysis of 0DTE volume, flow patterns and market-maker hedging.
- Findings: 0DTE is about half of S&P 500 option volume (from 5% in 2016). Market makers face gamma risk from directional flows but have adapted to consistent volume and flow patterns; retail spread trading (iron condors, put and call spreads) creates partially offsetting flows that help market makers manage gamma. The setting differs from the 2018 Volmageddon lead-up because 0DTE positions reset daily, but prolonged low volatility with growing short selling of 0DTEs could change the risk profile. The frequency of hedging "could exacerbate volatility of the underlying market and result in a loop that magnifies the initial market impact" (search summary).
- Limits: A blog post; conditional and qualitative.
- Use in the book: A balanced central-bank view for Chapters 9B and 8C: stabilizing on average, with a stated mechanism for a tail event if customer premium selling grows.

### BarbonBuraschi2021
- Citation: Barbon, A. and A. Buraschi (2020, revised March 18, 2021). "Gamma Fragility." Working paper, SSRN abstract_id=3725454 (first posted November 5, 2020); University of St. Gallen, School of Finance. Repository copy: https://alexandria.unisg.ch/entities/publication/b0c4de3d-74dd-4e62-b465-2d0337fe2904
- Type: working paper (SSRN 2020; revision dated March 18, 2021). No journal version found.
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3725454 ; https://alexandria.unisg.ch/entities/publication/b0c4de3d-74dd-4e62-b465-2d0337fe2904 ; https://www.econbiz.de/Record/gamma-fragility-barbon-andrea/10012387248 ; search result listing "Gamma Fragility Andrea Barbon Andrea Buraschi March 18, 2021 Abstract" (https://tashfeenomran.com/DB/Research%20Papers/Gamma%20Fragility.pdf); secondary summary by the Bocconi Students Investment Club, "How Dealers' Gamma impacts underlying stocks" (March 2022), https://bsic.it/how-dealers-gamma-impacts-underlying-stocks/ . Effect sizes come from search summaries of these documents and differ between versions (see Findings); exact regression tables were not seen [unverified].
- Question: Do large aggregate dealer gamma imbalances make underlying prices trend (when dealers are short gamma) or mean-revert (long gamma) within the day, and does this make markets fragile?
- Data and method: Option trade data from three Nasdaq options exchanges (ISE, GEMX, PHLX) merged with OptionMetrics IvyDB, 2010-2020, covering index options and a large cross-section of single-stock options; separate estimates for four broad indexes (S&P 500, Dow Jones, Nasdaq 100, Russell 2000). Gamma measure: "gamma imbalance" (GI), the aggregate dollar value of all market makers' outstanding gamma with their clients across strikes and maturities, computed daily per underlying from open interest, with only broker-dealers and market makers assumed to delta-hedge. [How client positions are signed from the Nasdaq trade data, and how GI is normalized across assets, unverified.] Regressions of intraday momentum/reversal and of absolute daily returns on ex-ante GI, interacted with illiquidity; flash-crash frequency and size on GI.
- Findings: (1) "Intra-day momentum (reversal) is explained by the interaction of negative (positive) ex-ante gamma imbalance and illiquidity"; the effect is stronger for the least liquid underlyings (abstract). (2) GI is related to the frequency and magnitude of flash-crash events (abstract). (3) Size (search summaries of the paper text; versions differ): one standard deviation of GI is associated with a DECREASE of roughly 12 bp in the absolute daily return of the underlying stock, against an average absolute daily return of about 109 bp; another version gives 5 to 25 bp for single stocks against an average absolute daily return of 180 bp; for the indexes tested, a one-SD increase in GI is associated with a decrease in absolute daily index return of more than 20 bp. (4) Increases in absolute returns on negative-gamma days are significantly larger for the most illiquid assets.
- How to read the units: "bp per standard deviation" means basis points of ABSOLUTE daily return (a proxy for that day's volatility) per one-standard-deviation change in the gamma-imbalance measure across the panel. Example: a stock that usually moves 1.09% a day in absolute terms moves about 0.97% on a day when its dealer gamma imbalance is one standard deviation higher (more long gamma). It is not a directional return and not an intraday-momentum coefficient.
- Limits: Working paper; version-dependent numbers; GI depends on the imputation of who holds what from exchange trade data, on three Nasdaq venues only (SPX trades on Cboe); 2010-2020 predates the 0DTE boom.
- Use in the book: Chapters 8A (limit 5), 8B, 9C. CORRECTIONS: (a) the book's "about 16 bps per standard deviation" was not found in any version; the figures found are about 12 bp (stocks, one version), 5-25 bp (stocks, another version) and more than 20 bp (indexes); the notes' question is answered by the units above. (b) 8B infers from the illiquidity interaction that "SPX itself ... has smaller gamma-feedback effects than less liquid single stocks"; the index estimates found (more than 20 bp per SD) are not smaller than the single-stock range, so that inference is not supported by the numbers seen; the illiquidity result is a cross-sectional comparison of underlyings. (c) 9C's "tens of basis points per standard deviation" is consistent with this paper's scale.

### NiPearsonPoteshmanWhite2021
- Citation: Ni, S. X., N. D. Pearson, A. M. Poteshman and J. White (2021). "Does option trading have a pervasive impact on underlying stock prices?" Review of Financial Studies 34(4): 1952-1986 (April 2021). Earlier versions: Pearson, Poteshman and White (2007), SSRN abstract_id=970592; SSRN abstract_id=2867461 (DOI 10.2139/ssrn.2867461).
- Type: peer-reviewed article.
- Verified via: https://academic.oup.com/rfs/article-abstract/34/4/1952/5873587 ; https://econpapers.repec.org/article/ouprfinst/v_3a34_3ay_3a2021_3ai_3a4_3ap_3a1952-1986..htm (volume, issue, pages); https://consensus.app/papers/details/2ca5a91172915fa896710dad5b36adc2/ (abstract); https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2867461 ; https://www.ou.edu/dam/price/Finance/CFS/paper/pdf/pearsonPoteshmanWhite.pdf (2007 working version); http://web.nbs.ntu.edu.sg/general/NTUFinanceConference2019/downloadpapers/paperfolder/FC2019D2_OptionTrading.pdf (2019 version). Numbers from search summaries of the paper's text; versions differ (below).
- Question: Beyond expiration days, does option market makers' hedge rebalancing change the volatility of the underlying stocks every day?
- Data and method: US single stocks. Daily net open interest and signed volume by investor type from the CBOE and the Nasdaq ISE. The gamma of the net option position of likely delta-hedgers (market makers and similar) is COMPUTED from positions for 1990-2001 and ESTIMATED from signed volume for 2002-2012. Panel regressions of daily absolute stock returns (and large-move indicators) on that gamma, with controls.
- Findings: (1) A statistically and economically significant NEGATIVE relation between stock return volatility and the net purchased option positions (gamma) of likely delta-hedgers: positive hedger gamma lowers volatility, negative gamma raises it, on all days, not only near expiration. (2) Size, published-era version: 9.5% of the daily absolute return of optioned stocks in the first period (1990-2001) and 13.4% in the second (2002-2012) can be attributed to hedge rebalancing; a one-standard-deviation shock to the gamma variable is associated with a 28.8 bp (first period) and 29.6 bp (second period) change in the absolute daily return. Earlier 2007 version: about 11.8% of the daily absolute return, and 37 bp per shock. (3) Hedge rebalancing also changes the probability of large stock price moves (abstract).
- How to read it: if a stock's absolute daily move averages, say, 2%, about a tenth of that size is attributable to dealers' hedge trades pushing with or against moves; a one-SD change in dealer gamma shifts the day's absolute return by roughly 0.3 percentage point.
- Limits: Single stocks, not the index; positions after 2001 are estimated from signed volume; the dealer side is identified from exchange data rather than assumed, which is the paper's strength.
- Use in the book: Chapter 8B. CORRECTION: the book states that hedge rebalancing "alters the probability of large daily moves, over 300 bps, by 5% to 14% historically, rising to 13% to 40% in their later sample". Those figures were not found in any summary [unverified]; the headline, verifiable effect sizes are 9.5% and 13.4% of daily absolute returns and about 29 bp of absolute return per SD of gamma. The book should quote those, or check the large-move table directly and give its units (relative change in probability or percentage points), as the notes already ask.

### Soebhag2023
- Citation: Soebhag, A. (2023). "Option gamma and stock returns." Journal of Empirical Finance 74 (December 2023): 101442. DOI 10.1016/j.jempfin.2023.101442. SSRN abstract_id=4256259.
- Type: peer-reviewed article.
- Verified via: https://consensus.app/papers/details/8e640b17797651ab987e923556b2e2bc/ (title, author, journal, DOI, abstract); https://ideas.repec.org/a/eee/empfin/v74y2023ics0927539823001093.html (volume 74, article 101442); https://www.sciencedirect.com/science/article/pii/S0927539823001093 ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4256259 ; https://pure.eur.nl/en/publications/option-gamma-and-stock-returns/ . Unverified: sample period, universe, and how net gamma exposure is signed (end-user positions observed or assumed).
- Question: Does the net gamma exposure that option hedgers carry on a stock predict its returns and volatility?
- Data and method: Cross-section of US optionable stocks; portfolio sorts on each stock's net gamma exposure (NGE) from its option positions; controls for known return predictors [details unverified].
- Findings: (1) Stocks with HIGH net gamma exposure underperform stocks with LOW net gamma exposure by about 10% per year (long-short spread), robust to known predictors. (2) Net gamma exposure predicts future realized volatility: low-NGE stocks are more volatile (the abstract's wording is "stocks with low net gamma exposure negatively predict future realized volatility"). (3) Interpretation: investors demand a risk premium to hold low-NGE (short-dealer-gamma, more volatile) stocks; the volatility predictability comes from a non-informational hedging channel, not private information.
- Limits: Single stocks; the gamma sign's construction is not seen; a return-premium interpretation is one of several possible.
- Use in the book: Chapters 8B and 8D. It extends the NPPW volatility result into returns: stocks where hedgers are short gamma are riskier and earn more. A caution against "negative gamma is bearish" narratives: in this paper the low-gamma stocks earn HIGHER average returns.

### BaltussenDaSoebhag2024
- Citation: Baltussen, G., Z. Da and A. Soebhag (2024). "End-of-Day Reversal." Working paper, SSRN abstract_id=5039009 (dated November 29, 2024); FEB-RN Research Paper No. 77/2025; presented at EFMA 2024 (Lisbon).
- Type: working paper (SSRN 2024).
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5039009 ; https://www.researchgate.net/publication/387148513_End-of-Day_Reversal ; http://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2024-Lisbon/papers/EndofDayReversal_withnames.pdf ; https://alphaarchitect.com/end-of-trading/ (practitioner summary).
- Question: What happens to individual stocks, relative to each other, in the last 30 minutes?
- Data and method: Cross-section of US individual stocks, intraday returns; sorts on the day's return up to the last half hour [sample period unverified].
- Findings: Individual stocks show sharp cross-sectional REVERSALS in the last 30 minutes (intraday losers bounce), economically and statistically highly significant, distinct from market intraday momentum, and coming mainly from positive price pressure on intraday losers. The effect "cannot be explained by liquidity- or gamma-hedging effects"; the authors attribute it to attention-driven retail buying and end-of-day risk management by short sellers.
- Limits: Working paper; concerns relative (cross-sectional) returns, not the index level.
- Use in the book: A necessary qualifier for Chapters 6C and 9B's claim that the last 30 minutes are dominated by hedging flows: at the index level, gamma hedging is linked to momentum (BaltussenDaLammersMartens2021), but in the cross-section of stocks the same authors find a reversal that gamma hedging does not explain. Not every end-of-day pattern is a dealer-gamma pattern.

### BeckmeyerMoerke2021
- Citation: Beckmeyer, H. and M. Moerke (2021). "End-of-Day Momentum in the Cross-Section and Option Hedging." Working paper presented at the EFMA 2021 Annual Meeting (Leeds). https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2021-Leeds/papers/EFMA%202021_stage-2049_question-Full%20Paper_id-237.pdf
- Type: working paper (conference paper, 2021).
- Verified via: the EFMA URL above (title; search summary giving authors and abstract).
- Question: Does market makers' delta hedging of single-stock option inventories move stocks in the last half hour?
- Data and method: US single stocks and their options; aggregated option-market-maker gamma exposure per stock, interacted with the stock's return up to 30 minutes before the close [sample and gamma construction unverified].
- Findings: Establishing delta neutrality around the close "causes return momentum or reversal of 18 basis points for each one percentage point move in the underlying until half an hour before trading close" (abstract, per search summary); the direction (momentum or reversal) depends on the sign of market makers' aggregated gamma; stronger for large-cap stocks; not explained by information.
- How to read it: if a stock is up 1% at 3:30 PM and its dealers are short gamma, it tends to add about 0.18% more by the close; if dealers are long gamma, it tends to give back about 0.18% [scaling of the 18 bp to a gamma level unverified].
- Limits: Conference working paper; later merged into BarbonBeckmeyerBuraschiMoerke2022 [inferred from the shared authors and topic; unverified]. Conflicts with BaltussenDaSoebhag2024, who find the cross-sectional end-of-day reversal is not explained by gamma hedging.
- Use in the book: A single-stock, gamma-signed version of the end-of-day effect for Chapters 6C and 9B, with an effect size in plain units.

### BarbonBeckmeyerBuraschiMoerke2022
- Citation: Barbon, A., H. Beckmeyer, A. Buraschi and M. Moerke (2021/2022). "The Role of Leveraged ETFs and Option Market Imbalances on End-of-Day Price Dynamics" (SSRN, September 2021); revised as "Liquidity Provision to Leveraged ETFs and Equity Options Rebalancing Flows: Evidence from End-of-Day Stock Prices." Swiss Finance Institute Research Paper No. 22-40 (2022). SSRN abstract_id=3925725.
- Type: working paper (SSRN 2021; SFI Research Paper 2022; presented at FoFI 2022 and the Northern Finance Association). No journal version found.
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3925725 ; https://www.sfi.ch/en/publications/n-22-40-liquidity-provision-to-leveraged-etfs-and-equity-options-rebalancing-flows-evidence-from-end-of-day-stock-prices ; https://econpapers.repec.org/paper/chfrpseri/rp2240.htm ; https://www.researchgate.net/publication/355381896_The_Role_of_Leveraged_ETFs_and_Option_Market_Imbalances_on_End-of-Day_Price_Dynamics ; https://wp.lancs.ac.uk/fofi2022/files/2022/08/FoFI-2022-027-Mathis-Moerke.pdf . Unverified: sample period and coefficient sizes.
- Question: Which end-of-day flow moves stock prices more, leveraged-ETF rebalancing or option market makers' delta hedging, and how does liquidity provision respond?
- Data and method: US stocks held by leveraged ETFs and with listed options; LETF rebalancing demand computed from each fund's assets and leverage; aggregated option-market-maker gamma imbalance scaled by average dollar volume; last-half-hour returns and next-day reversals.
- Findings: (1) A large NEGATIVE (positive) aggregated gamma imbalance, relative to average dollar volume, produces significant end-of-day MOMENTUM (reversal). (2) The LETF rebalancing effect is economically LARGER than the option gamma effect. (3) Both effects revert quickly at the next day's open (temporary price pressure). (4) LETF flows are perfectly predictable and attract more liquidity provision, so their price effect is shorter-lived and has DECREASED over time; option delta-hedgers can time their rebalancing, their flows are less predictable, and the gamma effect persists throughout the sample. (5) Implication drawn: disclosure of predictable flows helps liquidity.
- Limits: Working paper; stock-level, not SPX; dealer gamma imbalance inferred from exchange data.
- Use in the book: Chapter 8C's grind box (L(L-1)xA) and 6C's leveraged-fund rebalance: the paper shows LETF rebalancing moves closes more than option hedging does, but liquidity providers have learned to anticipate it. That tempers 8D's use of LETF flow as unbounded "mechanical buying".

### ParkZhao2024
- Citation: Park, T. and F. Zhao (2024). "Inelastic Hedging Demand and Intraday Momentum." Working paper presented at the Northern Finance Association, https://portal.northernfinanceassociation.org/viewp.php?n=2240183764 . A related AFA 2025 program paper, "Where does gamma hedge drive the intraday market move?" (dated June 2, 2024), https://afajof.org/management/viewp.php?n=129472 , studies the same mechanism [its authors were not seen; that it is the same paper is unverified].
- Type: working papers (conference).
- Verified via: the two URLs above (search summaries).
- Question: When does short-gamma hedging become price-insensitive ("inelastic"), and does that strengthen intraday momentum?
- Data and method: S&P 500 index options holdings data; the gamma-theta breakeven range (GTBR: the move at which a short-gamma book's gamma loss equals its theta income); intraday momentum in the Gao-Han-Li-Zhou framework at half-hour frequency.
- Findings: Intraday momentum is stronger when active option traders have short gamma exposure, and it surges when the index moves beyond the GTBR, where hedgers' demand for the underlying turns inelastic; when the range is hit, market makers on average keep delta hedging rather than buying back the options.
- Limits: Working papers; effect sizes not seen.
- Use in the book: A concrete, testable version of the "gamma flip" idea for Chapter 8A/8B: the regime change happens at a move size (breakeven range) rather than at a price level read off open interest.

### D. Leveraged and inverse ETFs: end-of-day rebalancing flows

### ChengMadhavan2009
- Citation: Cheng, M. and A. Madhavan (2009). "The dynamics of leveraged and inverse exchange-traded funds." Journal of Investment Management 7(4): 43-62. SSRN abstract_id=1539120.
- Type: peer-reviewed practitioner-academic journal article.
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1539120 ; https://www.econbiz.de/Record/the-dynamics-of-leveraged-and-inverse-exchange-traded-funds-cheng-minder/10009910816 ; https://consensus.app/papers/details/f937a6025b145beb9b4b5506ea5ffd73/ (abstract); search summary giving volume 7, issue 4, pages 43-62.
- Question: How do daily-reset leveraged and inverse ETFs trade, and what does that do to the market?
- Data and method: A framework for the daily rebalancing of leveraged and inverse funds (the rebalance is proportional to L(L-1) times the day's return times assets) with illustrative market data.
- Findings: The daily re-leveraging of these funds "creates profound microstructure effects and exacerbates volatility towards the close"; the funds' gross returns embed a path-dependent option that can destroy value for buy-and-hold investors.
- Limits: A framework with illustrative magnitudes, not a causal test; later empirical work (IvanovLenkey2018, Lenkey2024) finds the late-day effect economically small once capital flows are counted.
- Use in the book: Source for the rebalancing rule in Chapters 6C and 8C (L(L-1)xA), and for the claim that inverse and leveraged products trade with the day's move.

### ShumEtAl2016
- Citation: Shum, P., W. Hejazi, E. Haryanto and A. Rodier (2016). "Intraday share price volatility and leveraged ETF rebalancing." Review of Finance 20(6): 2379-2409. SSRN abstract_id=2161057.
- Type: peer-reviewed article.
- Verified via: https://academic.oup.com/rof/article-abstract/20/6/2379/2418138 ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2161057 ; https://consensus.app/papers/details/7a5d0dfa275e58cfa05572836fe3ee3f/ (abstract).
- Question: Did leveraged-ETF rebalancing raise end-of-day volatility?
- Data and method: US equity markets around the financial crisis, 2006-2011; end-of-day volatility against the ratio of potential LETF rebalancing trades to total trading volume.
- Findings: End-of-day volatility was positively and statistically significantly correlated with the rebalancing-to-volume ratio; "the impacts were not all economically significant, but largest during the most volatile days"; the predictable pattern invites predatory trading.
- Limits: Correlational; does not net out investor flows into and out of the funds (see IvanovLenkey2018).
- Use in the book: Supports "the effect is largest on the most volatile days" for Chapters 6C and 8C, with the caveat that economic size is modest.

### IvanovLenkey2018
- Citation: Ivanov, I. T. and S. L. Lenkey (2018). "Do leveraged ETFs really amplify late-day returns and volatility?" Journal of Financial Markets [volume and pages unverified]. DOI 10.1016/j.finmar.2018.09.001. Earlier version: "Are concerns about leveraged ETFs overblown?" Federal Reserve Board FEDS Working Paper 2014-106, DOI 10.17016/feds.2014.106.
- Type: peer-reviewed article (earlier version: Federal Reserve working paper).
- Verified via: https://consensus.app/papers/details/7c6441cd9c505116962d84ee91ab224b/ (2018 article: title, authors, journal, DOI, abstract); https://consensus.app/papers/details/ea2b7f7bc2505f2da669b074ea3a4d91/ (2014 FEDS version).
- Question: Once investor flows into and out of leveraged and inverse ETFs are counted, do their rebalancing trades still move late-day prices?
- Data and method: US equity-based leveraged and inverse ETFs, 2006-2014; model showing that capital flows offset (and can eliminate) rebalancing demand; late-day returns and volatility regressed on flow-adjusted rebalancing demand with risk factors.
- Findings: Capital flows "substantially reduce ETF rebalancing demand, even during periods of severe market stress"; after accounting for flows and risk factors, "the impact of ETF rebalancing on late-day returns and volatility is economically insignificant" (abstract).
- Limits: Pre-2015 sample; before the growth of single-stock leveraged ETFs and of 2x/3x products on individual names.
- Use in the book: A NEGATIVE result the book should cite beside Chapter 8C's grind box: the mechanical L(L-1)xA rebalance overstates actual flow, because fund investors trade against it (contrarian flows into leveraged funds after losses).

### Lenkey2024
- Citation: Lenkey, S. (2024). "The Market Impact of Leveraged ETFs: A Survey of the Literature." Working paper, SSRN abstract_id=4710812, DOI 10.2139/ssrn.4710812.
- Type: working paper (literature survey, SSRN 2024).
- Verified via: https://consensus.app/papers/details/ed52017816a453cda2e7ba0d21171437/ (title, author, DOI, abstract).
- Question: What does the whole literature say about leveraged ETFs and late-day prices?
- Data and method: Survey.
- Findings: Papers consistently report statistically significant associations between rebalancing demand and late-day returns and volatility, but "most of the available papers suffer from potentially serious methodological errors, and the economic associations appear to be insignificant"; the market supplies enough liquidity; policymakers' concerns "are not supported by the overall empirical evidence".
- Limits: Written by an author of the main negative-result paper; predates the 2025-2026 boom in single-stock leveraged ETFs (see Zhao2026).
- Use in the book: The skeptical summary for Chapters 6C, 8C and 8D.

### Todorov2023
- Citation: Todorov, K. (2023). "When passive funds affect prices: Evidence from volatility and commodity ETFs." Review of Finance [volume and pages unverified]. DOI 10.1093/rof/rfad038. Related: BIS Working Papers No 952, "Passive funds affect prices: ..." (title continuation unverified), https://www.bis.org/publ/work952.pdf .
- Type: peer-reviewed article (BIS working-paper version).
- Verified via: https://consensus.app/papers/details/4fa378aecf9f5c0494b4938179ddc2bd/ (title, author, journal, DOI, abstract); https://www.bis.org/publ/work952.pdf (search listing "BIS Working Papers No 952 Passive funds affect prices:").
- Question: How much do ETF rebalancing flows distort prices in the most ETF-dominated markets, VIX futures and commodities?
- Data and method: VIX futures and commodity futures; a futures-based measure isolating an ETF-related component of prices; decomposition of ETF demand into leverage rebalancing, calendar (roll) rebalancing and flow rebalancing.
- Findings: A component of VIX futures prices is strongly related to ETF rebalancing; LEVERAGE rebalancing has the largest effect; it "amplifies price changes and exposes ETF counterparties to variance"; trading against ETFs is risky.
- Limits: Magnitudes not seen; volatility and commodity futures only.
- Use in the book: The peer-reviewed evidence behind Chapter 8C's Volmageddon mechanism (inverse and leveraged VIX products' rebalancing amplifying VIX futures moves), to cite beside the BIS box of March 2018.

### Zhao2026
- Citation: Zhao, Y. (2026). "Preying on Leveraged ETFs." arXiv preprint, DOI 10.48550/arxiv.2608.03703.
- Type: working paper (arXiv 2026).
- Verified via: https://consensus.app/papers/details/cca3d34d914f59eba1bfbcf2310331db/ (title, author, DOI, abstract).
- Question: Did speculators front-running leveraged-ETF closing rebalances add to Korea's extreme volatility in 2026?
- Data and method: Korean stocks tracked by leveraged ETFs against control groups; responses to pre-open US news; a quantification of self-reinforcing rebalancing.
- Findings: LETF-tracked Korean stocks reverse about 75% of their first-day response to pre-open US news by the next close and oscillate for days, a pattern absent in all control groups; the self-reinforcing rebalance raised SK Hynix's annualized volatility from 100.0% to 136.7% over nine weeks and cost the products' mostly retail holders 17.6% of their initial investment.
- Limits: Very recent preprint; one market and episode.
- Use in the book: A current counterexample to Lenkey2024's reassurance: when leveraged products are large relative to a single stock's liquidity, the rebalance-and-predation loop can raise volatility by a third. Relevant to Chapter 8D's gamma-squeeze preconditions.

### E. Who holds what: the sign of dealers' index-option positions

### GarleanuPedersenPoteshman2009
- Citation: Garleanu, N., L. H. Pedersen and A. M. Poteshman (2009). "Demand-based option pricing." Review of Financial Studies 22(10): 4259-4299. DOI 10.1093/rfs/hhp005. NBER Working Paper 11843 (December 2005).
- Type: peer-reviewed article.
- Verified via: https://academic.oup.com/rfs/article-abstract/22/10/4259/1590158 ; https://ideas.repec.org/a/oup/rfinst/v22y2009i10p4259-4299.html ; https://www.nber.org/papers/w11843 ; https://consensus.app/papers/details/3a2733421bef5d8b8bf5842734221d8a/ (abstract).
- Question: If dealers cannot hedge perfectly, how does end-user demand move option prices?
- Data and method: Model of competitive, risk-averse intermediaries; empirically, CBOE daily closing long and short open interest on all SPX and equity options for public customers and firm proprietary traders, 1996 to 2001, which identifies aggregate dealer and end-user positions (observed, not assumed).
- Findings: (1) Demand pressure raises an option's price in proportion to the variance of its unhedgeable part, and raises other options' prices in proportion to covariances. (2) End users are net LONG SPX options (index options are expensive and have high positive end-user demand) and net SHORT single-stock options (small negative demand). (3) Demand helps explain the expensiveness and the skew of index options (demand concentrated in out-of-the-money puts) in the time series.
- Limits: 1996-2001 data, before weeklies, 0DTE, option-income funds and structured-product growth. The effect is on option prices; the paper does not test the effect of dealer gamma on the index.
- Use in the book: Chapters 8A, 10H, 10I. It is the empirical basis for the "JPM-era" convention's put side: in 1996-2001 end users were net long SPX puts, so dealers were net SHORT index puts (and short gamma there). Book check: citation details in 8A (Vol. 22, No. 10, 4259-4299) are correct. Both readings in the book are defensible: the Dealer Mechanics Lab's (foundation for dealer positioning) and the Edge Book's (effect on option prices, not the underlying).

### ChenJoslinNi2019
- Citation: Chen, H., S. Joslin and S. X. Ni (2019). "Demand for crash insurance, intermediary constraints, and risk premia in financial markets." Review of Financial Studies 32(1): 228-265. NBER Working Paper 25573; SSRN abstract_id=3341133.
- Type: peer-reviewed article.
- Verified via: https://academic.oup.com/rfs/article-abstract/32/1/228/4994715 ; https://www.nber.org/papers/w25573 ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3341133 ; search summary giving the sample (1991/01-2012/12), the PNBO measure and "32(1), 228-265".
- Question: What does the net amount of crash insurance that public investors buy from intermediaries say about intermediary constraints and risk premia?
- Data and method: CBOE data on deep out-of-the-money (DOTM) SPX puts, January 1991 to December 2012; measure PNBO = public net buy-to-open volume in DOTM SPX puts per month (what public investors buy, equivalently what intermediaries sell).
- Findings: On average public investors are net BUYERS of DOTM SPX puts from intermediaries (dealers net short crash insurance). When the net amount public investors buy falls, which the authors read as tighter intermediary constraints, option expensiveness rises, risk premia rise across many assets, funding liquidity deteriorates and broker-dealers deleverage; PNBO strongly predicts future market excess returns. [Size per one-SD change in PNBO not seen; unverified.]
- Limits: Monthly flow in DOTM puts only, not the dealers' full gamma book; ends 2012.
- Use in the book: The direct evidence for the sign of dealers' index PUT position before 2013: dealers net short deep OTM SPX puts. It shows the sign is not fixed: the quantity dealers are willing to carry shrinks when their constraints bind, which is when stress arrives. It does not settle the 0DTE era.

### ConstantinidesLian2021
- Citation: Constantinides, G. M. and L. Lian (2021). "The supply and demand of S&P 500 put options." Critical Finance Review 10(1) [pages unverified]. NBER Working Paper 21161 (2015); SSRN abstract_id=2645858.
- Type: peer-reviewed article (NBER working paper 2015).
- Verified via: https://www.nowpublishers.com/article/Details/CFR-0064 ; https://www.nber.org/papers/w21161 ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2645858 ; https://cfr.ivo-welch.info/published/papers/constantinides-lian.pdf ; https://consensus.app/papers/details/380cdedb044155029742181c1c808d9e/ (abstract). Unverified: sample years and the data source for net buying.
- Question: Why does the SPX put skew not flatten when disaster risk rises, as no-arbitrage models predict?
- Data and method: Equilibrium model of risk-averse market makers supplying at-the-money and out-of-the-money SPX puts to risk-averse customers who hold the index and buy puts as protection; tested against SPX implied volatility skew and customers' net buying of puts.
- Findings: In equilibrium market makers are net SELLERS and customers net BUYERS of index puts. As disaster risk rises, customers want more puts while market makers become more credit-constrained in writing them; the price rise is larger for OTM puts, which steepens the skew; the model-implied (and observed) customer net buy of puts FALLS as risk and put prices rise.
- Limits: Pre-0DTE; the net-buy measure is flow-based.
- Use in the book: Second, independent confirmation (with GPP 2009 and CJN 2019) that before the 0DTE era dealers were net short SPX puts, and that their capacity to stay short shrinks exactly in stress, a mechanism for 8C.

### HuKirilovaMuravyevRyu2023
- Citation: Hu, J., A. Kirilova, D. Muravyev and D. Ryu (2023, revised). "Options Market Makers." Working paper, SSRN abstract_id=4633451, DOI 10.2139/ssrn.4633451 (dated April 1, 2023); presented at the FMA Derivatives conference 2025 (https://www.fma.org/assets/docs/Derivatives2025/Muravyev.pdf).
- Type: working paper (SSRN).
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4633451 ; https://www.researchgate.net/publication/376103990_Options_Market_Makers ; https://experts.illinois.edu/en/publications/options-market-makers/ ; https://www.fma.org/assets/docs/Derivatives2025/Muravyev.pdf .
- Question: How do individual options market makers actually manage risk: by delta hedging, or otherwise?
- Data and method: Unique account-level data for KOSPI 200 index options and futures (Korea), identifying individual market makers; corroboration with aggregate S&P 500 options data.
- Findings: Market makers earn high Sharpe ratios, with positive profits on 74% of days; they reduce risk MAINLY BY REBALANCING INVENTORY WITHIN MINUTES (trading the options back out) rather than by costly delta hedging; only a minority consistently delta hedge. In S&P 500 options, daily trading volume exceeds net position changes by a factor of 32. The authors conclude "delta hedging is less universal than commonly assumed".
- Limits: The account-level evidence is Korean; the S&P 500 corroboration is aggregate.
- Use in the book: A direct challenge to the GEX premise in Chapters 6C, 8A and 8B that every dollar of dealer gamma turns into delta-hedging trades in the underlying. If dealers offload option inventory instead, the hedge-flow formula overstates the flow, and the "kappa" of 8B is lower than position data alone imply. Should appear among 8A's limits.

### Terstegge2025
- Citation: Terstegge, J. (2025). "Intermediary Option Pricing." Working paper, SSRN abstract_id=5877762; presented at the FMA Derivatives conference 2025 (https://www.fma.org/assets/docs/Derivatives2025/Terstegge.pdf), on the AFA program (https://afajof.org/management/viewp.php?n=181272) and as a CEPR poster (January 2025, https://cepr.org/system/files/2025-01/Terstegge_poster.pdf).
- Type: working paper (job-market-style paper, 2025).
- Verified via: the four URLs above (search summaries of the abstract and text).
- Question: Does dealers' inventory risk, from equity illiquidity overnight, explain the risk premium in S&P 500 options?
- Data and method: Cboe SPX option prices and quotes at 15-minute intervals and daily Cboe "Open Close Volume" files, 2011-2023, from which intermediary (dealer) aggregate positions are constructed [construction details unverified].
- Findings: (1) In calls, intermediaries' buy and sell volumes are roughly balanced and net call positions hover near zero; in puts, sell volumes consistently exceed buy volumes, leaving a PERSISTENT NET SHORT PUT position of about 19 million contracts, concentrated in deep out-of-the-money puts. (2) Without hedge adjustments, a 10% fall in the S&P 500 would cost roughly 200% of the dealers' option inventory value. (3) "Gap risk": even a perfectly delta-hedged dealer at the close cannot re-hedge a large overnight or weekend move because equity liquidity is thin then; intermediary inventory and equity illiquidity explain most of the SPX option risk premium since 2011.
- Limits: Working paper; Open-Close-based positions miss off-exchange and futures-option hedges; contract counts are not gamma, and deep OTM puts carry little gamma until a crash.
- Use in the book: The most direct recent evidence on the sign question of Chapter 8A for SPX, 2011-2023. By CONTRACTS, dealers were net short puts and flat calls, the put side of the "JPM-era" convention, NOT the 0DTE-era convention's "dealers long puts". It can coexist with DEV's and Adams et al.'s positive average dealer GAMMA only if dealers are long gamma near the money (short-dated options customers sell) while short far-OTM puts, whose gamma grows in a sell-off. That combination is exactly the "damping on normal days, amplifying in a crash" pattern of 8B and 8C, and it means a single sign convention per option type (calls +1, puts -1, or the reverse) is wrong for SPX.

### F. Stress episodes

### Jackwerth2020
- Citation: Jackwerth, J. C. (2020). "What do index options teach us about COVID-19?" Review of Asset Pricing Studies 10(4): 618-634. DOI 10.2139/ssrn.3573558 (SSRN version, abstract_id=3573558).
- Type: peer-reviewed article.
- Verified via: https://academic.oup.com/raps/article-abstract/10/4/618/5894979 ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3573558 ; https://consensus.app/papers/details/64c8d3035c3053ceabdbc119aa4050bb/ (abstract).
- Question: What did S&P 500 option prices and option trading reveal about crash expectations and hedging during COVID-19?
- Data and method: Risk-neutral distributions from S&P 500 options, February-March 2020; option trade data by investor type.
- Findings: On February 20, 2020 the index did not yet reflect the crisis; only on March 16, 2020 was the full impact visible, with pronounced bimodality in longer-maturity options (a sizeable crash scenario). "Firms bought crash protection ahead of the index crash, whereas retail customers bought it as the index was already recovering" (abstract).
- Limits: Short sample; investor classification from exchange data.
- Use in the book: Chapter 8C's March 2020 case: evidence on WHO bought puts and WHEN. Firms' pre-crash put buying is consistent with dealers being short put gamma into the fall (the book's precondition), and retail's late buying shows demand arriving after the move. The book's claim that dealers were short the put protection institutions bought is supported in direction; its size is not measured here.

### SushkoTurner2018BIS
- Citation: Sushko, V. and G. Turner (2018). "The equity market turbulence of 5 February - the role of exchange-traded volatility products." Box in BIS Quarterly Review, March 2018 (within the chapter "Volatility is back"). https://www.bis.org/publ/qtrpdf/r_qt1803t.htm
- Type: regulator report (central-bank research box).
- Verified via: https://www.bis.org/publ/qtrpdf/r_qt1803t.htm ; https://www.bis.org/publ/qtrpdf/r_qt1803a.pdf ; https://www.bis.org/publ/qtrpdf/r_qt1803.pdf (search summaries of the box's text).
- Question: What role did leveraged and inverse VIX exchange-traded products play on February 5, 2018?
- Data and method: VIX futures transaction data, ETP assets and rebalancing rules.
- Findings: On February 5 the S&P 500 fell about 4% and the VIX jumped about 20 points. Assets of select leveraged and inverse volatility ETPs were about $4 billion at end-2017. Issuers rebalance daily by trading VIX-related derivatives, usually in the last hour. "Transaction data show a spike in trading volume to 115,862 VIX futures contracts, or roughly one quarter of the entire market, and at highly inflated prices, within one minute at 16:08." The inverse ETP XIV lost 84% of its value and was terminated.
- Limits: A box, not a causal study; it quantifies the rebalancing channel in VIX futures, not dealer gamma in SPX options.
- Use in the book: Chapters 8C and 9A quote the 115,862 figure correctly. CORRECTIONS: the book's "combined approximately $3.5 billion" for XIV and SVXY is not the BIS figure; the BIS gives about $4 billion for "select leveraged and inverse" volatility ETPs at end-2017 (a broader group). XIV's 84% loss is the BIS figure (the book says "more than 80% intraday", consistent). The book's "VIX at 17.31 at the 9:30 open" is wrong: AugustinChengVandenBergen2021 give the February 5 VIX as 18.44 at the open and 37.32 at the close; 17.31 is consistent with the prior (February 2) close, from which 37.32 is +115% [the 17.31 prior close itself not seen in a search result]. The mechanism the book gives (dealers short VIX call wings "in FLEX", vanna across SPX puts) is not in the BIS box, which attributes the spike to ETP rebalancing.

### AugustinChengVandenBergen2021
- Citation: Augustin, P., I.-H. Cheng and L. Van den Bergen (2021). "Volmageddon and the failure of short volatility products." Financial Analysts Journal 77(3): 35-51. DOI 10.1080/0015198X.2021.1913040. SSRN abstract_id=3819342.
- Type: peer-reviewed article (practitioner-academic journal).
- Verified via: https://www.tandfonline.com/doi/full/10.1080/0015198X.2021.1913040 ; https://econpapers.repec.org/RePEc:taf:ufajxx:v:77:y:2021:i:3:p:35-51 (volume 77, issue 3, pages 35-51); https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3819342 ; https://rpc.cfainstitute.org/research/financial-analysts-journal/2021/volmageddon-failure-short-volatility-products .
- Question: Why did short-volatility ETPs collapse on February 5, 2018?
- Data and method: Case study of the VIX, VIX futures and short-volatility ETPs (XIV, SVXY), with their hedge and leverage rebalancing.
- Findings: A one-day loss of more than 90% in the value of short-volatility ETPs; the VIX rose over 100% in one day, "from 18.44 at open to 37.32 at close", after nearly a year of low volatility. ETPs can collapse when hedge and leverage rebalancing meets concentrated markets; the episode resembles 1987 portfolio insurance. Regulators and risk managers should monitor hedge and leverage rebalancing when concentration and volatility are high.
- Limits: Case study.
- Use in the book: Chapter 8C's Volmageddon timeline: corrects the opening VIX (18.44, not 17.31) and supports "rebalancing plus concentration" as the mechanism. Pair with Todorov2023 for the systematic evidence on VIX-ETP rebalancing.

### TodorovVilkov2024BISBulletin95
- Citation: Todorov, K. and G. Vilkov (2024). "Anatomy of the VIX spike in August 2024." BIS Bulletin No 95, October 29, 2024. https://www.bis.org/publications/bulletin-95-anatomy-vix-spike-august-2024 ; PDF https://www.bis.org/publ/bisbull95.pdf
- Type: regulator report (BIS Bulletin).
- Verified via: https://www.bis.org/publications/bulletin-95-anatomy-vix-spike-august-2024 ; https://finadium.com/bis-bid-ask-spread-activity-behind-august-vix-spike-not-etf-hedging/ ; https://www.centralbanking.com/central-banks/financial-stability/7962618/vix-spike-in-august-not-driven-by-actual-volatility-bis (press coverage); search summary of the bulletin's text.
- Question: Why did the VIX spike to about 65 before the US open on August 5, 2024, and was it driven by hedging flows?
- Data and method: SPX option quotes used in the VIX calculation, pre-market and regular session; decomposition of the VIX change by option; checks on VIX ETF rebalancing, market-maker option hedging and dispersion trades.
- Findings: The VIX recorded its biggest one-day spike ever, up 180% to almost 66 pre-market. Asymmetric widening of bid-ask spreads lifted the mid-quotes used by the VIX formula, especially for less liquid out-of-the-money puts, which accounted for more than 85% of the spike. Pre-market option volume was about 80 times lower than in regular sessions; once regular trading opened, volume surged and spreads narrowed sharply. "VIX ETFs, market makers' option hedging, and dispersion trades do not seem to have contributed meaningfully to the spike." The VIX can rise with wider quotes without a fundamental rise in expected volatility.
- Limits: A bulletin; explains the index print, not the equity sell-off itself.
- Use in the book: CORRECTIONS for Chapter 8C's August 5, 2024 section: (a) the "VIX above 65 intraday" was a PRE-MARKET print driven mostly by quote-spread widening in thin trading, not a traded level of volatility; (b) the BIS found no meaningful role for market makers' option hedging in the spike, so the book's use of the episode as dealer-gamma feedback (and its unsourced "SPX dealer gamma was short going into the event") needs to be restated as unproven; (c) the "third-highest reading in its history" is not the BIS's framing, which calls it the biggest one-day spike ever (in percentage terms) [the ranking of the 65.73 level among all VIX readings not verified].

### LiAskanaziSEC2025
- Citation: Li, S. and R. Askanazi (2025). "Demystify the Surge in VIX." SEC Division of Economic and Risk Analysis (DERA) working paper, April 2025. https://www.sec.gov/files/dera-vix-working-paper-2504.pdf ; summary page https://www.sec.gov/about/divisions-offices/division-economic-risk-analysis/staff-papers-analyses/demystify-surge-vix
- Type: regulator report (SEC staff working paper; views of the authors).
- Verified via: the two SEC URLs above (search summaries).
- Question: What drove the pre-market VIX print above 65 on August 5, 2024?
- Data and method: Decomposition of the VIX calculation (which strikes enter, and their mid-quotes) on August 5, 2024 against a typical day.
- Findings: The VIX rose from 23.9 to over 65 in pre-market hours while VIX futures stayed below 35. More out-of-the-money puts entered the VIX strike strip than usual and fewer OTM calls qualified; the surge was driven mainly by a sharp rise in the MID-QUOTES of OTM puts.
- Limits: Working paper on index construction; no test of hedging flows.
- Use in the book: Independent confirmation of TodorovVilkov2024BISBulletin95 for Chapter 8C and Chapter 9A: the headline "VIX 65" measured quote conditions in a thin pre-market, and the tradable VIX futures never exceeded 35. A stress episode's most-quoted number can be a measurement artifact.

### BangsgaardKokholm2025
- Citation: Bangsgaard, C. and T. Kokholm (2025). "The stock market impact of volatility hedging: Evidence from end-of-day trading by VIX ETPs." Journal of Banking and Finance 180 (November 2025): 107556. DOI 10.1016/j.jbankfin.2025.107556. SSRN abstract_id=4470636.
- Type: peer-reviewed article.
- Verified via: https://www.sciencedirect.com/science/article/pii/S0378426625001761 ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4470636 (search summary giving authors, volume, article number, DOI and abstract).
- Question: Do VIX ETPs' end-of-day rebalancing trades in VIX futures spill over into S&P 500 futures prices?
- Data and method: VIX ETP rebalancing at the close, VIX futures hedging by their counterparties, and SPX futures prices around the rebalancing window, with reversal tests [sample period unverified].
- Findings: SPX futures prices partly REVERSE after VIX-ETP rebalancing trades, evidence of a transitory SPX price impact from VIX-futures hedging; no indication that the impact comes from new information or from the hedging of market makers in SPX or VIX options.
- Limits: Effect sizes not seen.
- Use in the book: The peer-reviewed channel from volatility products to the S&P 500 itself, for Chapter 8C (Volmageddon) and 9A: hedging of VIX futures moves the index at the close, and the effect is NOT explained by SPX option market makers' hedging, which again separates ETP rebalancing from dealer gamma.

### SECStaffReport2021
- Citation: U.S. Securities and Exchange Commission, Staff (2021). "Staff Report on Equity and Options Market Structure Conditions in Early 2021." Dated October 14, 2021; announced in SEC press release 2021-212 (search summaries give October 14 and October 18, 2021 as the release date). https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf
- Type: regulator report (staff report; views of SEC staff).
- Verified via: https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf ; https://www.sec.gov/newsroom/press-releases/2021-212 ; https://www.marketsmedia.com/sec-reports-on-gamestop/ ; https://clsbluesky.law.columbia.edu/2022/02/22/an-academic-critique-of-the-secs-gamestop-report/ (search summaries of the report's text).
- Question: What drove GameStop's (GME) January 2021 price surge, and what market-structure issues did it expose?
- Data and method: Regulatory trade and position data (consolidated audit trail, options data by participant type, short interest, fails to deliver) for GME and other meme stocks.
- Findings: (1) Neither a short squeeze nor a gamma squeeze caused the price increase; positive sentiment, not buying-to-cover, sustained it (short covering did occur, especially January 22-27, when the price rose as short interest fell, but was a small part of buying). (2) On gamma: the "increase in options trading volume was mostly driven by an increase in the buying of put, rather than call, options. Further, data show that market-makers were buying, rather than writing, call options. These observations by themselves are not consistent with a gamma squeeze." (3) GME short interest as a percent of float peaked at about 122.97% in January 2021 (search summary; press figures of about 140% early in January circulate from other sources) [the report's exact figure and date unverified]. (4) Trading restrictions arose from clearing-deposit requirements.
- Limits: Staff report; the gamma analysis was limited (see MittsEtAl2022 for the critique).
- Use in the book: CORRECTIONS for Chapter 8C's GME case: the book presents GME as "the canonical single-name gamma squeeze" in which retail call buying left dealers short calls; the SEC staff found market makers were net BUYERS of calls and option volume was dominated by put buying, which by itself is inconsistent with a gamma squeeze. The book should present the gamma-squeeze account as contested, citing both the SEC report and MittsEtAl2022. Also: the book's "short interest approximately 140% of the float" matches press figures for early January; the SEC's January peak figure seen is about 123%.

### MittsEtAl2022
- Citation: Mitts, J., R. H. Battalio, L. R. Glosten and B. Kochuba (2022). "A Report by the Ad Hoc Academic Committee on Equity and Options Market Structure Conditions in Early 2021." SSRN abstract_id=4030179 (2022). Summary: "An Academic Critique of the SEC's GameStop Report," CLS Blue Sky Blog, February 22, 2022, https://clsbluesky.law.columbia.edu/2022/02/22/an-academic-critique-of-the-secs-gamestop-report/
- Type: working paper / academic committee report (SSRN 2022). One author (Kochuba) is the founder of SpotGamma, a GEX vendor: practitioner involvement to note.
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4030179 ; the CLS Blue Sky URL above (search summaries).
- Question: Did the SEC staff understate short-squeeze and gamma-squeeze effects in GME?
- Data and method: Additional public trade and options data; extension of the SEC's gamma analysis to include delta hedging by market makers in both puts and calls.
- Findings: Additional data suggest GME may have been subject to BOTH a short squeeze and a gamma squeeze; a nontrivial fraction of volume consisted of short sellers' covering purchases; the SEC's gamma analysis can be extended to include market makers' hedging of puts as well as calls to approximate the options' contribution to the price rise [size of the contribution not seen; unverified].
- Limits: Uses public data less granular than the SEC's; the vendor co-author's commercial interest.
- Use in the book: The counterpoint to SECStaffReport2021 for Chapter 8C: the GME gamma squeeze is disputed, not settled; the honest statement is that the mechanism is plausible, the SEC's position data did not show it, and academic critics argue it contributed.

### BaigZaynutdinovaStrong2025
- Citation: Baig, A., G. R. Zaynutdinova and C. Strong (2025). "Seeking Gamma: Lessons from the Meme Frenzy." Working paper, SSRN abstract_id=5959235; on the AFA 2026 program (https://afajof.org/management/viewp.php?n=183232) [the AEA/ASSA 2026 listing seen in search results is assumed to be the same paper; unverified].
- Type: working paper (SSRN 2025).
- Verified via: https://afajof.org/management/viewp.php?n=183232 ; https://papers.ssrn.com/sol3/Delivery.cfm/5959235.pdf?abstractid=5959235&mirid=1 (search summaries).
- Question: How common are gamma squeezes across all US stocks, and what do they do to prices?
- Data and method: Systematic identification of 669 potential gamma-squeeze events in US stocks, 2019-2023.
- Findings: [Results beyond the event count not seen in search results; unverified.] The paper engages the SEC staff's finding that GME option volume was put-driven and that market makers bought calls.
- Limits: Findings not verified.
- Use in the book: The first large-sample study of single-name gamma squeezes; worth reading directly for Chapter 8D's checklist before the rewrite.

### G. Tests of practitioner GEX (sign, flip, walls)

### SqueezeMetrics2017
- Citation: SqueezeMetrics (2016, revised 2017). "Gamma Exposure (GEX)." White paper. https://squeezemetrics.com/monitor/download/pdf/white_paper.pdf
- Type: vendor documentation / practitioner white paper. Claims by the vendor, not an independent test.
- Verified via: https://squeezemetrics.com/monitor/download/pdf/white_paper.pdf (search result titled "Gamma Exposure Disclaimer"); search summary giving the first public use in March 2016 and a 2017 revision and the numbers below. Unverified: the exact sample years and whether the quartile numbers below are quoted correctly (the summary's figures are internally inconsistent, see Findings).
- Question: Does the sign and size of dealers' aggregate gamma (under the vendor's long-calls/short-puts convention) predict the next day's S&P 500 variance better than the VIX?
- Data and method: SPX option open interest with the convention that dealers are long calls and short puts; daily GEX sorted into quartiles; standard deviation of next-day SPX returns by quartile, compared with sorts on the VIX.
- Findings (vendor claims, as summarized): next-day SPX standard deviation rises as GEX falls; one comparison quoted is 0.55% against 0.85% for the top two GEX quartiles, and the text then speaks of "the difference between 0.66% and 0.85%", about 4 index points of daily range at SPX 2000; by contrast, the lowest and second-lowest VIX quartiles give similar next-day standard deviations (0.51% and 0.66%), so the vendor argues GEX separates low-volatility states that the VIX does not.
- Limits: Vendor white paper; in-sample; the convention (dealers long calls, short puts) is assumed, not observed; no control for implied volatility beyond quartile comparison; the numbers as summarized do not reconcile.
- Use in the book: The origin of the public GEX formula and its original empirical claim (Chapter 8A). Present it as the vendor's claim, next to DobrowolskiFlashAlpha2026, which finds most of the raw GEX signal is the volatility regime.

### SpotGammaKeyLevels2024
- Citation: SpotGamma (2024). "SpotGamma SPX Key Levels Statistics." SpotGamma support article. https://support.spotgamma.com/hc/en-us/articles/31209900542867-SpotGamma-SPX-Key-Levels-Statistics
- Type: vendor documentation (self-reported statistics).
- Verified via: the URL above (search summaries).
- Question: How did SPX behave around SpotGamma's published Call Wall and Put Wall levels?
- Data and method: SpotGamma's daily SPX Call Wall and Put Wall, May 10, 2019 to May 28, 2024; frequencies of holds and breaches and forward returns after breaches.
- Findings (vendor claims): the Put Wall "held" in 89% of daily sessions (intraday low did not fall below it) and SPX closed above it in 93% of sessions; after a Put Wall breach, average forward returns were +14 bp (1 day), +7 bp (5 days) and +39 bp (10 days); after a Call Wall breach, -7 bp (1 day) and +5 bp (5 days).
- Limits: No base rate: a strike chosen well below spot would be "held" most days whatever its gamma; no comparison with arbitrary strikes at the same distance; forward returns of a few basis points with no standard errors; self-reported by the vendor.
- Use in the book: Chapters 8A, 10I, 11A: the only published statistics on walls found, and they do not test what they claim. A figure idea below shows the base-rate problem.

### DobrowolskiFlashAlpha2026
- Citation: Dobrowolski, T. (2026). "I Backtested My Own GEX Product Across 8 Years of SPY. Most of It Is Just VIX." DEV Community post, https://dev.to/tomasz_dobrowolski_35d32c/i-backtested-my-own-gex-product-across-8-years-of-spy-most-of-it-is-just-vix-a53 ; companion article "GEX Backtest: 8 Years of SPY Show Gamma Exposure Mostly Tracks ...", FlashAlpha, https://flashalpha.com/articles/gex-dex-vex-chex-8-year-backtest-spy-vix-control
- Type: practitioner (vendor) study; the author sells a dealer-exposure API (GEX, DEX, VEX, CHEX). A pre-registered self-test, not peer-reviewed.
- Verified via: the two URLs above (search summaries). Unverified: the exact date of the post (2026 per the sample end), and the GEX construction and sign convention.
- Question: Do GEX and its siblings (delta, vanna and charm exposure) predict next-day SPY realized volatility once the volatility regime is controlled for?
- Data and method: 1,972 SPY trading days, 2018-2026; pre-registered tests; rank correlations and top-minus-bottom sorts of next-day realized volatility on each exposure, raw and residualized on the VIX and at-the-money implied volatility.
- Findings: Raw GEX is strongly related to next-day realized volatility (rank correlation -0.36; top-minus-bottom difference -10.63 volatility points). After controlling for the VIX the difference shrinks to -3.15 points, and after the VIX plus ATM implied volatility to -0.99 points (p = 0.25), with the rank correlation falling to about -0.03. DEX, VEX and CHEX likewise add little after these controls.
- How to read it: high-GEX days are calm days mostly because GEX is high when implied volatility is low; once you already know implied volatility, GEX adds almost nothing about tomorrow's realized volatility.
- Limits: SPY rather than SPX; a vendor's own data; blog format.
- Use in the book: The clearest NEGATIVE result on the sign of GEX as a volatility predictor, supporting the Edge Book's low weight on GEX (Chapters 8B, 10H) and qualifying 8B's "regime" table: the regime information in GEX overlaps heavily with the VIX term structure that both sources already use.

### JonssonNyberg2025
- Citation: Jonsson, G. and T. Nyberg (2025). "Convexity in Motion: Leveraging Gamma Exposure to Predict Equity Market Returns and Improve Predictive Modeling." Master's thesis in Economics, Linköping University, Spring 2025. https://liu.diva-portal.org/smash/get/diva2:1972044/FULLTEXT01.pdf . Practitioner summary: Harbourfront Quant, "Gamma Exposure and S&P500 Return Predictability," https://harbourfrontquant.substack.com/p/gamma-exposure-and-s-and-p500-return
- Type: master's thesis (not peer-reviewed).
- Verified via: the two URLs above (search summaries). Unverified: sample years, the GEX source (the summary mentions SqueezeMetrics data), and coefficient sizes.
- Question: Do changes in aggregate SPX gamma exposure predict S&P 500 returns, and do they improve forecasts?
- Data and method: Daily aggregate GEX for S&P 500 index options; autoregressive distributed-lag models of returns on changes in GEX; out-of-sample Diebold-Mariano tests against a model without GEX and a random walk; sub-periods before and after 2020.
- Findings: Changes in GEX are significantly and positively associated with subsequent S&P 500 returns across horizons, robust before and after 2020 but weaker after; adding GEX significantly improves out-of-sample forecast accuracy against both benchmarks.
- Limits: Student thesis; convention-dependent vendor GEX; no control for implied volatility changes (compare DobrowolskiFlashAlpha2026); returns, not volatility or levels.
- Use in the book: The only academic-format test found of vendor GEX and index returns; weak evidence, to be cited with its status.

### CboeOptionIncome2024
- Citation: Cboe Global Markets (Xu, M., Volatility Insights) (2024). "Are Option Income Funds Suppressing Volatility?" Cboe Insights, https://www.cboe.com/insights/posts/are-option-income-funds-suppressing-volatility ; reprint on Seeking Alpha (article 4678140). Press coverage: Structured Retail Products, "Cboe: VIX downward trend not triggered by vol-selling strategies"; Reuters/Investing.com, "Analysis-Funds selling options help temper US stock swings" (the opposing view) [publication dates unverified; the note discusses 2023 data].
- Type: exchange research note (vendor/exchange material).
- Verified via: https://www.cboe.com/insights/posts/are-option-income-funds-suppressing-volatility ; https://seekingalpha.com/article/4678140-are-option-income-funds-suppressing-volatility ; https://www.structuredretailproducts.com/insights/79820/cboe-vix-downward-trend-not-triggered-by-vol-selling-strategies ; https://investing.com/news/economy/analysisfunds-selling-options-help-temper-us-stock-swings-3372419 (search summaries).
- Question: Has the growth of option-selling ("derivative income") funds suppressed equity volatility?
- Data and method: Fund assets; VIX levels; SPX skew and flow data.
- Findings: Assets in derivative-income funds grew about sixfold since 2019, from about $20 billion to over $120 billion; option-selling ETFs (about $65 billion) rival option-income mutual funds (about $65 billion). The VIX averaged 26 in 2022 and 17 in 2023. Cboe finds "no compelling evidence" that option-income ETFs or structured products are a primary cause of lower volatility, attributing it to the shift in the growth outlook from recession to soft landing; buying of upside calls for leverage, not call selling, dominated flows.
- Limits: Exchange material; no dealer-position data shown in the summary; conflicts with TodorovVilkov2024BIS (structured-product hedging as a damping channel) and with press accounts that call overwriting tempers swings.
- Use in the book: Documents the growth of customer option SELLING (a force that would leave dealers long gamma) for Chapters 8A and 9B, while showing that the exchange itself does not attribute low volatility to it. The sign question remains open.

### H. Further evidence on option flows, dealer hedging and the underlying

### LipsonTomioZhang2023
- Citation: Lipson, M. L., D. Tomio and J. Zhang (2023). "A Real Cost of Free Trades: Retail Option Trading Increases the Volatility of Underlying Securities." Working paper, SSRN abstract_id=4383463 (March 2023).
- Type: working paper (SSRN).
- Verified via: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4383463 ; https://www.wealthmanagement.com/equities/retail-options-trading-is-increasing-the-volatility-of-securities (press summary); https://www.darden.virginia.edu/sites/default/files/inline-files/CV-Lipson-February2025.pdf (author CV listing). Unverified: the size of the volatility increase and the sample period.
- Question: Did the arrival of commission-free retail option trading raise the volatility of the underlying stocks?
- Data and method: The fee shock when Robinhood introduced free options trading in January 2018 (discount-broker option fees had been $11-$28 per trade); stocks sorted by the increase in retail option trading; difference-in-differences on volatility, liquidity and price discovery.
- Findings: Retail option trading raises the volatility of underlying stocks. The channel is market makers' dynamic hedging of retail flow: retail trades are more likely to be intermediated by dealers and to involve higher-gamma contracts, for which dealer hedging in the underlying REINFORCES price moves (dealers short gamma to retail buyers). Liquidity of the underlying improves (quoted spreads 1.8% smaller in the top tercile of retail-option growth) and price discovery worsens.
- Limits: Working paper; single stocks; effect size not seen.
- Use in the book: Evidence for Chapter 8C/8D's single-stock mechanism (retail option buying leaves dealers short gamma, and their hedging amplifies moves), from a natural experiment rather than a convention. Contrast with the SPX evidence (DEV, Adams et al.), where dealers are on average long gamma.

### ChordiaKurovMuravyevSubrahmanyam2021
- Citation: Chordia, T., A. Kurov, D. Muravyev and A. Subrahmanyam (2021). "Index option trading activity and market returns." Management Science 67: 1758-1778 (online 2020). DOI 10.1287/mnsc.2019.3529. SSRN abstract_id=2798390.
- Type: peer-reviewed article.
- Verified via: https://consensus.app/papers/details/c6c3a9f0d1c55f608c8320caeb1e3dee/ (title, journal, DOI, abstract); https://pubsonline.informs.org/doi/abs/10.1287/mnsc.2019.3529 ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2798390 ; search summary giving all four authors and volume 67, pages 1758-1778.
- Question: Does order flow in index options carry information about the market?
- Data and method: Weekly index put and call order flow on the International Securities Exchange (ISE), which records the side and the opening or closing of customer trades; S&P 500 returns.
- Findings: Weekly index put order flow on the ISE positively and robustly predicts weekly S&P 500 returns, mainly through net put BUYING; stronger in high-VIX periods and after macroeconomic announcements. Of the explanations tested (sentiment, informed market makers, retail protection strategies), option-based risk protection by retail investors fits best.
- Limits: ISE is one venue among many; SPY and other ETF options rather than SPX [which products, unverified].
- Use in the book: Shows that customer index-put buying is measurable from ISE open/close data and is contrarian-positive for returns, a data source the rewrite could use when discussing "who holds what" for SPY-type products.

### KanneKornUhrigHomburg2023
- Citation: Kanne, S., O. Korn and M. Uhrig-Homburg (2023). "Stock illiquidity and option returns." Journal of Financial Markets 63 (March 2023): 100765. DOI 10.1016/j.finmar.2022.100765. SSRN abstract_id=2699529.
- Type: peer-reviewed article (working paper December 2020).
- Verified via: https://consensus.app/papers/details/6ffb2746b8e4594abf88014a080ac443/ (title, journal, DOI, abstract); https://www.sciencedirect.com/science/article/abs/pii/S1386418122000556 ; https://publikationen.bibliothek.kit.edu/1000148491/150552059 ; search summary giving the three authors and volume 63.
- Question: How does the underlying's illiquidity affect option returns?
- Data and method: Equity options; end-user net demand; simulation of market makers' hedging costs.
- Findings: Option returns can rise or fall with stock illiquidity depending on end-user net demand, which the authors explain by the hedging costs of market makers who are net LONG options on some underlyings and net SHORT on others.
- Limits: Option-return focus; not a study of underlying volatility.
- Use in the book: Direct support for 8A's point that the dealer's side differs across underlyings: no single sign convention fits every name.

### ChenEtAl2025SSE50
- Citation: Chen, H. et al. (2025). "Market maker or informed trader: Who drive the relationship between option trading and underlying returns? Evidence from Shanghai Stock Exchange 50 ETF options." Journal of Futures Markets [volume unverified]. DOI 10.1002/fut.70038.
- Type: peer-reviewed article.
- Verified via: https://consensus.app/papers/details/0d10503d53925c9f855be3706bce08fa/ (title, first author, journal, DOI, abstract).
- Question: In China's SSE 50 ETF options, is the link between option order flow and underlying returns due to market makers' hedging or informed trading?
- Data and method: Option order imbalance as a proxy for market makers' inventory pressure; event studies, out-of-sample tests, panel regressions across SSE-listed ETF options.
- Findings: Call (put) order imbalances move the underlying up (down) contemporaneously and then REVERSE quickly; the reversal stems from temporary price pressure from market makers' delta hedging, not information.
- Limits: Chinese ETF options; order-imbalance proxy for inventory.
- Use in the book: International evidence that dealer hedging moves the underlying temporarily and then reverses, the same price-pressure signature as NPPW and Baltussen et al.

### Bloomberg2020ShortVol
- Citation: Bloomberg News (2020). "Short Volatility Trade's Best Friend Is Now Its Biggest Enemy." March 23, 2020. https://www.bloomberg.com/news/articles/2020-03-23/short-volatility-trade-s-best-friend-is-now-its-biggest-enemy ; see also Bloomberg (2022), "Stock Market Chaos Revved Up by Options Dealers Rushing to Hedge," January 31, 2022, https://www.bloomberg.com/news/articles/2022-01-31/herky-jerky-stocks-lashed-by-gamma-hedging-in-thinning-liquidity
- Type: news report of practitioner (dealer-strategist) claims. Not a test.
- Verified via: the two Bloomberg URLs above (search summaries). Authors not seen [unverified].
- Question: What were dealers doing during the March 2020 sell-off?
- Data and method: Journalism quoting strategists and dealer estimates.
- Findings (claims): the coronavirus rout ignited demand for hedges and unwound option-selling strategies; dealers, "once a buffer to volatility, have morphed into short-term momentum traders, amplifying swings". The 2022 piece describes gamma hedging in thin liquidity lashing stocks.
- Limits: Claims without published data; estimates come from vendors and bank strategists using sign conventions.
- Use in the book: Documents that the "dealers flipped to short gamma in March 2020" story was contemporaneous practitioner narrative. No peer-reviewed estimate of SPX dealer gamma in March 2020 was found; Jackwerth2020 supports the direction (firms bought puts before the crash).


### Willeboordse2026
- Citation: Willeboordse, F. H. (2026). "Does gamma survive the close?" Finance Research Letters [volume unverified]: 110281. DOI 10.1016/j.frl.2026.110281.
- Type: peer-reviewed article (short letter).
- Verified via: https://consensus.app/papers/details/e898787a6205536da8612750954bc698/ (title, author, journal, DOI, abstract); https://www.sciencedirect.com/science/article/pii/S1544612326008093 .
- Question: Does Black-Scholes gamma identify the convexity actually realized in option returns?
- Data and method: 182 million intraday trade pairs and 0.16-2.6 million daily pairs per symbol across five underlyings, 2020-2025; correlation between empirical and theoretical gamma at intraday and daily horizons; regressions without model Greeks.
- Findings: The correlation between empirical and Black-Scholes gamma does not improve from intraday to daily horizons; at the daily horizon it turns significantly NEGATIVE (-0.25 to -0.47 across symbols), more so as vega exposure grows relative to gamma exposure, consistent with vega contamination through the negative co-movement of spot and implied volatility (the leverage effect).
- Limits: Five underlyings (not named in the abstract); about option P&L convexity, not dealer hedge flows.
- Use in the book: Supports 8A's limit 4 (Black-Scholes gamma is a poor measure under skew) with a different mechanism: over a day, spot-volatility co-movement (vanna) swamps the gamma term, so GEX built from Black-Scholes gamma mismeasures the hedge that dealers actually need.

## Corrections to the book

Each item gives the book's claim, what the sources show, and the source keys above. Market-data facts verified only for this section carry their URLs here.

### Chapter 8A (and 9C, 11B, 13B where the same citations recur)
1. **NPP 2005, "16.5 basis points on expiry days", converted to "about 10 points of SPX at 6,000" (8A limit 5; 9C).** The 16.5 bp is a lower-bound estimate of the average return distortion of optionable SINGLE STOCKS per expiration date, 1996-2002, with about $9 billion of market capitalization shifted; the paper does not study the index. Index-level pinning is GolezJackwerth2012 (S&P 500 futures pulled to the at-the-money strike at CME serial expirations, pushed away before SPX expirations; at least $115 million of notional per expiration day). Replace the SPX-points conversion. [NiPearsonPoteshman2005, GolezJackwerth2012]
2. **Barbon and Buraschi "around 16 bps per standard deviation" (8A limit 5).** Not found in any version. The figures found: one SD of gamma imbalance goes with a DECREASE of about 12 bp in the absolute daily return of a stock (average absolute return about 109 bp) in one version; 5 to 25 bp for stocks (average 180 bp) in another; more than 20 bp for the indexes tested. Units: basis points of absolute daily return (a volatility proxy) per one-SD change in dealer gamma imbalance. [BarbonBuraschi2021]
3. **Dim, Eraker and Vilkov (2024) "a working paper from George Washington University".** It is an SSRN working paper (abstract_id 4692190) first posted November 17, 2023; institutional attribution not supported by the sources checked. The quoted finding matches the abstract. [DimErakerVilkov2023]
4. **Adams et al. (2025) "posted December 3, 2025".** Search results give an SSRN date of October 17, 2025; check the SSRN page (written versus posted date). Quotation matches the abstract. [AdamsDimEtAl2025]
5. **"In 0DTE options, retail and small institutional accounts overwhelmingly sell premium ... with the dealers buying from them" (8A, 9B).** Contradicted or contested: customers' 0DTE buys and sells are about balanced (14.95% against 14.06% of SPX/SPXW volume, January 2020 to June 2023); Cboe calls customer 0DTE activity "very balanced"; the auction-identified retail slice was a net BUYER of 0DTE options and market makers held a growing net SHORT 0DTE position. The dealers' positive average gamma found by DEV and Adams et al. comes mainly from longer-dated positions rolling into expiry. [VasquezAmayaPearsonGarciaAres2025, CboeXu2023, BeckmeyerBrangerGayda2023, AdamsFontaineOrnthanalai2024]
6. **The "0DTE-era convention" (dealers long puts, short calls) as the likely SPX position.** Position data for all SPX options, 2011-2023, show dealers persistently net SHORT puts (about 19 million contracts, mostly deep OTM) with calls near zero, the put side of the JPM-era convention; earlier data (1991-2012) agree. A positive average dealer gamma near the money can coexist with a large short deep-OTM put book whose gamma grows in a crash. Neither per-type convention is right for SPX. [Terstegge2025, ChenJoslinNi2019, GarleanuPedersenPoteshman2009, ConstantinidesLian2021]
7. **"A Cboe study from 2025 estimated 0DTE market-maker gamma hedging at only about 0.2% of SPX daily liquidity" (8A, 8B, 9B, 9C and the Edge Book in 1G, 6A, 10A, 10H, 10I, 11A, 11D, 11K, 13B, 13F).** The Cboe figure found is 0.04% to 0.17% of S&P 500 FUTURES liquidity (about $400 billion a day), from Cboe's 2023 note (Mandy Xu, about September 2023). "0.2%" rounds the upper end; "2025" and "SPX daily liquidity" are not supported. [CboeXu2023]
8. **SqueezeMetrics "published its method in 2017".** The white paper first used the term publicly in March 2016 and was revised in 2017 (search summary). Minor. [SqueezeMetrics2017]
9. **Missing limit.** Add to the five limits: market makers often manage option risk by turning over inventory within minutes rather than delta hedging, so open-interest gamma overstates hedge flow. [HuKirilovaMuravyevRyu2023]

### Chapter 8B
10. **Ni, Pearson, Poteshman and White (2021): "alters the probability of large daily moves, over 300 bps, by 5% to 14% historically, rising to 13% to 40%".** Not found. Verified figures: 9.5% (1990-2001) and 13.4% (2002-2012) of optioned stocks' daily absolute returns are attributable to hedge rebalancing; a one-SD shock to hedgers' gamma goes with a 28.8 bp (29.6 bp) change in absolute daily return. Full citation: Review of Financial Studies 34(4): 1952-1986 (2021). [NiPearsonPoteshmanWhite2021]
11. **Barbon and Buraschi's illiquidity result "suggests that SPX itself ... has smaller gamma-feedback effects".** Not supported by the numbers seen: the index estimate (more than 20 bp per SD) is not smaller than the single-stock range (5-25 bp). [BarbonBuraschi2021]
12. **Adams et al. "establish causally".** The evidence is a natural experiment (days with and without 0DTE expirations, the 2022 Tuesday/Thursday additions), reported as a "robust negative relation"; quote the effect size from the precursor: index volatility 60-90 annualized bp lower on days with 0DTE trading. [AdamsDimEtAl2025, AdamsFontaineOrnthanalai2024]
13. **Regime claims.** A pre-registered vendor test finds raw GEX strongly related to next-day realized volatility (rank correlation -0.36) but almost none of it survives controls for the VIX and ATM implied volatility (-0.03; residual top-minus-bottom -0.99 vol points, p = 0.25). The regime table should say the GEX sign overlaps heavily with the volatility regime already in the VIX. [DobrowolskiFlashAlpha2026]

### Chapter 8C
14. **Volmageddon: "9:30 AM, open ... VIX at 17.31".** The VIX opened at 18.44 on February 5, 2018 and closed at 37.32. [AugustinChengVandenBergen2021]
15. **"Inverse-VIX ETPs, XIV ... and SVXY ... a combined approximately $3.5 billion" and "XIV ... AUM went from $1.9 billion".** The BIS gives about $4 billion for select leveraged AND inverse volatility ETPs at end-2017 and an 84% fall in XIV; Augustin et al. give a one-day loss of more than 90% in short-volatility ETPs. The $3.5 billion and $1.9 billion figures were not found [unverified]. [SushkoTurner2018BIS, AugustinChengVandenBergen2021]
16. **Volmageddon mechanism: "dealers short VIX call wings ... in FLEX", "vanna ... across SPX puts".** Not in the BIS, FAJ, Review of Finance or JBF sources, which attribute the amplification to leveraged/inverse VIX-ETP rebalancing in VIX futures and find its spillover to SPX futures is not explained by SPX or VIX option market makers' hedging. Label as the Dealer Mechanics Lab's interpretation. [SushkoTurner2018BIS, Todorov2023, BangsgaardKokholm2025]
17. **March 16, 2020: "The VIX printed 82.69, its all-time intraday high."** 82.69 was the record CLOSE (March 16, 2020); the March 2020 intraday high was 85.47 (March 18), and the all-time intraday high is 89.53 (October 24, 2008). Sources: https://www.bloomberg.com/news/articles/2020-03-16/stock-market-volatility-tops-financial-crisis-with-vix-at-record ; https://www.macroption.com/vix-all-time-high/ .
18. **March 16, 2020: "intraday it traded as low as 2,280, down approximately 12% from the prior close".** The about-12% (11.98%) fall was the close-to-close change (https://www.cnbc.com/2025/04/06/sp-500-circuit-breaker-on-tariff-worries-what-that-means.html ; https://www.bloomberg.com/news/articles/2020-03-16/stock-market-volatility-tops-financial-crisis-with-vix-at-record); a 2,280 intraday low was not found [unverified] and would be a much larger fall than 12%.
19. **August 5, 2024: "The VIX printed above 65 intraday, the third-highest reading in its history" and "SPX dealer gamma was short going into the event".** The print was PRE-MARKET (VIX from 23.9 to over 65 while VIX futures stayed below 35), driven by asymmetric widening of bid-ask spreads in thin pre-market trading, with OTM puts accounting for over 85% of the spike; the BIS found that "VIX ETFs, market makers' option hedging, and dispersion trades do not seem to have contributed meaningfully". No source for short dealer gamma was found. [TodorovVilkov2024BISBulletin95, LiAskanaziSEC2025]
20. **GME as "the canonical single-name gamma squeeze" with dealers short calls from retail call buying.** SEC staff found option volume growth was driven mostly by PUT buying and that market makers were BUYING, not writing, calls: "not consistent with a gamma squeeze". An academic committee (with a GEX-vendor co-author) argues both short and gamma squeezes may have contributed. Present as disputed. [SECStaffReport2021, MittsEtAl2022]
21. **GME: "Short interest was approximately 140% of the float".** Press figures of about 140% circulate for early January; the SEC-report figure seen is a January peak of about 123% [SECStaffReport2021; exact figure unverified].
22. **GME: "GME closed on January 28 down 44% from its intraday high."** It closed at $193.60, down 44.3% from the PREVIOUS CLOSE; against the $483 intraday high (not verified here) that close is about 60% lower. Source: a search summary drawing on the House Financial Services Committee staff memorandum and related results (https://financialservices.house.gov/uploadedfiles/memorandum_for_fsc-rs_re_meme_stock_event_final.pdf); the specific page stating $193.60 and 44.3% was not identified.
23. **Robinhood's deposits "from about $700 million to more than $3 billion".** Consistent with the House Financial Services Committee staff memorandum: NSCC's automated notice on January 28, 2021 asked for about $3.7 billion, including a VaR-based charge of nearly $1.3 billion (up from $696 million) and an excess capital premium charge over $2.2 billion; reduced to $1.4 billion later that morning. Same House FSC URL; Tenev's testimony is summarized at https://www.crowdfundinsider.com/2021/02/172361-gamestop-robinhood-testimony-out-as-house-committee-on-financial-services-preps-for-first-of-three-hearings/ .

### Chapter 9B (and 9C)
24. **Cboe "Much Ado About 0DTEs": "median of about +$173 million per percentage point ... 25th to 75th percentile ... −$1.1 billion to +$2.4 billion".** The +$173 million is the median AT 3:30 PM, with a "typical range" of -$1.1 billion to [about +$2.4 billion, unverified]; the all-day average range is $170-$670 million, which is where Cboe's own "0.04% to 0.17% of futures liquidity" comes from (answering the notes' question). [CboeXu2023]
25. **Brogaard, Han and Won (2024) "independently confirmed that the introduction of 0DTE did not increase market volatility ... event-study ... Tuesday and Thursday SPXW".** The opposite: they report that a one-SD increase in 0DTE trading raises volatility by 9.10% of its mean, driven mainly by speculative retail investors, identified with the staggered introduction of index weekly options as an instrument. Also "University of Utah working paper" is unverified; it is SSRN abstract_id 4426358 (April 2023; earlier title "How Does Zero-Day-To-Expiry Options Trading Affect the Volatility of Underlying Assets?"). [BrogaardHanWon2023]
26. **"The academic consensus ... is that 0DTE has stabilized rather than destabilized SPX".** The literature is split: position-based SPX studies find damping on average (DEV, Adams et al., Vasquez et al.'s upper bound of +3.3 points of daily volatility); a volume-based IV study finds amplification (Brogaard et al.); single-stock weeklies raised volatility (Ellahie et al.). [DimErakerVilkov2023, AdamsFontaineOrnthanalai2024, AdamsDimEtAl2025, VasquezAmayaPearsonGarciaAres2025, BrogaardHanWon2023, EllahieEtAl2025]
27. **"Tuesday and Thursday SPXW expirations were not available for trading until April 26 and May 19, 2022."** They were LISTED from April 18 and May 11, 2022; April 26 and May 19 were the first expiration days. Sources: https://ir.cboe.com/news/news-details/2022/Cboe-to-Add-Tuesday-and-Thursday-Expirations-for-SPX-Weeklys-Options-04-13-2022/default.aspx ; https://cdn.cboe.com/resources/product_update/2022/Cboe-Options-Exchanges-to-List-Tuesday-and-Thursday-Expiring-Weekly-Options-on-SPX-option-symbol-SPXW_OW-003-.pdf .
28. **"Retail 0DTE flow is mostly premium selling ... This is what keeps dealers net long gamma in 0DTE on most days."** See item 5. The Cboe retail share (about 50-60%; 53% in August 2025) is Cboe's own estimate; an auction-based academic identification gives about 6%. [CboeRetailShare2025, BeckmeyerBrangerGayda2023]
29. **April 2025 and October 10, 2025: "dealer gamma in 0DTE was likely net short, because retail was buying directional protection".** No source found; Cboe reports only that the retail share of 0DTE fell to 47% in the early-April spike. [CboeRetailShare2025]

### Chapters 2C and 6C (Baltussen et al.)
30. **2C: "the first half-hour's return predicts the last half-hour's return ... across more than 60 futures".** Two papers merged: the first-half-hour predictor is Gao, Han, Li and Zhou (2018, SPY 1993-2013); Baltussen et al. use the rest-of-day return (previous close to 30 minutes before the close) across 60+ futures, 1974-2020. [GaoHanLiZhou2018, BaltussenDaLammersMartens2021]
31. **6C: "Sharpe ratios in the 0.5 to 1.0 range" and "the morning return's predictive power".** Search summaries give annualized Sharpe ratios of about 0.87 to 1.73 at the asset-class level (unverified against the tables), and the predictor is the rest-of-day return. The S&P 500 gamma measure (NGE) ASSUMES dealers long calls and short puts; by it, NGE was negative on about 2,930 of 6,088 days, 1996 to May 2020. [BaltussenDaLammersMartens2021]
32. **6C/9B: the last 30 minutes as a mechanical hedging window.** Qualify: in the cross-section of stocks the last 30 minutes show a REVERSAL that the same authors find is not explained by gamma hedging, and LETF rebalancing effects have shrunk as liquidity providers anticipate them. [BaltussenDaSoebhag2024, BarbonBeckmeyerBuraschiMoerke2022, IvanovLenkey2018]

### Citations the book gets right
- Garleanu, Pedersen and Poteshman (2009), RFS 22(10): 4259-4299. [GarleanuPedersenPoteshman2009]
- Baltussen, Da, Lammers and Martens (2021), JFE 142(1): 377-403, and the quotation "Hedging short gamma exposure requires trading in the direction of price movements, thereby creating price momentum." [BaltussenDaLammersMartens2021]
- The BIS quotation on 115,862 VIX futures contracts at 16:08 (9A, 8C). [SushkoTurner2018BIS]
- The Dim, Eraker and Vilkov and Adams et al. quotations, which match the abstracts. [DimErakerVilkov2023, AdamsDimEtAl2025]
- Barbon and Buraschi's SSRN number (3725454) and revision date (March 18, 2021). [BarbonBuraschi2021]
- 0DTE volume shares (62% record in August 2025; retail about half by Cboe's estimate). [CboeRetailShare2025]


## Synthesis

### What the literature agrees on
1. **The direction of the effect.** Where dealers (or hedgers) are long gamma, the underlying is calmer and mean-reverting; where they are short gamma, it is more volatile and trends. This holds for single stocks (NiPearsonPoteshmanWhite2021, BarbonBuraschi2021, Soebhag2023, BeckmeyerMoerke2021, LipsonTomioZhang2023), the index intraday (BaltussenDaLammersMartens2021, ParkZhao2024), SPX 0DTE (DimErakerVilkov2023, AdamsFontaineOrnthanalai2024), FX (AndereggUlmannSornette2022), Chinese ETF options (ChenEtAl2025SSE50) and simulations (BuisEtAl2024). No study found reverses the sign of the mechanism.
2. **The effect is price pressure, not information.** It reverts: at the next open (BarbonBeckmeyerBuraschiMoerke2022), over following days (BaltussenDaLammersMartens2021), quickly in China (ChenEtAl2025SSE50); expiration-day exercise effects reverse too (Chiang2014). Authors repeatedly rule out information-based explanations.
3. **Typical-day magnitudes are modest.** About a tenth of single stocks' absolute daily moves (9.5% and 13.4%, NPPW); 12 to 30 bp of absolute daily return per SD of dealer gamma (Barbon-Buraschi, NPPW); 60 to 90 annualized bp lower SPX volatility on 0DTE days (Adams-Fontaine-Ornthanalai); at most a few points of annualized volatility even in the worst case (+3.3 points daily, +6.4 at 30 minutes, Vasquez et al.); under a point of FX volatility (Anderegg et al.); 0.04% to 0.17% of futures liquidity for 0DTE hedging (Cboe).
4. **Pinning exists but is small, and needs dealers long the options at the strike.** Single stocks (NPP 2005), index futures (Golez-Jackwerth), theory (Avellaneda-Lipkin; Jeannin et al.); it weakens as expirations multiply (Zhang et al.) and has a manipulation component (NPP 2005; Figueiredo et al.).
5. **Before the 0DTE era, end users were net long SPX puts and dealers net short them.** GPP 1996-2001, Chen-Joslin-Ni 1991-2012, Constantinides-Lian, and Terstegge 2011-2023 (about 19 million contracts short, calls flat). Dealers' willingness to stay short shrinks exactly when constraints bind (Chen-Joslin-Ni; Constantinides-Lian).
6. **In the index stress episodes, rule-based product rebalancing did the documented damage.** Volmageddon ran through leveraged and inverse VIX products (SushkoTurner2018BIS, AugustinChengVandenBergen2021, Todorov2023, BangsgaardKokholm2025); the August 2024 VIX spike was a quote artifact with no meaningful role for market-maker hedging (TodorovVilkov2024BISBulletin95, LiAskanaziSEC2025).

### Where it disagrees
1. **0DTE: damping or amplifying?** Position-based SPX studies find damping on average (DEV; Adams et al.; Vasquez et al.'s bound; Cboe). A volume-based instrumental-variables study finds amplification (BrogaardHanWon2023: +9.10% of mean volatility per SD of 0DTE trading). Short-dated single-stock options raised volatility (EllahieEtAl2025; LipsonTomioZhang2023 for retail options generally). The split tracks the method (positions against volume) and the market (SPX against single stocks).
2. **Who is on the other side of 0DTE.** The book and practitioner narrative say retail sells premium; the auction-identified retail slice was a net buyer, leaving dealers net short (BeckmeyerBrangerGayda2023); customer buys and sells are roughly balanced (Vasquez et al.; Cboe). Adams et al. locate the dealers' long gamma in longer-dated positions rolling into expiry, which reconciles part of this.
3. **Sign conventions.** Terstegge2025 (dealers short puts, flat calls, by contracts) against the "0DTE-era" convention (dealers long puts, short calls); DEV's positive average gamma is not a statement about contract counts by type. Kanne et al. show the dealer's side differs across underlyings.
4. **End of day.** Index intraday momentum tied to short gamma (Baltussen et al.) and gamma-signed momentum or reversal in stocks (Beckmeyer-Moerke; BBBM) against a cross-sectional end-of-day reversal that gamma hedging does not explain (BaltussenDaSoebhag2024).
5. **Leveraged ETFs.** Amplification (Cheng-Madhavan; Shum et al.; Zhao2026 in Korea) against economically insignificant once investor flows are counted (IvanovLenkey2018; Lenkey2024). BBBM finds LETF effects larger than option effects but shrinking over time.
6. **GameStop.** SEC staff: not consistent with a gamma squeeze (market makers bought calls; volume was put-driven). Academic committee: a gamma squeeze may have contributed.
7. **Does GEX add anything to the VIX?** The vendor white paper says GEX separates calm states the VIX does not (SqueezeMetrics2017); a vendor's pre-registered self-test finds almost nothing left after VIX and ATM implied volatility (DobrowolskiFlashAlpha2026); a master's thesis finds changes in GEX help forecast returns (JonssonNyberg2025).
8. **Do dealers even delta hedge as assumed?** Hu et al. find market makers mostly offload inventory within minutes and only a minority delta hedge consistently.
9. **What suppressed volatility in 2023-2024.** Dealers hedging structured products (TodorovVilkov2024BIS) against the macro outlook, with option-income funds not a primary cause (CboeOptionIncome2024).

### What is untested or only claimed
- **Gamma flip, call wall and put wall as levels.** No academic test found. The only statistics (SpotGammaKeyLevels2024) are self-reported and lack a base rate.
- **The sign of vendor GEX on a given day.** Every vendor number found rests on a sign convention; the position studies that avoid conventions (DEV, Adams et al., Vasquez et al., Terstegge) do not publish daily series comparable to vendor GEX.
- **The feedback formula sigma/(1 - kappa G) of Chapter 8B.** Not estimated anywhere; the nearest empirical analogues are Anderegg et al.'s FX estimate and Vasquez et al.'s counterfactual bound, both small.
- **SPX OPEX-week and 0DTE-era index pinning.** Evidence exists for single stocks (Stivers-Sun; NPP) and for S&P 500 futures before 2010 (Golez-Jackwerth); no study of SPX strike pinning in the 0DTE era was found.
- **Dealer gamma in March 2020 and August 2024.** No peer-reviewed estimate; the March 2020 story is contemporaneous practitioner narrative (Bloomberg2020ShortVol), and the BIS found no hedging role in the August 2024 VIX spike.
- **Dealer gamma and flash crashes.** Only Barbon-Buraschi's reported correlation with flash-crash frequency and size; nothing for May 2010 or August 2015.
- **Vanna and charm flows (for example "OPEX vanna rallies").** No academic test found in this search.
- **FLEX and OTC books' size and hedging effects.** The BIS box proposes structured-product hedging as a damping force; not measured.
- **The GME gamma squeeze and single-name squeezes generally.** Disputed for GME; BaigZaynutdinovaStrong2025 counts 669 candidate events (2019-2023) but its findings were not verified.

### Numbers worth quoting (with source keys)
| Number | What it measures | Key |
|---|---|---|
| at least 16.5 bp; about $9 billion | average return distortion of optionable single stocks per expiration date, 1996-2002; market-cap shift | NiPearsonPoteshman2005 |
| at least $115 million | notional S&P 500 futures value shifted per serial-option expiration day | GolezJackwerth2012 |
| 9.5% and 13.4% | share of single stocks' daily absolute returns due to hedge rebalancing (1990-2001; 2002-2012) | NiPearsonPoteshmanWhite2021 |
| 28.8 bp and 29.6 bp | change in absolute daily return per SD shock to hedgers' gamma | NiPearsonPoteshmanWhite2021 |
| about 12 bp per SD (average 109 bp); over 20 bp for indexes | fall in absolute daily return per SD of dealer gamma imbalance | BarbonBuraschi2021 |
| 18 bp per 1 pp move | last-half-hour momentum or reversal in stocks, sign set by dealer gamma | BeckmeyerMoerke2021 |
| 60-90 annualized bp | lower SPX volatility on days with 0DTE trading | AdamsFontaineOrnthanalai2024 |
| +3.3 and +6.4 points | MAXIMUM rise in annualized daily and 30-minute volatility from market-maker 0DTE gamma | VasquezAmayaPearsonGarciaAres2025 |
| $170-$670 million; 0.04%-0.17% | average market-maker 0DTE gamma through the day; share of about $400 billion daily S&P futures liquidity | CboeXu2023 |
| +$173 million | median market-maker 0DTE gamma at 3:30 PM | CboeXu2023 |
| 14.95% against 14.06% | customer 0DTE buys and sells to market makers as shares of SPX/SPXW volume | VasquezAmayaPearsonGarciaAres2025 |
| +9.10% of mean volatility | effect of a one-SD rise in 0DTE trading | BrogaardHanWon2023 |
| over 75%; $241,000 and $350,000 a day | retail SPX trades that are 0DTE; average daily retail losses (Feb 2021-Sep 2023; after May 2022) | BeckmeyerBrangerGayda2023 |
| about 19 million contracts | dealers' persistent net short SPX put position, 2011-2023 | Terstegge2025 |
| about 200% | dealers' option-inventory loss from a 10% S&P 500 fall without re-hedging | Terstegge2025 |
| 2,930 of 6,088 days | days with negative S&P 500 NGE under the long-calls/short-puts assumption, 1996-May 2020 | BaltussenDaLammersMartens2021 |
| 0.7 and 0.9 points | rise in EURUSD and USDJPY volatility from observed dealer short gamma | AndereggUlmannSornette2022 |
| 10% a year | underperformance of high- against low-net-gamma stocks | Soebhag2023 |
| -0.36 to -0.03 | rank correlation of GEX with next-day SPY realized volatility, raw and after VIX and ATM IV | DobrowolskiFlashAlpha2026 |
| 89% and 93% | SpotGamma put wall "held" intraday and at the close, 2019-2024 (no base rate) | SpotGammaKeyLevels2024 |
| 18.44 to 37.32; 115,862 contracts in one minute; XIV -84% | Volmageddon VIX open and close; VIX futures volume at 16:08; XIV loss | AugustinChengVandenBergen2021, SushkoTurner2018BIS |
| 23.9 to over 65, futures below 35; over 85% from OTM puts; volume 80x lower | the August 5, 2024 pre-market VIX print | LiAskanaziSEC2025, TodorovVilkov2024BISBulletin95 |
| 82.69 close; 85.47 intraday | VIX record close (March 16, 2020) and March 2020 intraday high (March 18) | Corrections item 17 |
| 32x | S&P 500 option volume relative to net position changes (inventory turnover) | HuKirilovaMuravyevRyu2023 |
| $20 billion to over $120 billion | derivative-income fund assets, 2019 to 2023/24 | CboeOptionIncome2024 |
| 100.0% to 136.7% | SK Hynix annualized volatility with and without leveraged-ETF rebalance predation, 2026 | Zhao2026 |

### Figure ideas (interactive)
1. **Forest plot in common units.** Each study is a row with its effect converted to one unit the reader chooses: "points of annualized volatility" or "bp of absolute daily return per SD of dealer gamma", with the original unit shown beside it. Toggles filter by market (single stocks, SPX, FX), by how the dealer side was identified (observed positions against assumed convention) and by era (before and after 2022). It shows the modest size of typical-day effects, and that the 0DTE disagreement lines up with method.
2. **The base rate for a "wall".** The reader sets how far below spot a level sits (in percent), implied volatility and the horizon; the figure shows the probability that SPX's intraday low stays above ANY level at that distance, from a simple return model, beside SpotGamma's reported 89% for put walls. It shows why a hold rate means nothing without a baseline.
3. **What GEX knows that the VIX already knows.** A stylized scatter of next-day realized volatility against GEX, colored by VIX, built to reproduce the reported statistics (rank correlation -0.36 raw). Checkboxes add the VIX and ATM implied volatility as controls and the scatter re-plots residuals, with the correlation falling toward -0.03 and the top-minus-bottom spread from about 10.6 to about 1 vol point. Labeled illustrative, with the source numbers.
4. **Contracts against gamma.** A dealer book by moneyness: short about 19 million deep-OTM puts, near-zero calls, and a near-the-money block the reader sets long or short. A spot slider moves the index down; bars show net gamma by strike and the total. It shows how "dealers net short puts" and "dealers long gamma on average" can both be true, and how the total flips negative in a sell-off.
5. **The 0DTE natural experiment.** A weekday calendar before and after April-May 2022 (listing dates April 18 and May 11; first expiries April 26 and May 19), above bars for volatility on days with and without an expiring contract, sized by the 60-90 annualized bp reported. A toggle switches between the damping studies and Brogaard et al.'s +9.10%, each with its identification written out.
6. **Pinning and anti-pinning.** A histogram of closes relative to the nearest heavy strike on expiration days against other days. The reader sets the dealers' position at the strike (long or short) and the hours left; long gamma piles mass at the strike and short gamma empties it, and a switch adds Golez-Jackwerth's anti-cross-pinning before SPX expirations.
7. **Anatomy of a VIX print.** August 5, 2024, pre-market to close: VIX index, front VIX future and the bid-ask spread of OTM SPX puts. The reader widens or narrows the put spreads and watches the mid-quote VIX move with no change in traded prices. It shows a stress statistic that measured quotes, not hedging.
8. **Rebalance with and without investor flows.** Bars for a leveraged ETF's closing trade L(L-1)xA beside option-dealer hedging for a given move; a slider for contrarian investor flows (money entering the fund after losses) shrinks the ETF trade toward zero, as in Ivanov-Lenkey. It shows why the mechanical formula overstates actual flow.

