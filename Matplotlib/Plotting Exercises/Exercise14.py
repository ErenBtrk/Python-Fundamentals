'''

14. Write a Pandas program to create a plot of adjusted closing prices, thirty days
 and forty days simple moving average of Alphabet Inc. between two specific dates.

What Is Simple Moving Average (SMA)?
A simple moving average (SMA) is an arithmetic moving average calculated by adding
recent prices and then dividing that figure by the number of time periods in the
calculation average. For example, one could add the closing price of a security
for a number of time periods and then divide this total by that same number of periods.
Short-term averages respond quickly to changes in the price of the underlying security,
while long-term averages are slower to react.


'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet-stock-data.txt")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')                         
df['Date'] = pd.to_datetime(df['Date']) 
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
stock_data = df1.set_index('Date')
close_px = stock_data['Adj Close']
stock_data['SMA_30_days'] = stock_data.iloc[:,4].rolling(window=30).mean() 
stock_data['SMA_40_days'] = stock_data.iloc[:,4].rolling(window=40).mean()
plt.figure(figsize=[10,8])
plt.grid(True)
plt.title('Historical stock prices of Alphabet Inc. [01-04-2020 to 30-09-2020]\n',fontsize=18, color='black')
plt.plot(stock_data['Adj Close'],label='Adjusted Closing Price', color='black')
plt.plot(stock_data['SMA_30_days'],label='30 days simple moving average', color='red')
plt.plot(stock_data['SMA_40_days'],label='40 days simple moving average', color='green')
plt.legend(loc=2)
plt.show()
