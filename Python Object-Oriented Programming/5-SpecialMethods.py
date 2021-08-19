myList = [1,2,3]
myString = "my string"

# print(len(myList))
# print(len(myString))
# print(type(myList))
# print(type(myString))

class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("movie object is created.")
    
    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("movie has deleted.")


m = Movie("Eyes Wide Shut","Stanley Kubrick",130)

print(str(myList))
print(str(m))


print(len(myString))
print(len(m))

del m

#print(m) its gives an error cause m object is deleted
