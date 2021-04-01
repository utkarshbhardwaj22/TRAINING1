from tkinter import *

class CustomerManagementApp:

    def on_click(self):
        customer = {"name": self.entry_name.get(),
                    "phone": self.entry_phone.get(),
                    "email": self.entry_email.get()}

        print(customer)

    def run_app(self):
        window = Tk()
        print(window, type(window))

        lbl_title = Label(window, text="Customer Management System")
        lbl_title.pack()

        lbl_name = Label(window, text="Name")
        lbl_name.pack()

        self.entry_name = Entry(window)
        self.entry_name.pack()

        lbl_phone = Label(window, text="Phone")
        lbl_phone.pack()

        self.entry_phone = Entry(window)
        self.entry_phone.pack()

        lbl_email = Label(window, text="Email")
        lbl_email.pack()

        self.entry_email = Entry(window)
        self.entry_email.pack()

        self.btn_add = Button(window, text="ADD CUSTOMER", command=self.on_click)
        self.btn_add.pack()

        window.mainloop()




def main():
    app = CustomerManagementApp()
    app.run_app()


if __name__ == '__main__':
    main()


