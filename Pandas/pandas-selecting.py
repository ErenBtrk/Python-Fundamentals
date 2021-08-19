import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3,3),index = ["A","B","C"],columns = ["Column1","Column2","Column3"])

result = df
print(result)
result = df["Column1"]
print(result)
result = type(result)
print(result)
result = df[["Column1","Column2"]]
print(result)

#loc["row","column"] => loc["row"] => loc[":","column"]
result = df.loc["A"]
print(result)
result = type(df.loc["A"])
print(result)
result = df.loc[:,"Column1"]
print(result)
result = df.loc[:,["Column1","Column2"]]
print(result)
result = df.loc[:,"Column2":"Column3"]
print(result)
result = df.loc[:,:"Column2"]
print(result)
result = df.loc["A":"B",:"Column2"]
print(result)
result = df.loc[:"B",:"Column2"]
print(result)
result = df.iloc[2]
print(result)
result = df.loc["A","Column2"]
print(result)
result = df.loc["C","Column1"]
print(result)
result = df.loc[["A","B"],["Column1","Column2"]]
print(result)

df["Column4"] = pd.Series(np.random.randn(3),["A","B","C"])
print(df)
df["Column5"] = df["Column1"] + df["Column3"]
print(df)
df.drop("Column5",axis=1,inplace=True)
print(df)