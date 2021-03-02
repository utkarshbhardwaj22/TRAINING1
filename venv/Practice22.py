class FlightBooking:

    # __init__ is known as constructor, executed automatically whenever object is constructed in memory
    # self can be any name
    # self -> self is the first input to any function which you created in class
    # self is a reference valriable which holds the hashcode of object which is in use
    def __init__(self):
        print("init executed and self is:", self)
        self.from_location = "Delhi"
        self.to_location = "Banglore"
        self.departure_date = "6th Aug 2020"
        self.travellers = 4

def main():
    oRef1 = FlightBooking()
    print("oRef1 is:",oRef1)
    print("Object Contains:", oRef1.__dict__)

    oRef2 = FlightBooking()
    oRef2.travellers = 18
    print("Object Contains:", oRef2.__dict__)



if __name__ == '__main__':
    main()
