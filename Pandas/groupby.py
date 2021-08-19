import pandas as pd
import numpy as np

workers = {
    "WORKER" : ["Ahmet Yilmaz","Can Erturk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Riza Erturk","Mustafa Can"],
    "DEPARTMENT" : ["Human Resources","IT","Accounting","Human Resources","IT","Accounting","IT"],
    "AGE" : [30,25,45,50,23,34,42],
    "DISTRICT" : ["Kadikoy","Tuzla","Maltepe","Tuzla","Kadikoy","Tuzla","Maltepe"],
    "WAGE" : [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(workers,index=[item for item in range(1,8)])
result = df
print(result)
result = df["WAGE"].sum()
print(result)
result = df.groupby("DEPARTMENT").groups
print(result)
result = df.groupby(["DEPARTMENT","DISTRICT"]).groups
print(result)


# for name,group in df.groupby("DISTRICT"):
#     print(name)
#     print(group)

# for name,group in df.groupby("DEPARTMENT"):
#     print(name)
#     print(group)

result = df.groupby("DISTRICT").get_group("Kadikoy")
print(result)

result = df.groupby("DEPARTMENT").get_group("Accounting")
print(result)

result = df.groupby("DEPARTMENT").sum()
print(result)

result = df.groupby("DEPARTMENT").mean()
print(result)

result = df.groupby("DEPARTMENT")["WAGE"].mean()
print(result)

result = df.groupby("DISTRICT")["AGE"].mean()
print(result)

result = df.groupby("DISTRICT")["WORKER"].count()
print(result)

result = df.groupby("DEPARTMENT")["AGE"].max()
print(result)

result = df.groupby("DEPARTMENT")["WAGE"].min()
print(result)

result = df.groupby("DEPARTMENT")["WAGE"].max()["Accounting"]
print(result)

result = df.groupby("DEPARTMENT").agg(np.mean)
print(result)

result = df.groupby("DEPARTMENT")["WAGE"].agg([np.sum,np.mean,np.max,np.min])
print(result)

result = df.groupby("DEPARTMENT")["WAGE"].agg([np.sum,np.mean,np.max,np.min]).loc["Accounting"]
print(result)