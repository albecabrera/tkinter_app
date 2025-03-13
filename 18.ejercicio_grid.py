#Importaciones
from tkinter import *

#Creación de la ventana principal
root = Tk()

#Título de la ventana
root.title("Mi primera ventana en Tkinter")

#Tamaño de ventana.
root.geometry("800x600+560+240")
#Creación de la etiqueta
mensaje = Label(root, text="Mi primera etiqueta").grid(row=1, column=0)
mensaje2 = Label(root, text="Mi segunda etiqueta").grid(row=0, column=0)
# Se muestra la etiqueta


#Bucle de ejecución
