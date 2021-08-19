#doesnt allocate memory for generators 
def cube():
    for i in range(5):
       yield i**3 


# print(next(cube()))
# print(next(cube()))
# print(next(cube()))
# print(next(cube()))
# print(next(cube()))
# #print(next(cube())) #Stop Iteration

for i in cube():
    print(i)

#######################################################

list1 = [i**3 for i in range(5)]  #it does return a list with list comprehension
print("list1 = ",list1)
for i in list1:
    print(i)

generator = (i**3 for i in range(5)) #it does return a generator when used with these brackets
print("generator = ",generator)
for i in generator:
    print(i)
