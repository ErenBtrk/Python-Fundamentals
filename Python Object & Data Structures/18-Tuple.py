my_list = [1,2,3]

my_tuple = (1,'iki',3)

print(type(my_list))
print(type(my_tuple))

print(my_list[2])
print(my_tuple[2])

print(len(my_list))
print(len(my_tuple))

my_list = ["ali","veli"]
my_tuple = ("damla","ayse")
my_tuple2 = ("demet","emel","ayse") + my_tuple

my_list[0] = "ahmet"
#my_tuple[0] = "deniz"     #cant assign a new value or cant delete an element

print(my_list)
print(my_tuple)
print(my_tuple2)

'''

The Key Difference between a List and a Tuple. 
The main difference between lists and tuples is the fact that lists are mutable whereas tuples are immutable. 
 A mutable data type means that a python object of this type can be modified. An immutable object can't...

'''