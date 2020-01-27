"""
    Types of recursion
    1.Direct Recursion
    2.Indirect Recursion
    3.Tail Recursion

"""
def fun1(): #Direct Recursion
    fun1()

def fun2(): #Indirect Recursion
    fun3()

def fun3():
    fun2()

def fun4(): #Tail Recursion
    #...
    #...
    #...
    fun4()


