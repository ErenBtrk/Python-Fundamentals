'''
10. Write a Pandas program to convert Series of lists to one Series. 

'''

import pandas as pd

pd_series = pd.Series([[1,2,3],["a","b","c"],[True,True,False]])
print(pd_series)
print(type(pd_series))

new_series = pd.Series([],dtype=int)
print(new_series)

j = 0

for item in pd_series:
    for item2 in item:
        new_series[j] = item2
        j = j+1

print(new_series)
print(type(new_series))

######################################################

import pandas as pd
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
print("Original Series of list")
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print("One Series")
print(s)
