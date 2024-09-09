#proposito: tarea ciclos anidados ejercicio 1
# autor: DRM
# Fecha: 24/11/2020
columna = 1
fila = 1
while fila <= 9 :
    while columna <= 9 :
        if fila == 1 or fila == 9 :
          if  columna == 5  :
           print("*", end="")
          else:
              print(" ",end="")
        elif fila== 2 or fila==8 :
            if 3 < columna < 7  :
                print("*", end="")
            else:
                print(" ", end="")
        if fila == 3 or fila== 7 :
            if 2 < columna < 8:
             print("*", end="")
            else:
                print(" ", end="")
        if fila == 4 or fila == 6:
            if 1 < columna < 9:
                print("*", end="")
            else:
                print(" ", end="")
        if fila == 5  :
             if columna > 0:
              print("*", end="")

        columna +=1
    fila += 1
    columna= 1
    print()


