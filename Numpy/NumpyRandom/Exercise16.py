'''
16. Write a NumPy program to get the n largest values of an array.

'''

import numpy as np
x = np.random.randint(0,50,10)
print("Original array:")
print(x)
np.random.shuffle(x)
n = 5
print (x[np.argsort(x)[-n:]])