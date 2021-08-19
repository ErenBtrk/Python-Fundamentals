# 9- Create a 3 x 5 matrix with values between 10-50

import numpy as np

np_matrix = np.random.randint(10,50,15)
print(np_matrix)
np_matrix = np_matrix.reshape(3,5)
print(np_matrix)