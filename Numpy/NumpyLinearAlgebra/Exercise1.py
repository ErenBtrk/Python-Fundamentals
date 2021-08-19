'''
1. Write a NumPy program to compute the multiplication of two given matrixes.

'''

import numpy as np

np_matrix1 = np.arange(0,15).reshape(5,3)
print(np_matrix1)
np_matrix2 = (np.ones(9,int)*2).reshape(3,3)
print(np_matrix2)

print(f"Multiplication of matrixes :\n{np.dot(np_matrix1,np_matrix2)}")
