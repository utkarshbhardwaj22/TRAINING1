from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("CORT Pvt. Ltd.")

lbl_title = Label(window, text='Welcome to CORT Pvt. Ltd.')
lbl_title.pack()

btn = Button(window,text = "Submit")
btn.pack()

combo = Combobox(window)
combo['values']= ("Select City", "Kapurthala","Ludhiana", "Jalandhar")
combo.current(0)
combo.pack()


window.geometry('300x300')
window.mainloop()