"""
Title: Codecademy's Analyze Financial Data with Python

Topic: Calculating Financial Statistics - Simple Rate of Return

Description: The difference between the starting and ending price of an investment over a time period, divided by the starting price.
If an investment returns dividends, those dividends should be added to the numerator.

Author: Eric Cantrell
Date: January 14, 2024
"""

#  Method for expressing the calculated rate of return as a percentage that takes in one parameter - decimal form
def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

#  Method for calculating simple interest that takes in 2 required parameters and 1 optional parameter
def calculate_simple_return(start_price, end_price, dividend = 0):
  return (end_price - start_price + dividend) / start_price
  
# Test function using starting & ending price - expect 0.2
print(calculate_simple_return(25, 30))

# Test function, again, using starting & ending price and store results - expect 0.25
simple_return = calculate_simple_return(200, 250)
print('The simple rate of return is', display_as_percentage(simple_return))