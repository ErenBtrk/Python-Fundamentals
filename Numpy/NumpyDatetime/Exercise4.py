'''
4. Write a NumPy program to create 24 python datetime.datetime objects
 (single object for every hour), and then put it in a numpy array.
 
'''


import numpy as np
import datetime
start = datetime.datetime(2000, 1, 1)
dt_array = np.array([start + datetime.timedelta(hours=i) for i in range(24)])
print(dt_array)