from tkinter import *

root = Tk()
root.title('Radio button')
root.geometry('500x500')

r = IntVar()
r.set('2')

con = [
    ('trato', 'trato'),
    ('tacto', 'tacto'),
    ('sciente', 'sciente'),
    ('tino', 'tino')
]

palabra= StringVar()
palabra.set('tino')

for x,y in con:
    Radiobutton(root, text=x, variable=palabra, value=y).pack()

l = Label(root, textvariable=palabra)
l.pack()

root.mainloop()