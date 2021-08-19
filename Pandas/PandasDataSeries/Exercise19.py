'''
19. Write a Pandas program to calculate the frequency counts of each unique value of a given series. 

'''

import pandas as pd

pd_series = pd.Series([1,3,5,1,4,3,1,5,3])

print(pd.value_counts(pd_series))