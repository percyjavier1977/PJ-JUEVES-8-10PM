#Programa que permite almacenar en una lista alumnos
nombres=[]
while True:
    nombre = input("Ingrese un nombre(o 'salir' para finalizar): ")
    if nombre.upper()=="SALIR":
        break #Cerrar el bucle
    nombres.append(nombre)
    
    
    
print("Los alumnos ingresados son:",nombres)

for nombre in nombres:
    print(f"Alumn@: {nombre}")

print("------------------------")

for i in range(len(nombres)):
    print(f"{i+1}. {nombres[i]}")

print("------------------------")

for i, nombre in enumerate(nombres,start=1):
    print(f"{i}. {nombre}")
    

for nombre in reversed(nombres):
    print(f"Alumn@: {nombre}")
    

print("---------------------")
nombres.sort() #Ordena la lista alfabéticamente
for i, nombre in enumerate(nombres,start=1):
    print(f"{i}. {nombre}")
    