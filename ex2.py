while True:
    try:
        print("=======División entre dod números====")
        numerador = float(input("Ingrese el numerador: "))
        denominador = float(input("Ingrese el denominado: "))
        resultado = numerador/denominador
        print(f"El resultado de la división es: {resultado}")
        break
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero..por favor ingrese el denominado diferente")
    except ValueError:
        print("Error: Entrada invalidad...Ingrese números")


