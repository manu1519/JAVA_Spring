from tkinter import * # El * indica que se esta importando todo

root = Tk()
root.title('Hola mundo') # cuando se tiene una ventana el titulo de la misma es por medio de title
root.geometry('400x400') # indica las dimensiones de la ventana ancho alto

label = Label(root, text='Hola mundo! mi primera etiqueta')# un widget es todo lo que se puede colocar en la ventana primer argumento es que instancia se va a modificar, despues el texto
label2 = Label(root, text='Hola mundo! GG')
#label(root, text='Hola mundo! mi primera etiqueta').pack() # ya que python es orientado a objetos, se puede realizar de la siguiente forma

#--------------------------------------------------- Modificando espacios
label.grid(row=0, column=0) # Para modificar espacios, es necesario de la función grid dentro del widget
label2.grid(row=0, column=0) # al colocar Grid no es necesario colocar .pack
# El sistema de Grid es relativo, es decir, se ajusta al contenido

#label.pack() # Despues se busca que se realicé el widget con label, pack solo agrega el elemento una vez
#label2.pack()


root.mainloop() # es necesario indicar esta función ya que es necesario que se generen cambios constantemente


