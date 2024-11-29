'''
Crear un programa donde debemos calcular el IMC
IMC = Peso / altura ^ 2
Parametros:
IMC < 18.5 ---> Bajo de peso
IMC esta entre 18.5 y 24.9 ----> Normal
IMC esta entre 25 y 29.9 ----> Sobre peso
caso contrario -----> Obesidad


'''
peso = float(input("Ingrese el peso:\n"))
altura = float(input("Ingrese la altura:\n"))

imc = peso / (altura ** 2)


if imc <18.5:
    categoria = "Bajo Peso"
elif 18.5 <= imc <=24.9: 
    categoria = "Normal"
elif 25 <= imc <= 29.9: 
    categoria = "Sobrepeso"
else:
    categoria = "Obeso"
    
print(f"Su IMC es: {imc:.2f}")
print(f"Esta en la categoria:{categoria}")

if imc <18.5:
    categoria = "Bajo de peso"
elif imc >=18.5 and imc <=24.9:
    categoria = "Normal"
elif imc >=25 and imc <=29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obeso"
    
print(f"Su IMC es: {imc:.2f}")
print(f"Esta en la categoria:{categoria}")
