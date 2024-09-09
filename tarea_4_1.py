#proposito: tarea ciclos anidados ejercicio 1
# autor: DRM
# Fecha: 24/11/2020
fila = 1
columna = 1
#externo - filas
while columna <= 20 :
    #interno - columnas
    while fila <= 5 :
        if 1 <= columna <= 5 :
          if fila <= columna :
             print("*", end="")
          else:
                print(" ", end="")
        if 6 <= columna <= 10 :
            if columna <= fila :
                print("*", end="")
            else:
                print(" ", end="")
        if 10 < columna <= 15 :
            if columna >= fila :
                print("*", end="")
            else:
                print(" ", end="")
        if 15 < columna <= 20 :
            if columna >= fila :
                print("*", end="")
            else:
                print(" ", end="")
        columna +=1
    columna += 1
    print("") #salto de linea
    fila =1