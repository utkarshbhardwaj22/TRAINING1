

def area_of_circle(radius = 1.1):
    return 3.14 * radius * radius


print("Area of circle: ",area_of_circle())
print("Area of circle: ",area_of_circle(2))
print("Area of circle: ",area_of_circle(radius= 4))


"""
Lamdas in python--> used to experss function with single expression
"""

ob1 = lambda x=int(input("Enter x: ")), y=int(input("Enter y: ")) : x**y

print("Result is :", ob1())


