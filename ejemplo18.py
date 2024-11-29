
'''
desempeño > = 90 ---> bonificación es 1000
desempeño > = 75 ---> bonificación es 500
desempeño > = 50 ---> bonificación es 250
Caso contrario -----> 0

'''
dese = float(input("Ingrese la calificación de desempeño (0-100):\n"))
if dese >= 90:
    boni = 1000
elif dese >= 75:
    boni = 500
elif dese >= 50:
    boni = 250
else:
    boni = 0
    
print(f"La bonificación del empleado es: S/.{boni}")
    
if dese <= 49:
    boni = 0
elif dese >=50 and dese <=74:
    boni = 250
elif dese >=75 and dese <=89:
    boni = 500
else:
    boni = 1000
    
print(f"La bonificación del empleado es: S/.{boni}")

    
    
