def sum(a,b):
    return a+b

def subst(a,b):
    return a-b

def multip(a,b):
    return a*b

def div(a,b):
    return a//b

def process(f1,f2,f3,f4,process_name):
    if(process_name == "sum"):
        print(f1(2,3))
    elif(process_name == "subst"):
        print(f2(5,3))
    elif(process_name == "multip"):
        print(f3(3,4))
    elif(process_name == "div"):
        print(f4(10,2))
    else:
        print("Invalid process.")

process(sum,subst,multip,div,"sum")
process(sum,subst,multip,div,"subst")
process(sum,subst,multip,div,"multip")
process(sum,subst,multip,div,"div")
process(sum,subst,multip,div,"expo")