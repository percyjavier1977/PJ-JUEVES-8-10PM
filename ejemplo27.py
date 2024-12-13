import random
numero_adivinar = random.randint(1,10)
intentos_max = 3
for intento in range(1,intentos_max+1):
    numero_ingresado = int(input(f"Intento {intento}: ingrese un número entre 1 y 10:\n"))
    if numero_ingresado == numero_adivinar:
        print("¡felicitaciones! Adivinaste el número.. Recoge tu premio")
        break
    if intento < intentos_max:
        if numero_ingresado < numero_adivinar:
            print("¡No adivinaste el número.....El número que quiere adivinar es mayor ")
        else:
            print("¡No adivinaste el número.....El número que quiere adivinar es menor")

else: # Solo sale cuando se cumple el bucle
    print("Lo siento no adivinaste el número.")
    print(f"El número de la suerte es {numero_adivinar}")
    print("FIN DEL JUEGO")
        
    