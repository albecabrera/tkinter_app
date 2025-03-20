# Importaciones
from tkinter import *
from tkinter.messagebox import *

# Creación de la ventana principal
root = Tk()
# Título de la ventana
root.title("Curso de Tkinter der programación fácil")

# Función para mensaje informativo
def preguntar():
    askyesno("¿Sabías que?", "Hoy brillará el sol el día entero pues está llegando la primavera!")

# Botón para llamar a la función
boton = Button(root, text="enviar", width=75, command=preguntar)
boton.pack()

# Bucle de ejecución 
root.mainloop()
