'''
35. Write a Pandas program to create a TimeSeries to display all the Sundays of given year.

'''

import pandas as pd
result = pd.Series(pd.date_range('2021-01-01', periods=52, freq='W-SUN'))
print("All Sundays of 2021:")
print(result)
