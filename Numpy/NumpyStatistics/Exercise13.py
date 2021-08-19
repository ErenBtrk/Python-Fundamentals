'''
13. Write a Python program to count number of occurrences of each value
 in a given array of non-negative integers.
Note: bincount() function count number of occurrences of each value
in an array of non-negative integers in the range of the array between
the minimum and maximum values including the values that did not occur.

'''

import numpy as np
array1 = [0, 1, 6, 1, 4, 1, 2, 2, 7] 
print("Original array:")
print(array1)
print("Number of occurrences of each value in array: ")
print(np.bincount(array1))