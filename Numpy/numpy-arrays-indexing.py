import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]
print(result)
print('*' * 50)
result = numbers[-1]
print(result)
print('*' * 50)
result = numbers[0:3]
print(result)
print('*' * 50)
result = numbers[:3]
print(result)
print('*' * 50)
result = numbers[3:]
print(result)
print('*' * 50)
result = numbers[::]
print(result)
print('*' * 50)
result = numbers[::-1]
print(result)
print('*' * 50)

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
print(numbers2)
print('*' * 50)
result = numbers2[0]
print(result)
print('*' * 50)
result = numbers2[2]
print(result)
print('*' * 50)
result = numbers2[0,2]
print(result)
print('*' * 50)
result = numbers2[2,1]
print(result)
print('*' * 50)
result = numbers2[:,2]
print(result)
print('*' * 50)
result = numbers2[:,0]
print(result)
print('*' * 50)
result = numbers2[:,0:2]
print(result)
print('*' * 50)
result = numbers2[-1,:]
print(result)
print('*' * 50)
result = numbers2[:2,:2]
print(result)
print('*' * 50)


arr1 = np.arange(0,10)
#arr2 = arr1 #ref copy
arr2 = arr1.copy()


print(arr1)
print(arr2)

arr2[0] = 20

print(arr1)
print(arr2)

