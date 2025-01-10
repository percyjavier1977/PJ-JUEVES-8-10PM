try:
    numero = int(input("Ingersa un numero: "))
    print(f"Ingresó el numero {numero}")
except ValueError:
    print("Error..entrada invalida")
    
else:
    #Codido que se ejecuta cuando no ocurre ningun error
    print("Se ingreso correctamente el número")
finally:
    #codigo que siempre se va a ejecutar
    print("Fin del programa")