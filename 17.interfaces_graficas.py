#Importaciones
from tkinter import *

#Creación de la ventana principal
root = Tk()
#Titulo de la aplicacion
root.title("Curso de Tkinter en programación fácil")
#Tamaño de la ventana.
root.geometry("800x600+560+240") 

#Creación de la etiqueta
mensaje = Label(root, text="Mi primer programa con Tkinter. ").grid(row=1, column=0)
mensaje2 = Label(root, text="Esta es la segunda etiqueta. ").grid(row=0, column=0)
 
#Bucle de ejecución
root.mainloop()