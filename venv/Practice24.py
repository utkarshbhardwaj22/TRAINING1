class Zomato:

    food_item_count=0
    total_quantity=0

    def __init__(self, name, price, quantity):
        Zomato.food_item_count +=1
        self.name=name
        self.price=price
        self.quantity=quantity

    def show_details(self):
        print("^^^^^^^^^^^^^^^^^^^^")
        print("Dish name:", self.name)
        print("Price: \u20b9", self.price)
        print("Quantity:", self.quantity)
        print("^^^^^^^^^^^^^^^^^^^^")


    def increment(self):
        Zomato.total_quantity += 1
        self.quantity += 1



    def decrement(self):
        Zomato.total_quantity -= 1
        self.quantity -= 1


    def show(self):
        print("Food item count:", Zomato.food_item_count)
        print("Total quantity:", Zomato.total_quantity)


def main():

    ob1 = Zomato("Burger",35, 3)
    ob2 = Zomato("Pizza", 120, 2)
    ob3 = Zomato("Oreo shake", 50, 1)



    ob2.increment()
    ob3.increment()

    ob1.show_details()
    ob2.show_details()
    ob3.show_details()

    ob1.show()

if __name__ == '__main__':
    main()



