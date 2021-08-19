numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y']

print(min(numbers))
print(max(numbers))
print(min(letters))
print(max(letters))

new_list = numbers[3:6]
print(new_list)
new_list = numbers[4:] 
print(new_list)
new_list = numbers[:3]
print(new_list)

numbers.append(49) #adds 49 to end of the list
print(numbers)
numbers.insert(3,78) #adds 78 at 3.index
print(numbers)
numbers.insert(-1,52) #adds 52 before last element of the list
print(numbers)

#numbers.pop() #removes last element
# numbers.pop(0) #removes first element
# numbers.pop(-1) #removes last element
numbers.remove(16)
print(numbers)

numbers.sort() #sorts the list
print(numbers)
letters.sort()
print(letters)

numbers.reverse() #reverses the list
letters.reverse()
print(numbers)
print(letters)

print(len(numbers)) #returns the number of elements of the list
print(len(letters))

print(numbers.count(10)) # return the number of searching data

numbers.clear() #removes all elements of the list
print(numbers)