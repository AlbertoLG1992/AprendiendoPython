# Los operadores booleanos son:
# or : ||
# and : &&
# not : para negar
x = True
y = False
if(x and not y):
    print("ok")
else:
    print("no")

# Para comparar listas tenemos all y any
# all(iterador) : Recibe un iterador, por ejemplo una lista,
# y devuelve True si todos los elementos son verdaderos o el iterador está vacío.
if(all([1, True, [1, 2]])):
    print("all ok")
else:
    print("all no")

# any(iterador) : Recibe un iterador, por ejemplo una lista,
# y devuelve True si alguno de sus elemento es verdadero, sino devuelve False.
if(any([1, False, [1, 2]])):
    print("any ok")
else:
    print("any no")