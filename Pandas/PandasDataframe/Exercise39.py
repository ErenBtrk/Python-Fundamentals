'''

39. Write a Pandas program to combining two series into a DataFrame.

'''

import pandas as pd
import numpy as np

s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
s2 = pd.Series(['10', '20', 'php', '30.12', '40'])

df = pd.DataFrame(pd.concat([s1,s2],axis=1))

print(df)





