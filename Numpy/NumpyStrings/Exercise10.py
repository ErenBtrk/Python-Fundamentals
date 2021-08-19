'''
10. Write a NumPy program to split the element of a given array with spaces. 

'''

import numpy as np

np_array = np.array([" Kevin Durant "," Lebron James "," Michael Jordan "])

new_array = np.char.split(np_array)

print(new_array)