class CA:
    def __init__(self):
        print("CA object Constructed")
    #If you redeine a function again, the previous function will get deleted
    def __init__(self,num):
        print("CA object Constructed and num is:",num)
    #In Python Overloading is not Supported
cRef=CA()