'''
11. Write a NumPy program to create random vector of size 15 and replace the maximum value by -1

'''

import numpy as np

np_vector = np.random.random(size=15)
print(np_vector)

print("Max value = ",np_vector.max())

np_vector[np_vector.argmax()] = -1

print(np_vector)