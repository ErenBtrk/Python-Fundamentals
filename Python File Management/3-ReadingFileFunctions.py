with open("newfile2.txt","r") as file:
    content = file.read(10) #reads first 10 byte
    print(content)
    file.seek(0) #cursor go back to 0.location
    print(file.tell()) #returns cursors location
    content2 = file.read()
    print(content2)
