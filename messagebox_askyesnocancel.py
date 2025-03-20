# Importaciones
from tkinter import *
from tkinter.messagebox import *

# Creación de la ventana principal
root = Tk()
# Título de la ventana
root.title("Curso de Tkinter der programación fácil")

# Función para mensaje informativo
def otrapregunta():
    askyesnocancel("Tenga precaución", "La acción que va a realizar puede comprometerlo!")

# Botón para llamar a la función
boton = Button(root, text="enviar", width=75, command=otrapregunta)
boton.pack()

# Bucle de ejecución 
root.mainloop()
