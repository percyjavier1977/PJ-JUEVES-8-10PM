def ingresar_nota(numero):
    while True:
        try:    
            nota = float(input(f"Ingrese la {numero} (0-20): "))
            try:
                if 0 <= nota <=20:
                    return nota
                else:
                   raise ValueError("La nota debe estar entre 0 y 20")
              
            except ValueError as e:
                print(f"¡ERROR!..{e}. Por favor intente nuevamente")

        except ValueError:
            print("¡ERROR!.. Debe ingresar un número entero. Intente nuevamente")


def calcular_promedio(nota1,nota2,nota3,nota4):
    return(nota1+nota2+nota3+nota4)/4





nota1 = ingresar_nota(1)
nota2 = ingresar_nota(2)
nota3 = ingresar_nota(3)
nota4 = ingresar_nota(4)

promedio = calcular_promedio(nota1,nota2,nota3,nota4)

print(f"El promedio es: {promedio}")