import numpy as np

array=np.loadtxt("data.txt",dtype=np.int)
print(array)

arr1D=np.arange(10,200,10)
print(arr1D)
#np.savetxt("arraydata.txt",arr1D)
np.savetxt("arraydata1.txt",arr1D,fmt="%04f")
print("data Saved")