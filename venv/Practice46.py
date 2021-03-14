"""
Misc concepts in python

"""

class Point:
    def __init__(self,x,y):
        self._x = x # _x means protected in python -> x must not be accessed directly [warning]
        self.__y = y # __y means private in pyhton -> cannot be accessed [error]

    def show(self):
        print("Points is {} | {}".format(self._x,self.__y))


def main():
    ob1 = Point(10,20)
    ob1.show()


    print("X is: ",ob1._x)
    print("Y is: ",ob1._Point__y)





if __name__ == '__main__':
    main()