#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:31:41 2026

@author: rhysbarker-white
"""

import matplotlib.pyplot as plt

# ---------------------------------
# Investment Growth Calculator
# ---------------------------------

# User Inputs
initial_investment = float(input("Initial investment (£): "))    # Starting amount (£)
monthly_contribution = float(input("Monthly contribution (£): "))     # Monthly contribution (£)
annual_interest_rate = float(input("Annual interest rate (%): "))     # Annual return rate (7%)
annual_interest_rate = annual_interest_rate/100
years = int(input("Number of years: "))                      # Investment period

# Convert annual interest to monthly
monthly_interest_rate = annual_interest_rate / 12

# Total months
months = years * 12

# Store values for graph
portfolio_values = []
month_list = []

# Starting portfolio value
portfolio_value = initial_investment

# Calculate growth month by month
for month in range(months + 1):

    portfolio_values.append(portfolio_value)
    month_list.append(month)

    # Apply monthly growth and contribution
    portfolio_value = (
        portfolio_value * (1 + monthly_interest_rate)
        + monthly_contribution
    )

# ---------------------------------
# Results
# ---------------------------------

total_contributions = (
    initial_investment
    + monthly_contribution * months
)

investment_growth = portfolio_value - total_contributions

print("\n--- Investment Growth Results ---")
print(f"Initial Investment: £{initial_investment:,.2f}")
print(f"Monthly Contribution: £{monthly_contribution:,.2f}")
print(f"Investment Period: {years} years")
print(f"Expected Annual Return: {annual_interest_rate*100:.1f}%")
print(f"Total Contributions: £{total_contributions:,.2f}")
print(f"Investment Growth: £{investment_growth:,.2f}")
print(f"Final Portfolio Value: £{portfolio_value:,.2f}")

# ---------------------------------
# Plot Investment Growth
# ---------------------------------

plt.figure(figsize=(12, 6))

plt.plot(month_list, portfolio_values)

plt.title("Investment Growth Over Time")
plt.xlabel("Months")
plt.ylabel("Portfolio Value (£)")

plt.grid(True)

plt.show()