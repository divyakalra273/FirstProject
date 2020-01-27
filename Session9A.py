employee ={
    "name":"John",
    "eid":101,
    "salary":60000,
    "rating":4.5
}

print(employee,type(employee))
print(len(employee))
print(max(employee))
print(min(employee))

employee["name"]="John Watson"
print(employee)

employee["address"]="Model Town"
print(employee)

#delete key value pair
del employee["address"]
print(employee)

#Deletion of dictionary
#del employee
#print(employee)

keys=employee.keys()
values=employee.values()

print(keys,type(keys))
print((values,type(values)))