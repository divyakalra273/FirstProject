import pandas as pd

num1=[10,20,30,40,50]
num2=[10,20,30,40,50]

emp1={"name":"John","age":22,"salary":30000}
emp2={"name":"Fionna","age":26,"salary":40000}
emp3={"name":"Dave","age":24,"salary":54000}
emp4={"name":"Kia","age":27,"salary":60000,"email":"kia@example.com"}

frame1=pd.DataFrame([num1,num2])
frame2=pd.DataFrame([emp1,emp2,emp3,emp4])

print(frame1)
print("----------")
print(frame2)

print("----Accessing Data------")
#Fetch data column wise
print(frame1[0])
print(frame2["name"])
print(frame1[1][1])
print(frame2["salary"][2])

print("-------Slicing-------")
print(frame1[0:2])
print("-------------")
del frame1[0]
print(frame1)

frame1[1][1]=60
print(frame1)