import options-pricer.monte_carlo.pricer

def generate_antithetic_normals(n):
    half_n = math.floor(n/2)
    positive_normal = pricer.generate_normals(half_n)
    negative_normal = -positive_normal
    return [negative_normal, positive_normal]

def mc_antithetic_price(S, T, K, r, sigma, n, option_type):
    Z_n = generate_antithetic_normals(n)
    for i in range(2):
        Z_n[i] = pricer.payoff(S, T, K, r, sigma, Z_n[i], option_type)
    Y = 0.5*(Z_n[0]+Z_n[1])
    price = np.exp(-r*T)*np.mean(Y)
    return price

def antithetic_payoff(S, T, K, r, sigma, Z_n, option_type):
    for i in range(2):
        Z_n[i] = pricer.payoff(S, T, K, r, sigma, Z_n[i], option_type)
    return Z_n
 

def antithetic_standard_error(payoffs, r, T):
    Y = 0.5*(payoffs[0]+payoffs[1])
    return pricer.mc_standard_error(Y, T, r)
        

