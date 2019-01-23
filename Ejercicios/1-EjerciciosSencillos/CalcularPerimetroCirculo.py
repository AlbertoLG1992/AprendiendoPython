# Calcular area y perimetro de un circulo

import math

radio = float(input("Indica el radio:"))

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print("Resultado: Área:", format(area, ".2f"), "Perímetro:", format(perimetro, ".2f"))