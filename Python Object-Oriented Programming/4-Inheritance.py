# Inheritance : 

# Person => name , lastname , age , eat() , run() , drink()
# Student(Person),Teacher(Person)

#Animal => Dog(Animal),Cat(Animal)

class Person():
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        print("Person created")

    def who_am_i(self):
        print("I am a person.")

    def eat(self):
        print("I am eating.")

class Student(Person):
    def __init__(self,firstName,lastName,number):
        Person.__init__(self,firstName,lastName)
        self.studentNumber = number
        print("Student created")

    def who_am_i(self): #override
        print("I am a student")

    def sayHello(self):
        print("Hello from a student.")

class Teacher(Person):
    def __init__(self,firstName,lastName,branch):
        super().__init__(firstName,lastName)
        self.branch = branch
    
    def who_am_i(self): #override
        print(f"I am a {self.branch} teacher") 

p1 = Person("Ali","Yilmaz")
s1 = Student("Isa","Musa",1256)
t1 = Teacher("Ayse","Fatma","Math")

print(p1.firstName + " " +p1.lastName)
print(s1.firstName + " " +s1.lastName + " "+ str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()

p1.eat()
s1.eat()
s1.sayHello()

print(t1.firstName + " " +p1.lastName)
t1.who_am_i()

