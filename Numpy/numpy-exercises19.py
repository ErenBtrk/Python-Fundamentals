# Which elements of the matrix are greater than 0 and even numbers.
# Matrix elements are between -50 and +50

import numpy as np

np_matrix = np.arange(-50,50)
print(np_matrix)

relationalVar1 = np_matrix > 0 
positiveNums = np_matrix[relationalVar1]
print(positiveNums)

relationalVar2 = positiveNums % 2 == 0
result = positiveNums[relationalVar2]
print(result)