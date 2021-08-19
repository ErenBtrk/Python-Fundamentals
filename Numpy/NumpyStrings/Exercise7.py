'''
7. Write a NumPy program to remove the leading and trailing
 whitespaces of all the elements of a given array.
 
'''

import numpy as np

np_array = np.array([" Kevin Durant "," Lebron James "," Michael Jordan "])
 
new_array = np.char.strip(np_array)

print(new_array)

