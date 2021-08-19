'''
4. Write a NumPy program to compute the determinant of a given square array.

'''

import numpy as np
from numpy import linalg as LA
a = np.array([[1, 0], [1, 2]])
print("Original 2-d array")
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a))

b = np.array([[1,3,2],[2,1,3],[3,2,1]])
print("Original 2-d array")
print(b)
print("Determinant of the said 2-D array:")
print(np.linalg.det(b))