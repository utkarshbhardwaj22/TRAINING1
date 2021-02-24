"""
Dictionary
also known as map or hashmap
"""

print("The Menu of Restaurant:")
menu={"lays":20,
      "paneer":130,
      "chicken":200,
      "donut":40
      }
print(menu)

cart=[]
choice="yes"

while choice =="yes":
    item=input("Enter your Item:")
    cart.append(menu[item])

    choice=input("Would you like to add more items?(yes/no)")

print("Your Cart[{}]".format(len(cart)))
print(cart)

total=sum(cart)


promo_code=input("Apply Promocode")

if promo_code=="CRAVINGS":
    print("Promocode Applied")
    total=total-(0.20*total)
else:print("Promocode not Valid")

print("You have to pay:",total)
