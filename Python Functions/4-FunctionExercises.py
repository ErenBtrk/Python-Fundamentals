#1- Create a function which takes a string and a number as parameters.
#   Function will print the string up to number

def printString(strArg,numArg):
    for item in range(numArg):
        print(strArg)

printString("Yarasa Reis",5) 

#2- Create a function which takes limitless arguments.
#   Function will convert these parameters to a list

def convertToList(*args):
    newList = []
    for item in args:
        newList.append(item)
    return newList

newList = convertToList("Ali",10,"Veli",20.2,1,5,"KD")
print(newList)

#3- Create a function which takes 2 numbers as parameters.
#   Function will return prime numbers between these number parameters

import math

def primeNumbers(num1,num2):
    if(num1 > num2):
        temp = num1
        num1 = num2
        num2 = temp
    if(num1 <= 1):
        num1 = 2
    primeList = []
    for item1 in range(num1,num2):
        flag = True
        for item2 in range(2,item1):
            if(item1 % item2 == 0):
                flag = False
                break
        if(flag):
            primeList.append(item1)
    return primeList

newList = primeNumbers(15,30)

print(newList)

#4- Create a function which takes a number as a parameter.
#   Function will return common divisors of this number as a list.

def commonDivisors(num):
    commonDivList = []
    for item in range(1,num+1):
        if(num % item == 0):
            commonDivList.append(item)
    return commonDivList

newList = commonDivisors(22)
print(newList)