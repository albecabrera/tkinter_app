from tkinter import *

root = Tk()
root.title("Frames")

buscador = LabelFrame(root, text="Buscador", padx=100, pady=100)
buscador.grid(row=0,column=0,padx=5, pady=5)

barra = Entry(buscador, text="¿Buscas algo?").grid(row=0, column=1)
boton = Button(buscador, text="Buscar").grid(row=0, column=0)

buscador2 = LabelFrame(root, text="Buscador 2", padx=100, pady=100)
buscador2.grid(row=1,column=0,padx=5, pady=5)

barra2 = Entry(buscador2, text="¿Buscas algo?").grid(row=0, column=0)
boton2 = Button(buscador2, text="Buscar").grid(row=0, column=1)

mainloop()