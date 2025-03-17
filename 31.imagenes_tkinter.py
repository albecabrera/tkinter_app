from tkinter import *
import os 

# Carga de directorios
# Carpeta principal

carpeta_principal = os.path.dirname(__file__)
print(carpeta_principal)
# Carpeta de imagenes
carpeta_imagenes =  os.path.join(carpeta_principal, "imagenes")
print(carpeta_imagenes)
# Creación de la ventana principal
root = Tk() 

# Código de la ventana
root.title("www.programacion.facil.org")

# Bucle de ejecución
mainloop()

