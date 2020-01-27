menu = {
    "paneer":200,
    "dal":100,
    "roti":10,
    "champ":150,
    "salad":10,
    "noodles":120
}

cart=[]
print(cart,type(cart),len(cart))
choice="yes"
while choice=="yes":
    fooditem = input("Enter a food item:")
    if fooditem in menu:
        cart.append(fooditem)
        choice = input("Would you like to add another food item(yes/no):")
    else:
        print("Please choose another food item")

print("Your cart:",cart)
totalPrice=0
for item in cart:
    totalPrice=totalPrice+menu[item]

print("Total Prices:",totalPrice)
promocode=input("Enter Promo Code:")
if totalPrice > 200 and promocode == "Zomato":
    totalPrice = totalPrice - (0.4 * totalPrice)
    print(">> Promo Code Zomato Applied Successfully. 40% OFF. Please Pay: \u20b9", amount)

elif totalPrice > 100 and promocode == "JUMBO":

    discount = 0.5*totalPrice
    # Nested if/else
    if discount > 150:
        totalPrice -= 150
    else:
        totalPrice -= discount

    print(">> Promo Code JUMBO Applied Successfully. 50% OFF. Please Pay: \u20b9", totalPrice)

else:
    print(">> No Promo Code Found and no Discount Available")
    print(">> Please Pay: \u20b9", totalPrice)

#extend functions supports mutability
"""
cart.extend(["Salad","Noodles"])
print("Surprises in Cart:",cart)

cart.insert(1,"Soya Champ")
print("More Surprise",cart)

cart.pop(2)
print("Final Cart",cart)
"""