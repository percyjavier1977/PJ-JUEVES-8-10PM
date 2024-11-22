cantidad = int(input("Ingrese la cantidad comprada: "))
precio = float(input("Ingrese el precio del producto: "))
importe = cantidad * precio

#Si compro mas de 12 productos o su importe supera los 500 3% de decuento

if cantidad >  12 or importe > 500:
    descuento = 0.03 *  importe
else:
    descuento = 0
    
tpago = importe -  descuento

print(f"El importe es..........: {importe:,.2f}")
print(f"El descuento es........: {descuento:,.2f}")
print(f"El total a pagar es....: {tpago:,.2f}")