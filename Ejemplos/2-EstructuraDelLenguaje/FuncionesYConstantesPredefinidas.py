#EJEMPLO DE FUNCIONES DE PYTHON

# Para mostrar por pantalla
print("hola")

# Para hayar el maximo
num = max(5, 10, 6)
print(num)

# Para hayar el valor hexadecimal de un número
num = hex(123)
print(num)

# Para crear un entero desde una cadena
num = int("22")
print(num)

# Para optener el tipo de una variable
salida = type(num)
print(salida)

# Indicar que una variable no tiene tipo
num = None
print(type(num))

# Para pedir ayuda con alguna función con help('función')
print(help(print))

# Para realizar una operación con cadenas de caracteres eval()
print(eval("2 + 2"))

# Para comparar un tipo de dato con una variables es la funcion isinstance()
if (isinstance(5, int)):
    print(True)
else:
    print(False)