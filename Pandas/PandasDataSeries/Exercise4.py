'''
4. Write a Pandas program to compare the elements of the two Pandas Series.

'''

import pandas as pd

pd_series1 = pd.Series([1,2,3,4,5])
pd_series2 = pd.Series([1,1,3,3,5])

print(pd_series1 > pd_series2)
print(pd_series1 < pd_series2)
print(pd_series1 >= pd_series2)
print(pd_series1 <= pd_series2)
print(pd_series1 == pd_series2)
print(pd_series1 != pd_series2)
