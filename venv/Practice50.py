import copy


class Customer:

    def __init__(self, name=0, phone=0, email=0):
        self.name = name
        self.phone = phone
        self.email = email

    def show_details(self):
        print("Name of the customer: {} \n"
              "Phone no.of the customer: {} \n"
              "Email : {}".format(self.name,self.phone,self.email))

    def __str__(self):
        return  "Name of the customer: {} \nPhone no.of the customer: {} \nEmail : {}".format(self.name,self.phone,self.email)

   # def __copy__(self,cust):
    #    cust.name = self.name
     #   cust.phone = self.phone
      #  cust.email = self.email


ob1 = Customer("Utkarsh", 7888327841, "utkarsh2000bhard@gmail.com")
ob2 = Customer("Piyush", 7526883506, "bhard96piyush@gmail.com")

ob2 = copy.copy(ob1)
print(ob2)