'''

63. Write a Pandas program to remove last n rows of a given DataFrame.

'''

import pandas as pd
from pandas.core.indexes.base import Index
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)

NumberOfRowsToRemove = 3
IndexOfRowsToRemove = df.tail(NumberOfRowsToRemove).index.tolist()

df1 = df.drop(index = IndexOfRowsToRemove)
print(df1)

df2 = df.iloc[:3]
print(df2)


