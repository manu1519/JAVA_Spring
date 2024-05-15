from tkinter import *

root = Tk()
root.title('Conociendo inputs')
root.geometry('500x500')

e = Entry(root, width=60) # estos son los inputs
e.pack()
e.insert(0, "Ingresa texto") # Se puede agregar texto desde antes

def click():
    texto = e.get() # Asi se recupera el texto con el que se ingresa
    textvar.set(texto)
    val = textvar.get() # Esto permite hacer que tengas el valor del input en la terminal
    print(val)
#    l = Label(root, text=texto)
#    l.pack()
    e.delete(0, END) # Permite eliminar los elementos dentro del input/entry
#    l.configure(text=texto)

btn = Button(root, text='Click', command=click)
btn.pack()

textvar = StringVar() # Esto permite resetear el input, sin tener que hace lo que se encuentra comentado

l = Label(root, text='Texto de la etiqueta')
l.pack()

root.mainloop()