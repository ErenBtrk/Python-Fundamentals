#value types => string,int,float
x = 5
y = 25

x = y
y = 10

print(x,y)

#reference types => list
my_list_1 = ["apple","banana"]
my_list_2 = ["apple","banana"]

my_list_1 = my_list_2 #when assign a list to another ,they both show same location in memory

my_list_2[0] = "grape"

print(my_list_1,my_list_2)