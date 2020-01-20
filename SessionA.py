#Single Value Container

age=20

print(age,type(age),id(age))
print(age,type(age),hex(id(age)))
print(age,type(age),oct(id(age)))
print(age,type(age),bin(id(age)))

johnsage=20
print("Johns Age:",age,id(johnsage))

age=30
print(" Age:",age,id(age))

#Containers in memory are stored as Data Structure :Hash tables with algorithm called
fionnasAge=age #copy
print("Fionna Age:",age,id(fionnasAge))