# To open and create a file open() function is used.
# Using open() : open(file_name,file_access_mode)
# File_accessing_mode => Our purpose of opening file

##########################################################

# "w" : (Write) writing mode.Creates a file at location
#       Deletes the file content and adds new content

# file = open("newfile.txt","w")
# file.close()

# file = open("C:/users/erenb/desktop/githubprojects/PythonFundamentals/Python File Management/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding ="utf-8") # utf-8 turkish chars
# file.write("Yarasa Reis")
# file.close()

##########################################################

# "a" : (Append) append mode.If file isnt at location ,creates file.
# file = open("newfile.txt","a",encoding ="utf-8") # utf-8 turkish chars
# file.write("\nHello World")
# file.close()

##########################################################

# "x" : (Create) creating mode.If file already exists it gives an error.

file = open("newfile2.txt","x",encoding ="utf-8") # utf-8 turkish chars

# "r" : (Read) reading mode.If file isnt at location ,it gives an error

