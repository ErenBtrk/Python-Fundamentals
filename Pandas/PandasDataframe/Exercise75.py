'''

75. Write a Pandas program to use a local variable within a query.

'''

import pandas as pd
df = pd.DataFrame({'W':[68,75,86,80,66],'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print("Original DataFrame")
print(df)
maxx = df["W"].max()
print("\nValues which are less than maximum value of 'W' column")
print(df.query("W < @maxx"))