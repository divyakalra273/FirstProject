class customer:
    pass

cref1=customer()#Object Construction
cref2=customer()##Object Construction
cref3=cref1 #Reference Copy Operation

print("Cref1 is:",cref1)
print("Cref2 is:",cref2)
print("Cref3 is:",cref3)
#Operations On Object
#1.Add data in object
cref1.name="John"
cref3.phone="91 9872528568"
cref3.email="john@example.com"
cref1.gender="male"
cref3.address="Redwood Shores"

#Dynamic
cref2.name="Fionna"
cref2.phone="91 9872574849"
cref2.email="fionna@example.com"
cref2.gender="female"
cref2.address="Country Homes"
cref2.vehicle="KA105899"
cref2.company="ABC International"

#2.Read Data from Object
print("Cref1 Details:",cref1.__dict__)
print("Cref2 Details:",cref2.__dict__)
print("Cref3 Details:",cref3.__dict__)

#For End User
print("{} can be called at {} and lives in {}.For E-mail {}".format(cref3.name,cref1.phone,cref1.address,cref1.email))

#3.Update Data in object
cref1.name="John Watson"
cref3.email="john.watson@example.com"

cref2.name="Fionna Flynn"

print("{} can be called at {} and lives in {}.For E-mail {}".format(cref3.name,cref1.phone,cref1.address,cref1.email))

#Deletion
del cref1
del cref2

