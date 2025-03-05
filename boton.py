from tkinter import *
root = Tk()


def click_boton():
    texto = Label(root, text="No vuelvas a presionar el boton").grid(row=1, column=1)

boton1 = Button(root, text="No presiones el botón", bg="red", padx=100, 
                pady=25, command=click_boton).grid(row=0, column=0)


root.mainloop()