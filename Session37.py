"""
    Supervised Machine Learning Algo
    Linear Regression->Predictive Modeling Technique

    Initial Data
    x=[1,2,3,4,5]
    y=[2,3,5,6,7]

    Regression Line  | Linear
    Y=b0 + b1X

    Primary Objective-> To find the slope of line with given data points
    i.e. b1-> since b1 is slope of line

    Mean of X [MX]=3
    Mean of Y [MY]=4

    Step 1:
    X   Y   X-MX  0

"""
import numpy as np
class LinearRegressionModel:
    def __init__(self):
        self.b0=0
        self.b1=0
        self.mse=0

    def fit(self,X,Y):
        self.X=X
        self.Y=Y
        self.b1 =  np.sum((self.X - np.mean(self.X))* (self.Y - np.mean(self.Y))) / np.sum(np.square(self.X - np.mean(self.X)))
        self.b0= np.mean(self.Y)-(self.b1 * (np.mean(self.X)))
        Y1=self.predict(self.X)


    def predict(self,X):
        Y=self.b0 + self.b1*X







X=[1,2,3,4,5]
Y=[2,4,5,4,5]
model=LinearRegressionModel()
b1=model.fit(X,Y)