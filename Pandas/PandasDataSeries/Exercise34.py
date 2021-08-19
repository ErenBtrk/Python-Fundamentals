'''
34. Write a Pandas program to compute the autocorrelations of a given numeric series. 
From Wikipedia:
Autocorrelation, also known as serial correlation, is the correlation of a signal with
a delayed copy of itself as a function of delay. Informally, it is the similarity between
observations as a function of the time lag between them

'''

import pandas as pd
import numpy as np
num_series = pd.Series(np.arange(15) + np.random.normal(1, 10, 15))
print("Original series:")
print(num_series)
autocorrelations = [num_series.autocorr(i).round(2) for i in range(11)]
print("\nAutocorrelations of the said series:")
print(autocorrelations[1:])