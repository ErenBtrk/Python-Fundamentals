'''
28. Write a Pandas program to get the day of month, day of year,
week number and day of week from a given series of date strings. 

'''

import pandas as pd

pd_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])

new_series = pd.to_datetime(pd_series)

print(new_series.map(lambda x:x.strftime("%d")))
print(new_series.map(lambda x:x.strftime("%j")))
print(new_series.map(lambda x:x.strftime("%U")))
print(new_series.map(lambda x:x.strftime("%A")))    