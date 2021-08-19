'''
11. Write a Pandas program to sort a given Series.

'''

import pandas as pd

pd_series = pd.Series(["b","c","a","d","z","i"])

print(pd_series.sort_values(ignore_index=True))