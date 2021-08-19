import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("player_data.csv")

df = df.groupby("name",sort=False).mean()
df.head(5).plot(subplots=True,marker= "o")
plt.legend()

plt.show() 