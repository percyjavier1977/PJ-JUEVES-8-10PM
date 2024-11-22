edad = int(input("Ingrese su edad: \n"))
nacionalidad = input("Ingrese su nacionlidad:\n").lower()
respuesta = input("¿Tiene DNI S/N:\n").lower()

if edad >17 and nacionalidad == "peruano" and respuesta == "s":
    print("Usted si puede votar")
    dni = input("Ingrese el número de su DNI: ")
    if len(dni)==8 and dni.isdigit():
        print("DNI Válido")
    else:
        print("DNI Inválido")
else:
    print("Usted no puede votar")
    
    
