# Section 2 · Quant Trading
*How edges get built and executed.*

Quantitative trading, distilled to one sentence: **create a statistical edge and execute it to produce risk-adjusted returns**. Both halves matter equally. A great model with poor execution makes no money. Great execution without a model is just clean losses. The quant trading industry is divided into firms that excel at the first half (the alpha researchers) and firms that excel at the second half (the execution engines like Jane Street, Citadel Securities, Tower Research) — and the most profitable firms in the world are those that have built unified pipelines from research to execution with minimal slippage between them.

This section walks through the five components in order: the model (2A), the simplest interesting model class (2B), how the model is fit (2C), how the resulting predictions are executed (2D), and how the position is sized and traded at appropriate frequency (2E). The treatment is deliberately introductory — entire books exist on each of these topics. The goal here is to give you enough mechanics to read the dealer chapters that follow without confusion.

---

## 2A · The model: regression vs classification

A **model** is a mathematical object that takes inputs and produces an output prediction. In trading, inputs are typically a vector of features observed at time t — past prices, volumes, technical indicators, macro variables, news sentiment scores — and the output is some quantity at time t+h, where h is the prediction horizon. Two basic flavors of model dominate the literature.

### Regression models predict a real number

A regression model predicts a continuous quantity. Examples in trading:

- **Predict the next bar's return.** Output: log return over the next minute, hour, or day.
- **Predict the price h minutes from now.** Output: a price level.
- **Predict realized volatility over the next 30 days.** Output: a non-negative number, often log-transformed to make it more Gaussian-shaped.
- **Predict the cost to execute a 1,000-share buy in the next 30 seconds.** Output: implementation shortfall in basis points.

