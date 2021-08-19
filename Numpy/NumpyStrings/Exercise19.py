'''
19. Write a NumPy program to add two zeros to the beginning
of each element of a given array of string values.

'''

import numpy as np

np_array = np.array(['1.12' ,'2.23' ,'3.71' ,'4.23' ,'5.11'])

print(np.char.zfill(np_array,6))