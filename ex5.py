try:
    edad = input("Ingrese la edad: ")
    if not edad.isdigit():
        raise ValueError("La edad debe ser un número entero")
    
    edad = int(edad)
    if edad < 0:
        raise ValueError("La edad no puede ser un número negativo")
    print(f"Ingresó la edad {edad}")

except ValueError as e:
        print("¡ERROR!...,",e)
