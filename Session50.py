import numpy as np
import math
class  Perceptron:

    def __init__(self,inputs):
        self.inputs=inputs

    def summationFunction(self):
        self.sum=0
        for i in range(len(self.inputs)):
            self.sum+=self.inputs[i][0]*self.inputs[i][1]

        print("<< The summation function:",self.sum)


    def activationFunctionLinear(self):
        print("<< Output is:",self.sum)

    def activationFunctionBinary(self):
        threshold=3
        if self.sum >= threshold:
            print("<< Output is 1")
            print("<< Decision Taken")
        else:
            print("<< Output is 0")
            print("<< Decision Not Taken")

    def activationFunctionSigmoid(self):
        value=1/(1+np.exp(-self.sum))
        print("<< Output is:",value)

    def activationFunctionTanh(self):
        value=math.tanh(self.sum)
        print("<< Output is:", value)

    def activationFunctionRelu(self):
        if self.sum < 0:
            print("<< Output is 0")
        else:
            print("<< Output is:",self.sum)

    def activationFunctionSoftmax(self):
        pass

def  main():
    inputs = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    per = Perceptron(inputs)
    per.summationFunction()
    per.activationFunctionLinear()
    per.activationFunctionBinary()
    per.activationFunctionSigmoid()
    per.activationFunctionTanh()
    per.activationFunctionRelu()
    per.activationFunctionSoftmax()



if __name__=="__main__":
    main()