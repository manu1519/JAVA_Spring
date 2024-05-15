from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Mensaje')

#def click():
#    messagebox.showwarning('Popup', 'Hola mundo') # Primer valor es el titulo de la ventana, el segundo es el mensaje

#def click():
#    messagebox.showinfo('Popup', 'Hola mundo') # Supongo que sirve para MAC OS
    
#def click():
#    messagebox.showerror('Popup', 'Hola mundo')  

#def click():
#    respuesta = messagebox.askquestion('Popup', 'Hola mundo')  
#    print(respuesta)
#    if respuesta == 'yes':
#        messagebox.showinfo('Respuesta', 'La respuesta fue: ' + respuesta)
#    else:
#        messagebox.showinfo('Respuesta', ':( La respuesta fue: ' + respuesta)

#def click():
#    respuesta = messagebox.askokcancel('Hola mundo', 'Desea realizar acción')
#    if respuesta:
#        messagebox.showinfo('Hola mundo', 'La respuesta fue ok')
#    else:
#        messagebox.showinfo('Hola mundo', 'La respuesta fue cancelar')

def click():
    respuesta = messagebox.askyesno('Hola mundo', 'Desea realizar acción')
    if respuesta:
        messagebox.showinfo('Hola mundo', 'La respuesta fue ok')
    else:
        messagebox.showinfo('Hola mundo', 'La respuesta fue cancelar')


btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()