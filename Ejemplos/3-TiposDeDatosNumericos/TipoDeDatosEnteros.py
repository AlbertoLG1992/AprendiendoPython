'''
TIPOS DE DATOS
Enteros (int): Representan todos los números enteros (positivos, negativos y 0), sin parte decimal.
En python3 este tipo no tiene limitación de espacio.

Reales (float): Sirve para representar los números reales, tienen una parte decimal y otra decimal.
Normalmente se utiliza para su implementación un tipo double de C.

Complejos (complex): Nos sirven para representar números complejos, con una parte real y otra imaginaria.
'''

'''
Operadores aritméticos

+ : Suma dos números
- : Resta dos números
* : Multiplica dos números
/ : Divide dos números, el resultado es float .
// : División entera
% : Módulo o resto de la división
** : Potencia
+ , - : Operadores unarios positivo y negativo
'''

'''
Funciones predefinidas que trabajan con números

abs(x) : Devuelve al valor absoluto de un número.
divmod(x,y) : Toma como parámetro dos números, y devuelve una tubla con dos valores, 
    la división entera, y el módulo o resto de la división.
hex(x) : Devuelve una cadena con la representación hexadecimal del número que recibe como parámetro.
oct(x) : Devuelve una cadena con la representación octal del número que recibe como parámetro.
bin(x) : Devuelve una cadena con la representación binaria del número que recibe como parámetro.
pow(x,y): Devuelve la potencia de la base x elevedao al exponete y. Es similar al operador **`.
round(x,[y]) : Devuelve un número real (float) que es el redondeo del número recibido como parámetro, 
    podemos indicar un parámetro opcional que indica el número de decimales en el redondeo.
'''

'''
Operadores a nivel de bit

x | y : x OR y
x ^ y : x XOR y
x & y : a AND y
x << n : Desplazamiento a la izquierda n bits.
x >> n : Desplazamiento a la derecha n bits.
~x : Devuelve los bits invertidos.
'''

'''
Conversión de tipos

int(x) : Convierte el valor a entero.
float(x) : Convierte el valor a float.
complex(x) : Convierte el valor a un complejo sin parte imaginaria.
complex(x,y) : Convierta el valor a un complejo, cuya parte real es x y la parte imaginaria y.
'''