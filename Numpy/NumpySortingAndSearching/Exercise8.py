'''
8. Write a NumPy program to sort the specified number of elements from beginning of a given array.

'''

import numpy as np

np_array = np.array([2,5,4,3,10,8,6,1,9,7])

print("Original array:")
print(np_array)
print("\nSorted first 5 elements:")
print(np_array[np.argpartition(np_array,range(5))])