#****Sistema de autenticacion****

print("**** Sistema de autenticacion ****")
CONSTANT_USUARIO = "admin"
CONSTANT_PASS = 123
usuario = str(input("Ingrese su nombre de usuario:> ")).strip().lower()
contra = int(input("Ingrese su contraseña numerica:> "))
print("¿El ingreso a sistema es valido?: {}".format(CONSTANT_USUARIO == usuario and contra == CONSTANT_PASS ))
print("Fin")

