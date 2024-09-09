#proposito: tarea ciclos anidados ejercicio 1
# autor: DRM
# Fecha: 24/11/2020
fila = 1
columna = 1
fila_negativa = 10
while fila <= 10 :
    while columna <= 48 :
        if  columna <= 10 :
          if fila >= columna :
             print("*", end="")
          else:
              print(" ", end="")
        if 10 < columna < 13 :
          print(" ", end="")
        if  13 <= columna <= 23 :
          if fila_negativa + 12 >= columna :
              print("*", end="")
          else:
              print(" ", end="")
        if 23 < columna < 26 :
            print(" ", end="")
        if 26 <= columna <= 35 :
          if fila + 25 <= columna  :
              print("*", end="")
          else:
            print(" ", end="")
        if 36 < columna < 39 :
            print(" ", end="")
        if 39 <= columna <= 48 :
            if fila_negativa + 38 <= columna :
                print("*", end="")
            else:
                print(" ", end="")
        columna +=1
    columna = 1
    print("")
    fila += 1
    fila_negativa -= 1