contador = 0
contraseña = "12345peru"
while True:
    contra = input("Ingrese la contraseña: ").lower()
    contador +=1
    if contra == contraseña:
        print("Ingresando al sistema")
        break
    else:
        print("Contraseña incorrecta")
    

print(f"Número de intentos {contador}")