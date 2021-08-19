'''
1. Write a NumPy program to sort a given array of shape 2
along the first axis, last axis and on flattened array.

'''

import numpy as np
a = np.array([[10,40],[30,20]])
print("Original array:")
print(a)
print("Sort the array along the first axis:")
print(np.sort(a, axis=0))
print("Sort the array along the last axis:")
print(np.sort(a))
print("Sort the flattened array:")
print(np.sort(a, axis=None))