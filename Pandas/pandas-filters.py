import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns = ["Column1","Column2","Column3","Column4","Column5"])

result = df
print(result)
result = df.columns
print(result)
result = df.head()
print(result)
result = df.head(10)
print(result)
result = df.tail()
print(result)
result = df.tail(10)
print(result)
result = df["Column1"].head()
print(result)
result = df.Column1.head()
print(result)
result = df[["Column1","Column2"]].head()
print(result)
result = df[["Column1","Column2"]].tail()
print(result)
result = df[5:15][["Column1","Column2"]].head()
print(result)

result = df[df>50]
print(result)
result = df[df%2 == 0]
print(result)
result = df["Column1"] > 50
print(result)
result = df[df["Column1"] > 50][["Column1","Column2"]]
print(result)
result = df[(df["Column1"] > 50) & (df["Column1"] <= 70)]
print(result)
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)]
print(result)
result = df[(df["Column1"] > 50) | (df["Column2"] >50)][["Column1","Column2"]]
print(result)
result = df.query("Column1 >= 50 & Column1 % 2 == 0")
print(result)
result = df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1","Column2"]]
print(result)