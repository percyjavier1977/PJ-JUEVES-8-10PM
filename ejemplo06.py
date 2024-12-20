'''
Crear un programa donde se debe ingresar edades. se debe preguntar cada ves que 
si deseo agregar otra edad. al final debenos mostrar una estadistica: 
Proemdio, edad maxima, edadminima
'''

suma_edades = 0
contador = 0
edad_maxima = None
edad_minima = None

print("===PROGAMA QUE CALCULA LA ESTADISTICA DE EDADES DE USUARIOS=====")

while True:
    edad = int(input("Ingrese una edad: "))
    suma_edades +=edad
    contador+=1
    
    #Buscar la edad mayor y menor
    if edad_maxima is None or edad > edad_maxima:
        edad_maxima = edad
    if edad_minima is None or edad < edad_minima:
        edad_minima = edad
    
    continuar = input("¿Desea agregar otra edad? (Si/no): ").strip().lower()
    if continuar == "no":
        break
    
    
promedio = suma_edades /  contador

print("\n===============ESTADISTICA=================")
print(f"Ingresó {contador} registros")
print(f"La edad mayor es--------: {edad_maxima}")
print(f"La edad menor es--------: {edad_minima}")
print(f"El promedio es----------: {promedio:.2f}")
    