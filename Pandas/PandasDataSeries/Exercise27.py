'''
27. Write a Pandas program to convert a series of date strings to a timeseries.

'''

import pandas as pd

pd_series = pd.Series(["01 Jan 2015",
                       "10-02-2016",
                       "20180307",
                       "2014/05/06",
                       "2016-04-12",
                       "2019-04-06T11:20"
                     ])

print(pd.to_datetime(pd_series))