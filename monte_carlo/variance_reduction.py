import monte_carlo.pricer as pricer
import numpy as np
import math

def generate_antithetic_normals(n):
    half_n = math.floor(n/2)
    positive_normal = pricer.generate_normals(half_n)
    negative_normal = -positive_normal
    return [negative_normal, positive_normal]

def antithetic_payoff(S, K, T, r, sigma, Z_n, option_type):
    for i in range(2):
        Z_n[i] = pricer.payoff(S, K, T, r, sigma, Z_n[i], option_type)
    return Z_n

def mc_antithetic_price(S, K, T, r, sigma, n, option_type):
    Z_n = generate_antithetic_normals(n)
    Z_n = antithetic_payoff(S, K, T, r, sigma, Z_n, option_type)
    Y = 0.5*(Z_n[0]+Z_n[1])
    price = np.exp(-r*T)*np.mean(Y)
    return price


def antithetic_standard_error(payoffs, r, T):
    Y = 0.5*(payoffs[0]+payoffs[1])
    return pricer.mc_standard_error(Y, T, r)
        
def variance_reduction_factor(n, n_repeats, S, K, T, r, sigma, option_type):
    p = []
    ap = []
    for i in range(n_repeats):
        p.append(pricer.mc_price(S, K, T, r, sigma, n, option_type))
        ap.append(mc_antithetic_price(S, K, T, r, sigma, n, option_type))
    return [np.var(p, ddof = 1)/np.var(ap, ddof = 1), p, ap]
