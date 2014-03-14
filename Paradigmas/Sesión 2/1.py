numero = int(raw_input("Introduzca numero de DNI: "))
letras = "TRWAGMYFPDXBNJZSQVHLCKE"
print "Su letra de DNI es", letras[numero%23]
