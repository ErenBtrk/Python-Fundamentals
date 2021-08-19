'''
17. Write a NumPy program to check whether each element of a given array
is composed of digits only, lower case letters only and upper case letters only.

'''

import numpy as np

np_array = np.array(['Python','PHP','JS','Examples','html5','5'])

print(np.char.isdigit(np_array))
print(np.char.islower(np_array))
print(np.char.isupper(np_array))