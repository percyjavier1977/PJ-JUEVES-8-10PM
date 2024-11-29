import random
numero_adivinar = random.randint(1,10)
adivinanza = int(input("Ingrese un numero entero(1-10):\n"))
if adivinanza == numero_adivinar:
    resultado = "¡Excelnete! Adivisnaste el número."
else:
    resultado = "No adivinaste el número"


print("El numero secreto es:",numero_adivinar)
print(resultado)
