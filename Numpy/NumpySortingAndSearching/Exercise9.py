'''
9. Write a NumPy program to sort an given array by the nth column.

'''

import numpy as np

np_array = np.array([2,5,4,3,10,8,6,1,9,7]).reshape(5,2)
print("Original Array:\n")
print(np_array)
print("\nSort the said array by the nth column: ")
print(np_array[np_array[:,1].argsort()])
