notas=[]
nombres = []

print("INGRESE LOS NOMBRES DE 5 ALUMNOS Y SUS RESPECTIVAS NOTAS (Entre 0 y 20): ")

for i in range(5):
    nombre = input(f"Nombre del alumno {i+1}: ")
    nota = float(input(f"Nota: {i+1}: de {nombre}: "))
    nombres.append(nombre)
    notas.append(nota)

 
puntaje = sum(notas)
promedio = puntaje / len(notas)
#Encontrar la nota maxima, minima y sus respectivos alumnos

nota_max = max(notas)
nota_min = min(notas)
alumno_maxima = nombres[notas.index(nota_max)]
alumno_minima = nombres[notas.index(nota_min)]



print("\nRESULTADOS")
print("Lista de alumnos y sus notas")
for nombre, nota in zip(nombres,notas): #Cuando queremos usar dentro del for dos listas
    print(f"{nombre} | {nota}")

print("---------------------------------------")
print(f"El puntaje: {puntaje}")
print(f"El promedio: {promedio:.2f}")
print(f"Nota máxima: {nota_max} | (Alumno: {alumno_maxima})")
print(f"Nota mínima: {nota_min} | (Alumno: {alumno_minima})")
