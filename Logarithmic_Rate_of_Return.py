"""
Title: Codecademy's Analyze Financial Data with Python

Topic: Calculating Financial Statistics - Logarithmic Rate of Return

Description: Known as continuously compounded return, the expected return for an investment where the earnings are assumed to be 
continually reinvested over the time period.

Author: Eric Cantrell
Date: January 14, 2024
"""

from math import log

#  Method for expressing the calculated rate of return as a percentage that takes in one parameter - decimal form
def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

# Method for expressing the calculated logrithmic rate of return as a percentage that takes in 2 parameters
def calculate_log_return(start_price, end_price):
    return log(end_price/start_price)

# Test function using starting & ending price - expect 0.22314355131420976
log_return = calculate_log_return(200, 250)

print('The log rate of return is', display_as_percentage(log_return))