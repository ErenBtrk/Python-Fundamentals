x,y,z = 2,5,10

numbers = 1,5,7,10,6   

#1- Prompt the user to enter 2 numbers and subtract it from x+y+z
userNumber1 = input("Please enter a number:")
userNumber2 = input("Please enter a number:")

userNumber1 = int(userNumber1)
userNumber2 = int(userNumber2)
sum1 = x+y+z
sum2 = userNumber1+userNumber2

print(sum1-sum2)

#2- divide y to x without remainder
print("y//x = ",y//x)

#3- what is x+y+z mod 3?
print("(x+y+z) % 3 = ",sum1%3)

#4- calculate y exponent x
print("y**x = ",y**x)

#5- x,*y,z = numbers => what is cube z
x,*y,z = numbers
print("z**3 = ",z**3)

#6- x,*y,z = number => calculate y list's values sum 
print(y[0]+y[1]+y[2])