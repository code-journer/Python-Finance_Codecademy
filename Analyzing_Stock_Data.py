"""
Title: Codecademy's Analyze Financial Data with Python

Topic: Calculating Financial Statistics - Analyzing Stock Data Project

Description: A program to analyze the monthly stock prices of two E-commerce companies, 
Amazon (AMZN) and eBay (EBAY). Analyzes the risk and return for each investment calculating 
the rates of return from this data, and key statistics such as variance and correlation.

Author: Eric Cantrell
Date: January 19, 2024
"""

import Logarithmic_Rate_of_Return as lrr
from math import log

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

#  Method for expressing the calculated rate of return as a percentage that takes in one parameter - decimal form
def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

# Calculate Rate of Return
def get_returns(prices): 

  return

calc_log_return = lrr.calculate_log_return()
