# Hacer una calculadora
print("---CALCULADORA MEJORADA DE NUEVO---")
# fuciones
# suma
def suma(numero1, numero2):
    return numero1 + numero2

# resta
def resta(numero1, numero2):
    return numero1 - numero2

# multiplicación
def multiplicacion(numero1, numero2):
    return numero1 * numero2

# división
def division(numero1, numero2):
    return numero1 / numero2
while True: 
    # Se le pide al usuario que elija una opción y se evalúa
    print("Por favor, elija una opción:")
    print("1- Suma. ")
    print("2- Resta. ")
    print("3- Multiplicacion. ")
    print("4- Division. ")
    print("5- Modulo. ")
    print("6- Exponente. ")
    print("7- Salir. ")

 # Se le pide al usaurio un número de opción
eleccion = int(input("Teclee un número y pulse ENTER:\n"))

if eleccion == 1:
    print('Ha elegido la opción "suma".')
elif eleccion == 2:
    print('Ha elegido la opción "resta".')
elif eleccion == 3:
    print('Ha elegido la opción "multiplicacion".')
elif eleccion == 4:
    print('Ha elegido la opción "division".')
elif eleccion == 5:
    print('Ha elegido la opción "modulo".')
elif eleccion == 6:
    print('Ha elegido la opción "exponente".')
elif eleccion == 7:
    print('Ha elegido la opción "salir".')
else:
    print('Opción no válida.')

# Se solicitan los dos números para cualquier operación que elija.
if eleccion in [1, 2, 3, 4, 5, 6]:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    if eleccion == 1:
        print(f"El resultado de la suma es: {suma(numero1, numero2)}")
    elif eleccion == 2:
        print(f"El resultado de la resta es: {resta(numero1, numero2)}")
    elif eleccion == 3:
        print(f"El resultado de la multiplicación es: {multiplicacion(numero1, numero2)}")
    elif eleccion == 4:
        if numero2 != 0:
            print(f"El resultado de la división es: {division(numero1, numero2)}")
        else:
            print("Error: División por cero.")
    elif eleccion == 5:
        print(f"El resultado del módulo es: {numero1 % numero2}")
    elif eleccion == 6:
        print(f"El resultado del exponente es: {numero1 ** numero2}")
    elif eleccion == 7:
        print("Saliendo del programa...")
    break

