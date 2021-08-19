'''

45. Write a Pandas program to find the row for where the value of a given column is maximum.

'''

import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print("Row where col1 has maximum value:")
print(df['col1'].argmax())
print("Row where col2 has maximum value:")
print(df['col2'].argmax())
print("Row where col3 has maximum value:")
print(df['col3'].argmax())