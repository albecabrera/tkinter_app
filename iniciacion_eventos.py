#Importaciones
from tkinter import *

#Creación de la ventana principal
root = Tk()
#Título de la ventana
root.title("Curso de Tkinter de Programación Fácil")


#Entrada de datos
entrada = Entry(root)
entrada.insert(0,"Escriba su nombre...")
entrada.bind("<Button-1>", lambda despejar : entrada.delete(0, END))
entrada.pack()

#Evento para el botón
def pulsar_boton():
    #Se obtiene el valor del Entry
    texto = entrada.get()
    #Se muestra en una etiqueta el valor del Entry
    Label(root, text=f"Hola {texto}.").pack()

#Botón
Button(root, text="¡Púlsame!", command=pulsar_boton).pack()

#Bucle de ejecución
root.mainloop()