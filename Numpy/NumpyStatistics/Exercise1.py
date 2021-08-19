'''
1. Write a Python program to find the maximum and minimum value of a given flattened array.

'''

import numpy as np

np_array = np.random.randint(0,100,10)

print(np_array)

print(np.amax(np_array))

print(np.amin(np_array))
