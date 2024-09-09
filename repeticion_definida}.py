calificacion= 0
contador=0
suma= 0
while calificacion != -1 :
    calificacion = int(input("introduce una calificacion: "))
    suma = suma + calificacion
    contador += 1
print(f"promedio: {suma + 1  / contador - 1}")