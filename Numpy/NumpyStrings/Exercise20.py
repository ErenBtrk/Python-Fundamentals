'''
20. Write a NumPy program to replace a specific character
with another in a given array of string values.

'''

import numpy as np

np_array = np.array(['Python' ,'PHP' ,'JS' ,'examples' ,'html'])

print(np.char.replace(np_array,"P","B"))