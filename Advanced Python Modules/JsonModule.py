import json

person_string = '{"name" : "Ali" , "languages" : ["python","c++"]}'

# # JSON string to Dict
# result = json.loads(person_string)
# print(type(result))
# print(result)
# # result = result["name"]
# # print(result)
# result = result["languages"][0]
# print(result)

# with open("person.json") as file:
#     data = json.load(file)
#     print(data["name"])
#     print(data["languages"])

person_dict = {
    "name" : "Ali",
    "languages" : ["Python","C++"]
}

# # Dict to JSON string
# result = json.dumps(person_dict) #convert dict to json
# print(result)
# print(type(result))

# with open("person.json","a") as file:
#     json.dump(person_dict,file)


person_dict = json.loads(person_string)
print(person_dict)

result = json.dumps(person_dict,indent = 4,sort_keys = True)
print(person_dict)
print(result)





