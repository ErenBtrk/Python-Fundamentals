# try:
#     file = open("newfile.txt") #default mode is "r"
#     print(file)
# except FileNotFoundError:
#     print("File not found error.")
# finally:
#     print("File is closed.")
#     file.close()

#######################################################

file = open("newfile.txt","r",encoding = "utf-8") #utf-8 turkish characters

# for loop

# for i in file:
#     print(i,"") #second parameter says dont add a space at last

#**********read function

# content = file.read()

# print("Content 1")
# print(content)

# file = open("newfile.txt","r",encoding = "utf-8") #if you add it content2 is not blank
# content2 = file.read() 

# print("Content 2")
# print(content2)

# content = file.read(5) # read 5 byte
# content = file.read(3)
# content = file.read(3)
# print(content)


#**********readline() function

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")

#**********readlines() function

list = file.readlines()

print(list)
print(list[0])
print(list[1])

file.close()




