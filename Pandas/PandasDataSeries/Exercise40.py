'''
40. Write a Pandas program to check inequality over the
index axis of a given dataframe and a given series.

'''

import pandas as pd
import numpy as np

df_data = pd.DataFrame({'W':[68,75,86,80,None],'X':[78,75,None,80,86], 'Y':[84,94,89,86,86],'Z':[86,97,96,72,83]});
sr_data = pd.Series([68, 75, 86, 80, None]) 

print(df_data)
print(df_data.ne(sr_data, axis = 0))