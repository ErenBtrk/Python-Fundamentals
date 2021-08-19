'''
13. Write a NumPy program to replace "PHP" with "Python" in the element of a given array.

'''

import numpy as np

np_array = np.array(['PHP Exercises, Practice, Solution'])

new_array = np.char.replace(np_array,"PHP","Python")

print(new_array)