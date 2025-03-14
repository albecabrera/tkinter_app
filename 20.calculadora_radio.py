# elaborar una calculadora que calcule el radio de un círculo

radio_cm = int(input("Introduzca el área del círculo en cm \n"))

PI = 3.14159

calcula_area = lambda radio : PI * radio * radio

area = round(calcula_area(radio_cm), 2)

print(f'El área de círculo es de {area} cm.')

(lambda nombre : print(f'El nombre es: {nombre}'))("Alberto")

colores = ["rojo", "negro", "azul", "amarillo"]
print(colores[0])

def calcular_radio(area):
    return round((area / PI) ** 0.5, 2)

area_circulo = float(input("Introduzca el área del círculo en cm²: "))
radio = calcular_radio(area_circulo)
print(f'El radio del círculo es de {radio} cm.')

#