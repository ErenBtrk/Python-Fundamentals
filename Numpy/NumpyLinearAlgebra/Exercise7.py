'''
7. Write a NumPy program to compute the eigenvalues and right eigenvectors of a given square array.

'''

import numpy as np
m = np.mat("3 -2;1 0")
print("Original matrix:")
print("a\n", m)
w, v = np.linalg.eig(m) 
print( "Eigenvalues of the said matrix",w)
print( "Eigenvectors of the said matrix",v)