# Proposito
# Autor: DRM
# Fecha: 10/11/20
hora = int(input("introduce la hora: "))
if hora < 0 or hora > 23:
    print ("la hora no es correcta")
if hora >= 5 and hora<= 12 :
    print("goood morning")
elif  hora > 12 and hora <= 19 :
    print("goood afternoon")
elif hora > 19 and hora <= 23 :
    print("goood evening")
else:
    print("good night")


