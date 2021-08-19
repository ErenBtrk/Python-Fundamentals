'''

36. Write a Pandas program to drop a list of rows from a specified DataFrame.

'''


import pandas as pd
import numpy as np
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(d)

print(df)

print(df.drop([2,4],axis=0))