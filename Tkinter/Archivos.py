from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.geometry('250x250')
root.title('Selección de archivos')

#root.filename = filedialog.askopenfilename(title='Elije una foto', filetypes=(("Archivos JPG","*.jpg"),('Todos', '*')))
#l = Label(root, text=root.filename)
#l.pack()
#img = Image.open(root.filename)
#imgTk = ImageTk.PhotoImage(img)

#l2 = Label(root, image=imgTk)
#l2.pack()

def open():
    global imgTk
    root.filename = filedialog.askopenfilename(title='Elije una foto', filetypes=(("Archivos JPG","*.jpg"),('Todos', '*')))
    l = Label(root, text=root.filename)
    l.pack()
    img = Image.open(root.filename)
    imgTk = ImageTk.PhotoImage(img)

    l2 = Label(root, image=imgTk)
    l2.pack()


btn = Button(root, text='Cargar imagen', command=open)
btn.pack()
root.mainloop()
