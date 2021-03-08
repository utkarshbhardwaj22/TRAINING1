import mysql.connector as db

def main():

    state = input("Enter State: ")
    confirmed = int(input("Enter Confirmed Cases: "))
    active = int(input("Enter active Cases: "))
    recovered = int(input("Enter recovered Cases: "))
    deceased = int(input("Enter deceased Cases: "))
    tested = int(input("Enter tested Cases: "))

    sql = "insert into covidindia values('{}', {}, {}, {}, {}, {})".format(state, confirmed, active, recovered, deceased, tested)

    connection = db.connect(user="root", password="", database="utkdb", host="localhost", port="3306")

    cursor = connection.cursor()
    cursor.execute(sql)

    connection.commit()

    print("Sql statement is executed.")

if __name__ == '__main__':
    main()