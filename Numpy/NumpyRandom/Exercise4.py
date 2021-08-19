'''
4. Write a NumPy program to create a 5x5 array with 
random values and find the minimum and maximum values. 

'''

import numpy as np

np_matrix = np.random.normal(size=25).reshape(5,5)

print(np_matrix)

print("min value",np_matrix.min())
print("max value",np_matrix.max())