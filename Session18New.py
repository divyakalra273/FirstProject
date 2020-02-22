class Customer:

    def __init__(self, mode):
        if mode == 1:
            self.id = 0
            self.name = input("Enter Customer Name: ")
            self.phone = input("Enter Customer Phone: ")
            self.email = input("Enter Customers Email: ")
        elif mode == 2:
            self.id = int(input("Enter Customer ID: "))
            self.name = input("Enter Customer Name: ")
            self.phone = input("Enter Customer Phone: ")
            self.email = input("Enter Customers Email: ")
        else:
            pass

    def showCustomerDetails(self):
        print("{} | {} | {}".format(self.name, self.phone, self.email))




repeat = "yes"

while repeat == "yes":

    print("==Welcome to Customer Management App==")
    print("1. Register New Customer")
    print("2. Update Existing Customer")
    print("3. Delete Existing Customer")
    print("4. View All Customers")
    print("5. View Customer by ID")
    print("6. View Customer by Phone")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        customer = Customer(1)
        customer.showCustomerDetails()

        save = input("Would you like to Save Customer? (yes/no): ")
        if save == "yes":

            print(">> CUSTOMER SAVED :)")

    elif choice == 2:

        customer = Customer(2)
        customer.showCustomerDetails()

        save = input("Would you like to Update Customer? (yes/no): ")
        if save == "yes":

            print(">> CUSTOMER UPDATED :)")

    elif choice == 3:

        id = int(input("Enter Customer ID to be Deleted: "))
        delete = input("Would you like to Delete Customer? (yes/no): ")

        if delete == "yes":

            print(">> CUSTOMER DELETED :)")

    elif choice == 4:

        # sql = "select id, name from Customer"

        # print(rows)     # List of Tuple | where each tuple represents row
        # print(type(rows))

        pass

    elif choice == 5:
        id = int(input("Enter Customer ID to be Searched: "))



        print(">> ID Not Found")

    elif choice == 6:
        pass

    repeat = input("Would You Like to Re Use App (yes/no): ")