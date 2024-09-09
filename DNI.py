dni= (input("introduce un numero de 8 digitos: "))
while len(dni) != 8 :
    dni=(input("el dni es incorrecto intenta de nuevo: "))

residuo = int(dni) % 23
lista = "TRWAGMYFPDXBNJZSQVHLCKE"
print(f"la letra del DNI es: {lista[residuo]}")


