#class 

class Person:
    #pass #keyword for classes without attributes or methods
    #class attributes
    adress = "No information"
    name = "" 
    year = 0
    #constructor
    def __init__(self,name,year):
        #object attributes
        self.name = name
        self.year = year
        print("init method is working.")
        #methods
    

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