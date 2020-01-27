num = 5
print("The Number is:",num)
def square(n):
    global num     #This num belongs to main frame. Now num=n means that it will use the num of main frame
    n = n*n
    num=n       #The value of n is copied in num that exits in Frame:Square
    print("The n is:",n)
    print("The num is:",num) #There is not a complusion to write a return statement
    #The last statement always means Return
square(7)
print("The num is:",num)