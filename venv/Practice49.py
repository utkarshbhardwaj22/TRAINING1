import copy

class Utkarsh:

    def __init__(self,name = 0):
        self.name = name

    def __str__(self):
        return "{}".format(self.name)

    def __copy__(self,namee):
       self.name= namee

    def __deepcopy__(self, namee):
       self.name= namee


def main():
     ob1 = Utkarsh("Utkarsh")
     print(ob1)
     ob2 = Utkarsh()
     ob2.__deepcopy__("Piyush")
     print(ob2,hash(ob2))
     print(ob1,hash(ob1))




if __name__ == '__main__':
    main()