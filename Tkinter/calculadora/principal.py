from tkinter import *
#from tkmacosx import Button    Es necesario colocar para MAC


root = Tk()
root.title('Calculadora')
root.configure(background='#333333')
root.geometry('386x168')

equation = StringVar()

def press(num):
    equation.set(equation.get() + str(num))
    print(equation.get())

def equalpress():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set('ERROR')

def clear():
    equation.set('')

expression_entry = Entry(root, textvariable=equation)
expression_entry.grid(row=0, columnspan=4, sticky='nswe') # Sticky ocupa todo el ancho y su valor es por medio de los puntos cardinales

# --------------- Botones lateral izquierdo columna 0
btn7 = Button(root, text=' 7 ', fg='#fff', background='#666', command=lambda: press(7)) # Lambda permite sobreponer una función antes de la principal
btn7.grid(row=1, column=0, sticky='nswe')
btn4 = Button(root, text=' 4 ', fg='#fff', background='#666', command=lambda: press(4))
btn4.grid(row=2, column=0, sticky='nswe')
btn1 = Button(root, text=' 1 ', fg='#fff', background='#666', command=lambda: press(1))
btn1.grid(row=3, column=0, sticky='nswe')
btn0 = Button(root, text=' 0 ', fg='#fff', background='#666', command=lambda: press(0))
btn0.grid(row=4, column=0, sticky='nswe', columnspan=2)

#---------------- Botones columna 1
btn8 = Button(root, text=' 8 ', fg='#fff', background='#666', command=lambda: press(8))
btn8.grid(row=1, column=1, sticky='nswe')
btn5 = Button(root, text=' 5 ', fg='#fff', background='#666', command=lambda: press(5))
btn5.grid(row=2, column=1, sticky='nswe')
btn2 = Button(root, text=' 2 ', fg='#fff', background='#666', command=lambda: press(2))
btn2.grid(row=3, column=1, sticky='nswe')

#---------------- Botones columna 2
btn9 = Button(root, text=' 9 ', fg='#fff', background='#666', command=lambda: press(9))
btn9.grid(row=1, column=2, sticky='nswe')
btn6 = Button(root, text=' 6 ', fg='#fff', background='#666', command=lambda: press(6))
btn6.grid(row=2, column=2, sticky='nswe')
btn3 = Button(root, text=' 3 ', fg='#fff', background='#666', command=lambda: press(3))
btn3.grid(row=3, column=2, sticky='nswe')
btnpunto = Button(root, text=' . ', fg='#fff', background='#666', command=lambda: press('.'))
btnpunto.grid(row=4, column=2, sticky='nswe')
btnclear = Button(root, text=' clear ', fg='#fff', background='#999', command=clear)
btnclear.grid(row=5, column=2, sticky='nswe')

#---------------- Botones columna 3
btnmas = Button(root, text=' + ', fg='#fff', background='#FF8000', command=lambda: press('+'))
btnmas.grid(row=1, column=3, sticky='nswe')
btnmenos = Button(root, text=' - ', fg='#fff', background='#FF8000', command=lambda: press('-'))
btnmenos.grid(row=2, column=3, sticky='nswe')
btnmulti = Button(root, text=' * ', fg='#fff', background='#FF8000', command=lambda: press('*'))
btnmulti.grid(row=3, column=3, sticky='nswe')
btndiv = Button(root, text=' / ', fg='#fff', background='#FF8000', command=lambda: press('/'))
btndiv.grid(row=4, column=3, sticky='nswe')
btnigual = Button(root, text=' = ', fg='#fff', background='#FF8000', command=equalpress)
btnigual.grid(row=5, column=3, sticky='nswe')

exit = Button(root, text='Salir', command=root.quit)
exit.grid(row=5, column=1, sticky='nswe')

root.mainloop()