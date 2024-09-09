#proposito: tarea figuras tortuga
# autor: DRM
# Fecha: 22/12/2020
numero=input("introduce un numero para comprobar si este es un palindromo: ")
numero_invertido=""
if len(numero) > 21 or len(numero)< 2 :
    print("el numero es incorrecto")
else:
    for i in range (len(numero),-1,-1):
        numero_invertido=numero_invertido + numero[i:i+1]
    if numero == numero_invertido:
        print("es palindromo")
    else:
        print("no es palindromo")

