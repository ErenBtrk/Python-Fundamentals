numbers = [1,3,5,7,9,12,19,21]

#1- Print numbers list with a while loop

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

#2- Prompt user to enter two numbers and print the odd number elements of numbers list between the numbers user entered

startNum = int(input("Please enter starting number : "))
endNum = int(input("Please enter ending number : "))

i = 0
while i < len(numbers):
    if(numbers[i] > startNum and numbers[i] < endNum):
        if(numbers[i] % 2 != 0):
            print(numbers[i])
    i += 1

#3 - Print the numbers between 1-100 in decreasing order

i = 100
while i>1:
    print(i)
    i -= 1

#4 - Prompt user to enter 5 numbers and print them in order

userNumbers = []
x = 0
while x<5:
    numberEntered = int(input("Please enter a number : ")) 
    userNumbers.append(numberEntered)
    x += 1

userNumbers.sort()
print(userNumbers)

#5 - Prompt the user to enter product information and store it in a list
#   ** Ask the product quantity to user
#   ** Make it a dictionary list
#   ** Print products after adding product process

# productQuantity = int(input("Please enter the product quantity : "))

# productDictionary = {}

# i = 0
# while i < productQuantity:
#     productID = input("Please enter product ID :")
#     pName = input("Please enter product name : ")
#     pClass = input("Please enter product class : ")
#     pColor = input("Please enter product color : ")
#     pPrice = float(input("Please enter product price : "))

#     productDictionary.update({
#     i:{
#         "productName" : pName,
#         "productClass" : pClass,
#         "productColor" : pColor,
#         "productPrice" : pPrice
#     }
#     })
#     i += 1
  
# i = 0
# while i<productQuantity:
#     print(productDictionary[i])
#     i += 1

urunSayisi = int(input("Please enter the product quantity : "))

urunler = []

i = 0
while i < urunSayisi:
    urunIsmi = input("Please enter product name : ")
    urunSinifi = input("Please enter product class : ")
    urunRengi = input("Please enter product color : ")
    urunFiyati = float(input("Please enter product price : "))
    urunler.append({
        "isim" : urunIsmi,
        "sinif": urunSinifi,
        "renk" : urunRengi,
        "fiyat": urunFiyati,
    })
    i += 1

for urun in urunler:
    print(f'Urun ismi : {urun["isim"]} , Urun sinifi : {urun["sinif"]}, '
    f'Urun rengi : {urun["renk"]} , Urun Fiyati : {urun["fiyat"]}')
    
