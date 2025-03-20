# Importaciones
import tkinter as tk

# Ventana principal

# Creación de la ventana principal
root = tk.Tk()
# Título de la ventana
root.title("Curso de Tkinter der programación fácil")

root.geometry()

# Ajustes de ventana y pantalla
root.eval('tk::PlaceWindow . center')

# Widgets 

# Entrada de datos
entrada = tk.Entry(root).pack()


# Bucle de ejecución 
root.mainloop()
