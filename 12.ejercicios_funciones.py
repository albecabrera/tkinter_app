# Añade un color a la lista con el uso de una función
colores = ["rojo", "verde", "amarillo"]

def anadir_color(color):
    colores.insert(0, color)

anadir_color(input("Escriba un color para añadirlo a la lista:\n"))

print(colores)