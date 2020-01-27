name="john watson"
print(name,type(name),hex(id(name)))

#name is a refernce variable whic hold the hashcode of John watson
#john watson will be created in constant pool

print("The length of string:",len(name))
print("Max of name is:",max(name))
print("Min of name is",min(name))

print(name[1])
print(name[len(name)-1])

print(name[1:4])
print(name[1],name[-1])
print(name[1],name[-2])#Negative indexing means reverse order
print(name[::-1])

email=input("Enter your Email:")
print("You entered",email)
phone=input("Enter your Phone No:")
print("You entered",phone)

if "@" in email and "." in email:
    print("You entered valid email")
else:
    print("you entered invalid email")

if len(phone) > 10 and len(phone) <=15:
    print("Invalid Phone")
else:
    print("Valid Phone")

