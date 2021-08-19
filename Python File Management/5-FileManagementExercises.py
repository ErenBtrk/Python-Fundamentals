def calculate_note(line):
    line = line[:-1]
    my_list = line.split(':')
    studentName = my_list[0]
    notes = my_list[1].split(',')

    note1 = int(notes[0]) 
    note2 = int(notes[1]) 
    note3 = int(notes[2]) 

    average = (note1 + note2 + note3) / 3

    if average >= 90 and average <= 100:
        letter = "AA"
    elif average >= 85 and average <= 89:
        letter = "AB"
    elif average >= 80 and average <= 84:
        letter = "BA"
    elif average >= 75 and average <= 79:
        letter = "BB"
    elif average >= 70 and average <= 74:
        letter = "BC"
    elif average >= 65 and average <= 69:
        letter = "CB"
    elif average >= 60 and average <= 64:
        letter = "CC"
    elif average >= 50 and average <= 59:
        letter = "CD"
    elif average >= 40 and average <= 49:
        letter = "DC"
    else : 
        letter = "FF"

    return studentName + ": " + letter + "\n"

def read_average():
    with open("exam_notes.txt","r") as file:
        for line in file:
            print(calculate_note(line))
def enter_note():
    firstName = input("Student first name:")
    lastName = input("Student last name:")
    note1 = input("note 1 : ")
    note2 = input("note 2 : ")
    note3 = input("note 3 : ")

    with open("exam_notes.txt","a") as file:
        file.write(firstName + ' ' + lastName + ':' + note1 + ',' + note2 + ',' + note3 + '\n' )

def save_notes():
    with open("exam_notes.txt","r") as file:
        my_list = []

        for i in file:
            my_list.append(calculate_note(i))

        with open("results.txt","w") as file2:
            for i in my_list:
                file2.write(i)

while True:
    userInput = input("1-Read the notes\n2-Enter a note\n3-Save the notes\n4-Exit\n")

    if(userInput == "1"):
        read_average()
    elif(userInput == "2"):
        enter_note()
    elif(userInput == "3"):
        save_notes()
    else:
        break