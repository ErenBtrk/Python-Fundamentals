'''

54. Write a Pandas program to convert a given list of lists into a Dataframe. 

'''

import pandas as pd

my_lists = [['col1', 'col2'], [2, 4], [1, 3]]
# sets the headers as list
headers = my_lists.pop(0) 
print("Original list of lists:")
print(my_lists)
df = pd.DataFrame(my_lists, columns = headers)
print("New DataFrame")
print(df)