'''
4. Write a NumPy program to make the length of each element 15 of a given array
and the string centered / left-justified / right-justified with paddings of _.

'''

import numpy as np

np_array = np.array(["Kevin Durant","Lebron James","Michael Jordan"])

new_array = np.char.center(np_array,20,'_')
print(new_array)

new_array = np.char.ljust(np_array,20,'_')
print(new_array)

new_array = np.char.rjust(np_array,20,'_')
print(new_array)