from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Este es el titulo de la ventana principal")
root.iconbitmap("img/computer.ico")

def muestra_ventana():
    showwarning(message="¿Debería dejar de programar y salir a la calle?", 
                title="Es es el mensaje que se muestra al usuario en la ventana.")

boton1 =Button(root, text="Enviar", command=muestra_ventana, width=75).pack()
root.mainloop()