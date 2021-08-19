'''
30. Write a Pandas program to filter words from a given series that contain atleast two vowels.

'''

import pandas as pd
from collections import Counter
color_series = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
print("Original Series:")
print(color_series)
print("\nFiltered words:")
result = mask = color_series.map(lambda c: sum([Counter(c.upper()).get(i, 0) for i in list('AEIOU')]) >= 2)
print(color_series[result])