def operaciones(a,b):
    s = a+b
    r = a-b
    m = a*b
    return s,r,m



#Programación:

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

s,r,m = operaciones(n1,n2)
print(f"La suma es: {s}")
print(f"La resta es: {r}")
print(f"La multiplicación es; {m}")