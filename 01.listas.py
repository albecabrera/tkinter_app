# Listas en Python
lista_colores = ["rojo", "azul", "verde", "amarillo"] # siempre se cuenta desde cero

print(lista_colores[2])
print(f'El segundo elemento de la lista es: {lista_colores[1]}')
print(lista_colores[3][3])

# posiciones negativas
print(lista_colores[-1])

lista_colores[1] = "naranja"
print(lista_colores)

lista_colores.append("rosado") #agregar elemento al final de una lista
print(lista_colores)

lista_colores.insert(2, "naranja") # insertar un elemento a una lista
print(lista_colores)

# lista_colores.clear() # vaciar la lista
# print(lista_colores)

lista_colores.pop(2)

lista_colores.remove("naranja")
print(lista_colores)

lista_nueva = lista_colores.copy()
print(lista_nueva)

lista_colores2 = ["rojo", "azul", "verde", "amarillo", "rojo", "rojo"]#
print(lista_colores2.count("rojo"))
print(lista_colores2.index("rojo"))

lista_colores2.sort()
print(lista_colores2)

lista_colores2.sort(reverse=True) # ordenar alfabeticamente de atrás para alante
print(lista_colores2)

lista_colores.extend(lista_colores2)
print(lista_colores)