names = ["Ali","Yagmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

#1- Add "Cenk" to end of the list 
names.append("Cenk")
print(names)

#2- Add "Sena" to head of the list
names.insert(0,"Sena")
print(names)

#3- Remove "Deniz" from the list
denizIndex = names.index("Deniz")
names.pop(denizIndex)
#names.remove("Deniz")
print(names)

#4- What is the index of "Deniz"
#print(names.index("Deniz")) #deleted

#5- is "Ali" an element of the list
aliIndex = names.index("Ali")
#print("Ali" in names)
print(bool(aliIndex))

#6-Reverse the elements of the list
names.reverse()
print(names)

#7-Sort the elements of the list
names.sort()
print(names)

#8-Sort the elements of years list
years.sort()
print(years)

#9-str1 = "Chevrolet,Dacia" Convert this string to a list
str1 = "Chevrolet,Dacia"
str1 = str1.split(',')
new_list =[str1[0],str1[1]]
print(new_list)

#10-What is the largest and smallest elements of years list
print(max(years))
print(min(years))

#11- How many 1998 does years list has?
print(years.count(1998))

#12-Delete all of the elements of years list
years.clear()
print(years)

#13-Prompt user to enter 3 brand names and store them in a list
brand_names = []
brand_names.append(input("Please enter a brand name = "))
brand_names.append(input("Please enter a brand name = "))
brand_names.append(input("Please enter a brand name = "))

print(brand_names)