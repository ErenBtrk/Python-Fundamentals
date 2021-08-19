'''
14. Write a NumPy program to convert cartesian coordinates to polar
coordinates of a random 10x2 matrix representing cartesian coordinates.

'''

import numpy as np
z= np.random.random((10,2))
x,y = z[:,0], z[:,1]
r = np.sqrt(x**2+y**2)
t = np.arctan2(y,x)
print(r)
print(t)