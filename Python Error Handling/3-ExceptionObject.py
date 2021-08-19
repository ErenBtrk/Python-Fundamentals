# x = 10

# if x > 5:
#     raise Exception("x cant be greater than 5")

def check_password(password):
    import re
    if len(password) < 8:
        raise Exception("Password must be atleast 8 characters.")
    elif not re.search("[a-z]",password):
        raise Exception("Password must include lower character.")
    elif not re.search("[A-Z]",password):
        raise Exception("Password must include upper character.")
    elif not re.search("[_@$]",password):
        raise Exception("Password must include alpha numeric character.")    
    elif re.search("\s",password): #\s white space
        raise Exception("Password shouldnt include white space character")

password = "12345678aA_"

try:
    check_password(password)
except Exception as excObj:
    print(excObj)
else:
    print("Valid password.")
finally:
    print("Validation is done.")

#######################################################

class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("Name has too many characters.")
        else:
            self.name = name

p = Person("Aliiiiiiiiiiiiiii",1989)