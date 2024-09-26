# **** Valor en rango ****

print("**** Sistema de autenticacion ****")
CONSTANT_VALOR_MAXIMO = 5
CONSTANT_VALOR_MINIMO = 0
valor = int(input("Ingrese su valor:> "))
print("¿El valor ingresado esta dentro el rango 0 - 5?: {}".format(CONSTANT_VALOR_MAXIMO >= valor and CONSTANT_VALOR_MINIMO<= valor))
print("Fin")
