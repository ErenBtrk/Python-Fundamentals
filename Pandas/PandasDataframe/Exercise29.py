'''
29. Write a Pandas program to delete DataFrame row(s) based on given column value.

'''

import pandas as pd

df1 = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})

relationalVar = df1["name"] == "James"

df1 = df1.drop(df1[relationalVar],axis=1)
print(df1)