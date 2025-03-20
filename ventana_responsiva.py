# Importaciones
import tkinter as tk

root = tk.Tk()
root.title("Curso de Tkinter der programación fácil")
root.resizable(True, True)
ancho_ventana = 500
alto_ventana = 400

# Pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

coordenadas_x = int((ancho_pantalla/2) - ((ancho_ventana/2)))
coordenadas_y = int((alto_pantalla/2) - ((alto_ventana/2)))

root.geometry("{}x{}+{}+{}".format(alto_ventana, ancho_ventana, coordenadas_x, coordenadas_y))


tk.Label(text=f"Ancho de pantalla: {ancho_pantalla} pixeles.").pack()
tk.Label(text=f"Alto de pantalla: {alto_pantalla} pixeles.").pack()




# Bucle de ejecución 
root.mainloop()
