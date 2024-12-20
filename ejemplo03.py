#Crear un programa donde se sume los números que el usuario ingresa hasta que ingersa cero
suma = 0
numero = None

print("Ingresa números para ejecutar la sumatoria...Ingresa 0 para cerrar o finalizar")

while numero !=0:
    numero = int(input("Ingrese el número: "))
    suma +=numero



print("La suma es:",suma)