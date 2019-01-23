lista = [1, 2, 3, 4, 5, 6]

# Para recorrer una secuencia se hará con un for
for num in lista:
    print(num, end=" ")

# Para saber si un elemento se encuentra en una lista es con in o not in
if 2 in lista:
    print("El 2 esta en la lista")

if 8 not in lista:
    print("El 8 no esta en la lista")

# Para concatenar una lista será con el operador "+"
lista = lista + [7,8,9]
print(lista)

# Para repetir una lista con "*"
print(lista * 2)

# Para obtener el dato de una posición
print(lista[3])

# Para optener un rango dentro de una lista
print(lista[2:5])

# Para saber el tamaño de la lista: len()
print("El tamaño de la lista es", len(lista))

# El valor máximo y el valor mínimo de una secuencia
print("El valor mínimo es", min(lista))
print("El valor máximo es", max(lista))

# Para borrar un elemento de la secuencia con del
del lista[5]
print(lista)

# Para sumar los valores de una secuencia en caso de que se pueda
print("la suma de todos es", sum(lista))

# Para ordenar una secuencia desordenada
print(sorted(lista))
# Para hacerlo en orden inverso
print(sorted(lista, reverse = True))