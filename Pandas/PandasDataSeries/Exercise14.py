'''
14. Write a Pandas program to change the order of index of a given series.

'''

import pandas as pd

pd_series = pd.Series([1,2,3,4,5])
print(pd_series)

pd_series.index = [5,4,3,2,1]
print(pd_series)