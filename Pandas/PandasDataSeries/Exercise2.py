'''
2. Write a Pandas program to convert a Panda module Series to Python list and it's type.

'''

import pandas as pd

pd_series = pd.Series([1,2,3,4,5])

print(pd_series)
print(type(pd_series))

pd_series = pd_series.tolist()
print(pd_series)
print(type(pd_series))