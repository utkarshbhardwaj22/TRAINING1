"""
Tkinter

"""

from tkinter import *

def on_click():
    customer= {"name": entry_name.get(),
               "phone": entry_phone.get(),
               "email": entry_email.get()}

    print(customer)

window = Tk()
print(window, type(window))

lbl_title = Label(window, text="Customer Management System")
lbl_title.pack()

lbl_name = Label(window, text="Name")
lbl_name.pack()

entry_name = Entry(window)
entry_name.pack()

lbl_phone = Label(window, text="Phone")
lbl_phone.pack()

entry_phone = Entry(window)
entry_phone.pack()

lbl_email = Label(window, text="Email")
lbl_email.pack()

entry_email = Entry(window)
entry_email.pack()

btn_add = Button(window, text="ADD CUSTOMER", command= on_click)
btn_add.pack()



window.mainloop()