'''
29. Write a Pandas program to convert year-month string to dates adding a specified day of the month.

'''


import pandas as pd
from dateutil.parser import parse

pd_series = pd.Series(["Jan 2015","Feb 2016","Mar 2017","Apr 2018","May 2019"])



changeDay = lambda x : x.day + 10
print(pd_series.map(lambda x : parse("10"+ x)))

