"""
Title: Codecademy's Analyze Financial Data with Python

Topic: Calculating Financial Statistics - Correlation

Description: Correlation is an important statistic for assessing risk is the correlation between the returns of two assets.
Correlation is a measure of how closely two datasets are associated with each other. It is often represented by the correlation coefficient, 
which is a value that ranges between -1 and 1. This indicates whether there is a positive correlation, negative correlation, or no correlation:

Author: Eric Cantrell
Date: January 15, 2024
"""

import numpy as np # Will use to access variance (var) method
from math import sqrt

# Method to calculate correlation
def calculate_correlation(set_x, set_y):
  # Sum of all values in each dataset
  sum_x = sum(set_x)
  sum_y = sum(set_y)

  # Sum of all squared values in each dataset using a List Comprehension approach
  sum_x2 = sum([x ** 2 for x in set_x])

  # Functionally the same as above, just using a for loop approach
  sum_y2 = 0
  for y in set_y:
    sum_y2 += y ** 2

  # Sum of the product of each respective element in each dataset -- ONE WAY OF DOING, BUT NOT CLEAN AND CONCISE
  # sum_xy = 0
  # for i in range(len(set_x)):
  #   sum_xy += set_x[i] * set_y[i]
    
  # Use zip() instead 
  sum_xy = sum([x * y for x, y in zip(set_x, set_y)]) # Takes 2 or more lists as inputs and returns an object that groups each respective element in a tuple
  
  # Length of dataset
  n = len(set_x)

  # Calculate correlation coefficient
  numerator = n * sum_xy - sum_x * sum_y
  denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

  return numerator / denominator

returns_general_motors = [0.018, -0.005, -0.047, -0.009, -0.012, 0.003, -0.027, -0.014, 0.029, -0.062, 0.009]
returns_ford = [0.002, -0.004, -0.027, -0.022, -0.001, 0.002, -0.006, -0.017, 0.035, -0.029, 0.002]
returns_exxon_mobil = [0.008, 0.015, 0.009, 0.012, 0.003, -0.007, 0.006, 0.005, -0.048, 0.025, -0.012]
returns_apple = [-0.002, 0.007, -0.004, -0.004, 0.002, 0.013, -0.011, 0.017, -0.001, 0.012, 0.006]

corr_gm_ford = calculate_correlation(returns_general_motors, returns_ford)
print('The correlation coefficient between General Motors and Ford is', corr_gm_ford)

corr_gm_xom = calculate_correlation(returns_general_motors, returns_exxon_mobil)
print('The correlation coefficient between General Motors and ExxonMobil is', corr_gm_xom)

corr_gm_aapl = calculate_correlation(returns_general_motors, returns_apple)
print('The correlation coefficient between General Motors and Apple is', corr_gm_aapl)

# numpy library function for generating a coefficient matrix that displays the correlation between all pairs of datasets in a list.
corrcoef_matrix = np.corrcoef([returns_general_motors, returns_ford, returns_exxon_mobil, returns_apple])
print(corrcoef_matrix)