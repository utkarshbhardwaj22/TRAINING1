# Multiple login options

def login_google():
    print("Enter Google credentials.")

def login_facebook():
    print("Enter Google credentials.")

def login_github():
    print("Enter Google credentials.")


def login(login_type):
    login_type()

choice = int(input(
                    "for google login press 1\n"
                   "for facebook login press 2\n"
                   "for github login press 3\n"
                    "Enter choice: "))

if choice== 1:
    login(login_google)

elif choice == 2:
    login(login_facebook)

elif cjoice == 3:
    login(login_github)

else:print("Invalid Input Try again")