'''
20. Write a Pandas program to display most frequent value in a given
series and replace everything else as 'Other' in the series.

'''

import pandas as pd

pd_series = pd.Series([1,3,5,1,4,3,1,5,3,3,1,3])

value = pd_series.mode().values[0]

relationalVar = pd_series != value

pd_series[relationalVar] = "Other"

print(pd_series)