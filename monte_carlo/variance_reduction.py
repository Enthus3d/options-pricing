import options-pricer.monte_carlo 

def generate_antithetic_normals(n):
    half_n = math.floor(n/2)
    positive_normal = monte_carlo.generate_normals(half_n)
    negative_normal = -positive_normal
    return np.concatenate(negative_normal, positive_normal)


