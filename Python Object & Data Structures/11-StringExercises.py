website = "http://www.sadikturan.com"
course = "Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"

# 1- How many chars does 'course' char array has?
arrayLength = len(course)
print(f"course array has {arrayLength} characters")
# 2- print only www  in 'website' char array
print(website[7:10])
# 3- print only com in 'website' char array
print(website[-3:])
# 4- print only first and last 15 chars from 'course' char array
print(course[:15],course[-15:])
# 5- Reverse 'course' char array 
print(course[::-1])

# s = "12345" * 5
# print(s[::5])

name,surname,age,job = "Bora","Yilmaz",32,"muhendis"

#6-Print the string below with the variables above.
# "Benim adim Bora Yilmaz,Yasim 32 ve meslegim muhendis"

print(f"Benim adim {name},{surname},yasim {age} ve meslegim {job} ")
print("Benim adim {},{},yasim {} ve meslegim {}".format(name,surname,age,job))
print("Benim adim {a},{b},yasim {c} ve meslegim {d}".format(a=name,b=surname,c=age,d=job))

#7-"Hello world" Change w letter into 'W' in this string
str1 = "Hello world"
str1 = str1[0:6] + 'W' + str1[-4:]
print(str1)

#8-print "abc" sequential 3 times
str2 = "abc" *3
print(str2)
