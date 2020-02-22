"""
#Built in APIs i.e Functions

#Strings are IMMUTABLE
name="Fionna Flynn"
print("Name is",name)
#Manipulation operations will create a new string in memory
newName=name.upper()
print("Name is",newName)

authorName="john watson"
#We are creating a new string and referring it in our old reference variable
authorName=authorName.capitalize()
print("Author Name is:",authorName)

names="John,Jennie,Jim,John,Jack,Joe"
print(names[0])
print(names[len(names)-1])
newNames=names.replace('J','K')
print(names)
print(newNames)
num=names.count("John",0,len(names))
print("Num is:",num)"""
data = """
    Work Hard, Get Luckier
    Search the candle ,rather than cursing the darkness
"""

def count(data,word):
    c=0
    j=0
    for i in range(data[0],len(data)):
        for j in range(word[0], len(word)):
            if data[i]==word[j]:
                j=j+1
            c=c+1
    print("The count is:",c)



word="the"
print(count(data,word))
