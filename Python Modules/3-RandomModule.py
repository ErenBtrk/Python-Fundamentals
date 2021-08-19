import random

# result = dir(random)
# print(result)

# result = help(random)
# print(result)

result = random.random() # 0.0 - 0.1
print(result)

result = int(random.uniform(10,100))
print(result)

result = random.randint(1,100)
print(result)

names = ["Ali","Veli","Isa","Musa","Ayse","Fatma","Faruk","Osman"]
result = names[random.randint(1,len(names)-1)]
print(result)
result = random.choice(names)
print(result)

greeting = "hello there"
result = random.choice(greeting)
print(result)

my_list = list(range(10))


result = my_list
print(result)

random.shuffle(my_list)
print(result)

my_list2 = range(100)
result = random.sample(my_list2,3)
print(result)