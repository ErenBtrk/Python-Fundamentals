import pandas as pd

#df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
data = [["Ahmet",50],["Ali",60],["Yagmur",70],["Cinar",80]]
df = pd.DataFrame(data,columns = ["Name","Grade"],index = [1,2,3,4],dtype = float)
print(df)

dict = {"Name" : ["Ahmet","Ali","Veli","Osman"],"Grade" : [50,60,70,80]}
df = pd.DataFrame(dict)
print(df)
df = pd.DataFrame(dict,index = ["111","222","333","444"])
print(df)

dict_list = [
                {"Name" : "Ahmet","Grade" : 50},
                {"Name" : "Ali","Grade" : 60},
                {"Name" : "Fatma","Grade" : 70},
                {"Name" : "Ayse","Grade" : 90}
            ]
df = pd.DataFrame(dict_list,index = ["123","456","789","000"])
print(df)
# pandas_series1 = pd.Series([3,2,0,1])
# pandas_series2 = pd.Series([0,3,7,2])

# data = dict(apples = pandas_series1,oranges = pandas_series2)

# df = pd.DataFrame(data)

# print(df)