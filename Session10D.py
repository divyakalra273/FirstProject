"""
def maxNumber(data):
    max=data[0]
    for i in data:
        if i>max:
            max=i
    return max

 number=[10,20,30,40,50]
print("{} Max number in {} is {}".format(number,maxNumber(number)))

"""
def maxNumber(data,length):
    if length == 1:
        return data[0]
    else:
        num= maxNumber(data,length-1)

    if num> data[length-1]:
        return num
    else:
        return data[length-1]

number=[10,20,30,80,45]
print("The max is:",maxNumber(number,5))

