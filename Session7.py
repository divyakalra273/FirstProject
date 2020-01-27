"""Sequences in python
    Sequence : Data with quite similar type

    Sequences listed below are also known as build in Data Structures in Python

    Why data should be structured?
    1.Sort
    2.Search
    3.Filter


    1.Tuple
    2.List
    3.String
    4.Set
    5.Dictionary

    Operation on Sequences
    1.Concatenation
    2.Repetition
    3.Membership
"""

students=("John","Jennie","Jim","Jack","George")
print(students)
print(type(students))
#Concatenation
newStudents= students + ("Fionna","Joe")
print(newStudents)
print(students)


#Repitation
print(students*2)


#Membership Testing
print("John" in students)
print("dave" not in students)

#Indexing
print(students[0])

#Slicing
print(students[0:2]) #o is inclusive and 2 is exclusive
print(students[1:4])
filteredStudents = students[1:4]
print(filteredStudents)

print()

#Basic Loop
for i in range(0,len(students)):
    print(students)


#Enhanced version of for-loop or for each loop
for student in students:
    print(student)