from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('imagen')

#imagen = Image.open('')
#imagen.show() # Al aplicar show abres el editor de imagenes del sistema operativo

img = ImageTk.PhotoImage(Image.open('')) # Es necesario realizar esta linea de codigo, porque el archivo se tiene que convertir de nativo .png o jpg a Tk
l = Label(image=img)    # Después es fácil de ocupar
l.pack()



root.mainloop()