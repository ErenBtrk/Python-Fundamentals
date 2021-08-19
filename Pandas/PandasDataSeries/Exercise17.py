'''
17. Write a Pandas program to get the items which are not common of two given series.

'''

import pandas as pd

pd_series = pd.Series([1,2,3,4,5])
pd_series2 = pd.Series([2,4,6,8,10])

relationalVar = ~pd_series.isin(pd_series2)
relationalVar2 = ~pd_series2.isin(pd_series)

new_series = pd_series[relationalVar]
new_series = new_series.append(pd_series2[relationalVar2])
print(new_series)