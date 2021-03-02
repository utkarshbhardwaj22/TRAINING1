"""
OOPs in Python
object and class

"""
# Class
class FlightBooking():
    pass

def main():
    oRef1= FlightBooking() #Object of class
    print("oRef1:",oRef1,type(oRef1))
    print("Object contains: ",oRef1.__dict__)  # {} -> empty dictionary

    # Object operations
    #1.add/update opertaion
    oRef1.from_location = "Delhi"
    oRef1.to_location = "Banglore"
    oRef1.departure_date = "6th Aug 2020"
    oRef1.travellers = 4
    oRef1.travellers = 6

    print("Object contains: ", oRef1.__dict__)

    #2. delete operation
    del oRef1.travellers
    print("oRef1:", oRef1, type(oRef1))
    print("Object contains: ", oRef1.__dict__)



if __name__ == '__main__':
    main()