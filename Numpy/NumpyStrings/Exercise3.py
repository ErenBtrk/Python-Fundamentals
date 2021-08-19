'''
3. Write a NumPy program to capitalize the first letter, lowercase,
uppercase, swapcase, title-case of all the elements of a given array.

'''

import numpy as np

np_array = np.array(["kevin durant","lebron james","kobe bryant"])

print(np.char.capitalize(np_array))
print(np.char.lower(np_array))
print(np.char.upper(np_array))
print(np.char.swapcase(np_array))
print(np.char.title(np_array))

