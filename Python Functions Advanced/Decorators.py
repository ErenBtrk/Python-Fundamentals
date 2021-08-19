def my_decorator(func):
    def wrapper(name):
        print("processes before function : ")
        func(name)
        print("processes after function : ")
    return wrapper


# say_hello = my_decorator(say_hello)
# say_hello()
@my_decorator
def say_hello(name):
    print("Hello.",name)

say_hello("Ali")

##############################################################################

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("function " + func.__name__ + " took " + str(finish-start) + " seconds." )
    return inner

@calculate_time
def expo(a,b):
    print(math.pow(a,b))
    
@calculate_time
def factorial(num):
    print(math.factorial(num))

@calculate_time
def sum(a,b):
    print(a+b)

expo(2,3)
factorial(5)
sum(5,10)


