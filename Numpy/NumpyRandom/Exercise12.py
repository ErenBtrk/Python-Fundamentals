'''
12. Write a NumPy program to find point by point distances of
 a random vector with shape (10,2) representing coordinates.
 
'''

import numpy as np
a= np.random.random((10,2))
x,y = np.atleast_2d(a[:,0], a[:,1])
d = np.sqrt( (x-x.T)**2 + (y-y.T)**2)
print(d)