name = "Yarasa"
surname = "Reis"
age = 99

greeting = "My name is "+ name + ' ' + surname + " and \nI am " + str(age) + " years old"
length = len(greeting)

# #print(greeting)
# print(greeting[0]) #printing char at 0.index
# print(greeting[3]) #printing char at 3.index
# print(greeting[length-1]) #printing char at last index
# print(greeting[-1]) #printing char at last index
#print(greeting[3:7]) #printing chars between 3 - 7 index
print(greeting[3:]) #printing chars after 3.index
print(greeting[:16])  #printing chars until 16.index
print(greeting[2:40:2]) #printing chars until 40.index but only prints chars after two each