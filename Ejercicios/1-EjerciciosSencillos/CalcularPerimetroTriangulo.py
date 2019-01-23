# Calcula el perimetro de un area y perimetro dada su base y altura

base = float(input("Indica la base del triangulo: "))
altura = float(input("Indica la altura del triangulo: "))

perimetro = (2 * base) + (2 * altura)
area = base * altura

print("El perímetro es:", perimetro, "y el area:", area)