'''
21. Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series.

'''

import pandas as pd
import numpy as np

pd_series = pd.Series([1,5,2,10,15,30])

relationalVar = pd_series % 5 == 0

print(pd_series[relationalVar].index.values)

##############################################################

result = [ pd.Index(pd_series).get_loc(item) for item in pd_series if item % 5 == 0 ]
print(result)