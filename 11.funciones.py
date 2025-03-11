# Como funcionan las funciones en Python

def saludar(nombre, edad):
    print(f"Tu nombre es: {nombre} y tu edad es: {edad}")
saludar("Alberto", 47)
saludar("Bijirita", 15)
saludar("Alfredo", 17)
saludar("Mati", 9) 
saludar("Cordula", 49)


def suma(numero1, numero2):
    return numero1 + numero2
resultado = suma(10, 50)

print(resultado)