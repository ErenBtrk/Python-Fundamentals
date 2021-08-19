from sqlite3.dbapi2 import connect
import pandas as pd
import sqlite3

from pandas.io import sql


df1 = pd.read_csv("addresses.csv")
df1.columns = ["First Name","Last Name","Street Name","City","Abbr","Postal Code"]
df1.index = [1,2,3,4,5]
print(df1)

df2 = pd.read_json("sample.json")
print(df2)

df3 = pd.read_excel("excel.ods")
print(df3)


#Creating DB
connection = sqlite3.connect("sample.db")

cursor = connection.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS students ( name TEXT,surname TEXT,num INT,grade INT)")
def addValue():
    cursor.execute("INSERT INTO students VALUES('Ali','Veli',1234,22)")
    connection.commit()
    connection.close()

createTable()
addValue()

connection = sqlite3.connect("sample.db")
df4 = pd.read_sql_query("SELECT * FROM students",connection)

print(df4)