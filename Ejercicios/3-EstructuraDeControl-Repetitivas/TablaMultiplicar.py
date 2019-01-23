# Pedir un número por teclado y mostrar la tabla de multiplicar
numero = int(input("Número:"))
for i in range(1,11):
    print (i, "x", numero, "=", (i * numero))
