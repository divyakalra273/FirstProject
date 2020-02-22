class Product:

    def __init__(self,pid,name,price):
        self.pid=pid
        self.name=name
        self.price=price
        self.nextProduct = None
        self.prevProduct = None
    def showProductDetails(self):
        print("---------------")
        print("{}\t{}\t{}\t".format(self.pid ,self.name ,self.price))
        print("---------------")

class LinkedList:

    def __init__(self):
        print("Linked List Created")
        print(self)

    def append(self,product):
        print(product)
        if self.head==None:
            self.head=product
        else:
            pass
