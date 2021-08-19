'''
2. Write a NumPy program to repeat all the elements three times of a given array of string

'''

import numpy as np

np_array = np.array(["Kevin","Lebron","Kobe"])

np_array = np.repeat(np_array,3)

print(np_array)