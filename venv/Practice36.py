import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebase-key.json')




class Dish:

    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating


    def show_dish(self):
        print("-------------------------------------")
        print("|  {}  |  {}  |  {}  |".format(self.name, self.price, self.rating))
        print("-------------------------------------")


    def to_dictonary(self):
        return {
            'name': self.name,
            'price': self.price,
            'rating': self.rating

        }



class Menu:

    def __init__(self, title, num_of_dishes, dishes): # dishes will be referring to a List of Dish Objects
        self.title = title
        self.num_of_dishes = num_of_dishes
        self.dishes = dishes

    def show_menu(self):
        print("^^^^^MENU^^^^^")
        print("-------------------------------------")
        print("|  {}  |  {}  |".format(self.title, self.num_of_dishes))
        print("-------------------------------------")

        print("DISHES: ")
        for dish in self.dishes:
            dish.show_dish()

    def to_dictonary(self):
        return {
            'title': self.title,
            'num_of_dishes': self.num_of_dishes,


        }


class Restaurant:

    def __init__(self, name, phone, address, description, ratings, menu):
        self.name = name
        self.phone = phone
        self.address = address
        self.description = description
        self.ratings = ratings
        self.menu = menu


    def show_restaurnat(self):
        print("^^^^^RESTAURANT^^^^^")
        print("-------------------------------------")
        print("|  {}  |  {}  |".format(self.name, self.phone))
        print("|  {}  |  {}  |".format(self.address, self.ratings))
        print(self.description)
        print("-------------------------------------")

        self.menu.show_menu()



    def to_dictonary(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'address': self.address,
            'description': self.description,
            'ratings': self.ratings

        }



def main():
    cred = credentials.Certificate('firebase-key.json')

    firebase_admin.initialize_app(cred)



    restaurant = Restaurant(
                            name="Gopal Sweets",
                            phone="+91 99999 66666",
                            address="Sarabha Nagar",
                            description="Mithai, Bakery, Indian, Chinese etc",
                            ratings=4.7,
                            menu=Menu(
                                        title="Veg Indian Food",
                                        num_of_dishes=5,
                                        dishes=[
                                            Dish(name="Samosa", price=36, rating=4.5),
                                            Dish(name="Chole Bhature", price=143, rating=4.6),
                                            Dish(name="Paneer Pakoda", price=25, rating=4.5),
                                            Dish(name="Burger", price=100, rating=3.5),
                                            Dish(name="Sandwich", price=80, rating=4.2)
                                        ]
                                     )
                            )

    data_to_save= restaurant.to_dictonary()
    print(data_to_save)

    menu_data = restaurant.menu.to_dictonary()
    print(menu_data)

    dishes = restaurant.menu.dishes

    db = firestore.client()
    #db.collection('restaurant').add(data_to_save)
    #db.collection('restaurant').document('ZTLzXHECCD6PEYVHM73a').collection('menu').add(menu_data)
    """for dish in dishes:
        dish_data = dish.to_dictonary()
        db.collection('restaurant').document('ZTLzXHECCD6PEYVHM73a').collection('menu')\
            .document('99cE2AK8BnzkdtyvPJv8').collection('dishes')\
            .document(dish.name).set(dish_data)
        print(dish.name,"Saved")
    """
    dish = Dish(name='Sandwich',price=120, rating=4.7)
    dish_data = dish.to_dictonary()


    db.collection('restaurant').document('ZTLzXHECCD6PEYVHM73a').collection('menu') \
        .document('99cE2AK8BnzkdtyvPJv8').collection('dishes') \
        .document(dish.name).set(dish_data)

    print("Dish data Updated.")



    print("Data Saved.")



if __name__ == '__main__':
    main()