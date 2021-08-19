'''
21. Write a NumPy program to count a given word in each row of a given array of string values.

'''

import numpy as np

np_array = np.array([['Python' ,'NumPy' ,'Exercises'],
                     ['Python' ,'Pandas' ,'Exercises'],
                     ['Python' ,'Machine learning' ,'Python']])

print(np.char.count(np_array,"Python"))
