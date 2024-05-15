from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Carrusel')

img1 = ImageTk.PhotoImage(Image.open(r'Tkinter\carrusel\Imagenes\1.jpg'))
img2 = ImageTk.PhotoImage(Image.open(r'Tkinter\carrusel\Imagenes\2.jpg'))
img3 = ImageTk.PhotoImage(Image.open(r'Tkinter\carrusel\Imagenes\3.jpg'))
img4 = ImageTk.PhotoImage(Image.open(r'Tkinter\carrusel\Imagenes\4.jpg'))

lista = [img1, img2, img3, img4]

l = Label(root, image=img1)
l.grid(row=0, column=0, columnspan=3)

def adelante(img_num):
    global l
    global btn_adelante
    global btn_atras

    l.grid_forget()
    l = Label(root, image=lista[img_num])
    btn_atras = Button(root, text='<-', command=lambda: btn_atras(img_num - 1))
    btn_adelante = Button(root, text='->', command=lambda: btn_atras(img_num + 1))

    if img_num == 3:
        btn_adelante = Button(root, text='N/A', state= DISABLED)   

    l.grid(row=0, column=0, columnspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)

def atras(img_num):
    global l
    global btn_adelante
    global btn_atras

    l.grid_forget()
    l = Label(root, image=lista[img_num])
    btn_atras = Button(root, text='<-', command=lambda: btn_atras(img_num - 1))
    btn_adelante = Button(root, text='->', command=lambda: btn_atras(img_num + 1))

    if img_num == 0:
        btn_atras = Button(root, text='N/A', state= DISABLED)   

    l.grid(row=0, column=0, columnspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)

btn_atras = Button(root, text='N/A', state=DISABLED) # Con state puedes hacer que no este habilitado
btn_adelante = Button(root, text='->', command=lambda: adelante(1))

btn_atras.grid(row=1, column=0)
btn_adelante.grid(row=1, column=2)

root.mainloop()