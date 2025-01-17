#Crear un progra donde se van a ingresar 3 y se debe validar. Al final sebe mostrar el promedio
#la nota maxima y minima

while True:
    try:    
        nota1 = float(input("Ingrese la primera nota: "))
        try:
           
            if nota1 < 0 or nota1 >20:
                raise ValueError("La nota debe estar entre 0 y 20")
            break
        except ValueError as e:
            print(f"¡ERROR!..{e}. Por favor intente nuevamente")

    except ValueError:
          print("¡ERROR!.. Debe ingresar un número entero. Intente nuevamente")

while True:
    try:    
        nota2 = float(input("Ingrese la segunda nota: "))
        try:
           
            if nota2 < 0 or nota2 >20:
                raise ValueError("La nota debe estar entre 0 y 20")
            break
        except ValueError as e:
            print(f"¡ERROR!..{e}. Por favor intente nuevamente")

    except ValueError:
          print("¡ERROR!.. Debe ingresar un número entero. Intente nuevamente")

while True:
    try:    
        nota3 = float(input("Ingrese la primera nota: "))
        try:
           
            if nota3 < 0 or nota3 >20:
                raise ValueError("La nota debe estar entre 0 y 20")
            break
        except ValueError as e:
            print(f"¡ERROR!..{e}. Por favor intente nuevamente")

    except ValueError:
          print("¡ERROR!.. Debe ingresar un número entero. Intente nuevamente")

suma_notas = nota1+nota2+nota3
promedio = suma_notas/3
nota_maxima = max(nota1,nota2,nota3)
nota_minima = min(nota1,nota2,nota3)

print(f"Promedio: {promedio:.2f}")
print(f"Nota mínima: {nota_minima}")
print(f"Nota máxima: {nota_maxima:.2f}")