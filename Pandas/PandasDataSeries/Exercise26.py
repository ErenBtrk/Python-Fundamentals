'''
26. Write a Pandas program to compute difference of differences
between consecutive numbers of a given series.
 
'''

import pandas as pd

pd_series = pd.Series([1,3,6,10,15,16,20,15])

print(pd_series)
print(pd_series.diff())
print(pd_series.diff().diff())
