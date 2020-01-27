number=int(input("Enter a number:"))
print("The entered number is",number)
n1=number//100
n2=number % 100
n3=n2//10
n4=n2 % 10
print(n1,n2,n3,n4)
n5=n1+n3+n4
print("The answer is",n5)
if n5 % 2 == 0 :
    print("The number is even")
else:
    print ("The number is odd")

