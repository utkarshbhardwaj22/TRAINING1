# Customer database management in covid-19
import mysql.connector as db
import datetime



class Customer:

    def __init__(self):
        self.name = input("Enter Your name: ")
        self.phone = input("Enter Your Phone Number: ")
        self.email = input("Enter Your email: ")
        self.temperature = input("Enter Your temperature: ")
        self.intime = str(datetime.datetime.today())
        self.outtime = ""
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    def show_details(self):
        print("Name: {}\n"
              "Phone.no: {}\n"
              "Email: {}\n"
              "Temperature: {}\n"
              "In-time: {}\n"
              "Out-time: {}".format(self.name, self.phone, self.email, self.temperature, self.intime, self.outtime))


class DB:

    def __init__(self):
        self.connection = db.connect(user="root", password="", database="utkdb", host="localhost")
        self.cursor= self.connection.cursor()


    def execute_sql_write(self,sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def execute_sql_read(self,sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data


def main():

    while True:

        print("=========================================")
        print("Welcome to customer management")
        print("``````````````````````````````")
        print("Press 1 to Register customer and mark entry.")
        print("Press 2 to mark exit of customer.")
        print("Press 3 to update customer.")
        print("Press 4 to fetch customer on the basis of Phone number.")
        print("Press 5 to fetch all customers.")
        print("Press 0 for exit.")
        print("=========================================")


        choice = int(input("Enter your choice: "))
        dbRef = DB()

        if choice == 0:
            break

        if choice == 1:
            cRef = Customer()
            cRef.show_details()

            save = input("Enter yes to save: ")
            if save == "yes":
                sql = "insert into Customer values(null, '{}', '{}', '{}', {}, '{}', '{}')".format(cRef.name, cRef.phone, cRef.email,
                                                                                            cRef.temperature,cRef.intime,
                                                                                            cRef.outtime)
                dbRef.execute_sql_write(sql)
                print("DATA REGISTERED")

        elif choice == 2:
            phone = input("Enter your phone number: ")
            outtime =str(datetime.datetime.today())
            sql = "update customer set outtime = '{}' where phone = '{}'".format(outtime,phone)

            update = input("Enter yes to Update: ")
            if update == "yes":
                dbRef.execute_sql_write(sql)
                print("EXECUTED")

        elif choice == 3:
            cRef = Customer()
            cRef.show_details()

            update = input("Enter yes to save: ")
            if update == "yes":
                sql = "update customer set temperature={} where phone = '{}'".format(cRef.temperature,cRef.phone)
                dbRef.execute_sql_write(sql)
                print("DATA UPDATED")

        elif choice == 4:
            phone = int(input("Enter your phone number: "))
            sql = "select * from customer where phone = '{}'".format(phone)
            data = dbRef.execute_sql_read(sql)
            print(data)

        elif choice == 5:
            sql= "select * from customer"
            data = dbRef.execute_sql_read(sql)
            for row in data:
                print(row)

        else:
            print("Wrong option selected.....Try Again")












if __name__ == '__main__':
    main()