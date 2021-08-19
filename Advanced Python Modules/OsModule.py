import os
import datetime

# result = dir(os)
# print(result)
result = os.name
print(result)
result = os.getcwd() #the directory of this file
print(result)

# os.mkdir("newdirectory") #creates a new folder
# os.makedirs("C:\\newdirectory/newdirectory2") #creates a new folder under first one
# os.chdir("C:\\") #changes directory
# os.chdir("..") # moves to previous directory
# os.chdir("../..") # moves to 2.previous directory

#listing
result = os.listdir()
print(result)
result = os.listdir("C:\\")
print(result)

for folder in os.listdir():
    if folder.endswith(".py"):
        print(folder)

result = os.stat("DatetimeModule.py")
print(result)
# result = result.st_size/1024 #returns the size of file
# print(result) 
# result = datetime.datetime.fromtimestamp(result.st_ctime) #returns the file's created date
# print(result)
# result = datetime.datetime.fromtimestamp(result.st_atime) #returns the file's last changed date
# print(result)

# os.system("notepad.exe") #opens the file
# os.rename("newdirectory","newfolder") #change the name of folder
# os.rmdir("newdirectory") #removes the file
# os.removedirst("newdirectory/newdirectory2") #removes the folder under first one

# path

# result = os.path.abspath("OsModule.py") #exact directory of file
# print(result)

# result = os.path.dirname("C://python/Advanced-Python-Modules/OsModule.py")
# print(result)

result = os.path.dirname(os.path.abspath("OsModule.py"))
print(result)
result = os.path.exists("OsModuleasdsdf.py")
print(result)
result = os.path.exists("C:\\Users\erenb\Desktop\githubprojects")
print(result)
result = os.path.isdir("C:\\Users\erenb\Desktop\githubprojects")
print(result)
result = os.path.isfile("C:\\Users\erenb\Desktop\githubprojects")
print(result)
result = os.path.join("C:\\","deneme","deneme1")
print(result)
result = os.path.split("C:\\deneme")
print(result)
result = os.path.splitext("OsModule.py")
print(result)
