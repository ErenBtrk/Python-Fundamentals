'''

49. Write a Pandas program to append data to an empty DataFrame. 

'''

import pandas as pd
import numpy as np

df = pd.DataFrame()

data = pd.DataFrame({'col1' : [0,1,2],
        'col2' : [0,1,2]})

df = df.append(data)

print(df)