from tkinter import *
root = Tk()

# marco1  0
marco_principal = Frame()
marco_principal.grid(row=0, column=0)
marco_principal.grid()
marco_principal.config(width="100", height="100", bg="blue")

# marco 1
marco_principal1 = Frame()
marco_principal1.grid(row=1, column=0)
marco_principal1.grid()
marco_principal1.config(width="100", height="100", bg="red")

# marco 2
marco_principal2 = Frame()
marco_principal2.grid(row=1, column=1)
marco_principal2.grid()
marco_principal2.config(width="100", height="100", bg="yellow")

# marco 3
marco_principal3 = Frame()
marco_principal3.grid(row=2, column=0)
marco_principal3.grid()
marco_principal3.config(width="100", height="100", bg="green")

# marco 4
marco_principal4 = Frame()
marco_principal4.grid(row=2, column=1)
marco_principal4.grid()
marco_principal4.config(width="100", height="100", bg="yellow")

# marco 5
marco_principal5 = Frame()
marco_principal5.grid(row=2, column=1)
marco_principal5.grid()
marco_principal5.config(width="100", height="100", bg="black")

def click_boton():
    texto = Label(root, text="No vuelvas a presionar el boton").grid(row=1, column=1)

boton1 = Button(root, text="No presiones el botón", bg="red", padx=100, 
                pady=25, command=click_boton).grid(row=0, column=0)


root.mainloop()