import numpy as np

x=np.array([(1,2,3),(4,5,6)])
y=np.array([(1,2,3),(4,5,6)])

print(np.vstack((x,y)))
print(np.hstack((x,y)))

z=np.arange(0,101,10)
print(np.log10(z))
print(np.sin(z))
print(np.tan(z))