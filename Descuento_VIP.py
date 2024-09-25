print("***Descuento VIP***")

NO_PRODUCTOS_VIP = 10
cantidad_product = int(input("ingrese la cantidad de productos comprados: "))
posee_Memb = input("Tienes la membresia (Si/No): ")

print("El valor de su Descuento VIP es: {}".format((cantidad_product > NO_PRODUCTOS_VIP) and (posee_Memb.strip().lower() == 'si')))