"""
Magic methods in Python

denoted as ==> __abc__ // abc may be str, dict and many more

"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print("Points is {} | {}".format(self.x,self.y))


    def __str__(self):
        return "Points is {} | {}".format(self.x, self.y)



def main():
    ob1 = Point(10,20)
    ob1.show()


    print(ob1.__str__())








if __name__ == '__main__':
    main()