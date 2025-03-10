'''
01. Añade un título con un print para la pizzaría, algo como -> Pizzería PF PIZZA PF!
02. El usuario introducirá el dinero que quiera. Guárdalo en una variable.
03. Crea una lista donde ir añadiendo los ingredientes extra. Pista: métodos de adición en listas.
04. Habrá mínimo tres tipos de pizzas para elegir (pon las que quieras).
05. Cada pizza tendrá un coste diferente.
06. El usuario podrá elegir solo una pizza
07. Una vez elegida la pizza, se le informará al usuario del total que lleva por el momento.
08. Se le debe pedir si quiere o no, añadir ingredientes extra (estos harán subir el precio final).
09. Añade al menos 3 ingredientes extra. El usuario podrá elegir uno o varios de estos. 
No hay límite de ingredientes extra. Si se pasa del dinero que tiene, se le dirá que no le llega y 
que vuelva a realizar el pedido.
10. Las pizzas e ingredientes, tendrán sus precios almacenados en variables.
11. Con cada ingrediente extra, se le debe ir sumando el precio al total y mostrárselo al usuario
con el cambio que le queda.
12. Si el usuario no quiere ingredientes extra, puede pagar directamente sin añadir ninguno.
'''
# 01. Añade un título con un print para la pizzaría, algo como -> Pizzería PF PIZZA PF!
print("---Pizzería PIZZA PF---")
# 02. El usuario introducirá el dinero que quiera. Guárdalo en una variable.
dinero = float(input("Introduce la cantidad de dinero que quieres gastar: "))
# 03. Crea una lista donde ir añadiendo los ingredientes extra. Pista: métodos de adición en listas.
ingredientes_seleccionados = []
# 04. Habrá mínimo tres tipos de pizzas para elegir (pon las que quieras).
# 05. Cada pizza tendrá un coste diferente.
pizzas = {
    "Margarita": 8.0,
    "Tonno": 12.5,
    "Hawai": 11.5
}
# 06. El usuario podrá elegir solo una pizza
print("Tipos de pizza disponibles:")
for pizza in pizzas:
    print(f"- {pizza}: ${pizzas[pizza]}")

pizza_elegida = input("Elige una pizza: ")

if pizza_elegida in pizzas:
    total = pizzas[pizza_elegida]
    print(f"Has elegido la pizza {pizza_elegida}. Total por el momento: ${total}")
else:
    print("La pizza seleccionada no está disponible.")

# 07. Una vez elegida la pizza, se le informará al usuario del total que lleva por el momento.
# 08. Se le debe pedir si quiere o no, añadir ingredientes extra (estos harán subir el precio final).
ingredientes_extra = {
    "extra queso": 1.5,
    "ajo": 0.5,
    "cebolla": 0.75,
    "aceitunas": 1.0
}

agregar_ingredientes = input("¿Quieres añadir ingredientes extra? (sí/no): ").strip().lower()

while agregar_ingredientes == "sí":
    print("Ingredientes extra disponibles:")
    for ingrediente, precio in ingredientes_extra.items():
        print(f"- {ingrediente}: ${precio}")

    ingrediente_elegido = input("Elige un ingrediente extra: ").strip().lower()

    if ingrediente_elegido in ingredientes_extra:
        if total + ingredientes_extra[ingrediente_elegido] <= dinero:
            ingredientes_seleccionados.append(ingrediente_elegido)
            total += ingredientes_extra[ingrediente_elegido]
            print(f"Has añadido {ingrediente_elegido}. Total por el momento: ${total}")
        else:
            print("No tienes suficiente dinero para añadir este ingrediente.")
    else:
        print("El ingrediente seleccionado no está disponible.")

    agregar_ingredientes = input("¿Quieres añadir más ingredientes extra? (sí/no): ").strip().lower()

print(f"Total a pagar: ${total}")


