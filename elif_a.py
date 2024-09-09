#Proposito: pedir el numero del mes al usuario y mostrar el nombre
# Autor: DRM
# Fecha:10/11/20
mes = int(input("introduce el numero del mes: "))
if mes < 1 or mes > 12 :
  print("el numero es incorrecto, el mes no existe")
if mes == 1 :
    print("enero")
elif mes == 2 :
    print("febrero")
elif mes == 3:
    print("marzo")
elif mes == 4 :
    print("abril")
elif mes == 5 :
    print("mayo")
elif mes == 6:
    print("junio")
elif mes == 7:
    print("julio")
elif mes == 8:
    print("agosto")
elif mes == 9:
    print("septiembre")
elif mes == 10:
    print("octubre")
elif mes == 11:
    print("noviembre")
elif mes == 12:
        print("diciembre")



