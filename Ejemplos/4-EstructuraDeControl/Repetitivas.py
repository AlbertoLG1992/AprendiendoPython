# While
year = 2000;

while year <= 2019:
    print(year)
    year += 1

# En Python es posible poner unas instrucciones finales al acabar el while
# mediante un else
year = 2000;

while year <= 2019:
    print(year)
    year += 1
else:
    print("Fin")

# FOR
# En Python el for recorre una secuencia
for i in range(10):
    print(i)

# Un string tambien se considera una secuencia
for i in "Hola":
    print(i)

# Una lista tambien es una secuencia
for i in [1, 2, 3, 4]:
    print(i)

# El for tambien puede tener una instrucción final
for i in [1, 2, 3, 4]:
    print(i)
else:
    print("fin")

# Para recorrer dos o más secuencias a la vez es necesario hacerlo mediante la función zip
for x,y in zip(range(1,4),["ana","juan","pepe"]):
    print(x, y)
