'''
5. Write a NumPy program to get the indices of the sorted elements of a given array.

'''

import numpy as np

np_array = np.random.randint(0,10,5)
print(np_array)

i = np.argsort(np_array)
np_array = np.sort(np_array)
print(np_array)
print("Indices of the sorted elements of a given array:")
print(i)