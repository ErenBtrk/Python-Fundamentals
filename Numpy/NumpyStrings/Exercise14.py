'''
14. Write a NumPy program to test equal, not equal, greater equal,
 greater and less test of all the elements of two given arrays.
 
'''

import numpy as np

np_array1 = np.array(["Kevin Durant","Lebron James","Michael Jordan"])
np_array2 = np.array(["Kobe Bryant","Hakeem Olajuwon","Michael Jordan"])

print(np.char.equal(np_array1,np_array2))
print(np.char.not_equal(np_array1,np_array2))
print(np.char.greater(np_array1,np_array2))
print(np.char.greater_equal(np_array1,np_array2))