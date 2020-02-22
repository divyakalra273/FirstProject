import numpy as np

array1=np.ones(8)
array2=np.zeros(8)

print(array1)
print()
print(array2)
print()

print(array1.shape)
print(array2.shape)


array=array1.reshape(2,2,2)
print(array)
print(array.shape)
array=array1.reshape(2,2,2)
print(array)
print(array.shape)

originalarray=array.ravel()
print(originalarray)
print()