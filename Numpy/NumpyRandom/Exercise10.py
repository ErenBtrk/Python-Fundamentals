'''
10. Write a NumPy program to check two random arrays are equal or not. 

'''

import numpy as np

np_array1 = np.random.randint(1,10,5)
print(np_array1)

np_array2 = np.random.randint(1,10,5)
print(np_array2)

print(np.allclose(np_array1,np_array2))