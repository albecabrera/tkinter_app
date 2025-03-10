# aprender bucles
for i in range(3,6):
    print(f'El valor del bucles es: {i}')
print("Fin del bucle")
for i in range(3,12,3): # incremento de 3-12 aumentando siempre de 3 en 3
    print(f'El valor del bucles es: {i}')
print("Fin del bucle")

# bucle con listas
# 1 opción
colores = ["rojo", "azul", "verde", "amarillo"]
print("---Listado de colores---")

for color in colores: 
    print(f'-{color}')
print() 
# 2. opción
print(f'-{colores[0]}')
print(f'-{colores[1]}')
print(f'-{colores[2]}')