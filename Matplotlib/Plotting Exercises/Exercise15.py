'''

15. Write a Pandas program to create a plot of adjusted closing prices, 30 days simple
moving average and exponential moving average of Alphabet Inc. between two specific dates.

What is Simple Moving Average (SMA)?
In financial applications a simple moving average (SMA) is the unweighted mean of the previous n data.
However, in science and engineering, the mean is normally taken from an equal number of data on either
side of a central value. This ensures that variations in the mean are aligned with the variations in the
data rather than being shifted in time.

What Is an Exponential Moving Average (EMA)?
From investopedia.com - An exponential moving average (EMA) is a type of moving average (MA) that places
a greater weight and significance on the most recent data points. The exponential moving average is also
referred to as the exponentially weighted moving average. An exponentially weighted moving average reacts
more significantly to recent price changes than a simple moving average (SMA), which applies an equal weight
to all observations in the period.

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
stock_data['EMA_20_days'] = stock_data.iloc[:,4].ewm(span=20,adjust=False).mean()
plt.figure(figsize=[15,10])
plt.grid(True)
plt.title('Historical stock prices of Alphabet Inc. [01-04-2020 to 30-09-2020]\n',fontsize=18, color='black')
plt.plot(stock_data['Adj Close'],label='Adjusted Closing Price', color='black')
plt.plot(stock_data['SMA_30_days'],label='30 days Simple moving average', color='red')
plt.plot(stock_data['EMA_20_days'],label='20 days Exponential moving average', color='green')
plt.legend(loc=2)
plt.show()

