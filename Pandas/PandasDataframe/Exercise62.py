'''

62. Write a Pandas program to remove first n rows of a given DataFrame. 

'''

import pandas as pd
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print("\nAfter removing first 3 rows of the said DataFrame:")
df1 = df.iloc[3:]
print(df1)

df2 = df.drop(index=[3,4,5])
print(df2)