salario = float(input("Ingrese su salario: "))
#Impuesto si el salario supera los 3000
if salario >3000:
    impuesto = salario * 0.08 #8% del salario
else:
    impuesto = 0
    

print(f"Tiene que pagar el siguiente impuesto {impuesto}")
    
