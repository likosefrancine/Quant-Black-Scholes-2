import math
from scipy.stats import norm

class BSParams:
    def __init__(self, S, K, T, r, sigma):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma


def bs_price(p, option_type="call"):
    d1 = (math.log(p.S / p.K) + (p.r + 0.5 * p.sigma ** 2) * p.T) / (p.sigma * math.sqrt(p.T))
    d2 = d1 - p.sigma * math.sqrt(p.T)

    if option_type == "call":
        return p.S * norm.cdf(d1) - p.K * math.exp(-p.r * p.T) * norm.cdf(d2)
    else:
        return p.K * math.exp(-p.r * p.T) * norm.cdf(-d2) - p.S * norm.cdf(-d1)


def bs_greeks(p, option_type="call"):
    d1 = (math.log(p.S / p.K) + (p.r + 0.5 * p.sigma ** 2) * p.T) / (p.sigma * math.sqrt(p.T))
    pdf = norm.pdf(d1)

    delta = norm.cdf(d1) if option_type == "call" else norm.cdf(d1) - 1
    gamma = pdf / (p.S * p.sigma * math.sqrt(p.T))
    vega = p.S * pdf * math.sqrt(p.T)

    return {
        "delta": delta,
        "gamma": gamma,
        "vega": vega
    }

