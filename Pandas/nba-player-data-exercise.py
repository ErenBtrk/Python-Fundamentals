import pandas as pd
import numpy as np
import datetime



# Print first 10 records

data = pd.read_csv("player_data.csv")
print(data.head(10))

# How many records are in file

print(f"Total records = {len(data.index)}")

# How much is average weight

print(f"total weight = {data['weight'].sum()}")
print(f"Average weight = {data['weight'].mean() *  0.45359237:.3} Kg")

# What is highest height?

data["height"] = data["height"].str.replace("-",".")
data['height'] = pd.to_numeric(data['height'])
highestHeight = data["height"].max() * 0.3048
print(f"Highest height  = {highestHeight:.3} meters")

#Who is highest player?

highestPlayerIndex = data["height"].idxmax(axis = 1, skipna = True)
print(f"Highest player is {data['name'][highestPlayerIndex]} from {data['college'][highestPlayerIndex]}")

#Print the players name and college who was born between 1980-1982

data["birth_date"] = data["birth_date"].str.replace(',','')
print(data)
data["birth_date"] = pd.to_datetime(data["birth_date"])
#data['year'] = data['birth_date'].dt.to_period('Y')
date1 = datetime.datetime(1980,1,1)
date2 = datetime.datetime(1982,12,31)
relationalVar = (data["birth_date"] > date1) &  (data["birth_date"] < date2)
print(data[relationalVar][["name","college","birth_date"]].sort_values("birth_date",ascending=False))


#What is John Holland's college

relationalVar = data["name"] == 'John Holland'
print(data[relationalVar][["college","name"]].iloc[0])

#What is the most frequent position for each college

result = data.groupby("college")["position"].value_counts()
print(result)

#How many colleges are there?

result = data["college"].nunique()
print(f"Total college number = {result}")

#How many players per college?

result = data["college"].value_counts()
print(result)


#Print the player names which involves "and"
#data.dropna(inplace=True)
relationalVar = data["name"].str.contains("and")
print(data[relationalVar])




