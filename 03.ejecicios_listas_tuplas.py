lista_numeros = [10, 45, 55, 76]
print(lista_numeros)
print(lista_numeros[3])
print(f'Aqui se muestra el número: {lista_numeros[0]} y el número {lista_numeros[3]}')
    
lista_colores = ["rojo", "azul", "verde", "amarillo"]
print(lista_colores[1][2])

lista_paises = ["Argentina", "España", "Alemania", "Cuba"]
print(lista_paises[-1]) #  
print(lista_paises[-2])


lista_colores = ["rojo", "azul", "verde", "amarillo"]
lista_colores.insert(0, "gris")
lista_colores.append("rosa")
lista_colores.insert(3, "naranja")
print(lista_colores)

print(lista_colores.pop(1))
print(lista_colores.pop(3))
print(lista_colores.pop(3))
print(lista_colores)

# Duplicar una lista en una lista nueva
 
lista_copia = lista_colores = ["rojo", "azul", "verde", "amarillo"]
print(lista_copia)

lista_numeros2 = [10, 45, 356, 10, 10, 10, 67, 54, 45, 54, 10 ,10]
print(lista_numeros2.count(10))

lista_numeros2.sort()
print(lista_numeros2)
lista_numeros2.reverse
print(lista_numeros2)
print(len(lista_numeros2))
