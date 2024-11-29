'''
puntaje < 50 ----> Insuficiente
puntaje esta entre 50 y 59 -----> Suficiente
puntaje esta entre 60 y 79 -----> Bueno
puntaje estra en 80 y 89 -------> Muy bueno
puntaje supera 89 --------------> "Excelente"

'''

puntaje = int(input("Ingrese el puntaje:\n"))
if puntaje < 50: 
    rendimiento = "Insuficiente"
elif 50 <= puntaje < 60:
    rendimiento = "Suficiente"
elif 60 <= puntaje < 80:
    rendimiento = "Bueno"
elif 80<= puntaje < 90:
    rendimiento = "Muy bueno"
else:
    rendimiento = "Excelente"

print(f"Su puntaje es: {puntaje}")
print(f"Su categoria de rendimiento es: {rendimiento}")
    