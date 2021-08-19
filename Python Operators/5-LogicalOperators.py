x = 5
health = 5
continuePlaying = True

#and
result = (x > 5) and (x < 10) 
print(result)
result = (health > 0) and (continuePlaying == True)
print(result)

#or
result = (x > 0) or (x % 2 == 0) 
print(result)
result = (x < 0) or (x % 2 == 0) 
print(result)

#not
result = (x > 0)
print(result)
result = not(x > 0)
print(result)
