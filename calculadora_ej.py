# '''Calculadora de exponentes'''
# numero_exponente1 = 10
# numero_exponente2 = 4
# print(input("Introduzca el primer número: ")) #10
# print(input("Introduzca el primer número: ")) #4
# # El resultado de 10 elevado a la 4 es 10000
# resultado = numero_exponente1 ** numero_exponente2
# print(f'El resultado de 10 elevado a la 4 es: {resultado} ')


# Se le indica al usuario de que va la aplicación.
print("--- Calculadora de exponentes ---")

# Se solicitan los números para realizar el cálculo y se transforman a integer.
numero_1 = int(input("Introduzca el primer número.\n"))
numero_2 = int(input("Introduzca el segundo número.\n"))

# Se realiza el cálculo y se almacena en una variable.
resultado = numero_1 ** numero_2

# Se le muestra el resultado al usuario.
print(f"El resultado de {numero_1} elevado a {numero_2} es {resultado}.")