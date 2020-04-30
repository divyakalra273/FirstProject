#Array Maths
import numpy as np
data = [
    (8,9),
    (10,12),
    (13,14)
]
arr1=np.array(data)
print(arr1)
print(arr1[0:2,1])
print(arr1.min())
print(arr1.max())
print(arr1.sum(axis=0))#axis=o columns
print(arr1.sum(axis=1))#axis=1 rows
print(arr1.min(axis=0))
print(arr1.min(axis=1))
print(arr1.max(axis=0))
print(arr1.max(axis=1))
print("======Sqrt Function======")
print(np.sqrt(arr1))

print("==std==")
print(np.std(arr1))
a1=np.array([(1,2,3),(4,5,6)])
a2=np.array([(1,2,3),(4,5,6)])

print(a1+a2)
print(a1-a2)
print(a1*a2)
#print(a1+a2)
print(a1+a2)
print(a1/a2)
print(a1//a2)

a3=a1+a2
a3=np.add(a1,a2)
print(a3)
print("========")
x=np.array([(1,2),(4,5)])
y=np.array([(5,6),(7,8)])
z=np.dot(x,y)
print(z)
print("=========")
u=np.array([9,10])
v=np.array([11,12])
w=np.dot(u,v)
print(w)

