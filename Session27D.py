"""
BroadCasting:when we work with arrays of different shapes

"""
import numpy as np

x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("x is:",x)
print(x.shape)

print()

v=np.array([1,0,1])
print("v is:",v)
print(v.shape)
y=np.empty_like(x)
print("y is:",y)
print(y.shape)

for i in range(4):
    y[i,:]=x[i,:] + v

print("y is:",y)
print(y.shape)