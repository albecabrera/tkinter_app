from tkinter import *
root = Tk()

x = IntVar()
x.set(value=1)

def actualiza(value):
    opcion_set = Label(root, text=x.get()).grid(row=3)

titulo = Label(root, text="Seleccione la respuesta correcta. ").grid(row=0)

opcion_1 = Radiobutton(root, text="Esta es la primera opción", 
                       value=1, variable=x).grid(row=1)

opcion_2 = Radiobutton(root, text="Esta es la segunda opción", 
                       value=2, variable=x).grid(row=2)

boton_envia = Button(root, text="Enviar", command=lambda : actualiza(x.get())).grid(row=4)

root.mainloop()