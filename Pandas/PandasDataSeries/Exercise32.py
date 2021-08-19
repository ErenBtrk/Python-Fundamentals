'''
32. Write a Pandas program to find the positions of the values 
neighboured by smaller values on both sides in a given series.

'''

import pandas as pd
import numpy as np

pd_series = pd.Series([1,8,7,5,6,5,3,4,7,1])
list1 = []
for i in range(len(pd_series)):
    if i == 0:
        continue
    else:
        if pd_series[i] > pd_series[i-1] and pd_series[i] > pd_series[i+1]:
            list1.append(i)

print(list1)

###############################################################

nums = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("Original series:")
print(nums)
print("\nPositions of the values surrounded by smaller values on both sides:")
temp = np.diff(np.sign(np.diff(nums)))
result = np.where(temp == -2)[0] + 1
print(result)