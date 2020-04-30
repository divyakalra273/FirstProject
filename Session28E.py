import numpy as np
import matplotlib.pyplot as plt

X=np.arange(1,21)
Y=np.sin(X)
Y1=np.tan(X)
plt.plot(X,Y)
plt.plot(X,Y1)
plt.show()