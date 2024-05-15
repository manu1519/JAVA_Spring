from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('ventanas')
root.geometry('250x250')

#def open():
#    img = ImageTk.PhotoImage(Image.open(r'Tkinter\carrusel\Imagenes\1.jpg'))
#    top = Toplevel()
#    top.geometry('250x250')
#    top.title('Hola mundo nueva ventana')
#    l = Label(top, text='Texto en segunda ventana')
#    l2  = Label(top, image=img)
#    l.pack()
#    l2.pack()
# ---->    top.mainloop()

#def open():
# --->   global img
#    img = ImageTk.PhotoImage(Image.open(r'Tkinter\carrusel\Imagenes\1.jpg'))
#    top = Toplevel()
#    top.geometry('250x250')
#    top.title('Hola mundo nueva ventana')
#    l = Label(top, text='Texto en segunda ventana')
#    l2  = Label(top, image=img)
#    l.pack()
#    l2.pack()

def open(img):
    top = Toplevel()
    top.geometry('250x250')
    top.title('Hola mundo nueva ventana')
    l = Label(top, text='Texto en segunda ventana')
    l2  = Label(top, image=img)
    l.pack()
    l2.pack()
    top.mainloop()


img = ImageTk.PhotoImage(Image.open(r'Tkinter\carrusel\Imagenes\1.jpg')) 
btn = Button(root, text='Click', command=lambda: open(img)).pack()


root.mainloop()