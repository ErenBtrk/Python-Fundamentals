'''
6. Write a NumPy program to shuffle numbers between 0 and 10 (inclusive).

'''

import numpy as np

np_array = np.arange(11)

np.random.shuffle(np_array)

print(np_array)