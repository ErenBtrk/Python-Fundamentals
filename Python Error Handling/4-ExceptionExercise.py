my_list = ["1","2","5a","10b","abc","10","50"]

# 1-Find the numerical elements in the list.
for item in my_list:
    try:
        print(int(item))
    except Exception as excObject:
        print(f"{item} element is not numerical.")

#####################################################################################

# 2-As long as user doesnt input 'q' character make sure user inputs a number
# Otherwise print an error message.

while True:
    try:
        number = input("Please enter a number : ")
        if(number == 'Q' or number == 'q'):
            break
        if(not number.isdigit()):
            raise Exception("You did not enter a number.")
    except Exception as excObject:
        print(excObject)

#####################################################################################

# 3-Print an error message if user inputs a Turkish character in password.

import re

while True:
    try:
        password = input("Please enter a password : ")
        if re.search("[ıİüÜşŞöÖçÇ]",password):
            raise Exception("Password shouldnt include a Turkish character")
    except Exception as excObject:
        print(excObject)   
    else:
        print("Password is valid.")
        break
    
# 4-Create a factorial function and for wrong parameters print error messages.



def factorial(number):
    if(not int(number)):
        raise Exception(f"{number} is not a number.")
    if(int(number) < 0):
        raise Exception(f"{number} is a negative number.")
    result = 1
    for item in range(1,int(number)+1):
        result *= item
    return result

number = "-5"

try:
    factorialResult = factorial(number)
except Exception as excObject:
    print(excObject)
else:
    print(f"{number}! = {factorialResult}")


    
        

        
       