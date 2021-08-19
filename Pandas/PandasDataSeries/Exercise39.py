'''
39. Write a Pandas program to find the index of the first
occurrence of the smallest and largest value of a given series.

'''

import pandas as pd

pd_series1 = pd.Series([5,1,2,4,1,10,8,3,7,10,6,9])

print(pd_series1.idxmax())
print(pd_series1.idxmin())
