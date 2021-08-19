import pandas as pd
import numpy as np

data = {
    "Column1" : [1,2,3,4,5],
    "Column2" : [10,20,13,20,25],
    "Column3" : ["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

def square(x):
    return x * x 

square2 = lambda x: x*x

result = df
result = df["Column2"].unique()
print(result)

result = df["Column2"].nunique()
print(result)

result = df["Column2"].value_counts()
print(result)

result = df["Column1"]*2
print(result)

result = df["Column1"].apply(square)
print(result)

result = df["Column1"].apply(square2)
print(result)

result = df["Column1"].apply(lambda x: x*x)
print(result)

result = df["Column3"].apply(len)
print(result)

df["Column4"] = df["Column3"].apply(len)
print(df)

result = df.columns
print(result)

result = len(df.columns)
print(result)

result = df.index
print(result)

result = len(df.index)
print(result)

result = df.info
print(result)

result = df.sort_values("Column2")
print(result)

result = df.sort_values("Column3")
print(result)

result = df.sort_values("Column3",ascending=False)
print(result)

data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)
print(df)
print(df.pivot_table(index="Ay",columns="Kategori",values="Gelir"))

