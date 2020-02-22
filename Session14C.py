""" Different types of Inheritance
 1.Single Level
        A
        |
        B
2. Multi Level
        A
        |
"""
class A:
    a=10
    def __init__(self,b):
        print("Constructor of Class A")
        self.b=b

    def show(self):
        print("a is:", A.a)
        print("b is:",self.b)

class B:
    x=10
    def __init__(self,y):
        print("Constructor of Class B")
        self.y=y

    def show(self):
        print("x is:",B.x)
        print("y is:",self.y)

class C(A,B):
    pass

cref=C(10)
cref.show()
print(cref.__dict__)
#1.Which parent init should be used to construct object of C?
#2.which parent show should be executed?
#3.Is Multiple Inheritance safe to use?
