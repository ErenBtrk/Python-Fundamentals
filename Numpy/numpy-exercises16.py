# 16-What is the element in 2.row and 3.column of the matrix in exercise 9

import numpy as np

np_matrix = np.random.randint(10,50,15)
np_matrix = np_matrix.reshape(3,5)
print(np_matrix)

print(np_matrix[1,2])