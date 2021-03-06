'''

58. Write a Pandas program to select all columns, except one given column in a DataFrame.

'''

import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print("\nAll columns except 'col3':")
df = df.loc[:, df.columns != 'col2']
print(df)