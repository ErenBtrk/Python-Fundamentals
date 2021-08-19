'''
9. Write a NumPy program to find the nearest value from a given value in an array.

'''

import numpy as np

value = 10

np_array = np.random.randint(1,20,5)

print(np_array)

n = np_array.flat[np.abs(np_array - value).argmin()]

print(n)