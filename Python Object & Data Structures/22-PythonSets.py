fruits = {"orange","apple","banana"}

# print(fruits[0]) cant index it

for x in fruits:
    print(x)

fruits.add("cherry")
fruits.update(["mango","grape","apple"]) # apple already is in list , so it doesnt add it
print(fruits)
fruits.remove("mango")
print(fruits)
fruits.discard("apple")
print(fruits)
fruits.pop() #removes a random element
print(fruits) 

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList)) #doesnt print repetitive elements
