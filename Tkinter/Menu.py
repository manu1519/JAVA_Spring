from tkinter import *

root = Tk()
root.geometry('250x250')
root.title('Menu')

def enviar():
    l = Label(root, text=value.get())
    l.pack()

lista = [
    'Noticias', 
    'Deportes', 
    'Videos'
]

value = StringVar()
value.set(lista[2])

drop = OptionMenu(root, value, *lista)
drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()