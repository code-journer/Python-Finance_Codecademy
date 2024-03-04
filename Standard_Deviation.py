"""
Title: Codecademy's Analyze Financial Data with Python

Topic: Calculating Financial Statistics - Standard Deviation

Description: Standard deviation measures risk; it is common to use the it to describe the spread of the dataset.
It is an alternative to variance in determining the relative risk of an investment, but it does not have the same unit as the original data;
this could make it more challenging to interpret.

Standard Deviation (σ) = sqrt(Σ (X_i - X̄)^2 / n)
σ: standard deviation
Xi: the ith value in the dataset
X̄: the mean of the dataset
n: the number of values in the dataset

Author: Eric Cantrell
Date: January 15, 2024
"""

import numpy as np # Will use to access variance (var) method
from math import sqrt
from Variance import calculate_variance

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

# Sample data sets
returns_disney = [0.22, 0.12, 0.01, 0.05, 0.04]
returns_cbs = [-0.13, -0.15, 0.31, -0.06, -0.29]

# Use numpy's std method to calculate standard deviation
stddev_disney = np.std(returns_disney)
stddev_cbs = np.std(returns_cbs)

print('The standard deviation of Disney stock returns is', display_as_percentage(stddev_disney))
print('The standard deviation of CBS stock returns is', display_as_percentage(stddev_cbs))

# Non specific sample data set
dataset = [10, 8, 9, 10, 12]

# Method to calculate standard deviation
def calculate_stddev(dataset):
    # Calculate variance
    variance = calculate_variance(dataset)
    stddev = sqrt(variance)
    return stddev

stddev_disney = calculate_stddev(returns_disney)
stddev_cbs = calculate_stddev(returns_cbs)

print('The standard deviation of Disney stock returns is', display_as_percentage(stddev_disney))
print('The standard deviation of CBS stock returns is', display_as_percentage(stddev_cbs))