import threading
import time
lock = threading.Lock()

class BookMyShow():

    def __init__(self, name, time, row, seat_num):
        self.name = name
        self.time = time
        self.row = row
        self.seat_num = seat_num
        self.booked = False

    def show_details(self):
        if self.booked:
            print("--------------")
        else:
            self.booked = True
            print("Details {} | {} | {} | {}".format(self.name,self.time,self.row,self.seat_num))

    def pay(self, email):
        self.email= email
        if self.booked :
            print("Sorry this ticket is already booked {}".format(self.seat_num))
        else:
            print("{} Please pay your amount".format(email))
            time.sleep(2)
            print("{} Your ticket booked".format(self.email))

class BookMovieTicket(threading.Thread):

    def select_seat(self,ticket,email):
        self.ticket = ticket
        self.email =email

    def run(self):
        lock.acquire()
        self.ticket.pay(self.email)
        self.ticket.show_details()
        lock.release()

def main():
    ticket1 = BookMyShow("Stranger Things", "21:00", "A", 1)
    ticket2 = BookMyShow("Stranger Things", "21:00", "A", 2)
    ticket3 = BookMyShow("Stranger Things", "21:00", "A", 3)
    ticket4 = BookMyShow("Stranger Things", "21:00", "A", 4)
    ticket5 = BookMyShow("Stranger Things", "21:00", "A", 5)
    ticket6 = BookMyShow("Stranger Things", "21:00", "A", 6)

    row = [ticket1, ticket2, ticket3, ticket4, ticket5, ticket6]

    user1 = BookMovieTicket()
    user2 = BookMovieTicket()

    user1.select_seat(row[1],"utkarsh2000bhard@gmail.com")
    user2.select_seat(row[1], "bhard96piyush@gmail.com")

    user1.start()
    user2.start()








if __name__ == '__main__':
    main()
