'''
16. Write a Pandas program to get the items of a given series not present in another given series.

'''

import pandas as pd

pd_series = pd.Series([1,2,3,4,5])
pd_series2 = pd.Series([1,3,5,7,9])

relationalVar = ~pd_series.isin(pd_series2)

print(pd_series[relationalVar])