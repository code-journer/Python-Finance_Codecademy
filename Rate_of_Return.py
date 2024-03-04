"""
Title: Codecademy's Analyze Financial Data with Python

Topic: Calculating Financial Statistics - Rate of Return

Description: There is often a tradeoff between risk and return, where the higher the potential return of an asset, the higher 
the risk involved. It's important to understand both aspects for making smart choices about an investmentt.

Author: Eric Cantrell
Date: January 14, 2024
"""

# Declare variable and set value
rate_of_return = 0.075

#  Method for expressing the calculated rate of return as a percentage that takes in one parameter - decimal form
def display_as_percentage(val):
    return str(round(val * 100, 1)) + '%'  # OR,  return '{:.1f}%'.format(val * 100)

# Call method and print out results - 7.5%
print(display_as_percentage(rate_of_return))