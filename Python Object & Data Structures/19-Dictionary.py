# key - value

# 06 -> ankara
# 34 -> Istanbul

cities = ["ankara","istanbul"]
keys = [6,34]

print(keys[cities.index("ankara")]) #list approach

keys = {"ankara" : 6 , "istanbul" : 34} #dictionary approach
print(keys["istanbul"])

keys["kocaeli"] = 41
print(keys)
keys["kocaeli"] = "new value"
print(keys)

users = {
    "YarasaReis" :{
        "age" : 99,
        "email" : "bat@gmail.com",
        "adress": "Ist-TUR",
        "phone" : "1234567",
        "roles" : ["admin","king"]
    },
    "KevinDurant" :{
        "age" : 32,
        "email" : "KD@gmail.com",
        "adress": "BRK-USA",
        "phone" : "7654321",
        "roles" : ["ScoreLeader","Snake"]
    }
}

print(users["KevinDurant"])
print(users["YarasaReis"]["age"])
print(users["YarasaReis"]["email"])
print(users["YarasaReis"]["adress"])
print(users["YarasaReis"]["phone"])
print(users["YarasaReis"]["roles"][0])