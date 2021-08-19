'''

6. Write a Pandas program to create a horizontal stacked bar plot of 
opening, closing stock prices of Alphabet Inc. between two specific dates.

'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet-stock-data.txt")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-4-30')                         
df['Date'] = pd.to_datetime(df['Date']).dt.date
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Date', 'Open', 'Close']]
df3 = df2.set_index('Date')
df3.plot.barh(stacked=True)
plt.ylabel("Price")
plt.suptitle('Opening/Closing stock prices Alphabet Inc.,\n01-04-2020 to 30-04-2020', fontsize=12, color='black')
plt.show()