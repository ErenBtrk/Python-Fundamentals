'''

78. Write a Pandas program to replace the current value in a dataframe
column based on last largest value. If the current value is less than
last largest value replaces the value with 0. 

'''

import pandas as pd
df1=pd.DataFrame({'rnum':[23, 21, 27, 22, 34, 33, 34, 31, 25, 22, 34, 19, 31, 32, 19]})
print("Original DataFrame:")
print(df1)
df1['rnum']=df1.rnum.where(df1.rnum.eq(df1.rnum.cummax()),0)
print("\nReplace current value in a dataframe column based on last largest value:")
print(df1)