"""
Title: Codecademy's Analyze Financial Data with Python

Topic: Calculating Financial Statistics - Annualizing Returns, Aggregate Across Time

Description:  Important to keep in mind is the time frame of the investment. This program converts the rate to a standard time period, annual rate of return.
Aggregating across time for a single asset can be calculated using the log rate of return, but to annualize the program multiplies the rate of return
by the number of original time periods there are in the new time period.

Author: Eric Cantrell
Date: January 14, 2024
"""

from math import log

#  Method for expressing the calculated rate of return as a percentage that takes in one parameter - decimal form
def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

# Logarithmic rates of returns
daily_return_a = 0.001
monthly_return_b = 0.022

# Displaying daily and monthly returns as percentages
print('The daily rate of return for Investment A is ', display_as_percentage(daily_return_a))
print('The monthly rate of return for Investment B is ', display_as_percentage(monthly_return_b))

# Method for calculating annualized return using logrithmic rate of return and time
def annualize_return(log_return, t):
  annual_return_a = log_return * t # Daily return
  return annual_return_a

# Annual Return
annual_return_a = annualize_return(daily_return_a, 252)
print('The annual rate of return for Investment A is ', display_as_percentage(annual_return_a))

# Monthly Return
annual_return_b = annualize_return(monthly_return_b, 12)
print('The annual rate of return for Investment B is ', display_as_percentage(annual_return_b))

# -- Aggregate Across Time II --
daily_returns = [0.002, -0.002, 0.003, 0.002, -0.001]

# Method for converting log returns 
def convert_returns(log_returns, t):
  total_log_returns = sum(log_returns)
  avg_log_returns = total_log_returns/len(log_returns)
  return avg_log_returns * t

# Annual rate of return
annual_return = convert_returns(daily_returns, 252)
print('The annual rate of return is', display_as_percentage(annual_return))

# Weekly rate of return
weekly_return = convert_returns(daily_returns, 5)
print('The weekly rate of return is', display_as_percentage(weekly_return))

# Equivalent to summing up all the daily returns in that period.
weekly_return = sum(daily_returns) / len(daily_returns)
print('The weekly rate of return is', display_as_percentage(weekly_return))