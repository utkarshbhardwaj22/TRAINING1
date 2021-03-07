class Fooditem:

    def __init__(self,item_name,item_quantity,item_price):
        self.item_name= item_name
        self.item_quantity= item_quantity
        self.item_price= item_price

    def food_item_details(self):
        return "{}, {}, {}, {}".format(self.item_name,self.item_quantity,self.item_price,(self.item_price*self.item_quantity))


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

file= open("order.csv", "a")
file.write(customer_name)
file.write("\n")


while True:
    code= int(input("Enter the code of item: "))

    if code==0:
        break

    quantity = int(input("Enter the quantity: "))
    items_list = Fooditem(items[code],quantity, prices[code])
    file.write(items_list.food_item_details())
    file.write("\n")

print("Order saved in file.")
