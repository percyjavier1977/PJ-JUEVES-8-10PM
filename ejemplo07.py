notas = [10,12,15,18]
lenguajes = ["Python","Java","JavaScript","PHP"]
list_mista = [10,"Juan",True]

#Acceder a un elemento de la lista

elemento = notas[2]
elemento2 = notas[0]
print(f"Selecciono el elemento: {elemento}")
print(f"Selecciono el elemento: {elemento2}")
print(f"Elemento seleccionado: {notas[3]}")
print(notas) #Muestra los elementos de la lista
print(lenguajes)

lenguajes[0] = "Lenguaje Python"
print(lenguajes)

#Añadir un elemento
lenguajes.append("C#")
print(lenguajes)

lenguajes.insert(0,"CSS") #Puedes especificar la posición
print(lenguajes)

lenguajes.pop() #Elimina y devuelve el ultimo elemento
print(lenguajes)

lenguajes.remove("PHP")
print(lenguajes)