The output of a regression model is, in principle, unbounded — though in practice it's bounded by what's physically possible (a single-day return less than −100% is impossible because you can't lose more than you have).

### Classification models predict a category

A classification model predicts which of a finite set of categories the next observation will fall into, often with an associated probability:

- **Predict next bar direction.** Output: probability of "up" vs "down."
- **Predict next event type.** Output: probabilities over {breakout, mean-reversion, range-bound}.
- **Predict whether a position will be a winner.** Output: probability of profit, given current setup and execution path.

Classification is useful when you only care about direction rather than magnitude. It's also useful when the underlying signal is structurally bounded (a tick can only go up or down — or stay flat, in a three-class formulation). And it's useful when you want to feed the output to a downstream sizing function — many sizing rules in 2E take a probability or signed signal in [−1, +1] as their input.

### Features and targets

A model is fit on training data consisting of (feature, target) pairs:

- **Features (x):** the inputs available at time t, before the future is revealed. Typically a vector — past returns, indicator values, volume, etc.
- **Target (y):** the quantity to be predicted at time t+h. For regression, a number. For classification, a label.

A core principle of model-building: **the feature must be available at the time of prediction**. If your feature set includes "tomorrow's open price" while trying to predict "tomorrow's close," you have lookahead bias and your backtest is meaningless. This sounds obvious; in practice, lookahead bias is the most common backtest error in retail strategy development. Every joined dataset must be checked for it. Every indicator that uses smoothing or filtering must be verified to use only past data. Every macro variable must be lagged to reflect publication timing.

### Univariate vs multivariate models

The simplest possible model is univariate — one feature, one target. The next-simplest is multivariate — many features, one target. The most complex is multi-target — many features, many targets simultaneously.

Univariate models are easy to interpret, easy to debug, and surprisingly competitive. The AR(1) model in 2B is univariate. A linear regression of next-bar return on past-bar return has two parameters (slope and intercept) and is often hard to beat for short-horizon prediction.

Multivariate models can capture interactions between features but pay a price in interpretability and overfitting risk. With more features than you have independent observations, even a linear regression can fit noise perfectly. The danger compounds when the features themselves are correlated.

### The Occam tax

There is a strong empirical prior in quant trading that **simpler is better**. This is not just folklore; it has explicit statistical foundations.

**Bias-variance tradeoff.** Every estimator has two sources of error: bias (consistently wrong in some direction) and variance (noisy estimate due to finite sample). Complex models reduce bias but increase variance. Simple models do the opposite. In finance, where signal-to-noise ratios are very low and sample sizes are effectively bounded by historical data length, the optimal point on the bias-variance tradeoff tends to favor simple models.

**Overfitting.** Given enough parameters, any model will fit any in-sample data perfectly — including the noise. The model "learns" patterns that don't exist in the underlying data-generating process. In financial time series, where the signal-to-noise ratio is roughly 1:100 to 1:1000 on short horizons, overfitting is the default outcome, not the exception. A neural network with 10,000 parameters trained on 5 years of daily data (1,260 observations) is *extremely* prone to overfit in the absence of regularization, dropout, early stopping, or other complexity-control mechanisms; with aggressive regularization and large auxiliary datasets it is possible to fit such a model usefully, but the burden of proof — that the fit reflects signal rather than noise — sits firmly on the modeler.

**The "no free lunch" theorem.** Wolpert and Macready (1997) proved that, averaged over all possible problems, no single algorithm outperforms any other. In specific problem domains, some algorithms work better than others — but you need strong prior knowledge to choose. In finance, that prior knowledge is hard to come by, so robust simple methods tend to outperform exotic complex ones once you account for transaction costs and out-of-sample degradation.

**López de Prado's principle (from "Advances in Financial Machine Learning," 2018).** Most published trading strategies are statistical artifacts. The probability that a backtested Sharpe ratio survives to live deployment is roughly inverse in the number of trials conducted to find it. If you tested 100 strategies and the best one has Sharpe 1.5, the deflated Sharpe (correcting for multiple testing) is probably indistinguishable from zero.

**Linear models are competitive baselines.** Univariate auto-regressive models — predicting the next value from the last one, with a single weight and bias — often outperform deep neural networks on noisy financial data, because the deep network finds patterns that don't generalize. This is the central empirical finding of three decades of academic finance: the linear baseline is hard to beat once you control for overfitting and transaction costs.

> *"Neural networks are a Ferrari. Powerful, but easy to crash. On financial time series, they overfit unless very carefully managed. Start with linear regression. Earn the right to add complexity."*

Earning the right to add complexity means: show that the simpler model leaves systematic residuals (deviations from prediction) that the more complex model can capture; verify that the improvement survives walk-forward cross-validation on data the more complex model never saw; account for the additional degrees of freedom in your performance evaluation; and stress-test that the more complex model is robust to feature noise. Most retail "ML for trading" content skips every one of these steps.

### Where the model fits in the pipeline

The model is one half of the trading system. The other half is the **strategy** — the execution layer that turns predictions into orders. A perfect predictor with no execution policy is useless because you don't know how big to trade, when to enter, when to exit, or how to handle the case where your model contradicts your existing position.

```
Model     →  produces edge (a prediction with positive E[outcome])
Strategy  →  executes edge (turns predictions into sized orders with entry/exit rules)
```

In card-counting blackjack, the counting system is the model — it produces an estimate of the deck's remaining favorable cards. The betting strategy is everything else — bet sizing as a function of count, table choice, session length, when to walk away. A perfect counter who bets the same amount on every hand loses. A perfect bettor with no counting system loses faster. You need both, and they have to be designed together.

Section 2B builds the simplest possible model class. Section 2D builds the execution layer.

### Cross-validation in time series

A subtle but critical point that retail strategy developers routinely get wrong: standard k-fold cross-validation does not work on time series data. The standard method splits the data randomly into k buckets, trains on k−1 buckets, and tests on the remaining bucket. This produces meaningless results in finance because it mixes future data into the training set.

The correct method is **walk-forward analysis** or, more rigorously, **purged k-fold cross-validation** (López de Prado, 2018):

1. Split the data into time-ordered chunks.
2. For each chunk, train on data strictly before the chunk start (and possibly a "purge" gap to avoid contamination from data labeling near the boundary).
3. Test on the chunk.
4. Aggregate test-set performance across all chunks.

This is computationally more expensive than standard cross-validation but it's the only honest way to estimate out-of-sample performance on time series data. Any backtest that doesn't use it is overestimating performance.

[INTERACTIVE: walk-forward-cv-visualizer]

---

## 2B · Mean reversion vs momentum (an AR(1) model)

The simplest possible model — an auto-regressive linear regression of order one, or **AR(1)** — captures the two most fundamental trading behaviors: mean reversion and momentum. The model predicts the next log return as a linear function of the previous log return:

```
ŷ_t = w × r_{t−1} + b
```

Just two parameters: a weight w and a bias b. That's it. The sign of w determines everything.

### Three regimes

**w < 0 · Mean reversion.** A negative weight flips the sign of the lag. A positive return is predicted to be followed by a negative one; a negative return predicts a positive next return. "What goes up must come down." This regime is common at second-to-minute timescales in liquid markets, where dealer mean-reversion (from gamma hedging) and microstructure noise (bid-ask bounce) dominate. It's also common at multi-week timescales for individual equities and indices, where overreaction-then-correction patterns recur.

**w > 0 · Momentum.** A positive weight reinforces the sign. "What goes up keeps going up." This regime is most common at intermediate timescales (weeks to months) across asset classes — the empirical foundation of decades of trend-following research and the basis of factor strategies like Jegadeesh-Titman 12-1 momentum (Jegadeesh and Titman, 1993, *Journal of Finance*). Cross-asset trend has been documented in 140+ years of data by Hurst, Ooi, and Pedersen (2017, *Journal of Portfolio Management*).

**w ≈ 0 · Random walk.** No predictive content. The next return is independent of the previous one. This is the efficient market hypothesis in its weakest form, and it's a good approximation at most timescales for most liquid markets. Trade fees, slippage, and adverse selection eat any strategy that operates in this regime.

The AR(1) process is **stationary** when |w| < 1 — variance stays bounded, distributions don't drift, forecasts converge. As |w| approaches 1, the process becomes non-stationary; variance grows unbounded with horizon and the AR(1) model loses predictive validity. Watch the simulated paths fan out as you push the weight toward ±1.

[INTERACTIVE: ar1-regime-explorer]

### How to interpret a fitted weight

The weight in a fitted AR(1) is interpretable as the **first-order autocorrelation** of returns:

```
w ≈ Corr(r_t, r_{t−1})
```

A weight of −0.05 means returns are weakly mean-reverting — a 1% up move predicts roughly a 0.05% down move on average. A weight of +0.10 means returns are weakly momentum-driven. The magnitude tells you the predictive content, and the magnitudes in financial markets are *small* — typical first-order autocorrelations on daily SPX returns are between −0.05 and +0.05, with most of the absolute value coming from microstructure noise rather than fundamental signal.

### Hurst exponent and the variance ratio test

A more powerful way to detect mean reversion vs momentum than just fitting AR(1) is to compute the **Hurst exponent (H)** of the return series. The Hurst exponent measures how variance scales with time horizon:

```
Var(returns over T periods) ∝ T^(2H)
```

For a random walk (no autocorrelation), H = 0.5 and variance scales linearly with time (because 2H = 1). For mean-reverting series, H < 0.5 — variance grows more slowly than linearly because reversals shrink the cumulative move. For momentum-driven (persistent) series, H > 0.5 — variance grows faster than linearly because trends compound.

The related **variance ratio test** (Lo and MacKinlay, 1988, *Review of Financial Studies*) formalizes this into a statistical test of the random-walk null hypothesis. The variance ratio at lag k is:

```
VR(k) = Var(r_t + r_{t+1} + ... + r_{t+k−1}) / (k × Var(r_t))
```

Under the random walk null, VR(k) = 1 for all k. VR(k) > 1 indicates momentum; VR(k) < 1 indicates mean reversion. Lo and MacKinlay's 1988 paper found significant momentum in weekly US stock returns (VR > 1 at lags of 1 to 4 weeks), challenging the random-walk hypothesis on those horizons.

These tools are how the academic literature has built robust statistical support for both mean reversion (at very short and very long horizons) and momentum (at intermediate horizons). The retail trader who claims "I'm a mean reversion guy" is making a horizon-specific assumption they may not realize they're making.

[INTERACTIVE: ar-fit-widget]

### Why AR(1) is the right starting point

You will not get rich on AR(1) alone. The reason to learn it is pedagogical: it is the simplest non-trivial model that captures the essential question every trading system must answer — do I expect the next move to continue the current move (momentum) or reverse it (mean reversion)? Every more sophisticated model is a refinement of this question:

- ARMA models add moving-average residual terms
- ARIMA models handle non-stationarity
- GARCH models add time-varying volatility
- Kalman filters add latent-state inference
- Hidden Markov models add discrete regime switching
- LSTMs and transformers add nonlinear temporal interactions

All of them, in their cleanest formulation, are answering some version of "given what we've seen, what do we expect next?" — and the simplest answer is a weighted combination of recent values. Start with AR(1); add complexity only when residuals demand it.

### The regime problem

The most important practical issue with AR(1) and its descendants is that **the sign of w changes over time**. SPX intraday autocorrelation in calm regimes is mildly negative (mean-reverting, courtesy of positive-gamma dealer hedging — we'll see this in Section 6). In stress regimes, intraday autocorrelation flips positive (momentum, courtesy of negative-gamma dealer hedging amplifying moves). A static AR(1) fit to "all available data" averages across these regimes and produces an estimated w near zero — neither regime, not predictive.

The fix is **regime-conditional modeling**: fit one AR(1) for "calm" regimes and another for "stress" regimes, with a classifier that identifies which regime is currently active. This is the essence of regime-switching models and the foundation of every serious quant trading framework. We'll return to this in Sections 8B (positive vs negative GEX as regime indicator) and 10F (composite regime scorecard).

---

## 2C · Optimization: closed-form vs gradient descent

Once a model is specified, we need to **fit** its parameters — find the weight and bias (in our AR(1) case) that minimize the prediction error on training data. Two canonical approaches: closed-form (exact, doesn't scale to massive datasets) and gradient descent (iterative, scales beautifully and underlies every modern ML library).

### Closed-form ordinary least squares

For linear regression with squared-error loss, there is a one-line analytical solution. Define the design matrix X (rows are observations, columns are features) and target vector y. The OLS estimator for the weight vector β is:

```
β̂ = (X^T X)^(-1) X^T y
```

Exact. Fast for small datasets. Used inside scikit-learn's `LinearRegression`, R's `lm()`, and basically every statistical software package's linear regression function. For the AR(1) case with one feature, this collapses to a particularly clean form:

```
ŵ = Cov(r_t, r_{t-1}) / Var(r_{t-1})

b̂ = mean(r_t) − ŵ × mean(r_{t-1})
```

Two numbers, no iteration, no learning rate. Compute the sample covariance and sample variance, divide. Done.

**The flaw of OLS.** It requires inverting a matrix of size (features × features). For a model with 5 features and 1,000 observations, this is trivial. For a model with 50,000 features and 100 million observations — typical of large-scale ML — the matrix inversion becomes infeasible. You cannot load all of the data into memory simultaneously, and matrix inversion is O(n³) in the feature count.

### Gradient descent

Gradient descent is iterative. At each step:

1. Compute the current loss on the training data (or a mini-batch of it).
2. Compute the gradient of the loss with respect to each parameter.
3. Take a small step in the direction opposite to the gradient (downhill on the loss surface).
4. Repeat.

The update rule for parameter w at step t:

```
w_{t+1} = w_t − η × ∂L/∂w
```

where η (eta) is the **learning rate** — the step size. Too large a learning rate and the optimizer overshoots, oscillates, and may diverge entirely. Too small and convergence is painfully slow. Tuning η is part of the art of optimization, and getting it right is most of the challenge in training modern ML models.

**Why gradient descent is the foundation of modern ML.** The crucial property of gradient descent is that it doesn't require loading all the data at once. You can compute the gradient on a *mini-batch* — a small random subset of the training data — and take a step. This is **stochastic gradient descent (SGD)**, and it scales to arbitrarily large datasets. Modern variants like Adam (Kingma and Ba, 2014), RMSProp (Tieleman and Hinton, 2012), and SGD with momentum (Polyak, 1964) all build on this idea: instead of inverting a giant matrix, take many small steps with smart adaptations.

### The geometry of optimization

For convex loss functions (like squared error on a linear model), gradient descent converges to the global optimum from any starting point, provided the learning rate is appropriate. Convex problems are easy.

For non-convex loss functions (like everything in deep learning, plus most realistic trading objectives), gradient descent converges to some local minimum that depends on the starting point. Real-world loss surfaces have:

- **Local minima** — points where every nearby direction increases the loss but the global optimum lies elsewhere.
- **Saddle points** — points where some directions go up and others go down; these are vastly more common than local minima in high-dimensional spaces.
- **Plateaus** — large regions where the gradient is nearly zero, slowing progress dramatically.
- **Cliffs** — regions where the gradient is enormous, causing standard SGD to take huge destabilizing steps.

[INTERACTIVE: gradient-descent]

### Modern optimizers

The plain SGD update is rarely used in practice. Modern variants address specific failure modes:

**SGD with momentum (Polyak, 1964).** Accumulates a running average of past gradients and uses it to dampen oscillation and escape saddle points. Update:

```
v_{t+1} = γ × v_t + η × ∂L/∂w
w_{t+1} = w_t − v_{t+1}
```

The "velocity" v keeps you moving in directions that have consistently pointed downhill, even if the current local gradient is noisy.

**AdaGrad (Duchi et al., 2011).** Adapts the learning rate per parameter, dividing by the running sum of squared past gradients. Parameters that have already seen big updates get smaller updates going forward.

**RMSProp (Tieleman and Hinton, 2012).** Like AdaGrad but uses an exponential moving average instead of a cumulative sum, preventing the learning rate from going to zero.

**Adam (Kingma and Ba, 2014).** Combines momentum with RMSProp. The default choice in most modern ML codebases. Robust, fast, requires minimal tuning.

You don't need to know the internals of these. You need to know that "the optimizer is doing something smarter than vanilla gradient descent" and that the choice of optimizer can dramatically affect training speed and final performance. For most trading applications with linear or simple nonlinear models, vanilla SGD or Adam with default hyperparameters works fine.

### Why optimization matters for trading

The optimization step is where most of the computational expense in modern quant research lives. Backtesting a strategy means fitting models, generating predictions, simulating execution, computing performance, and iterating. Fitting a model on millions of (feature, target) pairs is the slow step. Modern quant firms run massive distributed-training infrastructure precisely because they're optimizing thousands of model variants in parallel.

For retail-scale work — fitting a model on a few thousand observations — optimization is essentially free. The bottleneck is data acquisition, feature engineering, and avoiding overfitting, not the optimization step itself.

### Regularization

A core technique that addresses overfitting at the optimization stage: add a penalty term to the loss function that discourages large parameter values. The two most common forms:

**L2 regularization (ridge):**

```
L_total = L_data + λ × ∑_i w_i²
```

**L1 regularization (lasso):**

```
L_total = L_data + λ × ∑_i |w_i|
```

The hyperparameter λ controls the strength of regularization. Higher λ means smaller fitted weights, which means a smoother model with less overfitting risk.

L2 keeps all features but shrinks their weights toward zero. L1 has the additional property that it zeros out many weights entirely — performing feature selection automatically. For trading models with many candidate features, L1 is often the right choice because it produces sparse, interpretable models.

For AR(1) with a single feature, regularization is unnecessary; for multivariate models with dozens of features, it is essential.

---

## 2D · Making vs taking: the order book mechanics

Strategies fall into two execution families that have fundamentally different P&L characteristics: **making** (adding liquidity to the order book, earning the spread, paying low or even negative fees) and **taking** (removing liquidity, paying the spread and higher fees). The same predictive model can be wrapped in either execution layer, with very different results. Understanding the order book mechanics is what separates retail traders who lose 50 bps per round trip to slippage from professionals who lose 5 bps.

### The order book

The order book is the live record of supply (asks) and demand (bids) for a given security, organized in price levels. The **best bid** is the highest price any buyer is currently willing to pay. The **best ask** (or "offer") is the lowest price any seller is currently willing to accept. The gap between them is the **bid-ask spread**. The midpoint of the bid-ask spread is the **mid price**.

```
ASKS (sellers)
$118 @ 12   ← deeper ask levels (worse prices, more quantity)
$117 @ 8
$116 @ 5
$115 @ 3    ← best ask (top of book)
        ____________________  spread = $2  mid = $114.0
$113 @ 5    ← best bid (top of book)
$112 @ 8
$111 @ 10
$110 @ 15   ← deeper bid levels (worse prices, more quantity)
BIDS (buyers)
```

When a new order arrives, one of three things happens:

1. **A limit order at a price away from the book** — the order goes onto the book as a resting order, becoming part of the bid or ask at its specified price level. The trader is *adding* liquidity.

2. **A limit order at a price that crosses the book** — for a buy limit at or above the current best ask, the order *takes* liquidity by matching against the resting ask. Same for a sell limit at or below the best bid.

3. **A market order** — fills immediately at whatever prices are available on the opposite side, walking through the book as deep as necessary to fill the requested quantity.

### The bid-ask bounce

The "last trade" price alternates between bid and ask as trades alternate between buy-driven and sell-driven flow. This produces a sawtooth pattern called the **bid-ask bounce** that adds noise to any "last price" series. Professional quant work uses the **mid price** instead — the average of bid and ask — because mid is a less-biased estimator of the security's true value.

For SPY, where the bid-ask spread is typically $0.01 to $0.02, the bid-ask bounce is small. For SPX (the cash index), there is no bid-ask bounce because it's not directly tradable — the "level" is computed from constituent stocks. For SPX options, where spreads can be $0.10 to $0.30 wide, the bid-ask bounce dominates the high-frequency dynamics and any backtest that uses "last" instead of "mid" prices is systematically biased.

### Walking the book

A large market order that exceeds the quantity available at the top level **walks the book** — fills are spread across multiple levels, with each successive contract filling at a worse price.

[INTERACTIVE: order-book-walking]

For a small retail SPY market buy of 100 shares against a top-of-book ask of 1,000 shares, the entire order fills at the best ask with no slippage. For a 100,000-share market order, the order walks several levels and the average fill price might be 5 cents worse than the top-of-book ask — about 0.5 bps of slippage on a $580 stock. For a 10-million-share market order, the order might move the price by several dollars before completion.

This is why institutional-scale execution is its own specialty. Large orders are broken into many small pieces, executed over time using algorithms like VWAP (Volume-Weighted Average Price), TWAP (Time-Weighted Average Price), or implementation shortfall optimizers that trade off market impact against opportunity cost. The optimal execution problem was formalized by Almgren and Chriss (2000) and remains an active research area.

### Maker-taker fee structure

US exchanges operate a **maker-taker fee model** for most equity and options trading:

- **Makers** (resting orders that get filled when someone crosses them) typically receive a small **rebate** — they're paid to provide liquidity.
- **Takers** (incoming orders that cross the spread to fill against resting orders) pay a **fee** — they're paying for immediate execution.

For US equity exchanges, the maker rebate is typically 0.2 to 0.3 cents per share, and the taker fee is typically 0.3 to 0.4 cents per share. The exchange keeps the small difference. On 100 shares of SPY traded round-trip as a taker on both legs, that's roughly $0.60 of exchange fees — small but real.

For US options, the maker-taker structure is more variable across exchanges and contract types. SPX options on Cboe have a different fee schedule than SPY options across multiple competing venues. Institutional traders care deeply about these differences; retail traders rarely see them because their broker (Robinhood, Fidelity, Schwab) routes orders through wholesalers that internalize the fee structure (see Section 3B on PFOF).

### Inverted markets (subsidy markets)

A small number of US equity exchanges run **inverted markets** — they pay takers and charge makers. The economic rationale: traders who *want* immediate execution badly enough are willing to pay for it explicitly, while liquidity is harder to attract. Inverted markets exist at small share but provide a price-improvement venue for orders that absolutely must fill now.

### Queue position

When you place a limit order at a price level that already has resting orders, you go to the **back of the queue** at that price level. When a market order arrives and consumes some of the resting quantity, it fills against the front of the queue first. The order at position 50 in a queue of 100 contracts has to wait for 49 fills ahead of it before it gets to fill.

Queue position matters enormously for market makers, who rely on being at the front of the queue to capture maximum order flow. Latency arbitrage — the ability to update quotes faster than competitors — is largely about queue position management. A market maker that can see incoming flow microseconds before competitors can adjust their resting orders accordingly, capturing or avoiding the resulting fills.

For retail traders, queue position is invisible because retail orders are routed to wholesalers (not directly to exchanges) and wholesalers internalize execution against their own principal book. But understanding that queue position exists is important: a limit order at the NBBO might not fill even if the price touches your level, because there were 10,000 other contracts in the queue ahead of you.

### Adverse selection

A subtle and important risk for makers: when your resting order fills, the trade was almost certainly initiated by someone with marginally more information than the market consensus. If the price was about to move *up* and you had a resting ask, your ask gets filled and the price immediately moves above your fill price — you sold too cheaply. If the price was about to move *down* and you had a resting bid, your bid gets filled and the price immediately moves below your fill — you bought too high. This is **adverse selection** — the systematic tendency of your fills to come from informed counterparties at exactly the worst moments.

Adverse selection is the central risk that market makers manage. The bid-ask spread exists, fundamentally, to compensate the market maker for adverse selection. If spreads were too narrow, market makers would systematically lose to informed flow. If spreads were too wide, no one would trade and the market maker would earn nothing. The equilibrium spread is the one where the spread captured exactly compensates for adverse selection losses, plus a margin.

### Order types: what retail actually has

US brokerages typically expose five order types to retail traders. Each one has a specific contract — what it promises, what it doesn't guarantee, and when each one is appropriate.

**Market order.** Buy at the best available ask / sell at the best available bid. Crosses the spread. No price guarantee — you fill at whatever price is available. In thin markets, at the open, or in stressed conditions, can fill far from the NBBO. Use cautiously.

**Limit order.** Buy at or below a stated price / sell at or above. No fill guarantee — your order sits passive on the book until either matched or canceled. Use when price is more important than execution.

**Marketable limit.** A limit order set at or through the current NBBO. Behaves like a market order in normal conditions (gets you filled at the NBBO) but caps slippage in stress (won't fill above your limit). The recommended default for any retail order of meaningful size.

**IOC (Immediate-or-Cancel).** Fill whatever portion you can at the limit price right now; cancel the rest. Useful when you want to take some liquidity but not leave a resting order.

**MOC (Market-on-Close).** Execute at the official closing print, which is determined by the closing auction (see below). MOC orders are guaranteed to fill at the close, but the close price itself is set by the auction imbalance.

The recommended retail discipline: **use marketable limits as the default**. They give you fills in normal conditions while protecting you from blow-up fills in stress. Save market orders for tiny orders in highly liquid names where slippage is bound to be negligible.

### The closing auction

Between 3:50 PM and 4:00 PM ET, US equity exchanges enter their closing auction process. The exchanges publish **imbalances** every few seconds starting around 3:50 — "12 million shares of SPY to buy at the close, market-on-close" — so that liquidity providers know to step in if they want to take the other side. The final 10 seconds of trading set the official close, which is the print used by MOC orders, by ETF NAV computations, by index benchmark closing levels, and by most institutional performance measurement.

Approximately 10-15% of daily NYSE volume trades in the closing auction. For index ETFs (SPY, QQQ, IWM), the share is even higher — closer to 20-25% — because passive index funds rebalance to the close. This is why the last fifteen minutes of every trading day has a different microstructure character than the rest of the day: it is dominated by mechanical, non-fundamental order flow.

This mechanical flow is *also* where dealer end-of-day hedging happens. The Baltussen-Da-Lammers-Martens paper on intraday momentum (2021, *Journal of Financial Economics*) shows that the first half-hour of return predicts the last half-hour of return with statistical significance across 60+ futures contracts globally. The mechanism is the same in every market: dealers carry net option exposure through the day, accumulate hedging needs as the day progresses, and concentrate those hedging trades into the close. This is where Section 6 picks up.

### Slippage scaling

A practical model that captures most of the empirical behavior of trade execution:

```
Slippage (bps) ≈ k × √(Order_size / ADV)
```

where ADV is average daily volume. Slippage scales as the square root of relative order size — taking out 1% of ADV produces 10× more slippage than taking out 0.01% of ADV (not 100× more — that's the importance of the square root). This is the Almgren-Chriss "square-root law" of market impact, validated by extensive empirical work.

For SPY, daily volume is approximately 50-80 million shares; a 1,000-share retail trade is 0.001-0.002% of ADV, well below the threshold where impact becomes measurable. For a 1-million-share institutional trade — 1-2% of ADV — impact is noticeable, perhaps 5-15 bps depending on conditions. For a 100-million-share trade — covering days of execution — the price impact is large, and institutional execution algorithms slice the order across hours or days to minimize total impact.

---

## 2E · Sizing and frequency scaling

Even with a perfect model, oversizing a single trade can ruin the whole strategy. The intuition is brutal but simple: **bet small, bet often**. The best quant strategies often win 51-53% of trades; if you oversize at that win rate, the variance of any single trade dominates the expected value and ruin probability climbs fast.

### The Kelly criterion

Edward Thorp's gambling research, extended by Kelly (1956), provides the canonical answer to the sizing question. For a binary bet where you win amount G with probability p or lose amount L with probability 1−p, the fraction of wealth that maximizes expected log return is:

```
f* = p/L − (1 − p)/G
```

For the special case where G = L = 1 (symmetric payoffs, scaled to 1):

```
f* = 2p − 1
```

So a strategy with 55% win rate at symmetric payoffs has Kelly fraction 0.10 — bet 10% of wealth per trial. A strategy with 60% win rate has Kelly fraction 0.20. A strategy with exactly 50% win rate at symmetric payoffs has Kelly fraction zero — don't bet.

For continuous returns rather than binary outcomes, the Kelly fraction is:

```
f* = μ / σ²
```

where μ is the expected excess return and σ² is the variance. Equivalently, Kelly fraction equals the strategy's Sharpe ratio divided by its volatility — making Kelly fraction the leverage that maximizes expected compound growth.

### Why Kelly is a ceiling, not a target

The Kelly criterion maximizes *expected* compound growth, but it produces enormous *variance* in outcomes. A Kelly-sized strategy has roughly a 50% chance of seeing a 50%+ drawdown at some point. The math is unforgiving: optimal compound growth requires accepting wild swings in path.

Most professional traders use **fractional Kelly** — typically half-Kelly (f = 0.5 × f*) or quarter-Kelly. Half-Kelly gives up about 25% of expected compound growth but reduces drawdown probability dramatically. Quarter-Kelly gives up about 44% of expected compound growth but reduces drawdown probability further. The optimal fraction depends on the trader's tolerance for path-dependent risk and on the reliability of the estimated edge.

The reason half-Kelly is the dominant convention: estimates of edge are noisy. If your true Kelly fraction is f* but your estimate has a 30% standard error, betting at the point estimate means you're often betting at 1.3 × f* — which has *worse* expected compound growth than betting at f* (the Kelly utility function is concave; over-betting hurts more than under-betting). Half-Kelly accommodates the estimation error by buffering against over-betting.

### A retail-scale worked example

A formula and a buffering principle are useful but abstract. Walk one full chain at a retail account size and the operational shape comes into focus — including the seam between this framework and the loss-budget framework that Section 12C builds on top of.

**Setup.** Account size $250,000. A swing strategy with an estimated 60% win rate, $4 average winner per share, $3 average loser per share, traded on an underlying at $50/share with a $2 stop distance.

**Step 1 — apply the formula.** f* = p/L − (1 − p)/G = 0.60/3 − 0.40/4 = 0.200 − 0.100 = **0.100**. Full-Kelly fraction is 10%. Half-Kelly is 5%; quarter-Kelly is 2.5%.

**Step 2 — translate to dollars.** Full-Kelly bet = 10% × $250k = $25,000. Half-Kelly = $12,500. Quarter-Kelly = $6,250.

**Step 3 — translate to shares at $50.** Full = 500, half = 250, quarter = **125 shares**. The shop-floor share count under quarter-Kelly is small.

**Step 4 — what would the 1% loss-budget rule (Section 12C) produce?** Risk 1% × $250k = $2,500. With a $2 stop, that's n = $2,500 / $2 = **1,250 shares** — a $62,500 notional, or 25% of the account.

**The two frameworks disagree by an order of magnitude.** Quarter-Kelly says 125 shares with a $250 worst-case loss (0.1% of capital); the 1% loss-budget says 1,250 shares with a $2,500 worst-case loss (1% of capital). For this specific edge, Kelly is *far* more conservative than the loss-budget rule.

This disagreement is structural, not a bug in either rule. Kelly's "bet" is the *full notional at stake* under a binary-outcome geometry where the entire position rises or falls by G or L per unit; loss-budget's "size" is the *position scaled to a fixed-stop maximum loss* under a stop-distance geometry. The two converge in dollars only when the edge is mild enough that Kelly's recommended fraction sits near the loss-budget's risk fraction — empirically, around 52-53% win rate with near-symmetric payoffs.

For the strong edge above (60% with 4:3 payoffs), the divergence is the operational answer to "is the loss-budget rule sufficient on its own?" — and the answer is **only if you don't actually have 10% Kelly worth of edge**, which most retail strategies don't. Section 12C reconciles the two frameworks explicitly: loss-budget for individual-trade sizing, Kelly as a sanity check on the aggregate.

### Sizing functions

How big should the trade be when the model produces prediction strength p?

**Constant.** Same position size regardless of prediction strength. Just trade the sign of the prediction. This is the cleanest baseline for backtesting because the interpretation is unambiguous — every trade is the same size, so the P&L is a pure function of directional accuracy.

**Piecewise-linear (hard tanh).** Size scales linearly with prediction strength up to a cap. Stronger predictions get larger trades; the cap ensures a runaway prediction (a single extreme outlier in input data) can't blow up size.

**Smooth nonlinear (tanh).** Like hard tanh but smooth. Differentiable everywhere — useful if you're optimizing the sizing parameters with gradient-based methods alongside the model. The smooth transition between zero-prediction (zero size) and strong-prediction (capped size) avoids the "I just barely crossed the threshold, should I scale up?" decision discontinuity.

In practice, most production quant strategies use either piecewise-linear or smooth-tanh sizing, calibrated so that the cap corresponds to half-Kelly at the strongest prediction signal the model produces.

### Frequency scaling

If your model has a tiny edge per prediction — say, 51% win rate or Sharpe 0.05 per trade — you don't want to bet once. You want to bet many times. The reason follows directly from the frequency-Sharpe relationship in 1D:

```
SR_total ≈ SR_per_bet × √N
```

A tiny per-bet Sharpe becomes a robust strategy Sharpe when N is large. A model that predicts the 12-hour-ahead return with Sharpe 0.05 can be split into many smaller bets at finer temporal resolution — bet on the 1-hour-ahead return 24 times a day, each time at a smaller size. If the 24 bets are roughly independent, the daily Sharpe of the high-frequency version is √24 ≈ 4.9× higher than the daily Sharpe of the once-per-12-hours version.

This is the structural reason high-frequency strategies dominate the modern quant landscape. They aren't smarter about direction; they trade the same edge many more times. The compounding logic is identical to the Sharpe argument in 1D: more independent bets with positive EV → same terminal drift, lower variance → higher Sharpe → leverage becomes safer → returns scale.

The retail implication is sobering. Most retail strategies have N on the order of 10-100 trades per year. Even with substantial per-trade edge, the resulting annual Sharpe is modest. To compete with institutional high-frequency strategies you would need either (a) a per-trade edge that's an order of magnitude larger than what HFT firms exploit — which means you're operating in a different market regime, probably lower-liquidity products — or (b) the operational infrastructure to trade at high frequency, which retail doesn't have.

The honest path for retail is to accept that you can't compete on frequency, focus on capturing risk premia (variance, equity, trend) that don't require high frequency, and size conservatively because your effective Sharpe is going to be modest.

### Frequency vs cost

There's a fundamental tradeoff between frequency and transaction costs. Each trade costs spread plus commission plus slippage. At very high frequency, costs eat the edge. The optimal frequency for any strategy is the one where the marginal Sharpe gain from one more trade per day equals the marginal cost in basis points.

For HFT firms with co-located servers, near-zero latency, and rebate-earning maker strategies, the optimal frequency can be thousands of trades per second. For retail traders paying 1 cent per share commission plus 5 bps slippage per round-trip, the optimal frequency is dramatically lower — perhaps 10-50 trades per year, depending on the per-trade edge.

This is also why the "free trades" era (post-2019, when most US brokerages dropped commissions for retail equity orders) didn't actually transform retail performance. Commissions were already small. The dominant retail cost is slippage, which retail traders neither see directly nor can negotiate down, and the dominant retail edge-destroyer is behavioral — overtrading, sizing inconsistencies, and emotional exits. None of these were fixed by zero commissions.

### The path-vs-terminal distinction

A final point worth emphasizing: Kelly maximizes *expected log terminal wealth* over a long horizon. It does not minimize drawdown probability, doesn't bound worst-case outcomes, and doesn't account for behavioral capitulation during drawdowns.

For a real-world investor with finite emotional bandwidth, **drawdown discipline** is more important than Kelly optimization. A strategy sized at quarter-Kelly with a 30% maximum drawdown discipline (close-and-reset rule) outperforms a strategy sized at full Kelly with no drawdown discipline, in any realistic behavioral model, because the full-Kelly strategy gets abandoned during its first 50% drawdown and the quarter-Kelly strategy doesn't.

Section 12C will return to this with explicit kill rules at three levels. For now, the principle is: **size for survivability first, then for compound growth**. Kelly is the ceiling, half-Kelly is the working compromise, and quarter-Kelly is what you actually use if you want to sleep through drawdowns.
