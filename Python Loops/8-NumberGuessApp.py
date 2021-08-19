'''
    Generate a random number between 1-100.(Health = 5)
    Prompt user to guess number 
    If user enters a lower number print UP
    If user enters a greater number print DOWN
    ** use random module
    ** make a scoring system with 100 points
       every wrong guess is -20 points
    ** Prompt the user to enter health and make a scoring system according to it
'''

import random

# randomNumber = random.randint(1,10)

# health = 5
# totalPoint = 100

# while(health > 0):
#     userGuess = int(input("Please guess the number : "))
#     if(userGuess == randomNumber):
#         print("Your guess is right.Congrats!!!")
#         break
#     else:
#         if(userGuess > randomNumber):
#             print("DOWN")
#         elif(userGuess < randomNumber):
#             print("UP")
#     totalPoint -= 20
#     health -= 1
# if(health == 0):
#     print(f"The number was {randomNumber} and you have no health.TRY AGAIN...")
# print(f"Your total point is = {totalPoint}")
        

randomNumber = random.randint(1,100)
print(randomNumber)
health = int(input("Please enter number of rounds you bet to win : "))
count = 0
initHealth = health

while(health > 0):
    health -= 1
    count += 1
    userGuess = int(input("Please guess the number : "))

    if(userGuess == randomNumber):
        print(f"Your guess is right in {count} rounds.Congrats!!!.Your Total Point is = {100-(100/initHealth)*(count-1)}")
        break
    elif(userGuess > randomNumber):
        print("DOWN")
    elif(userGuess < randomNumber):
        print("UP") 

    if(health == 0):
        print(f"You have no health left.The number was {randomNumber}.")


    
