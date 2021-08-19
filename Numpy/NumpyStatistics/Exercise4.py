'''
4. Write a NumPy program to compute the 80th percentile
for all elements in a given array along the second axis.

'''

import numpy as np

np_array = np.random.randint(0,10,12).reshape(2,6)
print(np_array)

print(np.percentile(np_array,50,1))