def get_max(*args):
    maxi=args[0]

    for number in args:
        if number > maxi:
            maxi = number

    return maxi

number=[10,102,30,4,5,20,2011,456]

print("the greater number is :",get_max(10,102,30,4,5,20,2011,456))
