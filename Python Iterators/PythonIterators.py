# list1 = [1,2,3,4,5]

# iterator = iter(list1)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# #print(next(iterator)) # stop iteration

# for i in list1:
#     print(i)

# list1 = [1,2,3,4,5]
# iterator = iter(list1)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

class MyNumbers:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if(self.start <= self.end):
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbers(10,20)

myIter = iter(list)

#print(next(myIter))
#print(next(myIter))

while True:
    try:
        element = next(myIter)
        print(element)
    except StopIteration:
        break

# for x in list:
#     print(x)