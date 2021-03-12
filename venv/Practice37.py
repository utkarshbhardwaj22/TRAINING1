class Point:

    def __init__(self,x,y,label):
        self.x = x
        self.y = y
        self.label = label


    def show(self):
        print("Point {} is: {}|{}".format(self.label,self.x,self.y))

    #annotation : classmethod shall pass reference to class rather than object
    @classmethod
    def create_points_from_file(cls):
        print("cls is: ",cls)
        print("cls contains: ",cls.__dict__)

        file = open("points.csv", "r")
        lines = file.readlines()

        points = []

        lbl = 1
        for line in lines:
            point = line.split(",")
            points.append(cls(float(point[0]), float(point[1]), "P{}".format(lbl)))
            lbl += 1

        return points


def main():

    p1= Point(10,20,"A")
    p2 = Point(11, 22, "B")

    p1.show()
    p2.show()
    print()

    points = Point.create_points_from_file()
    for point in points:
        point.show()

if __name__ == '__main__':
    main()
    