'''
9. Write a Pandas program to convert a given Series to an array.

'''

import pandas as pd
import numpy as np

pd_series = pd.Series([1,2,3,4,5])

np_array = np.array(pd_series.values.tolist())
print(np_array)
print(type(np_array))

