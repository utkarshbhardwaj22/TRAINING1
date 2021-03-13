"""
Exception Handling

"""

print("Welcome to cashback rewards.")
print()

cashback = [100, 20, 48, 38, 265, 67, 54, 475, 666, 99]
lucky_number = int(input("Enter your lucky number between 1 to 100: "))
lucky_number %= 10
try:

    print("Thankyou. You won a cashbak of \u20b9 {}".format(cashback[lucky_number]))
except Exception as error:
    print("Something went wrong.",error)

finally:
    print("This will execute at any cost.")
