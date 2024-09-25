#Operador de asignacion
numero = 4
print("Valor de numero: {}".format(numero))
numero = 10
print("Valor de numero: {}".format(numero))
letra = 'Flash'
print("Valor de numero: {}".format(letra))

#Asignacion multiple
num, cadena, floatante  = 4, 'saludos', 4.562
print("Prueba de asignacion en cadenada: num: {}, cadena: {}, flotante: {}".format(num,cadena,floatante))

#Asignacion encadenada
num_a = num_b = num_c  = 25
print("Prueba de asignacion en cadenada: num_a: {}, num_b: {}, num_c: {}".format(num_a,num_b,num_c))

#Intercambio de valores de una variable sin utilizar variables auxiliares, con asignacion multiple
x , y = 5 , 10
x , y = y , x
print("Prueba de intercambio de valores: x: {}, y: {}".format(x,y))

#leer en consola multiplea de entradas de usuario.

nombre, apellido, direccion = input("Ingresar nombre, apellido y direccion separado por coma: ->").split(',')
print("Nombre: {}, Apellido: {}. Direccion: {}".format(nombre.strip(),apellido.strip(),direccion.strip()))


