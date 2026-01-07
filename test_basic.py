import math
from black_scholes import BSParams, bs_price, bs_greeks

p = BSParams(S=100, K=100, T=1, r=0.05, sigma=0.2)

call = bs_price(p, "call")
put = bs_price(p, "put")

print("Call:", call)
print("Put :", put)

lhs = call - put
rhs = p.S - p.K * math.exp(-p.r * p.T)
print("Parity diff:", lhs - rhs)

print("Greeks call:", bs_greeks(p, "call"))
print("Greeks put :", bs_greeks(p, "put"))
