name = "Yarasa Reis"

for letter in name:
    if(letter == 'a'):
        continue
    if(letter == 'R'):
        break
    print(letter)

x = 0
while x<5:
    if(x == 2):
        break
    print(x)
    x+=1

x = 0
while x<5:
    x+=1
    if(x == 3):
        continue
    print(x)

# Sum of the odd numbers between 1-100

x = 0
sum = 0
while x <= 100:
    x += 1
    if( x % 2 == 0):
        continue
    sum += x

print(sum)