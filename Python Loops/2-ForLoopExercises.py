numbers = [1,3,5,7,9,12,19,21]

#1- Which numbers are multiple of 3 of numbers list
#   Whats the sum of numbers list
#   Square the odd numbers in numbers list

for item in numbers:
    if(item % 3 == 0):
        print(item)

sumOfNumbers = 0
for item in numbers:
    sumOfNumbers += item
print("Sum Of Numbers = ",sumOfNumbers)

for item in numbers:
    if(item % 2 != 0):
        item **= 2 
        print(item)

##############################################################

sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

# 4- Which of the cities are 5 chars at max?

for item in sehirler:
    if(len(item) <= 5):
        print(item)

##############################################################

products = [
    {"name":"samsung S6","price":"3000"},
    {"name":"samsung S7","price":"4000"},
    {"name":"samsung S8","price":"5000"},
    {"name":"samsung S9","price":"6000"},
    {"name":"samsung S10","price":"7000"}
]      

#5- Whats the sum of products price?
#6-Print the products price which are 5000 at max

sumOfProducts = 0
for n in products:
    if(int(n["price"]) <= 5000):
        print(n["name"])
    for key,value in n.items():
        if(key == "price"):
            sumOfProducts += int(value)
        

print("Sum of Samsung Products Price = ",sumOfProducts)



