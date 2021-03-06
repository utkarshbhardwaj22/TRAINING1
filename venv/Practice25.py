"""
Inheritance

"""

class Parent:

    def __init__(self):
        print("Parent Object Constructed")

    def show(self):
        print("this is show of parent")

class Child(Parent):
    pass


def main():
    #pRef = Parent()

    print("Parent class Dictionary \n",Parent.__dict__)
    print("Child class Dictionary \n", Child.__dict__)

    cRef= Child()
    cRef.show()






if __name__ == '__main__':
    main()
