import pandas as pd
import numpy as np

# data
numbers = [20,30,40,50]
letters = ['a','b','c','d']
numlet = [1,2,3,'a']
scalar = 5
dict1 = {'a' : 10 ,'b' : 20,'c' : 30,'d' : 40}
random_numbers = np.random.randint(10,100,6)

#pandas_series = pd.Series()
pandas_series1 = pd.Series(numbers)
print(pandas_series1)

pandas_series2 = pd.Series(letters)
print(pandas_series2)

pandas_series3 = pd.Series(numlet)
print(pandas_series3)

pandas_series4 = pd.Series(scalar,[0,1,2,3])
print(pandas_series4)

pandas_series5 = pd.Series(numbers,['a','b','c','d'])
print(pandas_series5)

pandas_series6 = pd.Series(dict1)
print(pandas_series6)

pandas_series7 = pd.Series(random_numbers)
print(pandas_series7)

pandas_series8 = pd.Series([20,30,40,51],['a','b','c','d'])

result = pandas_series8[0]
print(result)
result = pandas_series8[-1]
print(result)
result = pandas_series8[:2]
print(result)
result = pandas_series8[-2:]
print(result)
result = pandas_series8['a']
print(result)
result = pandas_series8['d']
print(result)
result = pandas_series8[['a','c']]
print(result)
result = pandas_series8.ndim
print(result)
result = pandas_series8.dtype
print(result)
result = pandas_series8.shape
print(result)
result = pandas_series8.sum()
print(result)
result = pandas_series8.max()
print(result)
result = pandas_series8.min()
print(result)
result = pandas_series8 + pandas_series8
print(result)
result = pandas_series8 + 50
print(result)
result = np.sqrt(pandas_series8)
print(result)
result = pandas_series8 >= 50
print(result)
result = pandas_series8 %2 == 0
print(result)
print(pandas_series8[result])

opel2018 = pd.Series([20,30,40,10],["Astra","Corsa","Mokka","Insignia"])
opel2019 = pd.Series([40,30,20,10],["Astra","Corsa","Grandland","Insignia"])

total = opel2018 + opel2019

print(total["Astra"])
