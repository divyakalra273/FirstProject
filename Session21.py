
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("FirebaseFirstProject.json")
firebase_admin.initialize_app(cred)
print("This is awesome")
class Customer:

    def __init__(self):


        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customers Email: ")


    def showCustomerDetails(self):
        print("{} | {} | {} ".format( self.name, self.phone, self.email))

def main():
    db = firestore.client()
    """customer=Customer()
    customer.showCustomerDetails()
    customerdata=customer.__dict__
    print(customerdata,type(customerdata))
    
    db.collection("customers").document(customer.email).set(customerdata)
"""
    docRef=db.collection("customers").document("john@example.com").get()
    print(docRef.to_dict())
if __name__=="__main__":
    main()



