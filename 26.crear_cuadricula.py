# Crea 4 botones
#Importaciones
from tkinter import *

#Creación de la ventana principal
root = Tk()
#Título de la ventana
root.title("Ejercicio para crear cuatro botones.")


#Entrada de datos
Label(root, text="Nombre: ").grid(column=0, row=0)
entrada_nombre = Entry(root)
entrada_nombre.grid(column=1, row=0)

Label(root, text="Edad: ").grid(column=0, row=1)
entrada_edad = Entry(root)
entrada_edad.grid(column=1, row=1)

# Se obtienen los valores del entry
nombre = entrada_nombre.get()
edad = entrada_edad.get()
# Se muestra en una etiqueta el valor del entry
Label(root, text=f"Mi nombre es: {nombre}. Tengo {edad} años.")

def pulsar_boton(): 

# Botón
    Button(root, text="Enviar", command=pulsar_boton).grid(column=0, row=1)

#Evento para el botón

root.mainloop()