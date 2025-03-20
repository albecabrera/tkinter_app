# Importaciones
from tkinter import *
from tkinter.messagebox import *

# Creación de la ventana principal
root = Tk()
# Título de la ventana
root.title("Curso de Tkinter der programación fácil")

# Función para mensaje informativo
def muestra_info():
    showinfo("Esto es una información!", "Sigue aprendiendo!")

# Botón para llamar a la función
boton = Button(root, text="enviar", width=75, command=muestra_info)
boton.pack()

# Bucle de ejecución 
root.mainloop()
