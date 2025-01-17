try:
    edad = int(input("Ingrese la edad: "))
    try:
        if edad < 0:
            raise ValueError("La edad no puede ser un número negativo")
        print(f"Ingresó la edad {edad}")

    except ValueError as e:
        print("¡ERROR!...,",e)
except ValueError:
    print("Ingrese un número")
    