#1 to 100

x = 1

while x <= 100:
    if(x % 2 != 0):
        print("Number is odd ",x)
    else:
        print("Number is even ",x)
    x = x+1

print("Loop ended.")

name = ""
while not name.strip():
    name = input("Enter your name : ")
print(f"Hello ,{name}")