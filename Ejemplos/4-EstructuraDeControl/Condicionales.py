# El if siempre acabará con : y lo que haya dentro del if irá tabulado
# Para anidar else if sera con elif
num = 0
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Es 0")

# if ternario
lang = "es"
saludo = "hola" if lang == "es" else "hi"