# APPROACH 1
# import math
import math as process

# value = dir(math)
# print(value)

# value = help(math)
# print(value)

# value = help(math.factorial)

# value = math.sqrt(49)
# print(value)

# value = math.factorial(5)
# print(value)

# value = math.floor(5.9)
# print(value)

# value = math.ceil(5.9)
# print(value)

# value = process.factorial(5)

###################################################
#APPROACH 2

# from math import *
from math import factorial,sqrt

def sqrt(x):
    print("X : " + str(x))

value = factorial(5)
print(value)
value = sqrt(9)
print(value)
# value = ceil(9) # its not defined cause you have to import it
# print(value)


