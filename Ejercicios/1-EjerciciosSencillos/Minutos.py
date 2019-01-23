# Pedir al usuario un número de minutos y mostrar cuantas horas son

min = int(input("Indica los mínutos: "))

print("Horas:", format(min // 60), "Mínutos:", (min % 60)) # "//" es una división entera