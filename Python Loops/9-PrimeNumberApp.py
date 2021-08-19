'''
    Prompt user to enter a number and check if its a prime number
'''
# import math
# userInput = int(input("Please enter a number : "))
# if(userInput == 0 or userInput == 1):
#     print("The number you've entered is NOT a prime number")
# else:
#     i = 2
#     flag = True
#     while i <= math.sqrt(userInput):
#         if(userInput % i == 0):
#             flag = False
#             break
#         i += 1
#     if(flag):
#         print("The number you've entered is a prime number")
#     else:
#         print("The number you've entered is NOT a prime number")

number = int(input("Please enter a number : "))
flag = True

if(number == 1 or number == 0):
    flag = False

for i in range(2,number):
    if(number % i == 0):
        flag = False
        break

if(flag):
    print(f"{number} is a prime number")
else:
    print(f"{number} is NOT a prime number")