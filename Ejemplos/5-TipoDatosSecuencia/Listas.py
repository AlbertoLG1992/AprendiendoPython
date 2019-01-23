# Las listas ( list ) me permiten guardar un conjunto de datos que se pueden repetir y
# que pueden ser de distintos tipos. Es un tipo mutable.

'''
SLICE
Para optener un rango dentro de una lista:

lista[start:end] # Elementos desde la posición start hasta end-1
lista[start:] # Elementos desde la posición start hasta el final
lista[:end] # Elementos desde el principio hata la posición end-1
lista[:] # Todos Los elementos
lista[start:end:step] # Igual que el anterior pero dando step saltos.
Se pueden utilizar también índices negativos, por ejemplo: lista[::-1]
'''

# Con la función enumerate enumera la lista y devuelve un objeto como tupla
seasons = ['Primavera', 'Verano', 'Otoño', 'Invierno']
print(list(enumerate(seasons)))

# Si se quiere empezar en un número concreto es de la siguiente forma
print(list(enumerate(seasons, start=1)))

# Para copiar una lista sin copiar el id al que referencia es mediante slice
seasons2 = seasons[:]

# Listas bidimensionales
tabla = [[1,2,3],[4,5,6],[7,8,9]]
print(tabla[1][1])

# Recorrer una lista bidimensional
for fila in tabla:
    for elem in fila:
        print(elem, end=" ")
    print()
