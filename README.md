# Black-Scholes Option Pricing

This repository contains a simple and clean Python implementation of the Black–Scholes model for pricing European options.

The objective of this project is to build a reusable pricing module, following good coding practices commonly used in finance and quantitative development.

# Model Overview

The Black–Scholes model is based on the following assumptions:
- Log-normal dynamics of the underlying asset price
- Constant volatility
- Constant risk-free interest rate
- No arbitrage opportunities
- European-style options (exercise only at maturity)

Both Call and Put options are supported.

# Features

- Analytical pricing of European Call and Put options
- Computation of main Greeks:
  - Delta
  - Gamma
  - Vega
- Clear and readable Python implementation
- Modular design separating pricing logic and testing

# Project Structure

├── black_scholes.py   
├── test_basic.py      
└── README.md

## Example Usage

from black_scholes import BSParams, bs_price, bs_greeks

p = BSParams(S=100, K=100, T=1, r=0.05, sigma=0.2)

call_price = bs_price(p, "call")
put_price = bs_price(p, "put")

greeks = bs_greeks(p, "call")

print(call_price)
print(put_price)
print(greeks)

# How to Run

Install the required dependencies:
pip install -r requirements.txt
Run the basic test script:
python test_basic.py

# Notes

This project is intended for learning and demonstration purposes.
The implementation focuses on clarity and correctness rather than performance.

Possible extensions include implied volatility calculation, Monte Carlo pricing, and numerical Greeks.

 Author

Corporate Finance student  
Aspiring Quantitative Developer





