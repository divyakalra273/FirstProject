#Passing refernces | As Value
def square (num):
    print("[Square ]The num is:", num,hex(id(num)))
    num = num * num
    print("The num is:",num, hex(id(num)))


num = 10 #Num is a reference variable
print("[Main]The num is:",num, hex(id(num)))
square(10)
print("The num is:",num, hex(id(num)))