'''
5. Write a Pandas program to convert a dictionary to a Pandas series.

'''

dict1 = {"First Name" : ["Kevin","Lebron","Kobe","Michael"],
        "Last Name" : ["Durant","James","Bryant","Jordan"],
        "Team" : ["Brooklyn Nets","Los Angeles Lakers","Los Angeles Lakers","Chicago Bulls"]
        }

import pandas as pd

pd_series = pd.Series(dict1)
print(pd_series)