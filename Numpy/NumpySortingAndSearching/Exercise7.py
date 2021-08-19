'''
7. Write a NumPy program to partition a given array in a specified position
and move all the smaller elements values to the left of the partition, and
the remaining values to the right, in arbitrary order (based on random choice).

'''

import numpy as np
nums = np.array([70, 50, 20, 30, -11, 60, 50, 40])
print("Original array:")
print(nums)
print("\nAfter partitioning on 4 the position:")
print(np.partition(nums, 4))