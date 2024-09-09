#proposito: ejemplos de ciclos anidados
# autor: DRM
# Fecha: 17/11/2020
contador = 1
contador2 = 1
#externo - filas
while contador <= 5 :
    #interno - columnas
    while contador2 <= contador :
        print("*", end="")
        contador2 += 1
    contador += 1
    print("") #salto de linea
    contador2=1 # para recetear el contador y siga entrando al ciclo