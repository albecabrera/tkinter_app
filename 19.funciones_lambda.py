# Son funciones anónimas 
# def multiplicacion(numero1, numero2):
#     return numero1 * numero2
#     print(3, 5)

# 1. Primera opción
multiplicacion = lambda numero1, numero2: numero1 * numero2

resultado1 = multiplicacion(7,10)
resultado2 = multiplicacion(8,10)

print(resultado1)
print(resultado2)

print() 

# Las funciones lambda se utiliza para funciones pequeñas y para simplificar el código.
# 2. Segunda opción
(lambda numero1, numero2: print(numero1 * numero2))(7,5)