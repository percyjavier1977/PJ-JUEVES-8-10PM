dia = int(input("Ingrese el día de la semana:\n"))
if dia == 1:
    tipo_dia = "Lunes"
elif dia == 2:
    tipo_dia = "Martes"
elif dia == 3:
    tipo_dia = "Miércoles"
elif dia == 4:
    tipo_dia = "Jueves"
elif dia == 5:
    tipo_dia = "Viernes"
elif dia == 6:
    tipo_dia = "Sábado"
elif dia == 7:
    tipo_dia = "Domingo"
else:
    dia_no ="Día no existe..Ingresa bien el número"


if dia >7 or dia <=0 :
    print(dia_no)
else:
    print(f"El día es: {tipo_dia}")
    
