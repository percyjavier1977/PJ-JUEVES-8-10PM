años_trabajados = int(input("Ingrese su años trabajados: "))
cate = input("Ingrese su categoria (A,B,C): ").lower()


#Bonificacion 800 soles si tiene mas de 10 años trabajando y tiene categoria A o B

if (cate == "a" or cate == "b") and años_trabajados >10:
    
    bonificación = 800
else:
    bonificación = 0
    
print(f"Su bonificación es: S/. {bonificación}")
