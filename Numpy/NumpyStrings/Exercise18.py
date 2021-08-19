'''
18. Write a NumPy program to check whether each element of a given array starts with "P".

'''

import numpy as np

np_array = np.array(['Python' ,'PHP' ,'JS' ,'examples' ,'html'])

print(np.char.startswith(np_array,"P"))

