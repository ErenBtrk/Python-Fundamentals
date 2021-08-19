'''
15. Write a NumPy program to find the closest value (to a given scalar) in an array.

'''

import numpy as np
x = np.arange(100)
print("Original array:")
print(x)
a = np.random.uniform(0,100)
print("Value to compare:")
print(a)
index = (np.abs(x-a)).argmin()
print(x[index])