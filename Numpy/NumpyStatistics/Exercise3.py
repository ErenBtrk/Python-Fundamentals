'''
3. Write a NumPy program to calculate the difference between the
maximum and the minimum values of a given array along the second axis.

'''

import numpy as np

np_array = np.random.randint(0,100,12).reshape(4,3)
print(np_array)

maxVal = np.amax(a=np_array,axis=1)
print(maxVal)

minVal = np.amin(a=np_array,axis=1)
print(minVal)

print(maxVal-minVal)

