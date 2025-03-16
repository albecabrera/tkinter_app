texto = ("Adipiscing et pariatur voluptate, adipiscing fugiat et ut.Consectetur id, duis nostrud fugiat ad. Nostrud fugiat ad incididunt sed eiusmod. Ad incididunt sed eiusmod officia. Sed eiusmod officia magna, adipiscing. Magna adipiscing, exercitation ex anim reprehenderit dolor. Ex anim reprehenderit dolor aute. Reprehenderit dolor aute labore. Aute, labore ea eu laborum id anim amet.")
print(texto) 
texto = """Adipiscing et pariatur voluptate, adipiscing fugiat et ut.Consectetur id, duis nostrud fugiat ad. Nostrud fugiat ad incididunt sed eiusmod. Ad incididunt sed eiusmod officia. Sed eiusmod officia magna, adipiscing. Magna adipiscing, exercitation ex anim reprehenderit dolor. Ex anim reprehenderit dolor aute. Reprehenderit dolor aute labore. Aute, labore ea eu laborum id anim amet."""

p = "Programación"
f = "Fácil"
print((p + " ")*3) # Así se puede imprimir 3 veces la cadena de texto con espacios. 

frase = ["Estoy " "aprendiendo " "Python " "con " "el " "curso " "de " "100 " "días " "de " "programación " "fácil"]
print(" ".join(frase))

colores = [f"rojo", "azul", "verde", "amarillo" ]
GUION= "-"
PUNTO="."

for color in colores:
    print("{}{}{}".format(GUION, color.capitalize(), PUNTO))
