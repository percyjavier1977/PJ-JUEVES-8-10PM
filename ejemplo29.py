#Programa donde se ingresar 5 notas y debemos mostrar el punataje, promedio, nota maxima
#nota minima
notas=[]
suma = 0
print("INGRESE 5 NOTAS (Entre 0 y 20): ")

for i in range(5):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)


puntaje = sum(notas)
promedio = puntaje / len(notas)
nota_max = max(notas)
nota_min = min(notas)


print("\nRESULTADOS")
print(f"El puntaje: {puntaje}")
print(f"El promedio: {promedio:.2f}")
print(f"Nota máxima: {nota_max}")
print(f"Nota mínima: {nota_min}")


      
    
