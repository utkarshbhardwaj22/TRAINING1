"""
Operator Overloading in Python

"""


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print("Points are {} | {}".format(self.x, self.y))

    def __str__(self):
        return "Points are {} | {}".format(self.x, self.y)

    def __add__(self,point):
        temp = Point()
        temp.x = self.x + point.x
        temp.y = self.y + point.y
        return temp

def main():
    ob1 = Point(10,20)
    ob2 = Point(30,40)


    ob3 = ob1 + (ob2)
    print(ob3)


if __name__ == '__main__':
    main()