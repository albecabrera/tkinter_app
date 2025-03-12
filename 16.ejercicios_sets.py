colores = {
  1 : "rojo",
  2 : "azul",
  3 : "verde",
  4 : "amarillo"
 }

for clave in colores:
    print(f'{clave} - {colores[clave].capitalize()}')

colores[5] = "naranja"