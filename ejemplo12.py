usuario = input("Ingrese el usuario: ")
contraseña = int(input("Ingrese la contraseña: "))

#usuario = "python123"
#contrase = 12345


if usuario.lower() == "python" and contraseña == 12345:
    print("Usuario y contraseña correctos")
    print("Ingresando al sistema")   
else:
    print("Usuario o contraseña incorrectos")