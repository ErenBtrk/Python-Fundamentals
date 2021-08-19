'''
10. Write a NumPy program to find a matrix or vector norm.

'''

import numpy as np
v = np.arange(7)
result = np.linalg.norm(v)
print("Vector norm:")
print(result)
m = np.matrix('1, 2; 3, 4')
print(m) 
result1 = np.linalg.norm(m)
print("Matrix norm:")
print(result1)