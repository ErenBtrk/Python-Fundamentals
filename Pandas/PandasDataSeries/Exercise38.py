'''
38. Write a Pandas program to check the equality of two given series.

'''

import pandas as pd

pd_series1 = pd.Series([1,2,3,4,5])
pd_series2 = pd.Series([1,2,3,4,5])
pd_series3 = pd.Series([1,2,3,4,6])

print(pd.Series.equals(pd_series1,pd_series2))
print(pd.Series.equals(pd_series1,pd_series3))
print(pd_series1 == pd_series2)
print(pd_series1 == pd_series3)