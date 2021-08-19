'''
students = {
    "120":{
        "name : "Ali",
        "last name" : "Yilmaz",
        "phone" : "532 000 00 01"
    },
    "125":{
        "name" : "Can",
        "last name" : "Korkmaz",
        "phone" : "532 000 00 02"
    },
    "128":{
        "name" : "Volkan",
        "last name" : "Yukselen",
        "phone" : "532 000 00 03"
    }
}
 

    1-Prompt user to enter data and store it in a dictionary

    2-Prompt user to enter a student ID and print it.

''' 
students = {}

# studentID = input("Please enter a student ID : ")
# studentName = input("Please enter student's name : ")
# studentLastName = input("Please enter student's last name :")
# studentPhone = input("Please enter student's phone : ")

# students[studentID] = {
#     "name" : studentName,
#     "last name" : studentLastName,
#     "phone" : studentPhone
# }

studentID = input("Please enter a student ID : ")
studentName = input("Please enter student's name : ")
studentLastName = input("Please enter student's last name :")
studentPhone = input("Please enter student's phone : ")

students.update({
    studentID: {
        "name" : studentName,
        "last name" : studentLastName,
        "phone" : studentPhone
    }
})

studentID = input("Please enter a student ID : ")
studentName = input("Please enter student's name : ")
studentLastName = input("Please enter student's last name :")
studentPhone = input("Please enter student's phone : ")

students.update({
    studentID: {
        "name" : studentName,
        "last name" : studentLastName,
        "phone" : studentPhone
    }
})

studentID = input("Please enter a student ID : ")
studentName = input("Please enter student's name : ")
studentLastName = input("Please enter student's last name :")
studentPhone = input("Please enter student's phone : ")

students.update({
    studentID: {
        "name" : studentName,
        "last name" : studentLastName,
        "phone" : studentPhone
    }
})

userInput = input("Please enter a student ID to show information : ")
print("\n"*5,"*"*50)

print("The student with number {}:\nStudent name is {}\nStudent last name is {}\nStudent phone is {}".format(
    userInput,students[userInput]["name"],students[userInput]["last name"],students[userInput]["phone"])
)
    

