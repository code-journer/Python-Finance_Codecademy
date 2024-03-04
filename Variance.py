"""
Title: Codecademy's Analyze Financial Data with Python

Topic: Calculating Financial Statistics - Variance (assessing the risk involved in an investment)

Description: One of the key statistics for understanding risk is variance. Variance is a measure of the spread of a dataset, 
or how far apart each value is from the mean. The greater the variance, the more spread out or variable the data is.

Variance (σ^2) = Σ (X_i - X̄)^2 / n
σ2: variance
n is the number of observations (data points).
X_i represents each individual data point.
X̄ is the mean of the data points.

Author: Eric Cantrell
Date: January 14, 2024
"""

import numpy as np # Will use to access variance (var) method

# Sample data sets
returns_disney = [0.22, 0.12, 0.01, 0.05, 0.04]
returns_cbs = [-0.13, -0.15, 0.31, -0.06, -0.29]

# Use numpy's var method to calculate variance
variance_disney = np.var(returns_disney)
variance_cbs = np.var(returns_cbs)

# Non specific sample data set
dataset = [10, 8, 9, 10, 12]

# Programmed method to calculate variance instead
def calculate_variance(dataset):
    mean = sum(dataset) / len(dataset)
    numerator = 0

    for data in dataset:
        numerator += (data - mean)**2

    variance = numerator / len(dataset)

    return variance

variance_disney = calculate_variance(returns_disney)
variance_cbs = calculate_variance(returns_cbs)

print('The variance of Disney stock returns is', variance_disney)
print('The variance of CBS stock returns is', variance_cbs)