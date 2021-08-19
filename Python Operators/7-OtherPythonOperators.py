#Identity Operator : is

x = y = [1,2,3] #x and y have same adress
z = [1,2,3]

print(x==y)
print(x==z) #value comparison
print(x is y) #reference comparison
print(x is z) 
print(y is z) 

x = [1,2,3]
y = [2,4]

del x[2]
y[1] = 1
y.reverse()

print(x)
print(y)
print(x==y)
print(x is y)
print(x is not y)

# Membership Operator : in

x = ["Apple","Banana"]
print("Banana" in x)

name = "Yarasa"
print("a" in name)
print("a" not in name)