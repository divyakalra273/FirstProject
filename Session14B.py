# Why Inheritance
# code Reusability
#only write additional details in child
#Saves Time[Development]
#Inheritance is a IS-A relation (Generalisation)
#HAS-A relation menas Associativity
class Shoe:

    def __init__(self,pid,name,price,brand,size):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.size = size

    def showShoeDetails(self):
        print("------{} | {}--------".format(self.name,))




