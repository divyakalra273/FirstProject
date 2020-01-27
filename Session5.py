amount = int(input("Enter the amount"))
promoCode = input("Enter the Promocode")

if amount > 200:
    if promoCode=="ZOMATO":
        amount = amount - (0.4 * amount)
        print(" ZOMATO Applied Successfully !! 40% OFF")
        print(" Please Pay: \u20b9", amount)
    else:
        print(" Try using Zomato to get 40% OFF")

elif amount > 100:
    if promoCode == "JUMBO":
        discount = 0.5 * amount
        if discount > 150:
            amount = amount - 150
        elif discount < 150:
            amount = amount - discount
            print(">> JUMBO Applied Successfully !! 50% OFF upto 150")
            print(">> Please Pay: \u20b9", amount)
        else:
            print(">> Try using Zomato to get 50% OFF")

else:
    print(">> Please Pay: \u20b9", amount)


"""
    if promoCode == "JUMBO":
        discount = 0.5 * amount
        if discount > 150:
            amount = amount - 150
        elif discount < 150:
            amount = amount - discount
            print(">> JUMBO Applied Successfully !! 50% OFF upto 150")
            print(">> Please Pay: \u20b9", amount)
        else:
            print(">> Try using JUMBO to get 50% OFF")

elif amount > 100:
    if promoCode == "ZOMATO" and amount > 200:
        amount = amount - (0.4 * amount)
        print(" ZOMATO Applied Successfully !! 40% OFF")
        print(" Please Pay: \u20b9", amount)
    else:
        print(" Try using ZOMATO to get 40% OFF")


else:
    print(">> Please Pay: \u20b9", amount)
"""