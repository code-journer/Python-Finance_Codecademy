"""
Title: Codecademy's Analyze Financial Data with Python

Topic: Calculating Financial Statistics - Aggregate Across Assets

Description: Investments often make up the pieces of a larger financial portfolio. 
This program will calculate the expected rate of return for an entire portfolio of investments.

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

""" The "Aggregate Across Time" approach calculates the average return from a given set of return values over a specified time period. 
If all returns are available, it uses the total time period (t) to compute the average; otherwise, it calculates the average based 
on the actual number of returns (n). The formula involves summing up the returns and dividing by either the total time or the number 
of available returns, providing a consolidated measure of overall returns while accommodating variations in data availability 
across different time periods.
Let's say you have log returns for 5 months: a, b, c, d, e. You want to know the average, sum, and product for all 5 months, and then for just the first 4 months.
For All Changes:
   Average: (a + b + c + d + e) / 5
   Sum: a + b + c + d + e
   Product: (Average) * t
For the First 4 Changes:
   Average for 4 Changes: (a + b + c + d) / 4
   Sum for 4 Changes: a + b + c + d
   Product for 4 Changes: (Average for 4 Changes) * t """

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