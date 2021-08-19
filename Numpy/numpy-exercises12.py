# 12- Find the max value's index of the matrix in exercise 9

import numpy as np

np_matrix = np.random.randint(10,50,15)
print(np_matrix)
np_matrix = np_matrix.reshape(3,5)
print(np_matrix)

maxValue = np_matrix.max()
print(maxValue)

maxValueIndex = np_matrix.argmax()
print(maxValueIndex)

