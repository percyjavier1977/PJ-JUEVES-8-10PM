#Crear un programa donde vamos a calular el IMC

nombre = input("Ingres el nombre del paciente:\n")
peso = float(input("Ingrese el peso del paciente:\n"))
altura = float(input("Ingrese la altura del paciente:\n"))

#Formula(IMC = Peso / (Altura ** 2))

imc = peso / (altura ** 2)

print(f"Bienvenido señor(@): {nombre.upper()}")
print(f"Su indice de masa corporal es: {imc:.2f}")





