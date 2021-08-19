#range() method

for item in range(50,100,20): # range() => first parameter is starting number,
     print(item)              # second is ending
                              # number and third is increment

print(list(range(5,100,10)))

#enumerate() method

greeting =  "Hello There"

for index,letter in enumerate(greeting):
    print(f"index : {index} letter:{letter}")

#zip() method

my_list1 = [1,2,3,4,5]
my_list2 = ['a','b','c','d','e']
my_list3 = [100,200,300,400,500]

my_list4 =  list(zip(my_list1,my_list2,my_list3))

print(my_list4)


for item in zip(my_list1,my_list2,my_list3):
    print(item)

for a,b,c in zip(my_list1,my_list2,my_list3):
    print(a,b,c)
