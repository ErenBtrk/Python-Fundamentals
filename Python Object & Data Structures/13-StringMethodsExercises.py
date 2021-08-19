website = "http://www.sadikturan.com"
course = "Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"

#1-" Hello world " remove space chars from this string's head and tail
str1 = " Hello world "
str1 = str1.strip()
print(str1)
# str1 = str1.lstrip() #removes space from left of the string
# print(str1)
# str1 = str1.rstrip() #removes space from right of the string
# print(str1)
# str1 = str1.lstrip(" Hello") #removes characters from left of the string
# print(str1)

#2-"www.sadikturan.com" remove everything beside sadikturan
str2 ="www.sadikturan.com"
print(str2.strip("w.moc"))
# index = str2.find("sadikturan")
# str2 = str2[index:-4]
# print(str2)



#3-make all chars upper of course string
print(course.upper())
print(course.lower())
print(course.title())

#4- how many 'a' chars in website string?
print(website.count("a"))
#5-does website string starts with "www" and ends with ".com"
print('Does it start with "www" = ',website.startswith("www"))
print('Does it end with ".com" = ',website.endswith(".com"))


#6-is there ".com" in website string
index = print(website.find(".com"))
index2 = print(course.rfind("Python")) #returns index of this string from right of course string

#7-are characters of course string are letters?
print(course.isalpha())
print(course.isdigit())


#8-"Contents" put this string inside 50 chars and put '*' left and right of it
str8 = "Contents"
print(str8.center(50,"*"))
print(str8.ljust(50,"*"))
print(str8.rjust(50,"*"))

#9-Replace all space characters with '-' character in course string
print(course.replace(' ','-'))
print(course.replace(' ','-',5)) #Replaces only 5 characters

#10- "Hello World" replace "World" with "There"
print("Hello World".replace("World","There"))


#11- Remove space chars from course string
print(course.replace(' ',''))
print(course.split())
