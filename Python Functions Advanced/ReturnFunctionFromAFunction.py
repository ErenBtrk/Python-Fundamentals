def exponentation(number):

    def inner(power):
        return number ** power

    return inner


two = exponentation(2)
three = exponentation(3)

print(two(3))
print(three(3))

#####################################################################

def access_validation(page):
    def inner(role):
        if role == "Admin" :
            return "can access {0} role {1} page.".format(role,page)
        else:
            return "can not access {0} role {1} page.".format(role,page)   
    return inner    

user1 = access_validation("Product Edit")
print(user1("Admin"))
print(user1("User"))


#####################################################################

def process(process_name):
    def sum(*args):
        sum = 0
        for i in args:
            sum += i
        return sum
    
    def multip(*args):
        multip = 1
        for i in args:
            multip *= i
        return multip

    if process_name == "sum":
        return sum
    else:
        return multip

sum = process("sum")
print(sum(1,3,5,6,7))

multip = process("multip")
print(multip(1,2,3,6,4))