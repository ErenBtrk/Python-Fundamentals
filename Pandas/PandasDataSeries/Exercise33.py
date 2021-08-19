'''
33. Write a Pandas program to replace missing white spaces
 in a given string with the least frequent character. 
 
'''

import pandas as pd
import numpy as np

pd_series = pd.Series(["abc def abcdef icd"])

new_series = pd.Series(list(pd_series[0]))

a = [item for item in range(len(new_series.value_counts())) if item == new_series.value_counts().argmin()]

leastFreqVal = new_series.value_counts()[a].index.values[0]

print(pd_series.str.replace(" ",leastFreqVal).values[0])


#############################################################################


str1 = 'abc def abcdef icd'
print("Original series:")
print(str1)
ser = pd.Series(list(str1))
element_freq = ser.value_counts()
print(element_freq)
current_freq = element_freq.dropna().index[-1]
result = "".join(ser.replace(' ', current_freq))
print(result)

