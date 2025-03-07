from tkinter import *
root = Tk()

def click_boton():
	Label(root, text="¡No vuelvas a presionarlo!").grid()

boton1 = Button(root,
				text="No presiones el botón rojo",
				bg="red",
				padx=100,
				pady=25).grid(row=1, column=2)

root.mainloop()