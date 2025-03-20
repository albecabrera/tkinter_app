# Importaciones
from tkinter import *
from tkinter.messagebox import *

# Creación de la ventana principal
root = Tk()
# Título de la ventana
root.title("Curso de Tkinter der programación fácil")

# Función para mensaje informativo
def preguntamos():
    askokcancel("¿Seguro que desea continuar?", "La acción que va a realizar podría comprometer la integridad de la base de datos!")
    

# Botón para llamar a la función
boton = Button(root, text="enviar", width=75, command=preguntamos)
boton.pack()

# Bucle de ejecución 
root.mainloop()
