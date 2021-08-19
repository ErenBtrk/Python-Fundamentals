'''
15. Write a NumPy program to count the number of "P" in a given array, element-wise.

'''

import numpy as np

np_array = np.array(['Python' ,'PHP' ,'JS' ,'examples' ,'html'])

print(np.char.count(np_array,"P"))