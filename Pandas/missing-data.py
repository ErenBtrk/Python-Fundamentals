import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index = ['a','c','e','f','h'],columns=["Column1","Column2","Column3"])

df = df.reindex(['a','b','c','d','e','f','g','h'])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["Column4"] = newColumn

result = df
result = df.drop(["Column1","Column2"],axis=1)
print(result)
result = df.drop(['a'],axis=0)
print(result)
result = df.drop(['a','b','h'],axis=0)
print(result)

result = df.isnull()
print(result)
result = df.notnull()
print(result)
result = df.isnull().sum()
print(result)
result = df["Column1"].isnull().sum()
print(result)

result = df[df["Column1"].isnull()]
print(result)
result = df[df["Column1"].isnull()]["Column1"]
print(result)
result = df[df["Column1"].notnull()]["Column1"]
print(result)
result = df[df["Column1"].notnull()]
print(result)

result = df.dropna() # axis = 0 => row
print(result)
result = df.dropna(axis=1) #axis = 1 => column
print(result)
result = df.dropna(how = "any")
print(result)
result = df.dropna(how = "all")
print(result)
result = df.dropna(subset = ["Column1","Column2"],how = "all")
print(result)
result = df.dropna(subset = ["Column1","Column2"],how = "any")
print(result)
result = df.dropna(thresh = 2)
print(result)
result = df.dropna(thresh = 3)
print(result)

result = df.fillna(value = "no input")
print(result)
result = df.fillna(value = 1)
print(result)

result = df.sum()
print(result)
result = df.sum().sum()
print(result)
result = df.size
print(result)
result = df.isnull().sum().sum()
print(result)

def average(df):
    total = df.sum().sum()
    quantity = df.size - df.isnull().sum().sum()
    return total / quantity

result = df.fillna(value = average(df))
print(result)