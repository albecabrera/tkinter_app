# ¿Cuáles de estos strings son correctos?
''' Hoy es un gran día para programar"
'El cielo está nublado"
'¿Qué día es hoy?'
"Mañana, en inglés se dice "morning""'
'''

'''
2. Imprime en la consola el número de caracteres que tiene la palabra "automáticamente". 
Lo puedes hacer con variable o directamente en un print().

3. ¿Sabrías mostrar en la consola solo el caracter de la "á" con acento de "automáticamente"?
Lo debes hacer mediante las posiciones de string.

4. Realiza la operación de 10 elevado a 5 con el uso del operador exponente.
Ahora, ¿cómo harías esa operación sin el operador de exponente?

5. ¿En qué dos estados puede estar un dato booleano?
Muestra en la consola el tipo de dato que contiene esta variable: "numero_1 = 675.87".

6. Muestra la cantidad de dígitos que tiene este número (768763843) utilizando la función len().

7. Haz que estos datos float, se conviertan en integer mediante la conversión de tipos:
numero_1 = "14.527"
numero_2 = "560.92"
'''
# ejercicio 1
# 1. ¿Qué error devuelven los strings mal escritos?
print('Hoy es un gran día para programar')
print('El cielo está nublado')
print('¿Qué día es hoy?')
print('Mañana, en inglés se dice "morning"')

# ejericio 2
print(len("automáticamente"))
palabra = "automáticamente"
print("automáticamente")

# ejercicio 3
# 3. ¿Sabrías mostrar en la consola solo el caracter de la "á" con acento de "automáticamente"?
# Lo debes hacer mediante las posiciones de string.
print(palabra[5])

# ejercicio 4
# 4. Realiza la operación de 10 elevado a 5 con el uso del operador exponente.
# Ahora, ¿cómo harías esa operación sin el operador de exponente?
a = 10
b = 5
print(a ** b)

exponente = 1
for _ in range(b):
    exponente *= a
print(exponente)

# 5. ¿En qué dos estados puede estar un dato booleano?
# Muestra en la consola el tipo de dato que contiene esta variable: "numero_1 = 675.87".
print(True)
print(False)
numero_1 = "675.87"
print(type(numero_1))

# 6. Muestra la cantidad de dígitos que tiene este número (768763843) utilizando la función len().
número = "768763843"

print(len(número))

# 7. Haz que estos datos float, se conviertan en integer mediante la conversión de tipos:
# numero_1 = "14.527"
# numero_2 = "560.92"
numero_1 = "14.527"
numero_2 = "560.92"

numero_1 = int(float(numero_1))
numero_2 = int(float(numero_2))
print(numero_1)
print(numero_2)

# Redondea estos números con la cantidad de decimales indicada en los comentarios e imprímelos en la consola.
numero_1 = 10.897654876534 # 3 decimales
numero_2 = 7674.7886 # 2 decimales 
numero_3 = 68754.78 # 1 decimal

print(round(numero_1, 2))
print(round(numero_2, 1))
print(round(numero_3, 0))


# redondear un número
numero_1 = 345.5678
print(round(345.5678))
print(round(numero_1, 1))
# respuesta 345.6


# ¿Cuál es la diferencia entre el operador módulo y floor división?
print(a // b) # división sin resto
print(a % b) # división con resto

# Asigna con los operadores de asignación de incremento o decremento los siguientes valores 
# indicados en los comentarios.
numero_1 = 10 # +60
numero_2 = 24 # -100
numero_3 = 65.67 # +4.33

numero_1 += 60
numero_2 -= 100
numero_3 += 4.33

print(numero_1)
print(numero_2)
print(numero_3)

'''Mediante la técnica de formateo de strings (recuerda el prefijo f) muestra literalmente todos estos 
valores en una frase en el print(), sin utilizar la concatenación.
La frase es esta: "El valor 769.97 es bastante más grande que 4. ¿Am I a string? The answer is True.".
'''
valor = 769.97
print(f'"El valor 769.97 es bastante más grande que 4. ¿Am I a string? The answer is True."')

numero_1 = 4
numero_2 = 769.97
texto = "am I a string"
decision = True

print(numero_1)
print(numero_2)
print(texto)
print(decision)