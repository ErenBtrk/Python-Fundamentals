dictionary = {}

keyValue = input("Please enter a key value:")
firstName = input("Please enter your name:")
lastName = input("Please enter your last name:")
phone = input("Please enter your phone:")
language1 = input("Please enter language you can speak :")
language2 = input("Please enter second language you can speak :")

dictionary.update({
    keyValue:{
        "name" : firstName,
        "last name" : lastName,
        "phone" : phone,
        "languages" :{
            "language1" : language1,
            "language2" : language2
        }
    }
})

print("Please enter a key value to show information : ")
print(dictionary["keyValue"]["languages"]["language1"])