from tkinter import *
from tkinter.ttk import *

def on_Click():
    select = selected_var.get()
    print("You Selected : ",select)


window = Tk()
window.title("Utkarsh Ekectric Motors Pvt. Ltd.")

lbl= Label(window, text="Select your Gender:")

selected_var = IntVar()

radio_male= Radiobutton(window, text="MALE", value=1, variable=selected_var)
radio_female= Radiobutton(window, text="FEMALE", value=2, variable=selected_var)
radio_others= Radiobutton(window, text="OTHERS", value=3, variable=selected_var)

lbl.grid(column=0, row=0)
radio_male.grid(column=0, row=2)
radio_female.grid(column=0, row=3)
radio_others.grid(column=0, row=4)

btn_Submit = Button(window, text="Submit", command=on_Click)
btn_Submit.grid(column=0, row=5)


window.geometry('300x300')
window.mainloop()
