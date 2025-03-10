colores = ["rojo", "azul", "verde", "amarillo"]
print("---Listado de colores---")

for color in colores:
    if color == "azul" or color == "verde":
        print("Se ha saltado este valor")
        continue
    print(f'-Color {color}') 

for color in colores:
    if color == "azul":
        print("Se ha roto la ejecución del bucle")
        break
    print(f'-Color {color}') 