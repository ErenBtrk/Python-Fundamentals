#global scope
x = "global x"

def function():
    #local scope
    #x = "local x"
    print(x)

function()
print(x)

#########################################

name = "bat" #global

def changeName(new_name):
    name = new_name #local
    print(name)

changeName("Eagle")
print(name)

#########################################

name = "global string"

def greeting():
    #name = "Ali"

    def hello():
        #name = "Isa"
        print("hello " + name)

    hello()

greeting()

#########################################

x = 50
def test():
    global x
    print(f"x : {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)