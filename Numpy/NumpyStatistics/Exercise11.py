'''
11. Write a NumPy program to test element-wise of a given array for finiteness
(not infinity or not Not a Number), positive or negative infinity, for NaN,
for NaT (not a time), for negative infinity, for positive infinity. 

'''

import numpy as np
print("\nTest element-wise for finiteness (not infinity or not Not a Number):")
print(np.isfinite(1))
print(np.isfinite(0))
print(np.isfinite(np.nan))
print("\nTest element-wise for positive or negative infinity:")
print(np.isinf(np.inf))
print(np.isinf(np.nan))
print(np.isinf(np.NINF))
print("Test element-wise for NaN:")
print(np.isnan([np.log(-1.),1.,np.log(0)]))
print("Test element-wise for NaT (not a time):")
print(np.isnat(np.array(["NaT", "2016-01-01"], dtype="datetime64[ns]")))
print("Test element-wise for negative infinity:")
x = np.array([-np.inf, 0., np.inf])
y = np.array([2, 2, 2])
print(np.isneginf(x, y))
print("Test element-wise for positive infinity:")
x = np.array([-np.inf, 0., np.inf])
y = np.array([2, 2, 2])
print(np.isposinf(x, y))