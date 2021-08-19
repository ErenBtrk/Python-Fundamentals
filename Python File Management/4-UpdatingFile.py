# with open("newfile2.txt","r+") as file:
#     file.seek(20)
#     file.write(" deneme ")

# with open("newfile2.txt","r+") as file: #r+ is both reading and writing
#     print(file.read())

####################################################

#******** Updating at end of page ********

# with open("newfile2.txt","a") as file:
#     file.write("\nYarasa Reis")

#******** Updating at start of page ********

# with open("newfile2.txt","r+") as file:
#     content = file.read()
#     content = "Hello World\n" + content
#     file.seek(0)
#     file.write(content)
#     print(content)

# with open("newfile2.txt","r") as file:
#     print(file.read())

#******** Updating at middle of page ********


with open("newfile2.txt","r+") as file:
    list = file.readlines()
    list.insert(1,"Hello Python\n")
    file.seek(0)
    file.writelines(list)
    print(list)

with open("newfile2.txt","r") as file:  
    print(file.read())