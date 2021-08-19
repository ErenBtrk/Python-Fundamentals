'''
16. Write a NumPy program to count the lowest index of "P" in a given array, element-wise.

'''

import numpy as np

np_array = np.array(['Python' ,'PHP' ,'JS' ,'examples' ,'html'])
print("\nOriginal Array:")
print(np_array)
print("count the lowest index of ‘P’:")
r = np.char.find(np_array, "P")
print(r)