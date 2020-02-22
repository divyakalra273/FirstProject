#Inheritance
# It is a relationship where child class is allowed to access properties of parent class
class Parent:
    #Property of class
    vehicle="PB101234"

    def __init__(self,fname,lname,wealth):
        self.fname=fname
        self.lname=lname
        self.wealth=wealth

    def show(self):
        print("{} | {} | {} | {} ".format(self.name,self.lname,self.wealth,Parent.vehicle))


class Child(Parent):
    #Property of child class
    vehicle="PB102233"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show(self):
        print("{} | {} | {}".format(self.name,self.salary,Child.vehicle))


pref=Parent("John","Watson","10000")
print("pref Dictionary")
print(pref.__dict__)
print("Parent Dictionary")
print(Parent.__dict__)
print("Child Dictionary")
print(Child.__dict__)

cref=Child("Fionna Flynn",15000)
print("Dictionary of cref")
print(cref.__dict__) #property of class can be used by child
print(Child.vehicle)
print(cref.vehicle)
#print(cref.fname) Child class cannot access property of an object of Parent Class
#LookUp Rule
#If we have not found an attribute in object ,look up for the same in class
#In Inheritance it shall look up to parent class

print(pref.show())