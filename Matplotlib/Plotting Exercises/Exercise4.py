'''
4. Write a Pandas program to create a bar plot of opening, closing
stock prices of Alphabet Inc. between two specific dates.
 
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("alphabet-stock-data.txt")
start_date = pd.to_datetime('2020-4-1')
print(start_date)
end_date = pd.to_datetime('2020-09-30')                      
df['Date'] = pd.to_datetime(df['Date']).dt.date

new_df = (df['Date']>= start_date) & (df['Date']<= end_date)

df2 = df.loc[new_df]
x = np.arange(len(df2["Date"]))
width = 0.2

fig,ax= plt.subplots()
rects1 = ax.bar(x - width/2, df2["Open"], width, label='Open')
rects2 = ax.bar(x + width/2, df2["Close"], width, label='Close')

ax.set_ylabel('Prices')
ax.set_title('opening, closing stock prices of Alphabet Inc.')
ax.set_xticks(x)
ax.set_xticklabels(df2["Date"],rotation=90)
ax.legend()


fig.tight_layout()

plt.show()