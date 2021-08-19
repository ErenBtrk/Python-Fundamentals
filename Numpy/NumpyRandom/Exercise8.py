'''
8. Write a NumPy program to create a random vector of size 10 and sort it.

'''

import numpy as np

np_vector = np.random.randint(1,20,10)

np_vector.sort()

print(np_vector)