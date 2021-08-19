'''
18. Write a Pandas program to compute the minimum, 25th 
percentile, median, 75th, and maximum of a given series.

'''

import pandas as pd
import numpy as np

pd_series = pd.Series([1,2,3,4,5,6])

print(pd_series.min())
print(pd_series.max())
print(pd_series.median())
print(np.percentile(a=pd_series,q=[0,25,50,75,100]))  