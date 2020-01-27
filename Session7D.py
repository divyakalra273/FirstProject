def myLen(data):
    count=0
    for i in range(0,len(data)):
        count += 1
    print("The Length of string is:",count)

def myMax(data):
    max=data[0]
    for i in range(0,len(data)):
        if max < i :
            max=i
    print("The max is:",data[max])

def myMin(data):
    min=data[0]
    for i in range(0,len(data)):
        if min > i :
            min=i
    print("The min is:",data[min])
data=[1,2,3,4,5]
print(myLen(data))
print(myMax(data))
print(myMin(data))

#HW Code your own functions




#def myMin(data)

#List Comprehension
print([x**2 for x in data])

productPrices=[1123,1342,3341,4421,5456]
#List Comprehension and expressions give error
#Explore the alternate

numbers = list(range(1,101))
print(numbers)

names=("John","James","Jennie","Jim","John")
names1=list(names)
names2=set(names)

print(names,type(names))
print(names1,type(names1))
print(names2,type(names2))