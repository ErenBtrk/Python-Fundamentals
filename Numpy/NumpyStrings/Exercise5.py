'''
5. Write a NumPy program to insert a space between characters of all the elements of a given array.

'''

import numpy as np

np_array = np.array(["Kevin Durant","Lebron James","Michael Jordan"])
idx = (1,3)
new_array = np.char.join("-",np_array)
print(new_array)