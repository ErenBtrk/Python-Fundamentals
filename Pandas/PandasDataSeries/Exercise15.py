'''
15. Write a Pandas program to create the mean and standard deviation of the data of a given Series. 

'''

import pandas as pd

pd_series = pd.Series([1,2,3,4,5])

print(pd_series.mean())
print(pd_series.std())