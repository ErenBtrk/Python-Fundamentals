'''
27. Write a Pandas program to write a DataFrame to CSV file using tab separator.

'''

import pandas as pd
import numpy as np


d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)

df.to_csv("exercise27.csv",sep='\t',index=False)

print(pd.read_csv("exercise27.csv"))