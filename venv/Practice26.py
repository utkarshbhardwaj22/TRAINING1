class College:

    def __init__(self,Name,Class,Rollno):
        self.Name= Name
        self.Class= Class
        self.Rollno= Rollno

    def show_details(self):
        print("NAME: {} \n CLASS: {} \n Roll.No: {}".format(self.Name,self.Class,self.Rollno))



class SubCollege(College):

    def __init__(self,Name,Class,Rollno,Section,Type):
        College.__init__(self,Name,Class,Rollno)
        self.Section= Section
        self.Type= Type

    def show_details(self):
        College.show_details(self)
        print("SECTION: {} \n TYPE: {}".format(self.Section,self.Type))
        print()

ref= SubCollege("UTKARSH", "D3ITB1", 1706904, "B", "HOSTELER")
ref1= SubCollege("DEEPAK", "D3CSE1", 1706567, "E", "HOSTELER")
ref2= SubCollege("DINESH", "D3CSE1", 1706545, "B", "DAY SCHOLAR")

ref.show_details()
ref1.show_details()
ref2.show_details()