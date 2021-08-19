'''
14. Write a NumPy program to compute the condition number of a given matrix.

'''

import numpy as np
m = np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
result =  np.linalg.cond(m)
print("Condition number of the said matrix:")
print(result)