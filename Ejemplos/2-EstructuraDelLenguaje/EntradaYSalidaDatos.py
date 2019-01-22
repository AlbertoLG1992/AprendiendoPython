# Introducir datos por teclado input()
num1 = input("Dame el número 1:")
print(num1)

# Toda variable que se introduce por teclado se recoge como String
# Para cambiarlo como es este caso es necesario forzar el tipo
print(type(num1))
print(type(int(num1)))

# Para usar un print se puede concatenar como en Java mendiante + o
# se puede separar mediante ","
print("Hola son las", 6, "de la tarde")

# Esto hace que se introduzcan espacios por defecto, pero esos espacios se
# pueden cambiar por otro caracter o incluso añadir un caracter al final de linea
print(1, 2, 3, sep="-", end=".\n")

# Para cambiar el formato al sacar por pantalla un datos se hará mediante format()
print(format(31,"b"),format(31,"o"),format(31,"x"))

# para indicar el número de decimales de un numero tambien se puede hacer con format
print(format(2.345,".2f"))
