# Como crear una calculadora simple
from tkinter import *

root = Tk()
root.title("Calculadora básica") # titulo
root.resizable(0, 0)
root.geometry("296x265")

pantalla = Entry(root,
                 width=22,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 font=("arial", 18, "bold"))

pantalla.grid(row=0, padx=2, pady=2, columnspan=4)

boton_1 = Button(root, text="1",
                 width=9,
                 height=3,
                 bg="white",
                 fg="red",
                 borderwidth=0,
                 cursor="hand2").grid(row=1, column=0, padx=1, pady=1)

boton_2 = Button(root, text="2",
                 width=9,
                 height=3,
                 bg="white",
                 fg="red",
                 borderwidth=0,
                 cursor="hand2").grid(row=1, column=1, padx=1, pady=1)

boton_3 = Button(root, text="3",
                 width=9,
                 height=3,
                 bg="white",
                 fg="red",
                 borderwidth=0,
                 cursor="hand2").grid(row=1, column=2, padx=1, pady=1)

boton_4 = Button(root, text="4",
                 width=9,
                 height=3,
                 bg="white",
                 fg="red",
                 borderwidth=0,
                 cursor="hand2").grid(row=2, column=0, padx=1, pady=1)

boton_5 = Button(root, text="5",
                 width=9,
                 height=3,
                 bg="white",
                 fg="red",
                 borderwidth=0,
                 cursor="hand2").grid(row=2, column=1, padx=1, pady=1)

boton_6 = Button(root, text="6",
                 width=9,
                 height=3,
                 bg="white",
                 fg="red",
                 borderwidth=0,
                 cursor="hand2").grid(row=2, column=2, padx=1, pady=1)

boton_7 = Button(root, text="7",
                 width=9,
                 height=3,
                 bg="white",
                 fg="red",
                 borderwidth=0,
                 cursor="hand2").grid(row=3, column=0, padx=1, pady=1)

boton_8 = Button(root, text="8",
                 width=9,
                 height=3,
                 bg="white",
                 fg="red",
                 borderwidth=0,
                 cursor="hand2").grid(row=3, column=1, padx=1, pady=1)

boton_9 = Button(root, text="9",
                 width=9,
                 height=3,
                 bg="white",
                 fg="red",
                 borderwidth=0,
                 cursor="hand2").grid(row=3, column=2, padx=1, pady=1)

boton_0 = Button(root, text="0",
                 width=9,
                 height=3,
                 bg="white",
                 fg="red",
                 borderwidth=0,
                 cursor="hand2").grid(row=4, column=1, padx=1, pady=1)

boton_igual = Button(root, text="=",
                 width=9,
                 height=3,
                 bg="red",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2").grid(row=4, column=2, padx=1, pady=1)

boton_punto = Button(root, text=".",
                 width=9,
                 height=3,
                 bg="spring green",
                 fg="black",
                 borderwidth=0,
                 cursor="hand2").grid(row=4, column=0, padx=1, pady=1)

boton_mas = Button(root, text="+",
                 width=9,
                 height=3,
                 bg="deep sky blue",
                 fg="red",
                 borderwidth=0,
                 cursor="hand2").grid(row=1, column=3, padx=1, pady=1)

boton_menos = Button(root, text="-",
                 width=9,
                 height=3,
                 bg="deep sky blue",
                 fg="black",
                 borderwidth=0,
                 cursor="hand2").grid(row=2, column=3, padx=1, pady=1)

boton_multiplicacion = Button(root, text="x",
                 width=9,
                 height=3,
                 bg="deep sky blue",
                 fg="black",
                 borderwidth=0,
                 cursor="hand2").grid(row=3, column=3, padx=1, pady=1)

boton_division = Button(root, text="/",
                 width=9,
                 height=3,
                 bg="deep sky blue",
                 fg="red",
                 borderwidth=0,
                 cursor="hand2").grid(row=4, column=3, padx=1, pady=1)

mainloop()