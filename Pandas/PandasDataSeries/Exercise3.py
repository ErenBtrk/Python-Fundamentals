'''
3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

'''

import pandas as pd

pd_series1 = pd.Series([1,2,3,4,5])
pd_series2 = pd.Series([1,1,1,1,1])

print(pd.Series.add(pd_series1,pd_series2))
print(pd.Series.subtract(pd_series1,pd_series2))
print(pd.Series.multiply(pd_series1,pd_series2))
print(pd.Series.divide(pd_series1,pd_series2))
