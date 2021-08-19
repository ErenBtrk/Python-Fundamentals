'''
8. Write a NumPy program to compute the covariance matrix of two given arrays.

'''

import numpy as np
x = np.array([0, 1, 2])
y = np.array([2, 1, 0])
print("\nOriginal array1:")
print(x)
print("\nOriginal array1:")
print(y)
print("\nCovariance matrix of the said arrays:\n",np.cov(x, y))