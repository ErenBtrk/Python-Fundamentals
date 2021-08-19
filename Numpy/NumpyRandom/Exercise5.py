'''
5. Write a NumPy program to create a random 10x4 array and extract
the first five rows of the array and store them into a variable.
 
'''

import numpy as np

np_matrix = np.random.randint(0,100,40).reshape(10,4)
print(np_matrix)
print('*'*75)

var = np_matrix[0:5:]

print(var)