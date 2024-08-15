import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("¿Cuan grande quieres que sea la contrasena? Ingresa un numero:"))

contrasena = ""

for i in range (longitud):
    contrasena += random.choice(caracteres)

print(contrasena)
