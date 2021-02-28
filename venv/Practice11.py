"""
*args is for any numbers of arguments of a function
*anyName -> it can be of any name
It is of tuple type
"""
def sum_of_numbers(*utk):

    sum=0
    for i in range(0,len(utk)):
        sum+= utk[i]

    print("The sum is {}".format(sum))
    print(type(utk))


sum_of_numbers(10,20,30,40)
sum_of_numbers(12,34)
