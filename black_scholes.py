import math
from dataclasses import dataclass
from scipy.stats import norm


@dataclass
class BSParams:
    S: float      
    K: float      
    r: float      
    sigma: float  


def _validate(p: BSParams):
    if p.S <= 0 or p.K <= 0:
        raise ValueError("S and K must be > 0")
    if p.T <= 0:
        raise ValueError("T must be > 0")
    if p.sigma <= 0:
        raise ValueError("sigma must be > 0")


def _d1_d2(p: BSParams):
    _validate(p)
    d1 = (math.log(p.S / p.K) + (p.r + 0.5 * p.sigma**2) * p.T) / (p.sigma * math.sqrt(p.T))
    d2 = d1 - p.sigma * math.sqrt(p.T)
    return d1, d2


def bs_price(p: BSParams, option_type="call"):
    d1, d2 = _d1_d2(p)

    if option_type == "call":
        return p.S * norm.cdf(d1) - p.K * math.exp(-p.r * p.T) * norm.cdf(d2)
    elif option_type == "put":
        return p.K * math.exp(-p.r * p.T) * norm.cdf(-d2) - p.S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")


def bs_greeks(p: BSParams, option_type="call"):
    d1, d2 = _d1_d2(p)

    pdf_d1 = norm.pdf(d1)
    disc = math.exp(-p.r * p.T)

    if option_type == "call":
        delta = norm.cdf(d1)
    elif option_type == "put":
        delta = norm.cdf(d1) - 1
    else:
        raise ValueError("option_type must be 'call' or 'put'")
      
    gamma = pdf_d1 / (p.S * p.sigma * math.sqrt(p.T))
    vega = p.S * pdf_d1 * math.sqrt(p.T)

    if option_type == "call":
        theta = -(p.S * pdf_d1 * p.sigma) / (2 * math.sqrt(p.T)) - p.r * p.K * disc * norm.cdf(d2)
        rho = p.K * p.T * disc * norm.cdf(d2)
    else:
        theta = -(p.S * pdf_d1 * p.sigma) / (2 * math.sqrt(p.T)) + p.r * p.K * disc * norm.cdf(-d2)
        rho = -p.K * p.T * disc * norm.cdf(-d2)

    return {"delta": delta, "gamma": gamma, "vega": vega, "theta": theta, "rho": rho}
