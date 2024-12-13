#Crear un programa para cajero automatico donde solo tenemos tres opciones de ingresar
#correctamente la contraseña.
import getpass
c = 12345
for i in range(1,4):
   contra = int(getpass.getpass("Ingrese su contraseña:\n"))
   if contra == c:
       print("Contraseña correcta:...INGRESANDO AL SISTEMA")
       break #Cierra el bucle
   else:
       print("Contraseña incorrecta")
    
else:
       print("TARJETA BLOQUEDA")
       