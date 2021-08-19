#1 - Prompt user to enter two numbers and print larger one
number1 = int(input("Please enter a number : "))
number2 = int(input("Please enter a number : "))
result = number1 > number2
print(f"number1 : {number1} is greater than number2 : {number2} => {result}")
#2 - Prompt user to enter 2 exam notes and calculate average.If >50 print Passed ,if no print Try Again
exam1 = float(input("Please enter your exam note : "))
exam2 = float(input("Please enter your exam note : "))
average = (exam1+exam2)/2
result = average >= 50
print(f"Average is : {average} , You Passed the class : {result}")

#3 - Prompt user to enter a number.Print if its odd or even
number3 = int(input("Please enter a number : "))
result = (number3 % 2 != 0)
print(f"The number : {number3} is an odd number : {result}")

#4 - Prompt user to enter a number.Print if its negative or positive
number3 = int(input("Please enter a number : "))
result = (number3 > 0)
print(f"The number : {number3} ,is positive : {result}")

#5 - Prompt user to enter email and password.Check if its true
#  ( email = email@gmail.com password = abcd123)
email = "email@gmail.com"
password = "abcd123"
inputUserEmail = input("Please enter your email : ")
inputUserPassword = input("Please enter your password : ")
result = (email == inputUserEmail.strip()) & (password == inputUserPassword.strip())
print(f"Logged in : {result}")
