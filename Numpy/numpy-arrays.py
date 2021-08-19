import numpy as np

#result = np.array([1,3,5,7,9])
result = np.arange(1,10)
print(result)

result = np.arange(10,100,3)
print(result)

result = np.zeros(10)
print(result)

result = np.ones(10)
print(result)

result = np.linspace(0,100,5)
print(result)

result = np.linspace(0,5,5)
print(result)

result = np.random.randint(0,10)
print(result)

result = np.random.randint(20)
print(result)

result = np.random.randint(1,10,3)
print(result)

result = np.random.rand(5)
print(result)

result = np.random.randn(5)
print(result)

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)
print(np_multi)
print(np_multi.sum(axis=1))
print(np_multi.sum(axis=0))

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
maxNum = rnd_numbers.max()
print(maxNum)
minNum = rnd_numbers.min()
print(minNum)
average = rnd_numbers.mean()
print(average)
indexOfMaxNum = rnd_numbers.argmax()
print(indexOfMaxNum)
indexOfMinNum = rnd_numbers.argmin()
print(indexOfMinNum)