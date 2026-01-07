import math
from scipy.stats import norm


class BSParams:
    def __init__(self, S, K, T, r, sigma):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma


def _validate(p):
    if p.S <= 0 or p.K <= 0:
        raise ValueError("S and K must be > 0")
    if p.T <= 0:
        raise ValueError("T must be > 0")
    if p.sigma <= 0:
        raise ValueError("sigma must be > 0")


def bs_price(p, option_type="call"):
    _validate(p)

    d1 = (math.log(p.S / p.K) + (p.r + 0.5 * p.sigma ** 2) * p.T) / (p.sigma * math.sqrt(p.T))
    d2 = d1 - p.sigma * math.sqrt(p.T)

    if option_type == "call":
        return p.S * norm.cdf(d1) - p.K * math.exp(-p.r * p.T) * norm.cdf(d2)
    elif option_type == "put":
        return p.K * math.exp(-p.r * p.T) * norm.cdf(-d2) - p.S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")


def bs_greeks(p, option_type="call"):
    _validate(p)

    d1 = (math.log(p.S / p.K) + (p.r + 0.5 * p.sigma ** 2) * p.T) / (p.sigma * math.sqrt(p.T))
    pdf = norm.pdf(d1)

    if option_type == "call":
        delta = norm.cdf(d1)
    elif option_type == "put":
        delta = norm.cdf(d1) - 1
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    gamma = pdf / (p.S * p.sigma * math.sqrt(p.T))
    vega = p.S * pdf * math.sqrt(p.T)

    return {"delta": delta, "gamma": gamma, "vega": vega}
