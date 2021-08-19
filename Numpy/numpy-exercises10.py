# 10- Calculate the sum of columns and rows of matrix in exercise 9

import numpy as np

np_matrix = np.random.randint(10,50,15)
print(np_matrix)

np_matrix = np_matrix.reshape(3,5)
print(np_matrix)

columnSum = np_matrix.sum(axis=0)
print(columnSum)

rowSum = np_matrix.sum(axis=1)
print(rowSum)