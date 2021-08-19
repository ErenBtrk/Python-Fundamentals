#1- Make a list which has "Bmw,Mercedes,Opel,Mazda" elements.
my_list = ["Bmw","Mercedes","Opel","Mazda"]

#2- How many elements does list have?
numberOfElements = len(my_list)
print("number of elements ={}".format(numberOfElements))

#3- What is the first and last element of this list?
print(my_list[0],my_list[numberOfElements-1])

#4- Replace Mazda with Toyota
mazdaIndex = my_list.index("Mazda")
my_list[mazdaIndex] = "Toyota"
print(my_list)

#5- Is Mercedes an element of this list?
print('is "Mercedes" in my_list? =', "Mercedes" in my_list)
print('is "Sahin" in my_list? =', "Sahin" in my_list)

#6- What is the element of index -2
print(my_list[-2])

#7- Take first 3 elements of list
print("First 3 elements of my_list = ",my_list[0:3])

#8- Add "Toyota" and "Renault" instead of last 2 elements
my_list[-2:] = ["Toyota","Renault"]
print('Added "Toyota" and "Renault" instead of last 2 elements = ' ,my_list)

#9- Add "Audi" and "Nissan" to the list
my_list.append("Audi")
my_list.append("Nissan")
# new_list = my_list +["Audi","Nissan"]
# print("new_list = ",new_list)
print(my_list)

#10- Delete last element of the list
my_list.pop(len(my_list)-1)
#del my_list[-1]
print("Deleted last element of the list = ",my_list)

#11- Print list reverse
#my_list.reverse()
#print(my_list)
print("Reversed my_list = ",my_list[::-1])

#12- Store following data in a list.
    #studentA : Yigit Bilgi 2010 , (70,60,70)
    #studentB : Sena Turan 1999 , (80,80,70)
    #studentC : Ahmet Turan 1998 , (80,70,90)

studentA_list = ["Yigit","Bilgi",2010,[70,60,70]]
studentB_list = ["Sena","Turan",1999,[80,80,70]]
studentC_list = ["Ahmet","Turan",1998,[80,70,90]]
student_list = [studentA_list,studentB_list,studentC_list]


#13- Print list elements.
print(student_list)
print(student_list[1][3][2])
print('Student C is {} {} , {} years old and has {} note average'.format(
student_list[2][0],student_list[2][1],2021-student_list[2][2],
(student_list[2][3][0]+student_list[2][3][1]+student_list[2][3][2])/3 ))
