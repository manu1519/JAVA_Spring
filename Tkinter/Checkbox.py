from tkinter import *

root= Tk()
root.geometry('250x250')
root.title('Checkbox')

var = StringVar()
var.set('Meh')

def mostrar():
    l = Label(root, text=var.get())
    l.pack()

c = Checkbutton(root, text='Cehck box', variable=var, onvalue='Si', offvalue='Meh')
c.pack()

btn = Button(root, text='Click', command=mostrar)
btn.pack()

root.mainloop()