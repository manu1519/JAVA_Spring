from tkinter import *

root = Tk()
root.title('Slider')
root.geometry('250x300')

Vert = Scale(root, from_=0, to=200, command=lambda x: enviar()) # La función lambda permite la interacción directa con el o los argumentos que se tengan en una variable
                                                                # En este caso la variable es el slider, por lo que es necesario pasarle un argumento 'x' para que se almacene
                                                                # el valor de la variable del slider y posteriormente se realicen la operación en la terminal
Vert.pack()

hor = Scale(root, from_=0, to=200, orient=HORIZONTAL)
hor.pack()

def enviar():
    hor2 = hor.get()
    vert2 = Vert.get()
    print(str(hor2)+ ' '+str(vert2))


btn = Button(root, text='Enviar', command=enviar)
btn.pack()


root.mainloop()