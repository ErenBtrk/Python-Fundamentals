#class 

class Person:
    #pass #keyword for classes without attributes or methods
    #class attributes
    adress = "No information"
    
    #constructor
    def __init__(self,name,year):

        #object attributes
        self.name = name
        self.year = year
        print("init method is working.")
    #instance methods
    def intro(self):
        print(f"Hello World from {self.name}")
    def calculateAge(self):
        return 2021 - self.year
    

#object (instance)

p1 = Person("Bat",1993)
print(p1)
p1.name = "Ahmet" #Updating
print(f"name : {p1.name} , year : {p1.year} , adress : {p1.adress}") #accessing object attributes

p2 = Person(name = "Eagle",year = 1990)
print(p2)
print(f"name : {p2.name} , year : {p2.year} , adress : {p2.adress}") #accessing object attributes


print(type(p1))
print(type(p2))

print(p1==p2)

p1.intro()
p2.intro()

print(p1.calculateAge())
print(p2.calculateAge())


class Circle:
    #Class object attribute
    pi = 3.14

    def __init__(self,radius = 1):
        self.radius = radius

    #Methods
    def calculatePerimeter(self):
        return 2 * self.pi * self.radius
    def calculateArea(self):
        return self.pi * (self.radius ** 2)

c1 = Circle() # radius = 1
c2 = Circle(5) 

print(f"c1 : area = {c1.calculateArea()} , c1 : perimeter = {c1.calculatePerimeter()} ")
print(f"c2 : area = {c2.calculateArea()} , c2 : perimeter = {c2.calculatePerimeter()} ")

