# bucle para iterar la lista
lista_numeros = [10, 20, 10 ,40, 50, 365, 10, 25, 60, 80]

for i in lista_numeros: 
    if i == 10: # Se omiten los valores 10
        continue
    elif i == 365: # Se rompe la iteración en el momento que le toca al numero 365
        break
    else: 
        print(f'El valor del elemento es: {i}')

