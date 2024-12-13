#Ejemplo donde se ingresan n notas se debe calcular el puntaje y el promedio
#luego mostrar la nota mayor y menor

n_notas = int(input("Ingrese el número de notas:\n"))
suma_notas = 0
nota_maxima = float('-inf') #Inicia con un valor muy bajo
nota_minima = float('inf') #Inicia con un valor muy alto
for i in range(n_notas):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    suma_notas += nota
    if nota > nota_maxima:
        nota_maxima = nota
    if nota < nota_minima:
        nota_minima = nota


promedio = suma_notas / n_notas

print(f"El Puntaje es: {suma_notas}")
print(f"El promedio es: {promedio:.2f}")
print(f"La nota maxima es: {nota_maxima}")
print(f"La nota minima es: {nota_minima}")