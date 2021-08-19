'''

3. Write a Pandas program to create a bar plot of the trading
volume of Alphabet Inc. stock between two specific dates.

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("alphabet-stock-data.txt")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-09-30')                         
df['Date'] = pd.to_datetime(df['Date']) 
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)

df2 = df.loc[new_df]
plt.bar(df2["Date"],df2["Volume"],label="volume",width= 0.3,color = "red")
plt.tight_layout()
plt.legend()
plt.xlabel("Date",fontsize=1)
plt.xticks(df2["Date"].values,rotation=90,color="black",fontsize=7)
plt.ylabel("Volume")
plt.yticks(df2["Volume"].values,fontsize=7)
plt.title("Trading volume of Alphabet Inc.\n01-04-2020 to 30-09-2020")

plt.show()