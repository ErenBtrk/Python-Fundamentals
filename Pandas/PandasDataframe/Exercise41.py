'''

41. Write a Pandas program to convert DataFrame column type from string to datetime.

'''

import pandas as pd
import numpy as np

s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'])
print("String Date:")
print(s)
r = pd.to_datetime(pd.Series(s))
df = pd.DataFrame(r)
print("Original DataFrame (string to datetime):")
print(df)
