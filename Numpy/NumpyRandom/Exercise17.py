'''
17. Write a NumPy program to create a three-dimension array
with shape (300,400,5) and set to a variable. Fill the array
elements with values using unsigned integer (0 to 255).

'''

import numpy as np

np_matrix = np.random.randint(0,256,600000,dtype=np.uint8).reshape(300,400,5)
print(np_matrix)
