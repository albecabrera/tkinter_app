from tkinter import *
root = Tk()

etiqueta = Label(root, text="¡Esta es la primera etiqueta!")
etiqueta2 = Label(root, text="¡Esta es la segunda etiqueta!")
etiqueta.grid(row=2, column=0)
etiqueta2.grid(row=0, column=0)


marco_principal = Frame()
marco_principal.grid()
marco_principal.config(width="800", height="600", bg="red")





root.mainloop()