'''
Write a decorator which wraps functions to log function arguments and the return value on each call.
Provide support for both positional and named arguments (your wrapper function should take both *args
and **kwargs and print them both):

'''

def my_decorator(func):
    def wrapper(*args,**kwargs):
        with open("log2.txt","a") as file:
            for arg in args:
                file.write(str(arg)+'\n')
            for key,value in kwargs.items():
                file.write(f"{key} = {value}\n")
        return func(*args,**kwargs)
    return wrapper

@my_decorator
def function1(*args):
    for item in args:
        print(item)

@my_decorator
def function2(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

function1(3,4)
function2(num1 = 10,num2 = 20,num3 = 30)


