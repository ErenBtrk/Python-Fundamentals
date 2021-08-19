#1- Prompt user to enter name , age and educational information .And check if user can take a driver license.
#   To get a driver license user has to be at least 18 years old and educational situation must be highschool or university.

userName = input("Please enter your name : ")
age = int(input ("Please enter your age : "))
education = input("Please enter your education : ").lower()

if (age >= 18) and ((education == "university") or (education == "highschool")):
     print("You can get a driver license.")
else:
     print("You can NOT get a driver license.")

#2- Prompt user to enter 3 exam notes and calculate average.Print letter grade depending on average.
# 0 - 24 => F
# 25- 44 => D
# 45- 54 => C
# 55- 69 => B
# 70- 84 => A
# 85- 100 => A+
exam1 = float(input("Please enter first exam note : "))
exam2 = float(input("Please enter second exam note : "))
exam3 = float(input("Please enter third exam note : "))

average = (exam1+exam2+exam3) / 3
print(f"Your note average is {average}")

if (average >= 0) and (average <= 24):
    print("Your letter grade is F")
elif (average >= 25) and (average <=44):
    print("Your letter grade is D")
elif (average >= 45) and (average <=54):
    print("Your letter grade is C")
elif (average >= 55) and (average <=69):
    print("Your letter grade is B")
elif (average >= 70) and (average <=84):
    print("Your letter grade is A")
elif (average >= 85) and (average <=100):
    print("Your letter grade is A++")
else:
    print("There is not such average")

#3- Calculate the service time of a vehicle whose traffic date is taken from the user according to the following information.
#   1.service -> 1.year
#   2.service -> 2.year
#   3.service -> 3.year
import datetime

date = input("Please enter traffic date (yyyy/mm/dd): ").split('/')

trafficDate = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))

today = datetime.datetime.now()

howManyDays = today - trafficDate
print(f"Your car is in traffic for {howManyDays.days} days")

if(howManyDays.days < 365):
    print("1.service")
elif(howManyDays.days >= 365) and (howManyDays.days <= 730):
    print("2.service")
else:
    print("3.service")


