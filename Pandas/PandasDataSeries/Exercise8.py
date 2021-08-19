'''
8. Write a Pandas program to convert the first column of a DataFrame as a Series.

'''

import pandas as pd

dict1 = {
        "First Name" : ["Kevin","Lebron","Kobe","Michael"],
        "Last Name" : ["Durant","James","Bryant","Jordan"],
        "Team" : ["Brooklyn Nets","Los Angeles Lakers","Los Angeles Lakers","Chicago Bulls"]
        }

df = pd.DataFrame(data=dict1)
print(df)
print(type(df))

pd_series = df.iloc[:,0]
print(pd_series)
print(type(pd_series))