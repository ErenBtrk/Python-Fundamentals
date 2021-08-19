'''
6. Write a Pandas program to convert a NumPy array to a Pandas series.

'''

import numpy as np
import pandas as pd

np_array = np.array([1,2,3,4,5])
print(np_array)
print(type(np_array))

pd_series = pd.Series(np_array)
print(pd_series)
print(type(pd_series))