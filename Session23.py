import json
employee={
    "eid":101,
    "name":"John",
    "salary":3000,
    "projects":["CMS","GMS"],
    "manager":{"mid":201,"name":"Fionna"}

}
print(employee)
print(type(employee))

#Convert Dictionary Into Json
#Json is a String representation of dictionary

jsonData=json.dumps(employee)
print(jsonData)
print(type(jsonData))

#Convert Json to Dictionary
employeeDictionary=json.loads(jsonData)
print(employeeDictionary)
print(type(employeeDictionary))