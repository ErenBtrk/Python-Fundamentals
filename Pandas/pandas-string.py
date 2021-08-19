import pandas as pd

data = pd.read_csv("nba.csv")
print(data.columns)
data.dropna(inplace= True)


# data["player_name"] = data["player_name"].str.upper()
# print(data.head(10))
# data["player_name"] = data["player_name"].str.lower()
# print(data.head(10))
# data["index"] = data["player_name"].str.find('a')
# print(data.head(10))
# data = data[data["player_name"].str.contains("jordan")]
# print(data.head(10))
# data = data["player_name"].str.replace(' ','-')
# print(data.head(10))
data[['FirstName','LastName']] = data['player_name'].loc[data['player_name'].str.split().str.len()==2].str.split(expand=True)
print(data.head(10))
