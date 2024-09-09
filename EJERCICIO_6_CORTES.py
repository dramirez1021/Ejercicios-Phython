#proposito: tarea figuras tortuga
# autor: DRM
# Fecha: 26/01/2021
barra= int(input("introduce el tamaño de la barra: "))
v=int(input("introduce el tamaño del lado vertical: "))
h=int(input("introduce el tamaño del lado horizontal: "))
t_barras = 0
perimetroMarco = (v*4) + (h*2)
while barra * t_barras <= perimetroMarco:
    if (h*2) < barra:
        t_barras +=1
        if barra * t_barras == perimetroMarco:
            break
    else:
     t_barras +=2

print(f"Las barras que hay que usar son: {t_barras}")

