import pandas as pd
import numpy as np

numbers=[10,20,30,40,50]
numbers2=np.arange(10,51,10)
numbers3={1:10,2:20,3:30,4:40}
series=pd.Series(numbers)
print(series)
print("========")
series2=pd.Series(numbers2)
print(series2)
print("========")
series3=pd.Series(numbers3)
print(series3)

print("------------------")
#Access the data using indexing
print(series[1])
print(series2[3])
print(series3[1])

print("------Slicing-------")
print(series[1:3])
print(series2[3:])
print(series3[2:4])

series3[3]=35
print(series3)

print("----------")
