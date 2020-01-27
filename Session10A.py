#Variable arguments in python
def add(*args):
    print(args)
    print(type(args))

    sum=0
    for data in args:
        sum=sum+data
    print("Sum is:",sum)

print(10,20)
print(10,49,794)

def addAgain(numbers):
    sum = 0
    for data in numbers:
        sum = sum + data
    print("Sum is:", sum)

numbers=(10,20,30,40)
addAgain(numbers)