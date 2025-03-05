from tkinter import *
root = Tk()



entrada = Entry(root, width=100, show="*")
entrada.grid(row=0, column=0)

def click_boton():
    texto = Label(root, text=f'Se almacenó "{entrada.get()}" correctamente').grid(row=1, column=0)

boton1 = Button(root, text="Enviar", bg="red", padx=100, 
                pady=25, command=click_boton).grid(row=1, column=0)


root.mainloop()