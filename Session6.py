#Recursion : Executing the same function again and again from same function
def show(num):
    if num == 0:       #Checks the condition
        return

    print("The num is:",num)
    num -= 1
    show(num)
#Explore the running time of Loop and Recursive Function

