A European options pricing engine demonstrating Black-Scholes analytical pricing and Monte Carlo simulation with variance reduction and Greeks.
## Roadmap
Stage 1 - Analytical Pricer - Complete
1. Implement Black-Scholes closed-form solution for European call and put
2. Implement put-call parity as a verification check
3. Plot option price as a function of spot price $S$, volatility $σ$, and time to expiry $T$

Stage 2 - Monte Carlo Pricer
1. Simulate $N$ paths of ST under risk-neutral measure
2. Compute discounted average payoff
3. Compare convergence against analytical solution as $N$ increases
4. Implement antithetic variates variance reduction
5. Plot convergence rate demonstrating $\mathcal{O}(N^{−1/2} )$ behaviour

Stage 3 - Greeks and Extensions
1. Implement Delta, Gamma, Vega analytically from Black-Scholes formula
2. Implement numerically via finite differences as verification
3. Plot option price surface as joint function of $S$ and $σ$
## Stage 1
### Overview
The Black-Scholes analytical pricer has been implemented in Python. The equation itself has been fully derived and explained, along with its behaviours as $S,T,\sigma$ varies. A put-call parity check has also been implemented.

### The Model
In `analytical.py` the Black-Scholes analytical pricing equations:

$$
C = SN(d_1)-Ke^{-rT}N(d_2)
$$

$$
P =Ke^{-rT}N(-d_2) - SN(-d_1)
$$

$$
d_1 = \frac{\ln\left(\frac{S}{K}\right)+T\left(r+\frac{\sigma^2}{2}\right)}{\sigma\sqrt{T}}, \quad \quad d_2 = d_1-\sigma \sqrt{T}
$$

have been implemented. The fair price of the European call option is given by `bs_call(S, K, T, R, sigma)` and similarly the price of the put option is given by `bs_put(S, K, T, R, sigma)` which takes the same parameters: stock spot price ($S$, the price of the stock today), strike price ($K$, the price at which you have agreed to buy or sell the stock), time until expiration ($T$, in years), the risk-free rate ($R$) and the volatility of the underlying stock ($\sigma$). The function `intermediaries` (which also takes the same inputs) is used to return the values of $d_1, d_2$.

In `analytical_pricer.ipynb` there is a full explaination of how the Black-Scholes equation is derived and how it works starting at the equation modelling **Geometric Brownian Motion**: 

$$
dS = \mu S\:dt+\sigma S\:dW
$$

and **Itô's Lemma**: 

$$
dV = \frac{\partial V}{\partial t}dt+\frac{\partial V}{\partial S}dS+\frac{1}{2}\frac{\partial^2 V}{\partial S^2}(dS)^2
$$

and resulting in the **Black-Scholes PDE**: 

$$
\boxed{\frac{\partial V}{\partial t} +\frac{1}{2}\sigma^2S^2\frac{\partial^2V}{\partial S^2}+rS\frac{\partial V}{\partial S}-rV = 0}
$$

and its solutions which are the equations implemented in `analytical.py`.
#### Why $\mu$ vanishes
We can construct a portfolio: 

$$
\Pi = V(S,t)-\Delta S
$$

and determine that it is **risk-free** by selecting $\Delta = \partial V/\partial S$. Therefore by **no-arbitrage**, the portfolio must earn the **risk-free rate, $r$** : 

$$
\frac{d\Pi}{dt} = r\Pi
$$

which allows us to derive the boxed PDE above, within which there is no drift $(\mu)$ term, as our substitution of $\Delta$ removes that term alongside the Wiener Process, leaving us a deterministic equation. (This can also be shown using the **First Fundamental Theorem of Asset Pricing**)
#### Put-Call Parity
The pricing equations have an interesting relationship:

$$
C + Ke^{-rT} = P + S \implies C-P = S-Ke^{-rT}
$$

Using this equation we can verify the implementation of the equations to ensure their accuracy. This has been done across a wide range of values in `analytical_pricer.ipynb` to ensure the equations are correct.
### Results
Within `analytical_pricer.ipynb` a range of behaviours of the Black-Scholes pricer was explored, and the following relationships were discovered:
### Option price against spot price $S$
The following relationship was observed :

 ![Option price against spot price](option_S.png)

This graph shows how the price of the option varies as the spot price is varied while the other parameters are kept fixed. As $S$ moves to either extreme, the option price approaches the same linear asymptotes indicated by the terminal payoff condition:

$$
C = \max(0, S-K)
$$

$$
P = \max(0, K-S)
$$

The $S\to\infty$ behaviour means the call tends to infinty while the $-S$ in the put makes it have the opposite reacion and it tends to $0$, and vice versa for $S\to 0$, $C\to 0$ and $P\to Ke^{-rT}$. This tells us that a deep in the money or out of the money outcome becomes nearly certain as the spot price moves to either extreme, so the option behaves increasingly like a forward contract (ITM) or becomes worthless (OTM).
