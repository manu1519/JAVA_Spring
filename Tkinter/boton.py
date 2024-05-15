from tkinter import *

root = Tk()
root.title('Conociendo botones')

l = Label(root, text='Hola mundo')
def click():    # importante realizar la función para botones, que la acción se registre fuera de la función
    l.pack()

btn = Button(root, text='Click', command=click, fg='red', bg='blue') # Primero se coloca la instancia del Tk, posteriormente texto, despues colocamos el 'command' el cual busca realizar las acciones del boton
                                                          # fg realiza el cambio de color del texto, con bg se permite hacer cambio de fondo
btn. pack()

root.mainloop()