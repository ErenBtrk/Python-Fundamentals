import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)
print('*'*50)

result = numbers1 + numbers2
print(result)
print('*'*50)


result = numbers1 + 10
print(result)
print('*'*50)


result = np.sin(numbers1)
print(result)
print('*'*50)


result = np.cos(numbers1)
print(result)
print('*'*50)


result = np.sqrt(numbers1)
print(result)
print('*'*50)


result = np.log(numbers1)
print(result)
print('*'*50)


multiNums1 = numbers1.reshape(2,3)
multiNums2 = numbers2.reshape(2,3)
print(multiNums1)
print(multiNums2)
print('*'*50)


result = np.vstack((multiNums1,multiNums2))
print(result)
print('*'*50)

result = np.hstack((multiNums1,multiNums2))
print(result)
print('*'*50)


result = numbers1 >= 50
print(result)
print('*'*50)

result = numbers1 % 2 == 0
print(result)

print(numbers1[result])
