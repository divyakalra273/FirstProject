import numpy as np

array=np.arange(10,51,2)
#Fetching based on indexing
slices=slice(1,20,2)
indexes=list(range(1,20,2))

print(array)
print(slices)
print(array[slices])
print(array[indexes])