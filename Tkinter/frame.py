from tkinter import *

root= Tk()
root.title('Frames')
root.geometry('500x500')

# frame = LabelFrame(root, text='login', padx=10, pady=10, borderwidth=5) # para hacer que el frame sea visible, es necesario que se agregue una widget
frame = Frame(root, padx=10, pady=10, borderwidth=5)
frame.pack(padx=50, pady=50) # Se realiza el padding

l = Label(frame, text='Estoy dentro del frame')
btn = Button(frame, text='salir', command=root.quit)
l.pack()
btn.pack()

root.mainloop()