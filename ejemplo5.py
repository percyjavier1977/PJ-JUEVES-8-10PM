cliente = input("Ingrese el nombre del cliente:\n").upper()
producto = input("Ingrese el producto:\n").upper()
cantidad = float(input("Ingrese la cantidad:\n"))
precio = float(input("Ingrese el precio:\n"))
descuento = 0
#Importe
importe = cantidad * precio
#Descuento es el 3% del importe alos que tienen un importe mayor a 1000
if importe > 1000 :
    #verdad
    descuento = importe * 0.03
    
#Total a pagar
tpago = importe - descuento

print ("-------------REPORTE DE VENTA----------------")
print("----------------------------------------------")
print(f"Cliente---------------------: {cliente}")
print(f"Producto--------------------: {producto}")
print(f"Cantidad Comprada-----------: {cantidad}")
print(f"Precio de compra------------: S/ {precio:,.2f}")
print("-----------------------------------------------")
print(f"El importe es---------------: S/ {importe:,.2f}")
print(f"Descuento-------------------: S/ {descuento:,.2f}")
print(f"Total a pagar es------------: S/ {tpago:,.2f}")