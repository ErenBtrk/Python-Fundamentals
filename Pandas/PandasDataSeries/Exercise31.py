'''
31. Write a Pandas program to compute the Euclidean distance between two given series.

'''

import pandas as pd
import numpy as np

pd_series = pd.Series([1,2,3,4,5])

pd_series2 = pd.Series([6,7,8,9,10])

print(np.linalg.norm(pd_series-pd_series2))