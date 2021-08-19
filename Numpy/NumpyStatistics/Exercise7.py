'''
7. Write a NumPy program to compute the mean, standard deviation,
 and variance of a given array along the second axis.
 
'''

import numpy as np
x = np.arange(6)
print("\nOriginal array:")
print(x)
r1 = np.mean(x)
r2 = np.average(x)
assert np.allclose(r1, r2)
print("\nMean: ", r1)
r1 = np.std(x)
r2 = np.sqrt(np.mean((x - np.mean(x)) ** 2 ))
assert np.allclose(r1, r2)
print("\nstd: ", r1)
r1= np.var(x)
r2 = np.mean((x - np.mean(x)) ** 2 )
assert np.allclose(r1, r2)
print("\nvariance: ", r1)