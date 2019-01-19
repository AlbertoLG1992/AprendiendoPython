# Las instrucciones de las estructuras de control es obligatorio tabularlas, pues es la
# única forma de saber que se encuentran dentro, ya que no existen las llaves
edad = 26
if edad >= 18:
    print("Es mayor de edad")
else:
    print("es menor de edad")

# El punto y coma “;” se puede usar para separar varias sentencias
# en una misma línea, pero no se aconseja su uso.
edad = 15; print(edad)

# Cuando el bloque a sangrar sólo ocupa una línea ésta puede
# escribirse después de los dos puntos:
azul = True
if azul: print('Cielo')

# La barra invertida “\” permite escribir una línea de
# código demasiado extensa en varias líneas:
if edad < 5 and azul and 3 == 5 and \
    5 * 5 == 10 and edad == 0:
    print("Ha entrado en el if")

# Las expresiones entre paréntesis, llaves o corchetes pueden
# ocupar varias líneas:
dias = ['lunes', 'martes', 'miércoles', 'jueves',
        'viernes', 'sábado', 'domingo']
