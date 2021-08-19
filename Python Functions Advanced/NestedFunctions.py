# def greeting(name):
#     print("hello",name)

# print(greeting("Ali"))
# print(greeting)

# sayHello = greeting

# print(sayHello)
# print(greeting)

# print(greeting("ali"))
# print(sayHello("ali"))

# del sayHello

# print(greeting)

#encapsulation
def outer(num1):
    print("outer")
    def inner_increment(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1,num2)

outer(10)
#inner_increment(10) #cant access it

def factorial(number):
    if(not isinstance(number,int)):
        raise TypeError("number must be an integer.")
    if(not number >= 0):
        raise ValueError("Number must be zero or greater than zero.")

    def inner_factorial(number):
        if number <= 1:
            return 1

        return number * inner_factorial(number-1)

    return inner_factorial(number)

try:
    print(factorial(5))
    print(factorial(-1))
except Exception as excObject:
    print(excObject)