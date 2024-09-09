#proposito:
# autor: DRM
# Fecha: 16/11/2020
numero= int(input("introduce un numero positivo cualquiera: "))
if numero > 0 :
 salida = str(numero) + " "
 salida = salida + str(numero)
 while numero != 1 :
    if numero % 2 == 0:
        numero //= 2
    else:
        numero = numero * 3 + 1
    salida = salida + str(numero) + " "
else:
  print("numero invalido")
print(salida)
