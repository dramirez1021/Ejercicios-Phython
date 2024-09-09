#proposito: ejemplos de ciclos anidados
# autor: DRM
# Fecha: 24/11/2020
filas = 1
columnas = 1
#externo - filas
while filas <= 5 :
    #interno - columnas
    while columnas <= 5 :
        if columnas >= filas :
         print("*", end="")
        else:
            print(" ", end="")
        columnas += 1
    filas += 1
    print("") #salto de linea
    columnas=1