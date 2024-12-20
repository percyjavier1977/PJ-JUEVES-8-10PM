suma = 0
print("Ingresa números para ejecutar la sumatoria...Ingresa 0 para cerrar o finalizar")

while True:  #Emula la estructura do while
    numero = int(input("Ingrese el número: "))
    suma += numero
    if numero == 0:
        break


print("La suma es:",suma)
    