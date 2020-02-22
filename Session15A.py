class Customer:

    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email

    def showCustomer(self):
        print("Customer Details are:Name{},Phone{},E-Mail{}".format(self.name,self.phone,self.email))

class PrimeCustomer(Customer):

    def __init__(self, customer):
        customer.prime = True
        customer.videos = True
        customer.music = True

    def showPrimeCustomer(self, customer):
        customer.showCustomer()

        customerDetails = customer.__dict__
        keys = customerDetails.keys()

        if "prime" in keys:
            print("PRIME FEATURES: VIDEOS: {} | MUSIC: {}".format(customer.videos, customer.music))


cRef1 = Customer("John", "+91 99999 88888", "john@example.com")
primecRef1 = PrimeCustomer(cRef1)
print(cRef1.__dict__)
print(primecRef1.__dict__)

primecRef1.showPrimeCustomer(cRef1)
