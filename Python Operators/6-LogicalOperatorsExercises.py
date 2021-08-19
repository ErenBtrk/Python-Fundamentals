#1- Prompt the user to enter a number and check if its between 0-100
number1 = int(input("Please enter a number : "))
result = (number1 > 0) and (number1 < 100)
print(f"Number : {number1} is between 0-100 : {result}")

#2- Prompt the user to enter a number and check if its positive even number
number2 = int(input("Please enter a number : "))
result = (number2 >= 0) and (number2 % 2 == 0)
print(f"Number : {number2} is positive and even : {result}")

#3- Prompt the user to enter password and email and check if info is right
email = "email@gmail.com"
password = "123456"

inputEmail = input("Email : ")
inputPassword = input("Password : ")

result = (email == inputEmail.strip()) and (password == inputPassword.strip())
print(f"Logged in : {result}")


#4- Prompt the user to enter 3 numbers and compare them
number3 = int(input("Please enter a number : "))
number4 = int(input("Please enter a number : "))
number5 = int(input("Please enter a number : "))

result = (number3 > number4) and (number3 > number5)
print(f"{number3} is greater than {number4} and {number5} => {result}")

result = (number4 > number3) and (number4 > number5)
print(f"{number4} is greater than {number3} and {number5} => {result}")

result = (number5 > number3) and (number5 > number4)
print(f"{number5} is greater than {number3} and {number4} => {result}")

#5- Prompt the user to enter 2 exam notes (%60) and 1 final note.And calculate average.
#   if average is equal or larger than 50 print passed
#   a-)Even though average is 50 final note has to be at least 50
#   b-)If final note is equal or larger than 70 student can pass

exam1 = int(input("Please enter your first exam note : "))
exam2 = int(input("Please enter your second exam note : "))
final = int(input("Please enter your final exam note : "))

average = (((exam1+exam2) / 2)*0.6 + final*0.4)
result = ((average >= 50) and (final >= 50)) or (final >= 70)
print(f"Average : {average} , Passed => {result}") 


#6- Prompt the user to enter name,weight,height and calculate body mass index
#   Formula : (weight / height**2)
#   Whats user BMI according to table below 
#   0-18.4 => thin
#   18.5-24.9 => Normal
#   25.0-29.9 => Overweight
#   30.0-34.9 => Obese

name = input("Please enter your name : ")
weight = float(input("Please enter your weight : "))
height = float(input("Please enter your height in meters : "))

bmi = weight / (height**2)
print(f"Your body mass index is {bmi}")
result = (bmi >= 0) and (bmi <=18.4)
print(f"{name} is thin : {result}")
result = (bmi >= 18.5) and (bmi <=24.9)
print(f"{name} is normal : {result}")
result = (bmi >= 25.0) and (bmi <=29.9)
print(f"{name} is overweight : {result}")
result = (bmi >= 30.0) 
print(f"{name} is obese : {result}")


