from tkinter import *

root = Tk()
root.title("Ventana principal")
root.geometry("250x200")

def seleccion():
    etiqueta1 = Label(root, text=control1.get()).pack()
    etiqueta2 = Label(root, text=control2.get()).pack()

control1 = StringVar()
control2 = StringVar()

opcion_1 = Checkbutton(root,
					text="Opción 1",
					variable=control1,
					onvalue="Opción 1 seleccionada",
					offvalue="Opción 1 no seleccionada")
opcion_1.pack()
opcion_1.deselect()

opcion_2 = Checkbutton(root,
					text="Opción 2",
					variable=control2,
					onvalue="Opción 2 seleccionada",
					offvalue="Opción 2 no seleccionada")

opcion_2.pack()
opcion_2.deselect()

muestra_seleccion = Button(root, text="Mostrar selección", command=seleccion).pack()

mainloop()