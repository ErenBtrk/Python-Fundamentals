'''
13. Write a NumPy program to find the most frequent value in an array.

'''

import numpy as np
x = np.random.randint(0, 10, 40)
print("Original array:")
print(x)
print("Most frequent value in the above array:")
print(np.unique(x))
print(np.bincount(x))
print(np.bincount(x).argmax())