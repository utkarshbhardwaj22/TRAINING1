
items = {
    101: "Burger",
    102: "Pizza",
    103: "Masala Dosa",
    104: "Spring roll",
    105: "Coke"
}

prices = {
    101: 40,
    102: 120,
    103: 60,
    104: 40,
    105: 20

}

customer_name= input("Enter Customer name: ")
order_list= []

while True:
    code= int(input("Enter the code of item: "))

    if code==0:
        break

    quantity= int(input("Enter the quantity: "))
    items_list= []
    items_list.append(items[code])
    items_list.append(quantity)
    items_list.append(prices[code])
    items_list.append(prices[code]*quantity)

    order_list.append(items_list)


file= open("order.csv", "a")
file.write(customer_name)
file.write("\n")


print("Final Order details for: ",customer_name)
print("^^^^^^^^^^^^^____________^^^^^^^^^^^^^")
print(order_list)
print("^^^^^^^^^^^^^____________^^^^^^^^^^^^^")

for order in order_list:
    file.write("{}, {}, {}, {}".format(order[0],order[1],order[2],order[3]))
    file.write("\n")

print("Order saved in file.")
