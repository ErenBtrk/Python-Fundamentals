'''
2. Write a NumPy program to get the minimum and maximum value of a given array along the second axis.

'''

import numpy as np

np_array = np.random.randint(0,100,10).reshape(5,2)

print(np_array)

print(np.amax(np_array,1))
print(np.amin(np_array,1))