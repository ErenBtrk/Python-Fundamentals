'''
6. Write a NumPy program to compute the weighted of a given array.

'''

import numpy as np
x = np.arange(5)
print("\nOriginal array:")
print(x)
weights = np.arange(1, 6)
print("\nWeights : ")
print(weights)
r1 = np.average(x, weights=weights)
print("\nr1 : ")
print(r1)
r2 = (x*(weights/weights.sum())).sum()
print("\nr2 : ")
print(r2)
assert np.allclose(r1, r2)
print("\nWeighted average of the said array:")
print(r1)