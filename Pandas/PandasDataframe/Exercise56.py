'''

56. Write a Pandas program to get column index from column name of a given DataFrame.

'''

import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print("\nIndex of 'col2'")
print(df.columns.get_loc("col2"))   