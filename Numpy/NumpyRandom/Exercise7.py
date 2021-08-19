'''
7. Write a NumPy program to normalize a 3x3 random matrix.

'''

import numpy as np
x= np.random.random((3,3))
print("Original Array:")
print(x)
xmax, xmin = x.max(), x.min()
x = (x - xmin)/(xmax - xmin)
print("After normalization:")
print(x)