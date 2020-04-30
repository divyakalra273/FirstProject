from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

X=[1,2,3,4,5]
Y=[2,4,5,4,5]

data=stats.linregress(X,Y)
print("The slope is",data[0])
print("Intercepter is",data[1])

maxX=np.max(X)+10
minY=np.min(Y)-10

print("maxX:",maxX)
print("minY:",minY)

x=np.linspace(minY,maxX,100)
print(x)
y=data[1] + data[0] * x
print("--------")
print(y)
plt.plot(x,y)
plt.scatter(X,Y,label="Points",color="red")
plt.show()