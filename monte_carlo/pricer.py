import numpy as np
import scipy.stats

class InvalidOptionType(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error code: {self.error_code})"

def simulate_S_T(S, r, sigma, T, Z_n):
    return S*np.exp(T*(r-(0.5*(sigma**2)))+(sigma*np.sqrt(T)*Z_n))

def generate_normals(n):
    return np.random.normal(0.0, 1.0, n)

def payoff(S_T_n, K, option_type):
    if option_type == "call":
        return np.maximum(0,S_T_n-K)
    elif option_type == "put":
        return np.maximum(0, K-S_T_n)
    else:
        raise InvalidOptionType(f"Invalid option type \"{option_type}\" for options \"put\" or \"call\"", 400)

def mc_price(S, K, r, sigma, T, n, option_type):
    Z_n = generate_normals(n)
    payoffs = payoff(simulate_S_T(S, r, sigma, T, Z_n), K, option_type)
    price = np.exp(-r*T)*np.mean(payoffs)
    return price

def mc_standard_error(payoffs, r, T):
    return (np.std(payoffs, ddof = 1)*np.exp(-r*T))/np.sqrt(len(payoffs))

def confidence_interval(price, standard_error, level = 0.95):
    critical_value = stats.norm.ppf(1-(1-level)/2)
    return (price - (standard_error*critical_value), price + (standard_error*critical_value))

