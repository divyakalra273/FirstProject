import tkinter
from tkinter import *


class Customer:
    def __init__(self,name=None,phone=None,email=None):
        self.name=name
        self.phone=phone
        self.email=email

def clickHandler():
    print("Button Clicked")

window=Tk()

lblTitle=Label(window,text="Customer Managemant Solution")
lblTitle.pack()
lblName=Label(window,text="Enter Customer Name")
lblName.pack()

entryName=Entry(window)
entryName.pack()

lblPhone = Label(window, text="Enter Customer Phone")
lblPhone.pack()

entryPhone = Entry(window)
entryPhone.pack()
lblEmail = Label(window, text="Enter Customer Email")
lblEmail.pack()

entryEmail = Entry(window)
entryEmail.pack()

btnAddCustomer=Button(window,text="Add Customer",command=clickHandler)
btnAddCustomer.pack()





window.mainloop()