'''
3. Write a NumPy program to create a 3x3x3 array with random values.

'''

import numpy as np

np_matrix = np.arange(0,27).reshape(3,3,3)

print(np_matrix)