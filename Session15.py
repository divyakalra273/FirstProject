class Mcdonald:

    def __init(self,item,price):
        self.item=item
        self.price=price

    def showItem(self):
        print("{}  ".format(self.item,self.price))

class Meal(Mcdonald):

    def upgradeToMeal(self):
        self.meal=True
        self.coke=True
        self.fries=True
        self.toy=True

        Mcdonald.price+=150

    def showMealOrder(self):
        self.showCustomer

        customerDetails=self.__dict__
        keys=customerDetails.keys()

        if "meal" in keys:
            print("Your order is upgraded to a Meal.{} , {} and {} added to order".format(self.coke,self.fries,self.toy))


cref1=Mcdonald("Burger","80")
print(cref1.__dict__)






