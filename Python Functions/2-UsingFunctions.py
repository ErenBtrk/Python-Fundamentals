def sayHello(name = "user"):
    return "Hello " + name

message = sayHello("YarasaReis")
message = sayHello("Babba")
print(message)

def total(num1,num2):
    return num1+num2

sum = total(10,20)
print(sum)

def countAge(birthDay):
    return 2019 - birthDay

ageAli = countAge(2002)
ageAyse = countAge(1993)
ageSena = countAge(2005)

print(ageAli,ageAyse,ageSena)

def howManyYearsLeftToGetRetired(birthDay,name):
    '''
    DOCSTRING:How many years left you to get retired according to your age
    INPUT:Birthday
    OUTPUT:Calculated year info
    '''
    age = countAge(birthDay)
    retired = 65 - age

    if retired > 0:
        print(f"{retired} years left you to get retired.")
    else:
        print(f"You are already retired.")

howManyYearsLeftToGetRetired(1983,"Ali")
howManyYearsLeftToGetRetired(1950,"Ayse")

print(help(howManyYearsLeftToGetRetired))

print(help(list.append))