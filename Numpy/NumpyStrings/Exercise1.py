'''
1. Write a NumPy program to concatenate element-wise two arrays of string. 

'''

import numpy as np

np_array1 = np.array(["Kevin","Lebron","Michael","Kobe"])
np_array2 = np.array(["Durant","James","Michael","Bryant"])

new_array = np.char.add(np_array1,np_array2)
print(new_array)