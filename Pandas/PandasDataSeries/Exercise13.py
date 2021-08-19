'''
13. Write a Pandas program to create a subset of a given series based on value and condition.

'''

import pandas as pd

pd_series = pd.Series([1,2,3,4,5])
print(pd_series)

relationalVar = pd_series > 3

new_series = pd_series[relationalVar]
new_series.index = [0,1]
print(new_series)