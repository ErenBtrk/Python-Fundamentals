'''

11. Write a Pandas program to create a stacked histograms plot with more bins of 
opening, closing, high, low stock prices of Alphabet Inc. between two specific dates.

'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet-stock-data.txt")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')                         
df['Date'] = pd.to_datetime(df['Date']) 
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Open','Close','High','Low']]
df2.hist()
plt.suptitle('Opening/Closing/High/Low stock prices of Alphabet Inc., From 01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.show()