# 11- Find the max,min and average values of the matrix in exercise 9

import numpy as np

np_matrix = np.random.randint(10,50,15)
print(np_matrix)
np_matrix = np_matrix.reshape(3,5)
print(np_matrix)

minValue = np_matrix.min()
print(minValue)

maxValue = np_matrix.max()
print(maxValue)

average = np_matrix.mean()
print(f"{average:.4}")