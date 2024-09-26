#Programa que calcula el ticket de venta
print("---- Generacion Ticket Venta ----")

item1 = float(input("Ingrese el precio del Producto 1: "))
item2 = float(input("Ingrese el precio del Producto 2: "))
item3 = float(input("Ingrese el precio del Producto 3: "))
item4 = float(input("Ingrese el precio del Producto 4: "))

#Sumatoria din impuesto
total_sin_impuestos = item1 + item2 + item3 + item4

#Sumatoria en total con un impuestos (40%)

impuesto = total_sin_impuestos * 0.40

#Total de la compra
costo_total= impuesto + total_sin_impuestos

#Descuento de 15%
descuento = costo_total * 0.15

#Final
costo_final = costo_total - descuento

print(f''''------ Gracias Por su compra!!! -------
Subtotal: ${total_sin_impuestos:.2f}
Impuesto: ${impuesto:.2f}
Descuento: ${descuento:.2f}
Costo total: ${costo_total:.2f}
--------------------------------------------
Costo Final: ${costo_final:.2f}''')




