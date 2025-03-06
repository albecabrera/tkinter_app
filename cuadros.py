from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Este es el título de la ventana principal")
root.iconbitmap("img/computer.ico")

def muestra_ventana():
    respuesta = askquestion(title="Pregunta sería", message="¿Debería dejar de programar y salir a la calle?")
    
    if respuesta == "no":
        showinfo(title="A seguir programando!", 
                 message="Estupendo, eligió la respuesta correcta.")
    if respuesta == "yes":
        respuesta_retry = askretrycancel(title="Botón equivocado.",
                       message="Haga click en Reintentar para seguir programando.")
        
        if respuesta_retry:
           showinfo(title="A seguir programando!", 
                 message="Estupendo, eligió la respuesta correcta.")
        

        
boton1 =Button(root, text="Enviar",
               command=muestra_ventana,
               width=75).pack()


root.mainloop()
