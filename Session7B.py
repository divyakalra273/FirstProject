students={"John","Jennie","John","Jim","Jack","George"}
print(students)
print(type(students))
#Concatenation
#newStudents= students + {"Fionna","Joe"}
#print(newStudents)
#print(students)


#Repitation
#print(students*2)


#Membership Testing
print("John" in students)
print("dave" not in students)
"""
#Indexing
print(students[0])

#Slicing
print(students[0:2]) #o is inclusive and 2 is exclusive
print(students[1:4])
filteredStudents = students[1:4]
print(filteredStudents)

print()
"""
#Basic Loop
#for i in range(0,len(students)):
 #   print(students)


#Enhanced version of for-loop or for each loop
for student in students:
    print(student)