# 18- Calculate squares of the elements of the matrix in exercise 9

import numpy as np

np_matrix = np.random.randint(10,50,15)
np_matrix = np_matrix.reshape(3,5)
print(np_matrix)

np_matrix_square = np.power(np_matrix,2)
print(np_matrix_square)