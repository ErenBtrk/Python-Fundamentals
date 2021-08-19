'''
7. Write a Pandas program to change the data type of given a column or a Series.

'''

import pandas as pd

pd_series = pd.Series(['100', '200', 'python', '300.12', '400'])
print(pd_series)

pd_series2 = pd.to_numeric(pd_series,errors="coerce")
print(pd_series2)