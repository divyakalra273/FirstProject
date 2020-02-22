#init: It is a constructor that get executed when we create an object
#self is a refernce variable, which holds the hashcode of current object
class Customer:
    def __init__(self):
        print("Init Executed")
        print("Self is", self)
        self.name="John"


cref1=Customer()
print("cRef is", cref1)
cref1.phone="+91 77777 88888"
print(cref1.__dict__)

cref2=Customer()
print("cRef is", cref2)
cref2.phone="+91 99999 88888"
print(cref2.__dict__)

