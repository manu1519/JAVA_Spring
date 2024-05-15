from tkinter import *

root = Tk()
root.title('Pies a metros')
root.geometry('500x500')

def calcular(*args): # Con *args extrae todos los elementos dentro de una función
    try:
        value = float(pies.get())
        met = int(0.3048 * value * 10000 + .5)/10000
        metros.set(met)
    except ValueError:
        metros.set('ERROR')

frame = Frame(root, padx=5, pady=12)
frame.grid(column=0, row=0)

pies = StringVar()
pies_input = Entry(frame, width=7, textvariable=pies)
pies_input.grid(column=1, row=0)

metros = StringVar()

Label(frame, textvariable=metros).grid(column=1, row=1)

Button(frame, text='Calcular', command=calcular).grid(column=2, row=2)

Label(frame, text='Pies').grid(column=0, row=0)
Label(frame, text='es igual a:').grid(column=0, row=1)
Label(frame, text='Metros').grid(column=2, row=1)

pies_input.focus() # Focus permite que al abrir la app ya se selecciona el campo de input
root.bind("<Return>", calcular) # Permite escuchar eventos dento de la aplicación
root.mainloop()