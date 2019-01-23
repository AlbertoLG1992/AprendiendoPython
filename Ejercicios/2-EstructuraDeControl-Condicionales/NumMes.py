#Introducir un número entre 1 y 12 e indicar el mes que corresponde

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

num = int(input("Indica un número del 1 al 12: "))

if num < 1 or num > 12:
    print("El número se encuentra fuera de rango")
else:
    print(meses[num - 1])