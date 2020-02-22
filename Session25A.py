import numpy as np
import time

timeStamp1 = time.time()
# print(timeStamp1)

array1=np.array(list(range(1,1001)))
print(array1)
for num in array1:
    print(num)

timeStamp2 = time.time()
print(timeStamp2-timeStamp1)
numbers=list(range(1,1001))
timeStamp3 = time.time()
for num in numbers:
    print(num)
timeStamp4 = time.time()
print(timeStamp4-timeStamp3)