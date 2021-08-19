'''
23. Write a Pandas program to get the positions of items of a given series in another given series.

'''

import pandas as pd

pd_series = pd.Series([1,2,3,4,5,6,7,8,9])

pd_series2 = pd.Series([2,4,6,8])


result = [pd.Index(pd_series).get_loc(item) for item in pd_series2]
print(result)
