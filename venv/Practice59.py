from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


def on_click():
    response = messagebox.askquestion("Question", "Piyush Fudu Banda hai?")
    if response == 'yes':
        messagebox.showinfo(":)", "1 Crore")
    else: messagebox.showinfo(":(", "Wrong Answer")

window = Tk()
window.title("Utkarsh Electric Motors Pvt. Ltd.")

lbl= Label(window, text=" Click on button for Magic")
btn = Button(window, text='Click', command=on_click)

lbl.pack()
btn.pack()


window.geometry('400x400')
window.mainloop()