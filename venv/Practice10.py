"""
number = 20

def show():
    global number
    #number=10
    print("1. Number is:",number)
show()
print("2. Number is:", number)
"""



def recursion(number):

    if number == 0:
        return

    else:
        print("Number is:",number)
        recursion(number-1)
        return number

recursion(5)
