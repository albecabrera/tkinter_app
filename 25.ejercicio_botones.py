# Crea 4 botones
#Importaciones
from tkinter import *

#Creación de la ventana principal
root = Tk()
#Título de la ventana
root.title("Ejercicio para crear cuatro botones.")


#Entrada de datos
entrada = Entry(root)
entrada.insert(0,"Escriba tu nombre aquí socio...")
entrada.bind("<Key>", lambda despejar : entrada.delete(0, END))
entrada.pack()

#Evento para el botón
def pulsar_boton(): 
    #Se obtiene el valor del Entry
    texto = entrada.get()
   #Se muestra en una etiqueta el valor del Entry    
    Boton_1= Button(root, text=f"Se ha pulsado el primer botón{"Boton_1"}.").pack()
    Boton_2= Button(root, text=f"Se ha pulsado el segundo botón{"Boton_2"}.").pack()
    Boton_3= Button(root, text=f"Se ha pulsado el tercer botón{"Boton_3"}.").pack()
    Boton_4= Button(root, text=f"Se ha pulsado el cuarto botón{"Boton _4"}.").pack()

#Bucle de ejecución
root.mainloop()