'''
25. Write a Pandas program to calculate the number of characters in each word in a given series.

'''

import pandas as pd

pd_series = pd.Series(["kevin","lebron","kobe","michael"])

print(pd_series.map(lambda x:len(x)))