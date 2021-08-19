'''

17. Write a Pandas program to create a plot to visualize daily percentage 
returns of Alphabet Inc. stock price between two specific dates. 

'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet-stock-data.txt")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')                         
df['Date'] = pd.to_datetime(df['Date']) 
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Date', 'Adj Close']]
df3 = df2.set_index('Date')
daily_changes = df3.pct_change(periods=1)
daily_changes['Adj Close'].plot(figsize=(10,7),legend=True,linestyle='--',marker='o')
plt.suptitle('Daily % return of Alphabet Inc. stock price,\n01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.grid(True)
plt.show()