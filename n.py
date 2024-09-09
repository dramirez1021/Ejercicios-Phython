cadena= "hola en mi examen"
cadena2= "python si se puede"
c=len(cadena)
c2=len(cadena2)
menor =-1
if c < c2:
    menor =c
else:
    menor =c2
for indice in range(0,menor):
    if cadena[indice] == cadena2[indice]:
        print(cadena[indice], end="")