#Importaciones
from tkinter import *

#Creación de la ventana principal
root = Tk()
#Título de la ventana
root.title("Curso de Tkinter de Programación Fácil")

entrada = Entry(root)
entrada.pack()

# Evento para el botón
def pulsar_boton():
    texto = entrada.get()
    Label(root, text="Botón pulsado").pack()
    Button(root, text=f"{texto}").pack()
    
Button(root, text="Pulsar", command=pulsar_boton).pack()


#Bucle de ejecución
root.mainloop() 