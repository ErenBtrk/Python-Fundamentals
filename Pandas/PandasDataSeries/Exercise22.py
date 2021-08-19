'''
22. Write a Pandas program to extract items at given positions of a given series.

'''

import pandas as pd

pd_series = pd.Series([1,2,3,4,5,6,7,8,9])

print(pd_series.drop(index=[0,2,4,6,8]))
