
# try:
#     x = int(input("x : "))
#     y = int(input("y : "))
#     print(x/y)

# except (ZeroDivisionError,ValueError) as errorObj:
#     print("Your input was incorrect.")
#     print(errorObj)

# try:
#     x = int(input("x : "))
#     y = int(input("y : "))
#     print(x/y)

# except:
#     print("Your input was incorrect.")

while True:
    try:
        x = int(input("x : "))
        y = int(input("y : "))
        print(x/y)
    except Exception as excObj: 
        print("Your input was incorrect.")
        print(excObj)
    else:
        break
    finally:
        print("Try exception is ended.")
    