'''
1. Un título para la calculadora. ✅
2. El usuario podrá decidir que operación desea antes de introducir los operandos (números con los que operar). Con el fin de informar al usuario de cada opción, crea un menú con varios print(). Por ejemplo, print("1-Suma").
3. Se debe avisar al usuario de la opción que ha seleccionado.
4. Si el usuario elige una opción que no está en el menú, se le debe avisar del error.
5. Entrada de datos para dos números float.
6. Hay que crear un sistema que realice las operaciones.
7. Se le deberá mostrar el resultado correctamente al usuario.
8. Opcionalmente, le puedes añadir un redondeo (round()) a las operaciones, para que el resultado solo muestre dos dígitos.
9. Otro requisito opcional más complicado, es añadir, de alguna forma, un control para el caso en el que el usuario ponga una opción inválida (no se contemplarán los errores de tipo de dato todavía).

'''
# 1. Se le indica al usuario de que va la aplicación.
print("--- Calculadora de exponentes ---")
# 2. El usuario podrá decidir que operación desea antes de introducir los operandos (números con los que operar). Con el fin de informar al usuario de cada opción, crea un menú con varios print(). Por ejemplo, print("1-Suma").
'''
Hola, elija una opción:
1- Suma.
2- Resta.
3- Multiplicación
4- División
5- Módulo
6- Exponente
Teclee un número y pulse ENTER'
'''
# Mostrar el menú de opciones
print("Hola, elija una opción")
print("1- Suma")
print("2- Resta")
print("3- Multiplicación")
print("4- División")
print("5- Módulo")
print("6- Exponente")

# Leer la opción del usuario
opcion = input("Teclee un número y pulse ENTER: ")

# Avisar al usuario de la opción seleccionada
print(f"Ha seleccionado la opción {opcion}")

# Verificar si la opción es válida
if opcion not in ['1', '2', '3', '4', '5', '6']:
    print("Opción no válida. Por favor, elija una opción del 1 al 6.")
else:
    # Entrada de datos para dos números float
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Realizar la operación seleccionada
    if opcion == '1':
        resultado = num1 + num2
    elif opcion == '2':
        resultado = num1 - num2
    elif opcion == '3':
        resultado = num1 * num2
    elif opcion == '4':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: División por cero"
    elif opcion == '5':
        resultado = num1 % num2
    elif opcion == '6':
        resultado = num1 ** num2

    # Mostrar el resultado al usuario
    print(f"El resultado es: {resultado}")
