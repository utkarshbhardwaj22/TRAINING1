class FlightBooking:
    def __init__(self,from_location,to_location,departure_date,travellers):
        print("init executed and self is:", self)
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.travellers = travellers

    def show_details(self):
        print("Travel details from {} to {} on {} of {} travellers".format(self.from_location,self.to_location,self.departure_date,self.travellers))


def main():
    oRef1 = FlightBooking("Delhi", "Goa", "19th Aug, 2020", 35)
    oRef1.show_details()

    print("Class details: ",FlightBooking.__dict__)





if __name__ == '__main__':
    main()
