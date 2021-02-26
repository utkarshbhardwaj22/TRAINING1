amount = int(input("Enter the amount:"))
print()
print("1.Apply Promocode: ZOMATO and get 40% off upto 100 (Amount>=200)\n"
      "2.Apply Promocode: JUMBO and get 50% off upto 200 (Amount>=500)\n"
      "3.Apply Promocode: BINGO and get 20% off (Amount>=100)\n")

if amount >=100:
    promo_code= input("Enter Promocode:")

    if ((promo_code== "ZOMATO") & (amount>=200)):
        discount= 0.40*amount
        if discount >= 100:
            discount=100
            print("Your discount:", discount)
        amount -= discount

    elif ((promo_code== "JUMBO") & (amount>=500)):
        discount= 0.50*amount
        if discount >= 200:
            discount=200
            print("Your discount:", discount)
        amount -= discount

    elif (promo_code== "BINGO"):
        discount= 0.20*amount
        amount -= discount
        print("Your discount:", discount)

    else: print("Invalid Promocode :(")


print("Please pay: \u20b9",amount)

