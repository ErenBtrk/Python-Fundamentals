def changeName(n):
    n = "bat"

name = "eagle"

changeName(name)
print(name)

def change(n):
    n[0] = "istanbul"

cities = ["ankara","izmir"]
change(cities[:])

print(cities)

def add(*params): #if we want to pass tuple/list its just an asterisk
    print(params[0])
    print(params[2])
    return sum((params))

print(add(10,20,50))
print(add(10,20,30))
print(add(10,20,30,50,60,10,20))

def displayUser(**args): #double asterisk if we want to use dictionaries
    print(type(args))
    for key,value in args.items():
        print("{} is {}".format(key,value))

displayUser(name = "Ali",age = 2,city = "Istanbul")
displayUser(name = "Ayse",age =12,city = "Ankara",phone = 231312)
displayUser(name = "Isa",age =22,city = "Izmir",phone = 345344)

def myFunction(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunction(10,20,30,40,50,key1 = "value1",key2 = "value2")