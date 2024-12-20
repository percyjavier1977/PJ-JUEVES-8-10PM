#Crear un programa donde la aplicación pide la contraseña hasta que el ususario 
#ingrese correctamente.

contraseña_correcta = "python12345"
intento = ""
while intento != contraseña_correcta:
    intento = input("Ingrese la contraseña:").lower()
    if intento != contraseña_correcta:
        print("¡ERROR!...Contraseña incorrecta. Intente nuevamente")


print("Ingresando al sistema")

