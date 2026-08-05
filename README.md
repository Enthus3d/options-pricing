Stage 1 - Analytical Pricer
1. Implement Black-Scholes closed-form solution for European call and put
2. Implement put-call parity as a verification check
3. Plot option price as a function of spot price S, volatility σ, and time to expiry T
4. Verify outputs against known benchmark values

Stage 2 - Monte Carlo Pricer
1. Simulate N paths of ST under risk-neutral measure
2. Compute discounted average payoff
3. Compare convergence against analytical solution as N increases
4. Implement antithetic variates variance reduction
5. Plot convergence rate demonstrating O(N^−1/2 ) behaviour

 Stage 3 - Greeks and Extensions
1. Implement Delta, Gamma, Vega analytically from Black-Scholes formula
2. Implement numerically via finite differences as verification
3. Plot option price surface as joint function of S and σ
4. C++ port of core pricer - optional, only if Stages 1 and 2 are solid
