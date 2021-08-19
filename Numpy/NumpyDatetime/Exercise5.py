'''
5. Write a NumPy program to find the first Monday in May 2017.

'''

import numpy as np
print("First Monday in May 2017:")
print(np.busday_offset('2017-05', 0, roll='forward', weekmask='Mon'))