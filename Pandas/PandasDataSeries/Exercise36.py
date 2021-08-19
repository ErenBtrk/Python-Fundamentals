'''
36. Write a Pandas program to convert given series into a dataframe
 with its index as another column on the dataframe.
 
'''

import pandas as pd

pd_series = pd.Series(list('ABCDEFGHIJKLMNOP'))
print(pd_series.index.values)
pd_df = pd.DataFrame(pd_series)
pd_df[1] = pd_series.index.values
print(pd_df)

import numpy as np
char_list = list('ABCDEFGHIJKLMNOP')
num_arra = np.arange(16)
num_dict = dict(zip(char_list, num_arra))
num_ser = pd.Series(num_dict)
df = num_ser.to_frame().reset_index()
print(df)