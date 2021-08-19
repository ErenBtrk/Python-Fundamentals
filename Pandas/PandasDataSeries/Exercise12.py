'''
12. Write a Pandas program to add some data to an existing Series.

'''

import pandas as pd

pd_series = pd.Series([1,2,3,4,5])

print(pd_series.append(pd.Series([True,"Python"])))

