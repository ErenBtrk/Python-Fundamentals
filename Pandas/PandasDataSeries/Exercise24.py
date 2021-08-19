'''
24. Write a Pandas program convert the first and last character
 of each word to upper case in each word of a given series.
 
'''

import pandas as pd
import numpy as np

pd_series = pd.Series(["kevin","lebron","kobe","michael"])


print(pd_series.map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper() ))



