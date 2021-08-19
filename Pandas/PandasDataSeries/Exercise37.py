'''
37. Write a Pandas program to stack two given series vertically and horizontally.

'''

import pandas as pd

pd_series1 = pd.Series([1,2,3,4,5])
pd_series2 = pd.Series(["a","b","c","d","e"])

df = pd.DataFrame(pd_series1)
df[1] = pd.Series(pd_series2)

print(df)


series1 = pd.Series(range(10))
series2 = pd.Series(list('pqrstuvwxy'))
print("Original Series:")
print(series1)
print(series2)
df = pd.concat([series1, series2], axis=1)
print("\nStack two given series vertically and horizontally:")
print(df)