import pandas as pd

# customers = {
#     "CustomerID" : [1,2,3,4],
#     "FirstName" : ["Ahmet","Ali","Veli","Hasan"],
#     "LastName" : ["Yilmaz","Korkmaz","Celik","Toprak"]
# }

# orders = {
#     "OrderID" : [10,11,12,13],
#     "CustomerID" : [1,2,5,7],
#     "OrderDate" : ["2010-07-07","2010-08-04","2010-10-01","2010-12-03"]
# }

# df_customers = pd.DataFrame(customers,columns = ["CustomerID","FirstName","LastName"])
# df_orders = pd.DataFrame(orders,columns = ["OrderID","CustomerID","OrderDate"])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers,df_orders,how = "inner")
# print(result)
# result = pd.merge(df_customers,df_orders,how = "left")
# print(result)
# result = pd.merge(df_customers,df_orders,how = "right")
# print(result)
# result = pd.merge(df_customers,df_orders,how = "outer")
# print(result)

customersA = {
    "CustomerID" : [1,2,3,4],
    "FirstName" : ["Ahmet","Ali","Veli","Hasan"],
    "LastName" : ["Yilmaz","Korkmaz","Celik","Toprak"]
}

customersB = {
    "CustomerID" : [4,5,6,7],
    "FirstName" : ["Yagmur","Cinar","Cengiz","Can"],
    "LastName" : ["Bilge","Turan","Yilmaz","Turan"]
}

df_customersA = pd.DataFrame(customersA,columns = ["CustomerID","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB,columns = ["CustomerID","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB])
print(result)

result = pd.concat([df_customersA,df_customersB],axis=1)
print(result)