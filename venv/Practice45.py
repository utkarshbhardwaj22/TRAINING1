
class Product:

    def __init__(self,pid,name,price):
        self.pid = pid
        self.name = name
        self.price = price

    def show_product_details(self):
        print("Name: {}\n"
              "Product id: {}\n"
              "Price {}".format(self.name,self.pid,self.price))

class LinkedList:

    def __init__(self):
        self.head= None
        self.tail = None

    def append(self,element):

        if self.head == None:
            self.head = element
            self.tail = element

        else:
            element.previous = self.tail
            self.tail.next = element

            self.tail = element

            element.next = self.head
            self.head.previous = self.tail

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail



def main():
    product1 = Product("SAMSUNG OLED TV", 101, 55000)
    product2 = Product("iPhone XR", 201, 43000)
    product3 = Product("Macbook Pro", 301, 105000)
    product4 = Product("LG FRIDGE", 401, 30000)
    product5 = Product("DAIKIN AC", 501, 50000)


    ob1= LinkedList()
    ob1.append(product1)
    ob1.append(product2)
    ob1.append(product3)
    ob1.append(product4)
    ob1.append(product5)


    print("Head: ")
    ob1.get_head().show_product_details()
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Tail: ")
    ob1.get_tail().show_product_details()









if __name__ == '__main__':
    main()